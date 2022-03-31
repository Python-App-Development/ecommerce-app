import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def chrome_browser_instance(request):
    """
    chrome browser web driver instance
    """
    options = Options()
    options.headless = False
    browser = webdriver.Chrome(
        "/Users/muzammilpeer/chromedriver/chromedriver",
        chrome_options=options,
    )
    yield browser
    browser.close()
