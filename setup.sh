#!/bin/sh
php updateshares.php >logs/shares.txt 2>&1 &
./eloipool.py >logs/eloipool.txt 2>&1 &
cd contrib
./run-merge.sh >../logs/merge.txt 2>&1 &
wait