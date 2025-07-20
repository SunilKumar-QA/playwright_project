from playwright.sync_api import Page, expect
from pages.LoginPage import LoginPage

def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("Admin", "admin123")
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    login_page.logout()
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("Admin", "admin")
    expect(login_page.error_message).to_be_visible()

def test_login_empty_fields(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("", "")
    expect(login_page.required_message.nth(0)).to_be_visible()
    expect(login_page.required_message.nth(1)).to_be_visible()   
    
    
