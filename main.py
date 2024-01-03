# У нас есть класс Дата и есть класс Расписание,
# которые использует в себе класс Дата.
# Реализовать переопределение арифметических операций,
# логических операций + определить даты,
# на которые приходится больше всего занятий

import datetime


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def print_(self):
        print(f'{self.day}/{self.month}/{self.year}')

    def date_calculator(self, days):
        if days == 0:
            return self
        while days != 0:
            if (self.month == 1 or self.month == 3 or self.month == 5 or self.month == 7
                    or self.month == 8 or self.month == 10 or self.month == 12):
                if self.day + days > 31:
                    box = 31 - self.day
                    days = days - box
                    if self.month + 1 > 12:
                        self.month = 1
                        self.year = self.year + 1
                    else:
                        self.month = self.month + 1
                    self.day = 0

                elif self.day + days < 1:
                    days = days + self.day
                    if self.month - 1 < 1:
                        self.month = 12
                        self.year = self.year - 1
                    else:
                        self.month = self.month - 1
                    if (self.month == 1 or self.month == 3 or self.month == 5 or self.month == 7
                            or self.month == 8 or self.month == 10 or self.month == 12):
                        self.day = 31
                    if self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11:
                        self.day = 30
                    if self.month == 2:
                        if self.year % 4 == 0:
                            self.day = 29
                        else:
                            self.day = 28

                else:
                    self.day = self.day + days
                    days = 0

            if self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11:
                if self.day + days > 30:
                    box = 30 - self.day
                    days = days - box
                    self.month = self.month + 1
                    self.day = 0

                elif self.day + days < 1:
                    days = days + self.day
                    # if self.month - 1 < 1:
                    #     self.month = 12
                    #     self.year = self.year - 1
                    # else:
                    self.month = self.month - 1
                    if (self.month == 1 or self.month == 3 or self.month == 5 or self.month == 7
                            or self.month == 8 or self.month == 10 or self.month == 12):
                        self.day = 31
                    if self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11:
                        self.day = 30
                    if self.month == 2:
                        if self.year % 4 == 0:
                            self.day = 29
                        else:
                            self.day = 28

                else:
                    self.day = self.day + days
                    days = 0

            if self.month == 2:
                if self.year % 4 == 0:
                    if self.day + days > 29:
                        box = 29 - self.day
                        days = days - box
                        self.month = self.month + 1
                        self.day = 0

                    elif self.day + days < 1:
                        days = days + self.day
                        # if self.month - 1 < 1:
                        #     self.month = 12
                        #     self.year = self.year - 1
                        # else:
                        self.month = self.month - 1
                        if (self.month == 1 or self.month == 3 or self.month == 5 or self.month == 7
                                or self.month == 8 or self.month == 10 or self.month == 12):
                            self.day = 31
                        if self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11:
                            self.day = 30
                        if self.month == 2:
                            if self.year % 4 == 0:
                                self.day = 29
                            else:
                                self.day = 28

                    else:
                        self.day = self.day + days
                        days = 0
                else:
                    if self.day + days > 28:
                        box = 28 - self.day
                        days = days - box
                        self.month = self.month + 1
                        self.day = 0

                    elif self.day + days < 1:
                        days = days + self.day
                        # if self.month - 1 < 1:
                        #     self.month = 12
                        #     self.year = self.year - 1
                        # else:
                        self.month = self.month - 1
                        if (self.month == 1 or self.month == 3 or self.month == 5 or self.month == 7
                                or self.month == 8 or self.month == 10 or self.month == 12):
                            self.day = 31
                        if self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11:
                            self.day = 30
                        if self.month == 2:
                            if self.year % 4 == 0:
                                self.day = 29
                            else:
                                self.day = 28

                    else:
                        self.day = self.day + days
                        days = 0
        return self

    def __add__(self, other):
        return self.date_calculator(other)

    def __sub__(self, other):
        return self.date_calculator(-other)

    def __gt__(self, other):
        if self.year > other.year:
            return True
        elif self.year < other.year:
            return False
        elif self.year == other.year:
            if self.month > other.month:
                return True
            elif self.month < other.month:
                return False
            elif self.month == other.month:
                if self.day > other.day:
                    return True
                elif self.day < other.day:
                    return False
                elif self.day == other.day:
                    return False

    def __ge__(self, other):
        if self.year >= other.year:
            return True
        elif self.year <= other.year:
            return False
        elif self.year == other.year:
            if self.month >= other.month:
                return True
            elif self.month <= other.month:
                return False
            elif self.month == other.month:
                if self.day >= other.day:
                    return True
                elif self.day <= other.day:
                    return False
                elif self.day == other.day:
                    return False

    def __lt__(self, other):
        if self.year < other.year:
            return True
        elif self.year > other.year:
            return False
        elif self.year == other.year:
            if self.month < other.month:
                return True
            elif self.month > other.month:
                return False
            elif self.month == other.month:
                if self.day < other.day:
                    return True
                elif self.day > other.day:
                    return False
                elif self.day == other.day:
                    return False

    def __le__(self, other):
        if self.year <= other.year:
            return True
        elif self.year >= other.year:
            return False
        elif self.year == other.year:
            if self.month <= other.month:
                return True
            elif self.month >= other.month:
                return False
            elif self.month == other.month:
                if self.day <= other.day:
                    return True
                elif self.day >= other.day:
                    return False
                elif self.day == other.day:
                    return False

    def __eq__(self, other):
        return self.year == other.year and self.month == other.month and self.day == other.day

    def __ne__(self, other):
        return self.year != other.year and self.month != other.month and self.day != other.day


class Day:
    def __init__(self, list, d, m, y):
        self.list = list
        self.date = Date(d, m, y)
        self.week_day = datetime.datetime(y, m, d).weekday()

    def print_(self):
        self.date.print_()
        print(self.list)

    def __add__(self, other):
        self.date + other
        self.week_day = datetime.datetime(self.date.year, self.date.month, self.date.day).weekday()
        return self

    def __sub__(self, other):
        self.date - other
        self.week_day = datetime.datetime(self.date.year, self.date.month, self.date.day).weekday()
        return self

    def __gt__(self, other):
        return len(self.list) > len(other.list)

    def __lt__(self, other):
        return len(self.list) < len(other.list)

    def __eq__(self, other):
        return len(self.list) == len(other.list)


class Timetable:

    def __init__(self, days=[
        Day(['Физкультура', 'Математика', 'Физика', 'Информатика', 'ОБЖ', 'Труды', 'Биология'], 29, 11, 2021),
        Day(['Русский', 'Литература', 'Английский', 'Химия', 'Астрономия'], 30, 11, 2021),
        Day(['Музыка', 'Обществознание', 'Математика', 'Математика'], 1, 12, 2021),
        Day(['Физика', 'Физика', 'Информатика', 'Черчение'], 2, 12, 2021),
        Day(['Математика', 'Физика', 'Информатика', 'Биология', 'География'], 3, 12, 2021),
        Day(['Математика', 'Физика', 'Информатика', 'География', 'Биология'], 4, 12, 2021),
        Day([''], 5, 12, 2021)
    ]):
        self.days = days

    def find_day(self, d, m, y):
        new_day = None
        week_day = datetime.datetime(y, m, d).weekday()
        for day in self.days:
            if day.week_day == week_day:
                new_day = day
                break
        new_day.date = Date(d, m, y)
        new_day.print_()

    def find_max(self):
        max_day = max(self.days)
        max_day.print_()

    def what_will(self, week_day, count_days):
        new_day = None
        for day in self.days:
            if day.week_day == week_day:
                new_day = day
                break
        new_day = new_day + count_days
        new_day.print_()


timetable = Timetable()
# timetable.find_day(5, 12, 2021)
# timetable.find_max()
# timetable.what_will(0, 4)

date1 = Date(1, 3, 2020)
date1 = date1 + 364
date1.print_()
# date2 = Date(10,11,2021)
