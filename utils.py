import pandas as pd
import requests
import config
from datetime import datetime
import json


def get_nyt_data(start='1/19', end='12/19'):
    """
    Returns df with section name,headline, kicker, abstract, lead_paragraph, snippet, 
    keywords and publication date for all nyt articles published in specified date range.
    """
    start_date = datetime.strptime(start, '%m/%y')
    start_month = start_date.month
    start_year = start_date.year

    end_date = datetime.strptime(end, '%m/%y')
    end_month = end_date.month
    end_year = end_date.year

    months = []
    years = []
    for yr in range(start_year, end_year+1):
        years.append(yr)
        for m in range(start_month, end_month+1):
            months.append(m)
            
    df = pd.DataFrame(columns=['section_name',
                               'headline',
                               'kicker',
                               'abstract',
                               'lead_paragraph', 
                               'snippet',
                               'keywords',
                               'pub_date'
                              ])
    for year in years:
        for month in months:
            print(month, year)
            url = "https://api.nytimes.com/svc/archive/v1/{0}/{1}.json?api-key={2}".format(year,month,config.api_key)
            response = requests.get(url)
            data = response.json()
            errs = 0
            for x in data['response']['docs']:
                try:
                    df = df.append({'headline': x['headline']['main'],
                                    'kicker': x['headline']['kicker'],
                                    'abstract':x['abstract'],
                                    'lead_paragraph':x['lead_paragraph'],
                                    'snippet':x['snippet'],
                                    'keywords':", ".join([y['value'] for y in x['keywords']]),
                                    'pub_date':x['pub_date'],
                                    'section_name':x['section_name']},
                                    ignore_index=True)
                except KeyError as e:
                    errs +=1
                    pass
            print('{} KeyErrors'.format(errs))
    return df

if __name__ == "__main__":
    df = get_nyt_data()
    df.to_csv('nyt2019.csv',index=False)
    print("Pulled data for {} articles".format(len(df)))
