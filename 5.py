class Stationery:
    title = 'название'
    def draw(self):
        print('запуск зарисовки')

class Pen(Stationery):
    def draw(self):
        print('запускаем ручку')

class Pencil(Stationery):
    def draw(self):
        print('запускаем карандаш')

class Handle(Stationery):
    def draw(self):
        print('запускаем маркер')

st = Stationery()
st.draw()

p = Pen()
p.draw()

p_l = Pencil()
p_l.draw()

han = Handle()
han.draw()