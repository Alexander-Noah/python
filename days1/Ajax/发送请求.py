import requests
import logging

from days1.days3.Demo4 import RESULTS_DIR

logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(levelname)s-%(message)s')
INDEX_URL = 'https://spa1.scrape.center/api/movie/?limit={limit}&offset={offset}'

def scrape_api(url):
    logging.info('Scraing %s...',url)
    try:
        response = requests.get(url)
        if response.status_code==200:
            return response.json()
        logging.error('get invalid status code %s while scraping %s',response.status_code,url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s',url,exc_info=True)

LIMIT=10
def scrape_index(page):
    url=INDEX_URL.format(limit=LIMIT,offset=LIMIT*(page-1))
    print("成功")
    return scrape_api(url)
DETATL_URL='https://spa1.scrape.center/api/movie/{id}'
def scrape_detail(id):
    url=DETATL_URL.format(id=id)
    return scrape_api(url)

import json
from os import makedirs
from os.path import exists
RESULTS_DIR='results'
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)
def save_data(data):
    name=data.get('name')
    data_path=f'{RESULTS_DIR}/{name}.json'
    json.dump(data,open(data_path,'w',encoding='utf-8'),ensure_ascii=False,indent=2)

TOTAL_PAGE=10
def main():
    for page in range(1,TOTAL_PAGE+1):
        index_data=scrape_index(page)
        for item in index_data.get('results'):
            id=item.get('id')
            detail_data=scrape_detail(id)
            logging.info('datail data %s',detail_data)
            save_data(detail_data)

if __name__ =='__main__':
    main()



















