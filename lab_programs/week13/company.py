# 1) Write a program creating a class called company. Create attributed called name, turnover,
# revenue and number of employees working in company. Also write a method that calculates the
# revenue generated per employee called productivity
class Company:
    name = "ABC"
    turnover = 500000
    revenue = 100000
    no_of_emp = 10

    def productivity(self):
        return self.revenue/self.no_of_emp


c1 = Company()
print(c1.productivity())
