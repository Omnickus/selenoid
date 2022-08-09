import pytest
import allure


from src.object_registration import Registration

@allure.step
@allure.issue('JIRA-3813')
@pytest.mark.registration
def test_registration_page(browser):
    Registration(browser=browser).registration_user()



