from io import TextIOWrapper
from ghapi import get_most_used_langs

def write_ghstats(file: TextIOWrapper, lang_count: int, token: str):
	file.write('\n<!--LANGS-->\n')

	file.write("""<div align="right">

| | Most Used Languages: | |
|-:|:-:|:-|\n""")

	langs = get_most_used_langs(lang_count, token)

	for lang in langs:
		file.write("""{name}:|\t\t{bar}<br> | {percent}%\n"""
			.format(name=lang, bar=percent_to_bar(langs[lang]), percent=langs[lang]))
	file.write('</div>')

def percent_to_bar(percent: float) -> str:
	out = ''
	for i in range(0, 25):
		if i * 4 <= percent:
			out += chr(ord('\u2588'))
		else:
			out += chr(ord('\u2591'))
	return out