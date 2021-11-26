from selenium import webdriver
import time

url = 'https://camping.gtdc.or.kr/DZ_reservation/reserCamping_v3.php?xch=reservation&xid=camping_reservation' # 목적 홈페이지 주소
driver_url = 'C:/Users/khyun/OneDrive/바탕 화면/toy_project/camping_reservation/chromedriver.exe' # chromedriver 파일 주소

# 드라이버 실행
driver = webdriver.Chrome(driver_url)
driver.get(url)

# 화면 최대화
# driver.maximize_window()

# 팝업 제거
driver.find_element_by_css_selector('.btn-dark').click()

# 날짜 지정
xpath = "//button[@value='A:2021-11-28']" 
driver.find_element_by_xpath(xpath).click()
time.sleep(0.1)

# 구역 지정
driver.find_element_by_css_selector('#camping_zone > button:nth-child(11)').click()

# 인원 지정
xpath = "//html/body/div[4]/table/tbody/tr/td[3]/div/div/table[1]/tbody/tr/td[4]/select/option[3]" 
driver.find_element_by_xpath(xpath).click() 

# 예약 기간
xpath = "//html/body/div[4]/table/tbody/tr/td[3]/div/div/div[5]/select/option[1]" 
driver.find_element_by_xpath(xpath).click() 

# 다음 단계
xpath = "//html/body/div[4]/table/tbody/tr/td[3]/div/div/div[6]/button[2]" 
driver.find_element_by_xpath(xpath).click() 