import time
class TrafficLight():
    _color = 'цвет'

    def running(self):
        print('Красный')
        time.sleep(7)
        print('желтый')
        time.sleep(2)
        print('зеленый')
        time.sleep(5)

tr = TrafficLight()
tr.running()
