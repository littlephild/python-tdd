import unittest
from datetime import datetime, timedelta
from modules.employee import Employee

class EmployeeHoliday(unittest.TestCase):
    """docstring for EmployeeHoliday"""

    def SetUp():
        print("Christmas Employee Holiday Registration")

    def TearDown():
        pass


    def test_is_employee_registered(self):
        workers = Employee()
        self.assertTrue({"name": 'Ronald', 'email': "ronald@s8works.com"},
                        workers.register('Ronald', 'ronald@s8works.com'))

    def test_christmas_holiday_end_date(self):
        workers = Employee()
        current_date = datetime.now()
        self.assertTrue("2018/01/16",
                         workers.holiday_period("2017/12/17") )

if __name__ == '__main__':
    unittest.main()
