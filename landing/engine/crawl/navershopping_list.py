import pymysql
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.sql import select
import pandas as pd
import re
from pandas import json_normalize
from datetime import datetime
def get_navershopping_product_list(search_keyword,task_id):
        engine = create_engine(
            ("mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8").format
            ('datacast',
             'radioga12!',
             'datacast-rds.crmhaqonotna.ap-northeast-2.rds.amazonaws.com',
             3306,
             'datacast'),
            encoding='utf-8'
        )
        now = datetime.now()
        today = now.strftime('%Y-%m-%d')
        curs = engine.execute("select * from review_search_task where search_keyword=\'%s\' and registered_date=\'%s\'"%(search_keyword,today))
        rows = curs.fetchall()
        if len(rows)==1:
            ### naver shopiing api 사용
            clientID = 'vDMsgzbR0LTqOZPunT7w'
            client_secret = 'Fte_UsmhS6'
            import json
            import requests
            ##네이버 쇼핑 검색 키워드 설정
            keyword = search_keyword
            ##가져올 상품 갯수 설정
            display = '100'
            ##어디서부터 가져올지 설정
            start = '1'
            ##정렬 기준 설정 (sim: 유사도)
            sort = 'sim'

            params = (
                ('query', keyword),
                ('display', display),
                ('start', start),
                ('sort', sort),
            )

            ##header를 설정해준다. header 는 naver_api clientID 와 secret 을 이용
            headers = {
                'X-Naver-Client-Id': clientID,
                'X-Naver-Client-Secret': client_secret,
            }
            ##네이버쇼핑 상품 리스트 가져오기
            response = requests.get('https://openapi.naver.com/v1/search/shop.json?', headers=headers,params=params)
            response = re.sub('(<([^>]+)>)', '', str(response.json()['items']))
            response = response.replace("\'","\"")
            response = re.sub(r'\\x..', '', response)
            response_json = json.loads(response)
            # keyword_bog.to_sql(name='review_product_list', con=engine, if_exists='append', index=False)

            response_json = json_normalize(response_json)
            response_json['search_keyword'] = keyword
            response_json['review_search_task_id'] = task_id
            for idx in response_json.index:
                if len(response_json._get_value(idx,'title'))>35:
                    response_json._set_value(idx,'title',response_json._get_value(idx,'title')[0:45]+'...')
            response_json.to_sql(name='review_product',con=engine,if_exists='append',index=False)
            #NB. Original query string below. It seems impossible to parse and
            #reproduce query strings 100% accurately so the one below is given
            #in case the reproduced version is not "correct".
            # response = requests.get('https://openapi.naver.com/v1/search/shop.xml?query=%EC%A3%BC%EC%8B%9D&display=10&start=1&sort=sim', headers=headers)
        else:
            task_id = rows[0][0]
        return task_id