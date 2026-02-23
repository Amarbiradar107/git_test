import time

import pytest
# @pytest.mark.skip
class Test_Login:
    def test_login(self, setup):
        driver = setup
        time.sleep(5)
        print(driver.title)
