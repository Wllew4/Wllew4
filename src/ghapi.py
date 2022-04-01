from github import Github


def get_most_used_langs(first: int, token: str) -> dict[str, float]:
	g = Github('Wllew4', token)
	languages = {}

	for repo in g.get_user().get_repos(affiliation='owner'):
		langs = repo.get_languages()
		for lang in langs:
			if lang not in languages:
				languages[lang] = langs[lang]
			else:
				languages[lang] += langs[lang]

	sort = dict()
	sum = 0
	k = sorted(languages, key=languages.get, reverse=True)
	v = sorted(languages.values(), reverse=True)
	for i in range(0, first):
		sum += v[i]
	for i in range(0, first):
		percent = v[i] / sum * 100
		sort[k[i]] = round(percent, 2)
	return sort