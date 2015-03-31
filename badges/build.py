import glob
import os
import csv
from jinja2 import Environment, FileSystemLoader


TEMPLATES_DIR = 'templates'

PEOPLE = []
with open('data/__badges.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		(fname, lname, org, title, role, country) = row
		PEOPLE.append({ 'fname': fname, 'lname': lname, 'org': org, 'title': title, 'role': role, 'country': country })

template_data = {
	'badges': PEOPLE
}

def Main():
	env = Environment(loader=FileSystemLoader(TEMPLATES_DIR),
		extensions=['jinja2.ext.with_'])

	template = env.get_template('index.html')
	html = template.render(template_data)
	with open('site/index.html', 'w') as f:
		f.write(html.encode('utf8'))
		f.close()

if __name__ == '__main__':
  Main()