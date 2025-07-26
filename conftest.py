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

#---------------- Cross Browser ---------------

# import pytest
# from playwright.sync_api import sync_playwright
# from pages.LoginPage import LoginPage
# from pages.EmployeePage import EmployeePage

# # Cross-browser support: parametrize the browser type
# @pytest.fixture(params=["chromium", "firefox", "webkit"], scope="session")
# def browser_type_launch_args(request):
#     return request.param

# # Launch browser instance based on type
# @pytest.fixture(scope="session")
# def browser(browser_type_launch_args):
#     with sync_playwright() as p:
#         browser_type = getattr(p, browser_type_launch_args)
#         browser = browser_type.launch(headless=False)
#         yield browser
#         browser.close()

# # New browser context and page for each test function
# @pytest.fixture(scope="function")
# def page(browser):
#     context = browser.new_context(
#         viewport={"width": 1920, "height": 1080}  # simulate full screen
#     )
#     page = context.new_page()
#     yield page
#     context.close()

# # Fixture to log in to the system before test
# @pytest.fixture(scope="function")
# def logged_in_page(page):
#     login_page = LoginPage(page)
#     login_page.load()
#     login_page.login("Admin", "admin123")
#     return page

# # Fixture to add a new employee before test
# @pytest.fixture
# def new_employee(logged_in_page):
#     employee_page = EmployeePage(logged_in_page)
#     employee_page.goto_addEmp()
#     employee_page.add_employee("Akshay", "Kumar", "Kotwani")
#     emp_id = employee_page.saved_employee_id
#     return employee_page, emp_id

