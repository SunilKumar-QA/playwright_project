from playwright.sync_api    import Page,expect

class EmployeePage:
    def __init__(self, page: Page):
        self.page = page
        # Navigation
        self.pim = page.get_by_text("PIM")
        self.add_employee_link = page.get_by_text("Add Employee")

        # Add Employee Fields
        self.first_name = page.get_by_placeholder("First Name")
        self.middle_name = page.get_by_placeholder("Middle Name")
        self.last_name = page.get_by_placeholder("Last Name")
        self.btn_save = page.get_by_role("button", name="Save")

        # Table & Details
        self.table_rows = page.locator("div.oxd-table-body > div.oxd-table-card")
        self.confirm_save_button = page.get_by_role("button", name="Save").nth(0)

    def goto_addEmp(self):
        self.pim.click()
        self.add_employee_link.click()

    def goto_employee_list(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")

    def fill_input(self, locator, value):
        locator.fill("")
        locator.fill(value)

    # def add_employee(self, fname, mname, lname):
    #     self.fill_input(self.first_name, fname)
    #     self.fill_input(self.middle_name, mname)
    #     self.fill_input(self.last_name, lname)

    #     # Capture employee ID before saving
    #     self.saved_employee_id = self.page.locator("input.oxd-input").nth(4).input_value()

    #     self.btn_save.click()
    #     self.page.wait_for_selector("text=Personal Details")
    #     self.confirm_save_button.click()

    def search_employee_by_id(self, emp_id):
        self.goto_employee_list()
        self.page.locator("input.oxd-input").nth(1).fill(emp_id)
        self.page.wait_for_timeout(1000)
        self.page.get_by_role("button", name="Search").click()
        self.page.wait_for_timeout(1000)

    def add_employee(self, fname, mname, lname):
        while True:
            self.fill_input(self.first_name, fname)
            self.fill_input(self.middle_name, mname)
            self.fill_input(self.last_name, lname)

            self.saved_employee_id = self.page.locator("input.oxd-input").nth(4).input_value()

            self.btn_save.click()
            self.page.wait_for_timeout(2000)

            try:
                self.page.wait_for_selector("text=Employee Id already exists", timeout=2000)
                print("⚠️ Duplicate Employee ID. Reloading page...")
                self.page.reload()
                self.page.wait_for_timeout(2000)
            except:
                self.page.wait_for_selector("text=Personal Details", timeout=5000)
                self.confirm_save_button.click()
                break

    
    def find_row_by_employee_id(self, emp_id):
        try:
            row = self.page.locator("div.oxd-table-body > div.oxd-table-card").first
            name = row.locator("div.oxd-table-cell").nth(2).inner_text()
            return name
        except:
            return None


    def edit_employee(self, emp_id, new_first, new_last):
        self.search_employee_by_id(emp_id)
        self.table_rows.first.click()
        self.page.wait_for_timeout(1000)
        self.fill_input(self.page.locator("input[name='firstName']"), new_first)
        self.fill_input(self.page.locator("input[name='lastName']"), new_last)

        self.confirm_save_button.click()

        self.f_name = self.page.locator("input[name='firstName']").input_value()
        self.l_name = self.page.locator("input[name='lastName']").input_value()

    def delete_employee(self,emp_id):    
        self.search_employee_by_id(emp_id)
        self.page.wait_for_timeout(1000)
        self.page.locator("button:has(i.bi-trash)").click()
        self.page.wait_for_timeout(2000)
        self.page.get_by_role("button", name="Yes, Delete").click()
        self.page.wait_for_timeout(2000)
        self.search_employee_by_id(emp_id)
        expect(self.page.locator("span:has-text('No Records Found')")).to_be_visible(timeout=5000)

