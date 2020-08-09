from selenium import webdriver
from PIL import Image
import time


def test():

    browser = webdriver.Chrome()
    browser.get("http://localhost:8080/jpress/user/register")
    browser.maximize_window()
    t = time.time()
    pic_name = str(t)+".png"
    browser.save_screenshot(pic_name)
    time.sleep(2)
    ce = browser.find_element_by_id("captchaimg")
    print(ce.location)
    left = ce.location['x']
    top = ce.location['y']
    right = ce.size['width']+left
    height = ce.size['height']+top
    print(left,top,height,right)
    im = Image.open(pic_name)

    img = im.crop((left,top,right,height))

    t = time.time()

    pic_name2 = str(t)+".png"
    img.save(pic_name2)
    browser.close()

