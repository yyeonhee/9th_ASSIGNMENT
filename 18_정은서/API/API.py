from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import requests
import json
from requests.api import get

# 프로그램 설명 
print("이 프로그램은 의약품 낱알 식별정보를 출력하는 프로그램입니다. ")

# 입력 
name = input("의약품명을 입력하세요. ex_알레기살정10밀리그람(페미로라스트칼륨): ")
company = input("업체명을 입력하세요. ex_현대약품(주): ")

# api 호출 
url = 'http://apis.data.go.kr/1470000/MdcinGrnIdntfcInfoService/getMdcinGrnIdntfcInfoList'

# 전송할 파라미터 입력 
queryParams = '?' + urlencode(
     { 
     quote_plus('ServiceKey'): unquote("iHd%2BVifPOIRSPuBfHmZwFCcEBOFpL9zFzCB3ic9zXFQ%2BUnDzv7MrPu%2BALP6u8sBlRnhuacJgErgTPaRi9TAgRA%3D%3D"),
     # 의약품명
     quote_plus('item_name'): name, 
     # 업체명
     quote_plus('entp_name'): company, 
     # 품목일련번호
     quote_plus('item_seq'):'200402488',
     # 약학정보원 이미지 생성일
     quote_plus('img_regist_ts'): '20041222',
     # 보험코드
     quote_plus('edi_code'): '642003260',
     }
     )

# response 를 get 형식으로 받아서 저장 
# unquote : 한글로 보내준 url 풀어줌
get_data = requests.get(url + unquote(queryParams))

# 응답 확인(200이면 정상)
print(get_data.status_code)

# json 형식을 딕셔너리 형태로 저장 
res = get_data.json()