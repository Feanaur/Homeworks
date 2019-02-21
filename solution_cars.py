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
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__( brand, photo_file_name, carrying)
        if body_whl == "":
            self.body_width = 0
            self.body_height = 0
            self.body_length = 0
        else:
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
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader) #пропускаем заголовок
        try:
            for row in reader:
                car_type = row[0]
                brand = row[1]
                passenger_seats_count = row[2]
                photo_file_name = row[3]
                body_whl = row[4]
                carrying = row[5]
                extra = row[6]
                if row[0] == "car":
                    car = Car(brand = brand, photo_file_name = photo_file_name, carrying = carrying, passenger_seats_count = passenger_seats_count)
                    car_list.append(car)
                if row[0] == "truck":
                    truck = Truck(brand = brand, photo_file_name = photo_file_name, carrying = carrying, body_whl = body_whl)
                    car_list.append(truck)
                if row[0] == "spec_machine":
                    spec_machine = SpecMachine(brand = brand, photo_file_name = photo_file_name, carrying = carrying, extra = extra)
                    car_list.append(spec_machine)
        except IndexError:
            pass
        return car_list
print(get_car_list("coursera_week3_cars.csv"))
print()
