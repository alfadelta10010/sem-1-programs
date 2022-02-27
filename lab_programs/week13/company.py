class Company:
    name = "ABC"
    turnover = 500000
    revenue = 100000
    no_of_emp = 10

    def productivity(self):
        return self.revenue/self.no_of_emp


c1 = Company()
print(c1.productivity())
