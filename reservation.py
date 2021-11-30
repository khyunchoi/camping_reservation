from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import time

url = 'https://camping.gtdc.or.kr/DZ_reservation/reserCamping_v3.php?xch=reservation&xid=camping_reservation&step=Areas&sdate=202112' # 목적 홈페이지 주소
driver_url = 'C:/Users/khyun/OneDrive/바탕 화면/toy_project/camping_reservation/chromedriver.exe' # chromedriver 파일 주소

def check_time():
    driver_time = webdriver.Chrome(driver_url)
    driver_time.get('https://time.navyism.com/?host=camping.gtdc.or.kr') # 네이비즘 캠핑장 주소

    # 밀리세컨드 체크
    xpath = "//input[@id='msec_check']"
    driver_time.find_element(By.XPATH, xpath).click()

    while True:
        xpath = "//div[@id='time_area']"
        a = driver_time.find_element(By.XPATH, xpath).text
        xpath = "//div[@id='msec_area']"
        b = driver_time.find_element(By.XPATH, xpath).text

        current_time = re.findall('[0-9]+', a)
        # current_time[3] 시, current_time[4] 분, current_time[5] 초
        if(current_time[3] == '10' and current_time[4] == '00' and current_time[5] == '00'):
            msec = re.findall('[0-9]+', b)

            if(int(msec[0]) >= 0):
                print(msec[0])
                # 드라이버 실행
                driver = webdriver.Chrome(driver_url)
                driver.get(url)

                # 화면 최대화
                # driver.maximize_window()

                # 팝업 제거
                driver.find_element(By.CSS_SELECTOR, '.btn-dark').click()

                # 날짜 지정
                xpath = "//button[@value='D:2021-12-31']"
                driver.find_element(By.XPATH, xpath).click()
                time.sleep(0.1)

                # 구역 지정
                xpath = "//html/body/div[4]/table/tbody/tr/td[3]/div/div/div[4]/div/button[2]" 
                driver.find_element(By.XPATH, xpath).click()

                # 인원 지정
                xpath = "//html/body/div[4]/table/tbody/tr/td[3]/div/div/table[1]/tbody/tr/td[4]/select/option[3]" 
                driver.find_element(By.XPATH, xpath).click()

                # 예약 기간
                xpath = "//html/body/div[4]/table/tbody/tr/td[3]/div/div/div[5]/select/option[2]" 
                driver.find_element(By.XPATH, xpath).click()

                # 다음 단계
                xpath = "//html/body/div[4]/table/tbody/tr/td[3]/div/div/div[6]/button[2]" 
                driver.find_element(By.XPATH, xpath).click()
                

# 함수 실행
check_time()