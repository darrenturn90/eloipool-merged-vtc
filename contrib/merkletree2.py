# Eloipool - Python Bitcoin pool server
# Copyright (C) 2011-2012  Luke Dashjr <luke-jr+eloipool@utopios.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

try:
	from bitcoin.txn import Txn
except ImportError:
	class Txn:
		pass

from hashlib import sha256

def dblsha(b):
	return sha256(sha256(b).digest()).digest()

class MerkleTree2:
	def __init__(self, data, detailed=False):
		self.data = data
		self.recalculate(detailed)
	
	def recalculate(self, detailed=False):
		L = self.data
		steps = []
		if detailed:
			detail = []
			PreL = []
			StartL = 0
		else:
			detail = None
			PreL = [None]
			StartL = 2
		Ll = len(L)
		if detailed or Ll > 1:
			if isinstance(L[1] if Ll > 1 else L[0], Txn):
				L = list(map(lambda a: a.txid if a else a, L))
			while True:
				if detailed:
					detail += L
				if Ll == 1:
					break
				steps.append(L[1])
				if Ll % 2:
					L += [L[-1]]
				L = PreL + [dblsha(L[i] + L[i + 1]) for i in range(StartL, Ll, 2)]
				Ll = len(L)
		self._steps = steps
		self.detail = detail
	
	def withFirst(self, f):
		if isinstance(f, Txn):
			f = f.txid
		steps = self._steps
		for s in steps:
			f = dblsha(f + s)
		return f
	
	def merkleRoot(self):
		return self.withFirst(self.data[0])
