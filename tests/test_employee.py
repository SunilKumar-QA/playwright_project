from playwright.sync_api import Page, expect
from pages.LoginPage import LoginPage
from pages.EmployeePage import EmployeePage


def test_add_employee(new_employee): # Using "new_employee" fixture.
    employee_page, emp_id = new_employee
    employee_page.search_employee_by_id(emp_id)
    full_name = employee_page.find_row_by_employee_id(emp_id)

    assert full_name is not None, f"❌ Employee ID {emp_id} not found in table"
    assert full_name == "Akshay Kumar", f"❌ Full name mismatch: found '{full_name}'"


def test_edit_employee(new_employee):
    employee_page, emp_id = new_employee
    employee_page.edit_employee(emp_id, "Sunil", "Lohana")

    # Optional: Add assertion to verify name change
    first_name = employee_page.f_name
    last_name = employee_page.l_name
    
    assert "Sunil" in first_name, "❌ Name edit not reflected in UI." 
    assert "Lohana" in last_name, "❌ Name edit not reflected in UI."

def test_delete_employee(new_employee):
    employee_page, emp_id = new_employee
    employee_page.delete_employee(emp_id)
