import csv
import os

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        file_ext = os.path.splitext(self.photo_file_name)
        return file_ext


class Car(CarBase):
    def __init__(self, brand, passenger_seats_count, photo_file_name, carrying):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__( brand, photo_file_name, carrying)
        self.body_whl = body_whl.split("x")
        self.body_width = float(self.body_whl[0])
        self.body_height = float(self.body_whl[1])
        self.body_length = float(self.body_whl[2])

    def get_body_volume(self):
        body_volume = self.body_height*self.body_length*self.body_width
        return body_volume


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        pass


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader) #пропускаем заголовок
        for row in reader:
            try:
                pass
            except Exception:
                pass
    return car_list
car = Car(brand = "djhfgv", photo_file_name = "coursera_week3_cars.csv", carrying = "2.5", passenger_seats_count = "5" )
print(car.get_photo_file_ext())
print(get_car_list("coursera_week3_cars.csv"))
