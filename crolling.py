from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

baseUrl = 'https://www.google.com/search?q='
plusUrl = input('검색어를 입력하세요: ')
url = baseUrl + quote_plus(plusUrl)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
driver.implicitly_wait(20)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

v = soup.select('.tF2Cxc')  # Google 검색 결과 컨테이너의 업데이트된 클래스 이름

results = []
for i in v:
    title = i.select_one('.LC20lb.DKV0Md').text
    link = i.a.attrs['href']
    # 요약 텍스트를 가져오기 위해 여러 요소를 조합하여 사용할 수 있습니다.
    summary_parts = i.select('.VwiC3b, .s3v9rd')  # 여러 클래스를 쉼표로 구분하여 추가
    summary = ' '.join([part.text for part in summary_parts if part.text]) if summary_parts else "No summary available"
    results.append({
        'Title': title,
        'Link': link,
        'Summary': summary
    })

print('done')
driver.close()

# 데이터 프레임 생성
df = pd.DataFrame(results)

# 엑셀 파일로 저장
df.to_excel('search_results.xlsx', index=False)
