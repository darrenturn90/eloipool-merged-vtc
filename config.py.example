### Settings relating to server identity

# Name of the server
ServerName = 'server.com'

### Settings relating to server scaling/load

# Share hashes must be below this to be valid shares
# If dynamic targetting is enabled, this is a minimum
ShareTarget = 0x0000ffff00000000000000000000000000000000000000000000000000000000

# Automatically adjust targets per username
# 0 = disabled
# 1 = arbitrary targets
# 2 = power of two difficulties (zero bit counts)
DynamicTargetting = 3

# How many shares per minute to try to achieve on average
DynamicTargetGoal = 8

# Number of seconds hashrate is measured over
DynamicTargetWindow = 180

# Minimum and maximum of merkle roots to keep queued
WorkQueueSizeRegular = (0x100, 0x1000)

# Minimum and maximum of BLANK merkle roots to keep queued
# (used if we run out of populated ones)
WorkQueueSizeClear = (0x1000, 0x2000)

# Minimum and maximum of BLANK merkle roots to keep queued, one height up
# (used for longpolls)
WorkQueueSizeLongpoll = (0x1000, 0x2000)

# How long to wait between getmemorypool updates normally
MinimumTxnUpdateWait = 5

# How long to wait between retries if getmemorypool fails
TxnUpdateRetryWait = 1

# How long to sleep in idle loops (temporary!)
IdleSleepTime = 0.1

### Settings relating to reward generation

# Address to generate rewards to
TrackerAddr = 'Vi6sMm6HLBxdqs4eaz5jzX1NN4PuFJspD6'

# Coinbaser command to control reward delegation
# NOTE: This example donates 1% of block rewards to Luke-Jr for Eloipool development
#CoinbaserCmd = 'echo -e "1\\n$((%d / 100))\\n1579aXhdwvKZEMrAKoCZhzGuqMa8EonuXU"'

### Settings relating to upstream data providers

# JSON-RPC server for getmemorypool
# Your VTC WALLET address http://username:password@host:port
UpstreamURI = ''

# Set to True if you want shares meeting the upstream target to wait for a
# response from the upstream server before logging them. Otherwise, for such
# shares, upstreamResult will always be True and upstreamRejectReason will
# always be None. Note that enabling this may cause shares to be logged out of
# order, or with the wrong timestamp (if your share logger uses the log-time
# rather than share-time).
DelayLogForUpstream = True

# Bitcoin p2p server for announcing blocks found

UpstreamBitcoindNode = ('127.0.0.1', 9001)

# Network ID for the primary blockchain

# 'v' 'e' 'r' 't'
UpstreamNetworkId = b'\x76\x65\x72\x74'

# Secret username allowed to use setworkaux
SecretUser = "secretUser"

# URI to send gotwork with info for every share submission
# this is the port that the merged mining listens on
GotWorkURI = 'http://localhost:9401'

# Share hashes must be below this to be submitted to gotwork
GotWorkTarget = 0x0000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff

# Aim to produce blocks with transaction counts that are a power of two
# This helps avoid any chance of someone abusing CVE-2012-2459 with them
# 1 = cut out feeless transactions; 2 = cut out even fee-included transactions (if possible)
POT = 0

# Avoid mining feeless transactions except to satisfy POT
# Note this only works if POT is in fact enabled in the first place
Greedy = False

### Settings relating to network services

# Addresses to listen on for JSON-RPC getwork server
# Note that Eloipool only supports IPv6 sockets, and if you want to bind to an
# IPv4 address you will need to prepend it with ::ffff: eg ::ffff:192.168.1.2

# this is the port merge-mine-proxy connects to 
JSONRPCAddresses = (
	('::ffff:127.0.0.1', 8344),
)

# this is your mining port - obviously this should be your external IP
StratumAddresses = (
	('::ffff:127.0.0.1', 9950),
)

# Addresses to listen on for Bitcoin node
# Note that Eloipool only supports IPv6 sockets, and if you want to bind to an
# IPv4 address you will need to prepend it with ::ffff: eg ::ffff:192.168.1.2
BitcoinNodeAddresses = (
	('::ffff:127.0.0.1', 9004),
)

# Addresses that are allowed to "spoof" from address with the X-Forwarded-For header
TrustedForwarders = ('::ffff:127.0.0.1',)

ShareLogging = (
	{
		'type': 'logfile',
		'filename': '/tmp/shares.log',
	},
)
