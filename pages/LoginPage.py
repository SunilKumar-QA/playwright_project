from playwright.sync_api import Page
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.locator('input[name="username"]')
        self.password = page.locator('input[name="password"]')
        self.login_btn = page.locator('button[type="submit"]')
        self.dashboard = page.locator("h6:has-text('Dashboard')")
        self.error_message = page.locator("text=Invalid credentials")
        self.required_message = page.locator("text=Required")
        self.drp = page.locator("span.oxd-userdropdown-tab")
        self.btn_logout = page.locator("a", has_text="Logout")


    def load(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_btn.click()

    def logout(self):
        self.drp.click() 
        self.btn_logout.click()   

    