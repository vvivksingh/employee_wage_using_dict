import random

IS_ABSENT = 0
IS_PRESENT_FULL_DAY = 1
IS_PRESENT_PART_TIME = 2
FULL_DAY_HOURS = 8
PART_TIME_HOURS = 4


class Employee:

    def __init__(self, ename, emp_working_hour, emp_wage_per_hour):
        self.ename = ename
        self.emp_working_hour = emp_working_hour
        self.emp_wage_per_hour = emp_wage_per_hour

    @staticmethod
    def check_emp_working_hours(check_emp):
        emp_attendence = {
            IS_PRESENT_FULL_DAY: FULL_DAY_HOURS,
            IS_PRESENT_PART_TIME: PART_TIME_HOURS,
            IS_ABSENT: 0
        }
        return emp_attendence.get(check_emp)

    def calculate_wage(self):
        global daily_wage
        working_days = 0
        working_hours = 0
        total_wage = 0
        while working_days < comp_max_working_day and working_hours < comp_max_working_hrs:  # Calculating wages for month

            employee_working_hours = self.check_emp_working_hours(check_emp)
            daily_wage = self.emp_wage_per_hour * employee_working_hours
            working_days += 1
            working_hours += employee_working_hours
            total_wage = total_wage + daily_wage
        return total_wage


class Company:

    def __init__(self, cname, maximum_working_hour, maximum_monthly_working_day):
        self.cname = cname
        self.maximum_working_hour = maximum_working_hour
        self.maximum_monthly_working_day = maximum_monthly_working_day

    def add_employee(self, emp_name):
        employee_dict[emp_name] = employee_obj

    def add_company(self, com_name):
        company_dict[com_name] = employee_obj


if __name__ == '__main__':
    check_emp = random.randrange(0, 2)
    emp_hour = Employee.check_emp_working_hours(check_emp)
    employee_dict = {}
    company_dict = {}

    while True:
        print("Choose operation you want to perform :- ")
        print("1 -> Add Employee")
        print("2 -> Quit")

        options = int(input("Enter your choice :- "))
        if options == 1:
            comp_name = input("Enter company name :- ")
            comp_max_working_hrs = int(input("Enter maximum working hour set by the company:- "))
            comp_max_working_day = int(input("Enter maximum no. of days a employee have to work:- "))
            wage_per_hour = int(input("Enter wage per hour of employee:- "))
            employee_name = input("Enter employee name:- ")
            employee_obj = Employee(employee_name, emp_hour, wage_per_hour)
            company_obj = Company(comp_name, comp_max_working_hrs, comp_max_working_day)
            company_obj.add_employee(employee_name)
            company_obj.add_company(comp_name)
            print(employee_dict)
            print(company_dict)
            print(f" Total wage of the employee is : INR ₹ {employee_dict.get(employee_name).calculate_wage()}")

        else:
            break