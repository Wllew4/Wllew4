import datetime
from dateutil.relativedelta import relativedelta
import re

age = str(relativedelta(datetime.date.today(), datetime.date(2003, 2, 3)).years)

def main():
	readme_read = open('README.md', 'r', encoding='utf8')

	readme_text = readme_read.read()
	readme_text = re.sub("...y/o", age + " y/o", readme_text)
	
	readme_write = open('README.md', 'w', encoding='utf8')
	readme_write.write(readme_text)
	print('Readme.md updated!')
main()
