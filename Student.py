import StudentClass as s
from datetime import date


def main():
    kid = s.Student("1", "Billy", date(2000, 2, 21), "Sr")

    print("Age:", kid.get_age(), "\nRegistration:", kid.get_registration())


main()
