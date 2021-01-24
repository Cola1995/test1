from selenium import webdriver


chrome_capabilities = {
    "browserName": "chrome",        # 浏览器名称
    "version": "",                  # 操作系统版本
    "platform": "ANY",              # 平台，这里可以是windows、linux、andriod等等
    "javascriptEnabled": True,      # 是否启用js
}
driver = webdriver.Remote("http://localhost:4444/wd/hub", desired_capabilities=chrome_capabilities)
driver.get("http://www.baidu.com")
print(driver.title)

# 运行一次结束
