import requests
from bs4 import BeautifulSoup
import sys
import config
import os.path

# �p�����[�^�Z�b�g
args = sys.argv
level = args[1]
round = int(args[2])
prob = args[3]
LOGIN_URL = "https://beta.atcoder.jp/login"
task_screen_name = "{}{:03d}_{}".format(level, round, prob)
CPP_ID = 3003

source_path = "{level_camel}/{level}{round:03d}/{level}{round:03d}{prob_camel}.cpp".format(
    level_camel=level.upper(), level=level, round=round, prob_camel=prob.upper())

if os.path.exists(source_path):
    # ��o�p�\�[�X�R�[�h�̓ǂݍ���
    f = open(source_path)
    source_code = f.read()  # �t�@�C���I�[�܂őS�ēǂ񂾃f�[�^��Ԃ�
    f.close()
else:
    print("File to submit is not found.")
    quit()

# �Z�b�V�����J�n
session = requests.session()
r = session.get(LOGIN_URL)
s = BeautifulSoup(r.text, 'lxml')
csrf_token = s.find(attrs={'name': 'csrf_token'}).get('value')

# �p�����[�^�Z�b�g
login_info = {
    "csrf_token": csrf_token,
    "username": config.USERNAME,
    "password": config.PASSWORD
}

result = session.post(LOGIN_URL, data=login_info)
result.raise_for_status()
if result.status_code==200:
  print("log in!")
else:
  print("failed...")

target_url = "https://beta.atcoder.jp/contests/{level}{round:03d}/submit".format(
    level=level, round=round)

html = session.get(target_url)
html.raise_for_status()
soup = BeautifulSoup(html.text, 'lxml')

csrf_token = soup.find(attrs={'name': 'csrf_token'}).get('value')

submit_info = {
    "data.TaskScreenName": task_screen_name,
    "csrf_token": csrf_token,
    "data.LanguageId": CPP_ID,
    "sourceCode": source_code
}


result = session.post(target_url, data=submit_info)
result.raise_for_status()

if result.status_code == 200:
    print("Submitted!")
else:
    print("Error in submitting...")