import csv
import os



class CarBase:
    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        self.car_type = car_type

    def get_photo_file_ext(self):
        file_ext = os.path.splitext(self._photo_file_name)
        return file_ext



class Car(CarBase):
    def __init__(self, car_type, brand, passenger_seats_count, photo_file_name, carrying):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count



class Truck(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, body_whl):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.body_whl = body_whl
    def body_whl(self):
        return type(self._body_whl)


class SpecMachine(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        pass


def get_car_list(csv_filename):
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader) #пропускаем заголовок
        for row in reader:
            print(row)
    return

print(get_car_list("coursera_week3_cars.csv"))
