import pytest
import os

from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.safari.service import Service as SafariService


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default='http://bitnami/')
    parser.addoption("--drivers", action="store", default=os.path.expanduser("~/drivers"))
    parser.addoption("--executor", action="store", default=None)
    parser.addoption("--vnc", action="store_true", default=True)
    parser.addoption("--logs", action="store_true", default=True)
    parser.addoption("--videos", action="store_true", default=True)
    parser.addoption("--bv")


@pytest.fixture
def browser(request):
    # Сбор параметров запуска для pytest
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    driver = request.config.getoption("--drivers")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bv")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")

    if executor == None:
        if browser == "chrome":
            service = ChromiumService(executable_path=driver + "/chromedriver")
            try:
                driver = webdriver.Chrome(service=service)
            except Exception as e:
                options = webdriver.ChromeOptions()
                driver_path = driver + "/chrome/chromedriver"
                driver = webdriver.Chrome(  
                                        executable_path = driver_path,
                                        options = options
                                    )
        elif browser == "firefox":
            service = FFService(executable_path=driver + "/geckodriver")
            try:
                driver = webdriver.Firefox(service=service)
            except Exception as e:
                options = webdriver.FirefoxOptions()
                driver_path = driver + "/geckodriver"
                driver = webdriver.Chrome(  
                                        executable_path = driver_path,
                                        options = options
                                    )
        elif browser == "Edge":
            service = EdgeService(executable_path=driver + "/edge")
            try:
                driver = webdriver.Edge(service=service)
            except Exception as e:
                options = webdriver.FirefoxOptions()
                driver_path = driver + "/edge"
                driver = webdriver.Chrome(  
                                        executable_path = driver_path,
                                        options = options
                                    )
        else:
            driver = SafariService()
    else:
        executor_url = f"http://{executor}:4444/wd/hub"
        capabilities = {
            "browserName": browser,
            "browserVersion": version,
            "selenoid:options": {
                "enableVNC": vnc,
                "enableVideo": videos,
                "enableLog": logs
            }
        }   
        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=capabilities,
        )

    driver.maximize_window()

    #request.addfinalizer(driver.close)
    def fin():
        driver.quit()

    request.addfinalizer(fin)

    driver.get(url)
    driver.url = url


    return driver
