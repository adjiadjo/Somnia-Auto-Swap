from web3 import Web3

USE_ALL_TOKEN_BALANCE = True
RPC_URL = "https://dream-rpc.somnia.network"
ROUTER_ADDRESS = Web3.to_checksum_address("0xb98c15a0dC1e271132e341250703c7e94c059e8D")
DELAY_SWAP = 3  # Increase delay between swaps for smoother transactions
DELAY_ERROR = 5  # Keep delay for retry error handling
MAX_RETRY = 5  # Increase retries for more stability
SLIPPAGE = 0.01
GAS_LIMIT = 300000
GAS_PRICE = 0.0035  # Can be increased if needed
GAS_MULTIPLIER = 1.2  # Slightly increase the multiplier to ensure faster processing
BASE_TOKEN = "STT"
MIN_NATIVE_BALANCE = 0.0001
SWAP_PERCENTAGE = 0.3

SOMNIA_TOKENS = {
    "STT": {"address": None, "decimals": 18},
    "TOK1": {"address": Web3.to_checksum_address("0xdc07E5Cc79140551da92A2Bc2E6D31530B9c2dCA"), "decimals": 18},
    "USDT.g": {"address": Web3.to_checksum_address("0xDa4FDE38bE7a2b959BF46E032ECfA21e64019b76"), "decimals": 18},
    "WSTT": {"address": Web3.to_checksum_address("0xF22eF0085f6511f70b01a68F360dCc56261F768a"), "decimals": 18}
}

ERC20_ABI = '[{"constant":true,"inputs":[{"name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"amount","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"type":"function"},{"constant":true,"inputs":[{"name":"owner","type":"address"},{"name":"spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"type":"function"}]'
ROUTER_ABI = '[{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"}]'
