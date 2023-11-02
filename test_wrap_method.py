from abc import ABC, abstractmethod
from typing import List


class Employee:

    # more code ...

    def pay(self):
        amount: Money = new Money()
        for card in timecards:
            if pay_period.contains(date):
                amount.add(card.getHours() * pay_ate)
        self.pay_dispatcher.pay(self, date, amount)


# TODO:
# Every time that we pay an employee, we have to update a ﬁle with the employee’s name
# so that it can be sent off to some reporting software.



class Employee:

    # more code ...

    def dispatch_payment(self):
        amount: Money = new Money()
        for card in timecards:
            if pay_period.contains(date):
                amount.add(card.getHours() * pay_ate)
        self.pay_dispatcher.pay(self, date, amount)

    def pay(self):
        self.log_payment()
        self.dispatch_payment()

    def log_payment(self):
        pass




# OR
# We can give users the option of paying in either way

class Employee:

    # more code ...

    def pay(self):
        amount: Money = new Money()
        for card in timecards:
            if pay_period.contains(date):
                amount.add(card.getHours() * pay_ate)
        self.pay_dispatcher.pay(self, date, amount)

    def make_logged_payment(self):
        self.log_payment()
        self.pay()

    def log_payment(self):
        pass
