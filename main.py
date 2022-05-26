from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    assert browser.find_element(By.XPATH, "//button[@value]").text == 'Add to basket'

