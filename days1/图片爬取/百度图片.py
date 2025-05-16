import requests
import os
import urllib.request


def get_image_urls_from_api(api_url, headers=None, params=None):
    response = requests.get(api_url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        # 这里需要根据实际的 API 响应结构来提取图片链接
        image_urls = []
        for item in data.get('items', []):
            img_url = item.get('image_url')
            if img_url:
                image_urls.append(img_url)
        return image_urls
    else:
        print(f"请求失败，状态码: {response.status_code}")
        return []


def download_images(image_urls, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    for i, url in enumerate(image_urls):
        try:
            image_name = f"{save_dir}/image_{i}.jpg"
            urllib.request.urlretrieve(url, image_name)
            print(f"已下载图片: {image_name}")
        except Exception as e:
            print(f"下载图片失败: {url}, 错误信息: {e}")


if __name__ == "__main__":
    api_url = "https://image.baidu.com/search/acjson?tn=resultjson_com&word=%E7%99%BD%E4%B8%9D&ie=utf-8&fp=result&fr=&ala=0&applid=&pn=30&rn=30&nojc=0&gsm=5a&newReq=1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    cookies={
        'cookie':'BAIDUID=6B97D988758124551ADB894202E2548D:FG=1; BAIDUID_BFESS=6B97D988758124551ADB894202E2548D:FG=1; BIDUPSID=6B97D988758124551ADB894202E2548D; PSTM=1741372860; ab_jid=d6ba0486be693417991f211fdde598b417d5; ab_jid_BFESS=d6ba0486be693417991f211fdde598b417d5; __bid_n=1959e40a74382084dd7657; H_WISE_SIDS_BFESS=110085_620758_1991828_1992049_626068_628198_632154_633617_636745_639041_632702_639929_639975_640074_641221_639680_640773_642411_642657_642951_642976_643243_643252_643274_643588_643980_644025_643811_641767_644322_644409_644458_644552_644658_644640_644846_644864_644957_644972_644896_645102_645223_645214_645344_645356_645374_644369_645477_645428_645161_645434_645170_645592_645651_645862_644900_645843_645927_645988_645996_646016_646053_645870_645868_645304_646157_646066_646259_646307_646340_645905_644402_646404_646410_646422_646446_623184_646466_646363_646359_646356_646484_644646_644657_646499_646523_646538_645867_646371_646367_644053_645044_646728_646557_646751_646769_646779_646775_646772_646778_637755; ZFY=KJQ0ZstDwCGkoDWvod9V5FRtU6hAQlTtazAL8FP7I2o:C; BAIDU_WISE_UID=wapp_1744589294282_565; RT="z=1&dm=baidu.com&si=f232f73e-cd64-4885-8d01-e743f12a2ac7&ss=m9gb1mmz&sl=c&tt=fgs&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=12l77&ul=7r42t&hd=7r43d"; H_PS_PSSID=60272_61027_62325_62337_62485_62718_62867_62883_62886_62919_62927_62922_62968; BA_HECTOR=0ha020ag858ga42h2g010g8k020bo01k04m9o23; H_WISE_SIDS=62325_62867_62968; arialoadData=false; ppfuid=FOCoIC3q5fKa8fgJnwzbE67EJ49BGJeplOzf+4l4EOvDuu2RXBRv6R3A1AZMa49I27C0gDDLrJyxcIIeAeEhD8JYsoLTpBiaCXhLqvzbzmvy3SeAW17tKgNq/Xx+RgOdb8TWCFe62MVrDTY6lMf2GrfqL8c87KLF2qFER3obJGm51EODDlnqgz44AdUN5VVLGEimjy3MrXEpSuItnI4KD46xh6KcipCBP3WBNo1ZhUL2p1N6CkMY1aSnXgB1lGFtQHqkToJfxaYbEh3hm54O4PE5I5MtLWOB8EmCFAOTz6/GgLbz7OSojK1zRbqBESR5Pdk2R9IA3lxxOVzA+Iw1TWLSgWjlFVG9Xmh1+20oPSbrzvDjYtVPmZ+9/6evcXmhcO1Y58MgLozKnaQIaLfWRFwa8A3ZyTRp/cDxRMhYc94MJmBV3DqpyTuzDwSUDbMyyfzO9u0S9v0HHkJ/i4zKsdnTNS/pLMWceus0e757/UNkQhA4BJH1ZqCtXJJ8GJaKAAv3LCf1Y7/fHL3PTSf9vid/u2VLX4h1nBtx8EF07eCMhWVv+2qjbPV7ZhXk3reaWRFEeso3s/Kc9n/UXtUfNU1sHiCdbrCW5yYsuSM9SPGDZsl7FhTAKw7qIu38vFZiq+DRc8Vbf7jOiN9xPe0lOdZHUhGHZ82rL5jTCsILwcRVCndrarbwmu7G154MpYiKmTXZkqV7Alo4QZzicdyMbWvwvmR2/m//YVTM8qeZWgDSHjDmtehgLWM45zARbPujeqU0T92Gmgs89l2htrSKIdfmoX+qWtG6/y2q+vGsEuBqC+fndmgQjkkMta9b+Fnc8XOA2Aoum1BoRIznpsqWppdImdyxYIjA1uSy2hfTFv/d3cnXH4nh+maaicAPllDg5eQg3PzwS3cxyDdVnXm0S3SzlDBMoJre+/eEVILl9qerpN79NJCIge96NZiXdJF9KSPYcmpuN4s42OCHrb1gDYGZbJZF2cdnYPJr70FQi7jkHNGy4rHPin1m+4ZUWd+8U/DHdNp0WOpGUbl3SfdQzQaYXvleBbteLbUi5NoCAChP5oZfoCeoKKuvUEAPXXTPVjO0TTi0sVqFSdG+GFyi03wlrm3wCRN8QsWhT10pXJL0RhcLTagDnxauF9flnVwiWaq+daLSn0MEazavBACRErAMWXEI9EFQPGJKv0Ijpq+0VDw8xeJloxMf4I+yn8oxuqFuBSz8I0Kfe0QZwk5OQTHYIxIgLZyqbNsJTLj5WVXzQ2GA5eh8aiV0nDOGmtfhiYNjbs2NxP0acAgApNd0ew==; BDUSS=Q2Tzhwc35GaDk0NklYa2R1LVp4cmdPTDAyVkU0WlFkfnk3SFJnVXBKa2Z1aXBvRVFBQUFBJCQAAAAAAQAAAAEAAAAJC9dTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB8tA2gfLQNoZ1; BDUSS_BFESS=Q2Tzhwc35GaDk0NklYa2R1LVp4cmdPTDAyVkU0WlFkfnk3SFJnVXBKa2Z1aXBvRVFBQUFBJCQAAAAAAQAAAAEAAAAJC9dTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB8tA2gfLQNoZ1; ab_bid=c344cacccb8991445fc382583b86083feab4; ab_sr=1.0.1_MTczNDkzNWI4YTAwYzRlY2Y2ZjIxOWRhYmFjYjUwM2I4OTQxZjE3NTRkYjc4NDA0Yjg0NjNhMzYxNzY5YWQ5ZmNlZWExM2ZhZDQyZmNlZDM3NDQyZTg1OTI3ZmJhMmU0Y2ZjOTdkOWEyOGI1MjBhYTlhZmM0YWIwYWQ1ZmQzNWQ1ZjMyY2Q1ZTBiNTQ2Mjg1NjQxZmExOTM1NTRjYTcwYQ=='
    }
    save_directory = "downloaded_images"
    image_urls = get_image_urls_from_api(api_url, headers, cookies)
    download_images(image_urls, save_directory)