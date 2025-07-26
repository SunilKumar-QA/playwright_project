import pytest
from playwright.sync_api import sync_playwright
from pages.LoginPage import LoginPage
from pages.EmployeePage import EmployeePage

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture(scope="function")
def logged_in_page(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("Admin", "admin123")
    return page

@pytest.fixture
def new_employee(logged_in_page):
    employee_page = EmployeePage(logged_in_page)
    employee_page.goto_addEmp()
    employee_page.add_employee("Akshay", "Kumar", "Kotwani")
    emp_id = employee_page.saved_employee_id
    return employee_page, emp_id 