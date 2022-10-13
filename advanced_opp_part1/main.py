# from datetime import datetime

# time_data = "25/05/99 02:35:5.523"
 
# # format the string in the given format :
# # day/month/year hours/minutes/seconds-micro
# # seconds
# format_data = "%d/%m/%y %H:%M:%S.%f"

# date_obj1 = datetime(1999, 5, 25, 2,35, 5)
# date_obj2 = datetime.strptime(time_data, format_data)

# print(date_obj1)
# print(date_obj2)


class Employee:
    working_time = '10:00-19:00'

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @classmethod
    def change_working_time(cls, new_working_time):
        cls.working_time = new_working_time

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    @classmethod
    def full_name_parser(cls, full_name):
        name, surname = full_name.split(',')
        return cls(name, surname)



idris_fullname = input('Ad, Soyad')
ferid_fullname = input('Ad, Soyad')


ferid = Employee.full_name_parser(idris_fullname)
idris = Employee.full_name_parser(ferid_fullname)

print(ferid.get_full_name())
print(idris.get_full_name())