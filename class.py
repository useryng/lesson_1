class Patient:
    insulin = 1500
    def __init__(self, name, glyc):
        self.id = name
        self.glyc = glyc
        self.hypo = check_hypo(glyc)
        self.hyper = check_hyper(glyc)
    def new_glyc(self, glucose):
        self.glyc = glucose
        self.hypo = check_hypo(glucose)
        self.hyper = check_hyper(glucose)
    @classmethod
    def take_insulin(cls, dose):
        cls.insulin = cls.insulin - dose

class Infected(Patient):
    ibuprofen = 10
    def __init__(self, name, glyc, temp):
        Patient.__init__(self, name, glyc)
        self.temp = temp
    @classmethod
    def take_ibuprofen(cls):
        cls.ibuprofen = cls.ibuprofen - 1
    def new_temp(self, new_temp):
        self.temp = new_temp


def check_hyper(glucose):
    if glucose > 5.5:
        return True
    else:
        return False

def check_hypo(glucose):
    if glucose < 3.3:
        return True
    else:
        return False
    
Ivanov = Infected('Иванов', 5, 40)
Smirnov = Infected('Смирнов', 4, 39)
Sidorova = Infected('Сидорова', 3, 38)

Sidorova.new_glyc(7)
print(f"Уровень глюкозы {Sidorova.glyc}")
print(f"Гипергликемия: {Sidorova.hyper}")
print(f"Гипогликемия: {Sidorova.hypo}")

print(f"Запасы инсулина: {Infected.insulin}")
Sidorova.take_insulin(25)
print(f"Остаток инсулина: {Infected.insulin}")

print(f"Остаток до приема: {Infected.ibuprofen}")
Sidorova.take_ibuprofen()
print(f"Остаток полсе приема: {Infected.ibuprofen}")