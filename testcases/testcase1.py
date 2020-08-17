from selenium import webdriver
from PIL import Image
import time
import pytesseract

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
#   560 448
    img = im.crop((left,top,right,height))
#     img = im.crop((783,470,108,height))

    t = time.time()

    pic_name2 = str(t)+".png"
    img.save(pic_name2)
    browser.close()


def test1():
    imge1 = Image.open('qq.jpg')
    str = pytesseract.image_to_string(imge1)
    print(str)


def test2():
    # https://www.showapi.com/apiGateway/view/?apiCode=184&pointCode=4
    #from ShowapiRequest import ShowapiRequest
    from lib.ShowapiRequest import ShowapiRequest
    # r = ShowapiRequest("http://route.showapi.com/184-4", "272526", "a924d4e982ae404b8a068b4d1c7784f2")
    # r.addFilePara("image", "test.png")
    # r.addBodyPara("typeId", "34")
    # r.addBodyPara("convert_to_jpg", "0")
    # r.addBodyPara("needMorePrecise", "0")
    # res = r.post()
    # print(res.text)  # 返回信息
    # print(res.json()['showapi-res_body'])
    r = ShowapiRequest("http://route.showapi.com/184-4", "328507", "e8bbff9dba8f43aeb834652b8959844b")
    r.addFilePara("image", "test.png")
    r.addBodyPara("typeId", "34")
    r.addBodyPara("convert_to_jpg", "0")
    r.addBodyPara("needMorePrecise", "0")
    res = r.post()
    result = res.text
    print(result)
    body = res.json()['showapi_res_body']
    print(body['Result'])

