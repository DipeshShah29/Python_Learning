# To check whether an Employee has achieved a weekly sales target or not
# Take input from users as Name and Sales target per week


class Employee:
    def __init__(self, name, target):
        self.name = name
        self.target = target

    def hasTargetAchieved(self):
        if self.target >= 6:
            print("The weekly target has been achieved by", self.name)
        else:
            print("The weekly target has not been achieved by", self.name)


employee1 = Employee("Dipesh", 6)
employee1.hasTargetAchieved()

# Using **kwargs (keyword arguments)
class EmployeeArgs:
    def hasTargetAchievedNew(self, **params):
        if params["target"] >= 6:
            print("The weekly target has been achieved by", params["name"])
        else:
            print(
                "The weekly target has not been achieved by {0} for month {1}".format(
                    params["name"], params["month"]
                )
            )


employee2 = EmployeeArgs()
employee2.hasTargetAchievedNew(name="Dev", target=4, month="April")
employee2.hasTargetAchievedNew(name="Admin", target=7)

# Using Dictionary as a parameter object
class EmployeeDict:
    def hasTargetAchievedDict(self, dict):
        from datetime import datetime
        import calendar

        if calendar.month_name[datetime.today().month] == dict["Month"]:
            for key in dict:
                print(key, dict[key])


value = {"Name": "Dipesh", "Target": 6, "Month": "April"}
e1 = EmployeeDict()
e1.hasTargetAchievedDict(value)
