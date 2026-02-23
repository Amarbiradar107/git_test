# from pages.customer_management_page import CustomerManagementPage
from ..pages.customer_management_page import CustomerManagementPage
from ..utilities.read_excel import Utils
import pytest

class Test_CustomerManagement:

    # added by amar

    test_data = Utils.read_data_from_excel("Optima_Automation/testdata/customer_management_data.xlsx", "customer_data")
    @pytest.mark.parametrize("test_data", test_data)
    # @pytest.mark.skip
    def test_create_customer(self,setup, test_data):
        self.driver = setup
        print(test_data)
        self.customer_management_pages = CustomerManagementPage(self.driver)
        self.customer_management_pages.navigate_to_customer_management()
        self.customer_management_pages.create_customer(test_data)


    test_data_search=Utils.read_data_from_excel("Optima_Automation/testdata/Search_parameter.xlsx","search_parameter")
    @pytest.mark.parametrize("test_data", test_data_search)
    def test_customer_search_parameter(self,setup,test_data):
        self.driver = setup
        print(test_data)
        self.customer_management_pages = CustomerManagementPage(self.driver)
        self.customer_management_pages.search_parameter(test_data)


        # Add assertions to verify customer creation
        # Add assertions or further actions as needed



