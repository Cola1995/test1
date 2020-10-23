import os
import pickle
import random
import string
import time

from PIL import Image

from lib.ShowapiRequest import ShowapiRequest

def get_logger():
    import logging
    import logging.handlers
    import datetime

    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)

    rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7,
                                                           atTime=datetime.time(0, 0, 0, 0))
    rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

    f_handler = logging.FileHandler('error.log')
    f_handler.setLevel(logging.ERROR)
    f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))


    # 设置日志控制台输出
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))
    logger.addHandler(console)

    logger.addHandler(rf_handler)
    logger.addHandler(f_handler)
    return logger


def get_code(driver, id):
    # 获取验证码图片
    t = time.time()
    path  = os.path.dirname(os.path.dirname(__file__))+"\\screenshots"  # 获取项目截图类路径
    pic_name = path + '\\'+str(t) + ".png"
    driver.save_screenshot(pic_name)
    # time.sleep(2)
    ce = driver.find_element_by_id(id)
    #print(ce.location)
    left = ce.location['x']
    top = ce.location['y']
    right = ce.size['width'] + left
    height = ce.size['height'] + top
    #print(left, top, height, right)
    im = Image.open(pic_name)
    #   560 448
    # 获取windows分辨率缩放比例
    dpr = driver.execute_script('return window.devicePixelRatio')
    img = im.crop((left*dpr, top*dpr, right*dpr, height*dpr))
    #     img = im.crop((783,470,108,height))

    t = time.time()

    pic_name2 = path + '\\' + str(t) + ".png"
    img.save(pic_name2)

    # r = ShowapiRequest("http://route.showapi.com/184-4", "328507", "e8bbff9dba8f43aeb834652b8959844b")   # hero
    r = ShowapiRequest("http://route.showapi.com/184-4", "272526", "a924de982ae404b8a068b4d1c7784f2")

    r.addFilePara("image", pic_name2)
    r.addBodyPara("typeId", "34")
    r.addBodyPara("convert_to_jpg", "0")
    r.addBodyPara("needMorePrecise", "0")
    res = r.post()
    # https://www.showapi.com/apiGateway/view/?apiCode=184&pointCode=4  api后台
    print(res.text)   # 打印万源接口返回信息
    text = res.json()['showapi_res_body']
    code = text['Result']
    return code


# 生成随机字符串
def gen_random_str():
    rand_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    return rand_str

def save_cookie(driver, path):
    with open(path, 'wb') as filehandler:
        cookies = driver.get_cookies()
        print(cookies)
        pickle.dump(cookies, filehandler)


def load_cookie(driver, path):
    with open(path, 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookie)