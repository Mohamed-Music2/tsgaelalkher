from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "16050450"))
API_HASH = getenv("API_HASH", "0dd89e225b6ddd6f03e8135460d31177")
BOT_TOKEN = getenv("BOT_TOKEN", "5409818512:AAHNVmbdbgAV_NBWmRl3cpU7Wpp2rWDzpz4")
SESSION_NAME = getenv("SESSION_NAME", "session", "BAAokFYkNkouh3MyD9WJzi6L-J5Kh_p1qRCj5KUluNf4Dvcl8YniPxTvqyCgeGKLQcAZSTxIC_ixRHwoDsls3IX4iDwR4y2OAhvdYJvFO6w4OyRunLg4R5hEH0AWzTFe_SLSdqNOIcB7YnbPebTljrCi4-YNm99oU9OGuqt_glN74Xz2J1EFWVXdx5rehErxH3WprgwhZjXWyqh-IiaZoWION15eSfScfhtTlsVOPaHh9lpPAriVDsd5i8Ktq3kyfjMpP1bJZAVbf1jG9H1j2RUV8YiTLaEITPxQvusecD5xPOOOa9VZAaq5YVjdZgo80khY5S5SbSsf94_QK3rJ9jNJAAAAAS2FcekA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "lMl4ll")
ALIVE_NAME = getenv("ALIVE_NAME", "- 𝚃𝙰𝙴𝙼 𝙴𝙸𝚂𝙰 𝙼𝚄𝚂𝙸𝙲 ‹𝟹 .")
BOT_USERNAME = getenv("BOT_USERNAME", "lMl4ll_MUSIC_BOT")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/lMl10l/lMl10l")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "BarEisa")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "D_o_m_A12")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL","mongodb+srv://MOHAMEDMUSIC:MOHAMEDMUSIC@cluster0.xda63.mongodb.net/?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "5191100896").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5191100896").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
