from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions() # chrome浏览器配置
# options = webdriver.FirefoxOptions() # firefox浏览器配置 
# options = webdriver.EpiphanyOptions() # epiphany-browser浏览器配置

# options.add_argument("--headless")  # 无头模式，后台运行
options.add_argument("--disable-gpu")  # 禁用GPU加速
options.add_argument("--no-sandbox")  # 无沙盒模式
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

t = 10  # 设置等待时间

driver.get("https://www.pailixiang.com/album_ia6216703860.html")
time.sleep(t)

# 查看第一张图片
view_button = driver.find_element(By.XPATH, '//*[@id="ulPhoto"]/li[1]')
view_button.click()
time.sleep(t)

# 下载
for i in range(518):
    print(f"当前为第{i+1}张图片")

    download_button = driver.find_element(By.ID, "download")
    driver.execute_script("arguments[0].setAttribute('onclick', 'downloadPhoto({})')".format(i), download_button)
    download_button.click()
    time.sleep(t)

    print(f"第{i+1}张图片下载完成")

driver.quit()