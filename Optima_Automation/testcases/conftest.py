import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from ..pages.login_page import LoginPage
from ..utilities.read_excel import Utils

filename = 'Optima_Automation/testdata/usercradentials.xlsx'

testdata = Utils.read_data_from_excel(filename, "Cradentials")



@pytest.fixture(scope="function", params=testdata)
def setup(request):
    # if browser == "chrome":
    #     driver = webdriver.Chrome()
    # elif browser == "firefox":
    #     driver = webdriver.Firefox()
    # elif browser == "edge":
    #     driver = webdriver.Edge()
    # driver.maximize_window()
    options = Options()
    # options.add_argument("--log-level=3")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    username, password = request.param
    driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
    driver.maximize_window()
    driver.get("https://optimahp-qa.kellton.net/")
    login_page = LoginPage(driver)
    login_page.login(username, password)

    yield driver
    driver.quit()

# ut = Utils()
# testdata = ut.read_data_from_excel("testdata/usercradentials.xlsx",)
# @pytest.fixture(params=testdata)
# # @pytest.mark.parametrize("username,password", testdata)
# def login_test(request, setup,username,password):
#     driver = setup
#     driver.get("https://optimahp-qa.kellton.net/")
#     login_page = LoginPage(driver)
#     login_page.login(username,password)# Replace with the actual login URL
#     return driver
