import re
import requests

countries_file = open('country_text.txt', 'r', encoding ='utf-8')
country_caps_file = open('country_capital_text.txt', 'w', encoding = 'utf-8')
wrong_countries = set()

for line in countries_file:
    country = re.sub(r'\n| \Z', '', line)
    country_link = re.sub(r' ', '_', country)
    r = requests.get('https://en.wikipedia.org/wiki/' + country_link)
    text = r.text
    print(country)

    try:
        helper = re.search(r'(?<=Capital<)[\w\W]+?(?=</a>){1}?', text).group()
        capital = re.search("[\w'-. ]+\Z", helper)

        if capital == None:
            capital = re.search("(?<=<td>)[\w'. -]+?(?=<)", helper)
        capital = capital.group()

        if capital == 'city-state':
            capital = country
            wrong_countries.add(country_link)

        if country_link == 'Switzerland':
            capital = 'Bern'

        print('The capital of', country, 'is', capital)
        country_caps_file.write(country + ':' + capital + '\n')

    except AttributeError:
        print('SOMETHING WENT WRONG, CHECK THE CAPITAL')
        wrong_countries.add(country_link)

print('Something wrong with the countries:', wrong_countries)

countries_file.close()
country_caps_file.close()
