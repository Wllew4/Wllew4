from writer import write_header, write_bullets, write_socials
from write_ghstats import write_ghstats
from datatypes import Social, Bullet
import sys

banner = 'img/wave.png'

intro = """I go by Will/Felix/Janelle

(he/him)
[soupsu.dev](https://soupsu.dev)"""

socials: list[Social] = [
	Social('https://twitter.com/soupsu_',	'img/twitter.svg'),
	Social('https://twitch.tv/soupsu'	,	'img/twitch.svg' ),
	Social('https://youtube.com/soupsu'	,	'img/youtube.svg'),
	Social('https://discord.gg/BaJ4r9e'	,	'img/discord.svg'),
]

bullets: list[Bullet] = [
	Bullet('💖', '19 y/o [**Twitch Streamer**](https://twitch.tv/soupsu) and **Software Developer**.'),
	Bullet('🪨', 'From southern New Hampshire.'),
	Bullet('🎓', 'Studying at [**Wentworth Institute of Technology**](https://wit.edu) in Boston, MA.'),
	Bullet('💻', 'Focusing on low-level/backend development.'),
	Bullet('👀', 'Currently making my own language using Rust.'),
	Bullet('🌹', 'Web3 is gigacringe.'),
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