# api id, hash
API_ID = 1488
API_HASH = 'abcde1488'


DELAYS = {
    'ACCOUNT': [5, 15],  # delay between connections to accounts (the more accounts, the longer the delay)
    'GAME': [5, 10],     # delay after the game
    'REPEAT': [5, 18]
}

# what games the soft will play (in case of several variants it is selected randomly)
GAMES = {
    "512": True,
    "stack": True
}

PROXY = {
    "USE_PROXY_FROM_FILE": False,  # True - if use proxy from file, False - if use proxy from accounts.json
    "PROXY_PATH": "data/proxy.txt",  # path to file proxy
    "TYPE": {
        "TG": "socks5",  # proxy type for tg client. "socks4", "socks5" and "http" are supported
        "REQUESTS": "socks5"  # proxy type for requests. "http" for https and http proxys, "socks5" for socks5 proxy.
        }
}
# session folder (do not change)
WORKDIR = "sessions/"


# timeout in seconds for checking accounts on valid
TIMEOUT = 30

# Set your referral link
REF_LINK = "https://t.me/claytoncoinbot/game?startapp=918432365"

SOFT_INFO = f"""{"Clayton Game".center(40)}
Soft for https://t.me/claytoncoinbot; play in 512 game;
play in stack game, complete tasks; register accounts in web app

The soft also collects statistics on accounts and uses proxies from {f"the {PROXY['PROXY_PATH']} file" if PROXY['USE_PROXY_FROM_FILE'] else "the accounts.json file"}
"""
