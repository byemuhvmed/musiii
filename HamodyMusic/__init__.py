from HamodyMusic.core.bot import hamody
from HamodyMusic.core.dir import dirr
from HamodyMusic.core.git import git
from HamodyMusic.core.userbot import Userbot
from HamodyMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = hamody()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
