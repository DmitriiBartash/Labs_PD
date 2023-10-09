import requests
import json
# importing pandas as pd
import pandas as pd

url = "www.cbr-xml-daily.ru/daily_json.js"

for i in range(3):

    urlmodified = "https://" + url

    response = requests.get(urlmodified)
    response_json = json.loads(response.text)

    date = response_json['Date']
    dollar = response_json['Valute']['USD']['Value']
    # print(date, dollar)

    url = response_json['PreviousURL'][2:]

    dllar = [dollar]
    dte = [dollar]
    dict = {'date': dte, 'dollar': dllar}
    df = pd.DataFrame(dict)
    print(df)

# saving the dataframe
df.to_csv('file1.csv')
# print(url)
# print(response_json)
# import requests
# import json
# from bs4 import BeautifulSoup

# url = 'https://www.cbr-xml-daily.ru/daily_json.js'
# html = requests.get(url)
# # print(html.content)
# soup = BeautifulSoup(html.text,'html.parser')
# site_json=json.loads(soup.text)
# print(site_json)

# print(dollar_dict)
# print(html.content)
# soup = BeautifulSoup(html.text, 'html')
# print(soup)
