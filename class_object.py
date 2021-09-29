class Empolyee:
    def __init__(self, empid, empname, empsal, empdept):
        self.empid = empid
        self.empname = empname
        self.empsal = empsal
        self.empdept = empdept

    def details(self):
        print("Employee id:", self.empid)
        print("Employee name:", self.empname)
        print("Employee salary:", self.empsal)
        print("Employee department:", self.empdept)

class Timesheet:
    def __init__(self, date, no_hrs, activity, description, status):
        self.date = date
        self.no_hrs = no_hrs
        self.activity = activity
        self.description = description
        self.status = status


    def createtimesheet(self):
        print("date:", self.date)
        print("no_hrs:", self.no_hrs)
        print("activityy:", self.activity)
        print("description:", self.description)
        print("status:", self.status)