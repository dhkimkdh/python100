# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 12:55:10 2021

@author: ddhhkk
"""

import requests
from bs4 import BeautifulSoup

#찾을 위치 변수명에 저장한다.
url = "https://news.v.daum.net/v/20210801133552596"
#주소의 변수에 저장한다.
resp = requests.get(url)
#변수에 들은 내용물을 text로 변환시켜 저장한다.
html_src = resp.text

#'html.parser'를 이용 해석한 것을 변수에 저장한다.
soup = BeautifulSoup(html_src,'html.parser')

target_img = soup.find(name='img', attrs={'class':'thumb_g_article'})

print('HTML요소:', target_img)
print("\n")


#그림태그 소스파일 가지고오기
target_img_src = target_img.get('src')
print('img파일의 경로 :', target_img_src)
print("\n")


target_img_resp = requests.get(target_img_src)
#저장할 폴더 위치와 파일명 정하기
out_file_path = "./output/find_tola.jpg"

with open(out_file_path,'wb') as out_file:
    out_file.write(target_img_resp.content)
    print("이미지 파일로 저장하였습니다.")
    

