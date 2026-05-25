from appium import webdriver
from appium.options.android import UiAutomator2Options

def test_login_screen_opens():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.app_package = "com.example.app"
    options.app_activity = ".MainActivity"

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    try:
        assert driver.find_element("accessibility id", "Login").is_displayed()
    finally:
        driver.quit()
