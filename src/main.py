from writer import write_header, write_bullets, write_socials
from write_ghstats import write_ghstats
from datatypes import Social, Bullet
import sys
import datetime
from dateutil.relativedelta import relativedelta

banner = 'img/banner.png'

intro = """I go by Felix

(he/him)
[soupsu.dev](https://soupsu.dev)"""

socials: list[Social] = [
	Social('https://twitter.com/soupsu_',	'img/twitter.svg'),
	Social('https://twitch.tv/soupsu'	,	'img/twitch.svg' ),
	Social('https://youtube.com/soupsu'	,	'img/youtube.svg'),
	Social('https://discord.gg/BaJ4r9e'	,	'img/discord.svg'),
]

age = relativedelta(datetime.date.today(), datetime.date(2003, 2, 3)).years

bullets: list[Bullet] = [
	Bullet('💖', '{} y/o **Software Developer** and [**Twitch Streamer**](https://twitch.tv/soupsu).'.format(age)),
	Bullet('📍', 'From Southern New Hampshire.'),
	Bullet('🎓', 'Undergrad student @ [**Wentworth Institute of Technology**](https://wit.edu) in Boston, MA.'),
	Bullet('💻', 'Currently helping develop medical devices.'),
]

lang_count = 6
token = sys.argv[1]

def main():
	readme = open('README.md', 'w', encoding='utf8')

	write_header (readme, banner, intro)
	write_bullets(readme, bullets)
	write_ghstats(readme, lang_count, token)
	write_socials(readme, socials)
	print('Readme.md updated!')
main()
