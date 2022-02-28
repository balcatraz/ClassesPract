from datetime import date


class Student:
    def __init__(self, sid, name, dob, cl):
        self.__studentID = sid
        self.__name = name
        self.__dob = dob
        self.__classification = cl

        self.set_age()
        self.set_registration()

    def set_age(self):
        self.__age = date.today().year - self.__dob.year

    def set_registration(self):
        if self.__classification == "Sr":
            self.__registration = "4/1 thru 4/3"
        elif self.__classification == "Jr":
            self.__registration = "4/4 thru 4/6"
        elif self.__classification == "S":
            self.__registration = "4/7 thru 4/9"
        elif self.__classification == "F":
            self.__registration = "4/10 thru 4/12"
        else:
            self.__registration = "Invalid Classification"

    def get_age(self):
        return self.__age

    def get_registration(self):
        return self.__registration
