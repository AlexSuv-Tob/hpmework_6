class Road:
    def __init__(self):
         self.__lenght = 'длина'
         self.__width = 'ширина'


    def weight_as(self,__lenght, __width):
        return __lenght * __width * 5 * 1

r = Road()
num = r.weight_as(20, 5000)
print(num, 'кг - расчет массы асфальта на полотно толщиной 1 см')