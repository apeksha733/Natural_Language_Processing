import urllib.request
import bs4 as bs
import string
import re
import nltk

f = open("data.txt","a")

raw_html = urllib.request.urlopen('https://bharatdiscovery.org/india/%E0%A4%AC%E0%A5%88%E0%A4%A1%E0%A4%AE%E0%A4%BF%E0%A4%82%E0%A4%9F%E0%A4%A8')
raw_html = raw_html.read()

article_html = bs.BeautifulSoup(raw_html, 'lxml')

article_paragraphs = article_html.find_all('p')

article_text = ''

for para in article_paragraphs:
    article_text += para.text
article_text = article_text.replace('।','.')

article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
article_text = re.sub(r'\s+', ' ', article_text)

f.write(article_text)

raw_html = urllib.request.urlopen('https://hi.wikipedia.org/wiki/%E0%A4%AC%E0%A5%88%E0%A4%A1%E0%A4%AE%E0%A4%BF%E0%A4%82%E0%A4%9F%E0%A4%A8')
raw_html = raw_html.read()

article_html = bs.BeautifulSoup(raw_html, 'lxml')

article_paragraphs = article_html.find_all('p')

article_text = ''

for para in article_paragraphs:
    article_text += para.text
article_text = article_text.replace('।','.')

article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
article_text = re.sub(r'\s+', ' ', article_text)
f.write(article_text)

f.close()
