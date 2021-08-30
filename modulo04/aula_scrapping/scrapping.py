from bs4 import BeautifulSoup
import requests

url = 'https://stackoverflow.com/questions/tagged/python'

response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

for pergunta in html.select('.question-summary'):
    title = pergunta.select_one('.question-hyperlink')
    date = pergunta.select_one('.relativetime')
    votes = pergunta.select_one('.vote-count-post strong')
    print(title.text, date.text, votes.text, sep='\t')
