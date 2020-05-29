incom = {"wage": 20000, "bonus": 5000}

class Worker:
    def __init__(self):
        self.name = 'Имя'
        self.surname = 'Фамилия'
        self.position = 'Должность'
        self.__income = incom

class Position(Worker):
    def get_full_name(self, position, name, surname):
        return (position, name, surname)

    def get_total_income(self):
       return (sum(incom.values()))

w = Position()
n_s = w.get_full_name('dir', 'Suv', 'Alex')
b_i = w.get_total_income()
print('Информация по сотруднику: Должность Фамилия Имя:', n_s)
print('Общий доход', b_i)
