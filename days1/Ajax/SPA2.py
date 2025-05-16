import requests
import json

headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'referer':'https://spa2.scrape.center/'
}
url = "https://spa2.scrape.center/api/movie/?limit=10&offset=0&token=OTA5OGNkMzJiNzQxMTYwY2JlN2FiMTFiMTJlZTBiMGY0NGJiMTM1OCwxNzQ1NDEyMTAy"
response =requests.get(url,headers=headers)