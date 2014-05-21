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

from jsonrpcserver import JSONRPCHandler

class _setlog:
	def doJSON_setlog(self, time, coinid,remotehost,username,rejectReason,solved,solution_safe,difficulty):
#	def doJSON_setlog(self, time, coinid, remotehost):
#		print("LOG HERE")
		if self.Username != self.server.SecretUser:
			self.doAuthenticate()
#			print("LOG NOT HERE")
			return None
#		print("LOG HERE 2")
#		print(solved)
		share = {
			'username_safe': username,
			'coinid': coinid,
			'remoteHost': remotehost,
			'time': time,
			'rejectReason': rejectReason,
			'upstreamResult': solved,
			'solution_safe': solution_safe,
			'difficulty': difficulty
		}
		for i in self.server.loggers:
			i.logShare(share)
		return True

JSONRPCHandler._register(_setlog)

#print("LOG REGISTERED")