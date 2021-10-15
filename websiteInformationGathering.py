import re
import requests

##url = 'https://www.secdaemons.org/'
url = 'https://www.cdw.com/content/cdw/en/locations.html'
infile = open('WebPath.txt')
txt = infile.read()
txt = txt.split()
infile.close()

sitePath = [] # in the case for multiple paths found, I want em saved
for each in txt:
    resp = requests.get(url + each)
    if (resp.status_code == 200):
        print(f'Successful link:', url+each)
        sitePath.append(url+each)


email = '\w+\@[\w+\.]+\w{3}'
phone = '\(?\d{3}\)?\-?\ ?\.?\d{3}\.?\-?\ ?\d{4}'
for i in sitePath:
    site = requests.get(i)
    html = site.text
    print(re.findall(phone, html))
    print(re.findall(email, html))
