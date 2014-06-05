import urllib.request
from subprocess import *
import re

pattern = 'N[^P](S|T)[^P]'

websites = []
websitesdata = []
with open('rosalind.txt') as f:
        for line in f:
            websites.append(line.strip())
            websitesdata.append('')
print('Websites: ',websites)

urls = []
for website in websites:
    urls.append('http://www.uniprot.org/uniprot/' + website + '.fasta')
print('URLs: ', urls)

for url in range(len(urls)):
    data = urllib.request.urlopen(urls[url])
    for line in data:
        line = line.decode("utf-8")
        if '>' in line:
            pass
        else:
            line = line.strip()
            websitesdata[url] += line
print(websitesdata)
solutions = []
for i in websites:
    solutions.append([])
for data in range(len(websitesdata)):
    for i in range(len(websitesdata[data])):
        if i < (len(websitesdata[data])-4):
            if re.search(pattern, websitesdata[data][i:i+4]):
                solutions[data].append(i+1)
print(solutions)

for i in range(len(solutions)):
    if len(solutions[i]) == 0:
        pass
    else:
        print(websites[i])
        for x in solutions[i]:
            print(x, end=' ')
        print('')
