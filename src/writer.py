from io import TextIOWrapper
from datatypes import Social, Bullet

def write_header(file: TextIOWrapper, banner: str, intro: str):
	file.write(
"""<!--HEADER-->
<h1 align="center">
<img src="{banner}">
</h1>

<h3 align="center">
{intro}
</h3>\n
""".format(banner=banner, intro=intro))

def write_socials(file: TextIOWrapper, socials: list[Social]):
	file.write('<!--SOCIALS-->\n<p align="center">\n')

	for i in socials:
		file.write(
	"""<a href="{url}" target="_blank">
	<img src="{img}" width="10%"></a>\n"""
			.format(url=i.url, img=i.img))

	file.write(
"""<br>
<a href="https://ko-fi.com/soupsu" target="_blank">
	<img src="https://ko-fi.com/img/githubbutton_sm.svg"></a>
</p>\n
"""
	)

def write_bullets(file: TextIOWrapper, bullets: list[Bullet]):
	file.write('<!--BULLETS-->\n<h3>\n\n')
	for bullet in bullets:
		file.write('{b} {txt}<br>\n'
			.format(b=bullet.bullet, txt=bullet.txt))
	file.write('</h3>\n')