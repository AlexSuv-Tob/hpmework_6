class Car:
    def __init__(self):
        self.speed = int()
        self.color = 'color'
        self.name = 'name'
        self.is_police = bool()

    def go(self, show_speed):
        if show_speed != 0:
            print('Машина начала движение')

    def stop(self, show_speed):
        if show_speed == 0:
            print('машина остановилась')

    def turn(self, param_1):
        if param_1 == 1:
            print('Машина развернулась')
        if param_1 == 2:
            print('Машина повернула на право')

    def show_speed(self, speed):#показывает текущую скорость
        print('текущая скорость', speed)

class TownCar(Car):
    def info(self, name, color, speed):

        if speed <= 60:
            print('Городской автомобиль марка', name, 'цвет', color, 'скорость', speed)
        else:
            print('Вы превысели скорость, ваша скорость больше 60 км/ч')

    def show_speed(self, speed):
        if speed <= 60:
            print('текущая скорость', speed)
        else:
            print(f'Вы превысели скорость, ваша скорость {speed} больше 60 км/ч')

class SportCar(Car):
    def info(self, name, color, speed):
        print('Спортивный автомобиль марка', name, 'цвет', color, 'скорость', speed)


class WorkCar(Car):
    def info(self, name, color, speed):
        if speed <= 40:
            print('Городской автомобиль, марка', name, 'цвет', color, 'скорость', speed)
        else:
            print('Вы превысели скорость, ваша скорость больше 40 км/ч')

    def show_speed(self, speed):
        if speed <= 40:
            print('текущая скорость', speed)
        else:
            print(f'Вы превысели скорость, ваша скорость {speed} больше 40 км/ч')

class PoliceCar(Car):
    def police_car(self, name, color, speed):
        print('Полицейский автомобиль марка', name, 'цвет', color, 'скорость', speed)

#sc = SportCar()
#sc.info('lamba', 'red', 90)
#sc.go(20)

#tc = TownCar()
#tc.info('vaz', 'gray', 90)
#tc.show_speed(90)

wc = WorkCar()
wc.info('vaz', 'yellow', 40)
wc.turn(2)
wc.show_speed(90)







