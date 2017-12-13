from datetime import timedelta, datetime

class Employee(object):
	"""docstring for Employee"""
	def register(self, name, email):
		return {"name": name, "email": email}

	def holiday_period(self, setoff_date):
		date = datetime.strptime(setoff_date, "%Y/%m/%d")
		modified_date = date + timedelta(days=30)

		return datetime.strftime(modified_date, "%Y/%m/%d")