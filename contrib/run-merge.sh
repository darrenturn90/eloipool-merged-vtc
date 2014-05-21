#!/bin/sh
# -p eloipool user/pass for rpc
# -x <http://user:pass@host:port> for each merged coin
# -s number of merged coins
./merged-mine-proxy -w 9401 -p http://user:pass@localhost:8344 -x http://user:pass@localhost:9003 http://user:pass@localhost:9002 -s 2
