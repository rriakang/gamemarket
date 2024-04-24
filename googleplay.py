import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import pyautogui
from openpyxl import Workbook

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://play.google.com/store/apps/details?id=com.and.games505.TerrariaPaid&hl=ko&gl=US') #크롤링 하고 싶은 플레이스토어 앱 URL
time.sleep(2)

elements = driver.find_elements(By.CLASS_NAME, 'VfPpkd-Bz112c-LgbsSe.yHy1rc.eT1oJ.QDwDD.mN1ivc.VxpoF') #리뷰 상세로 진입하기 위한 class

elements[2].click() #3번째 항목이 리뷰 상세로 진입하기 위한 버튼
time.sleep(2)

driver.find_element(By.CLASS_NAME, 'RHo1pe').click() #키를 누르기 위해 리뷰 상세 내 class 클릭
time.sleep(2)

for i in range(10): #원하는 횟수만큼 pagedown 키 누르기
    pyautogui.press('pagedown')

time.sleep(30)

# 날짜, 리뷰, 별점 수집
reviews = driver.find_elements(By.CLASS_NAME, 'h3YV2d') #리뷰 class값
grades = driver.find_elements(By.CLASS_NAME, 'iXRFPc') #평점 class값
dates = driver.find_elements(By.CLASS_NAME, 'bp9Aid') #날짜 class값

li = [] #데이터 묶음 저장할 리스트

for i in range(len(reviews)):
    if i < 3: #리뷰 상세 외 대표 리뷰 3개 항목이 있기 때문에 중복 제외하기 위함
        continue
    else:
        li.append([dates[i].text, grades[i].get_attribute('aria-label')[10] + '점', reviews[i].text]) #각 항목 리스트에 저장

wb = Workbook() #Workbook 생성
ws = wb.active #시트 활성화
ws.title = 'review' #시트 타이틀 설정

ws.append(['날짜', '평점', '리뷰 내용']) #첫 행에 저장할 데이터 항목 추가

for data in li:
    ws.append(data) #추출한 데이터 엑셀 파일에 쓰기

wb.save('google_Terraria_reviews.xlsx') #해당 경로에 엑셀 파일 저장

driver.close()

