import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd  # pandas 라이브러리 추가
from openpyxl import Workbook
import pyautogui




driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://play.google.com/store/games?hl=ko&gl=US') #크롤링 하고 싶은 플레이스토어 앱 URL
time.sleep(30)

elements = driver.find_elements(By.CLASS_NAME,'aoJE7e b0ZfVe') #리뷰 상세로 진입하기 위한 class
# ranker = driver.find_elements(By.CLASS_NAME, 'sT93pb DdYX5 OnEJge')
# #ranker = driver.find_elements(By.CLASS_NAME,'fy9T3c') # 구글 플레이 스토어 내 게임 순위
# name = driver.find_elements(By.CLASS_NAME,'sT93pb DdYX5 OnEJge') #구글 플레이 스토어 내 게임 이름
# game_type = driver.find_elements(By.CLASS_NAME,'sT93pb w2kbF') #구글 플레이 스토어 내 게임 종류
# game_star = driver.find_elements(By.CLASS_NAME,'w2kbF') #구글 플레이 스토어 내 게임 별점
ranker = driver.find_elements(By.CLASS_NAME, 'fy9T3c')
#ranker = driver.find_elements(By.CLASS_NAME,'fy9T3c') # 구글 플레이 스토어 내 게임 순위
name = driver.find_elements(By.CLASS_NAME,'ubGTjb') #구글 플레이 스토어 내 게임 이름
game_type = driver.find_elements(By.CLASS_NAME,'ubGTjb') #구글 플레이 스토어 내 게임 종류
game_star = driver.find_elements(By.CLASS_NAME,'ubGTjb') #구글 플레이 스토어 내 게임 별점



#수집된 데이터를 저장할 리스트

data = []


#수집된 데이터 출력 및 리스트에 추가

for ranker,name,gametype,gamestar in zip(ranker,name,game_type,game_star):
    ranker_text = ranker.get_attribute('aria-label'), #게임은 aira-label 속성에 저장되어 있음
    name_text = name.text,
    gametype_text = gametype.text,
    gamestar_text = gamestar.text




wb = Workbook()
ws = wb.active
ws.title="rank"

ws.append(['순위','이름','종류','평점'])

for data in data:
    ws.append(data)



wb.save('google_rank.xlsx') #해당 경로에 엑셀 파일 저장

driver.close()

# <div class="fy9T3c"><div aria-label="1위">1</div></div> # 게임 순위
# <span class="sT93pb DdYX5 OnEJge ">Hexa Sort</span> # 게임 이름
# <span class="sT93pb w2kbF ">퍼즐</span> #게임 종류
# <span class="w2kbF">4.5</span> #게임 별점

