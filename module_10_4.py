import threading
from queue import Queue
from random import randint, random
import time

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        #super().__init__()
        self.name = name
    def run(self):
        random_time = randint(3, 10)
        time.sleep(random_time)

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    table.guest.start()
                    break
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
         while (not self.queue.empty()) or (not (table.guest for table in self.tables)):
             for table in self.tables:
                 if (not self.queue.empty()) and (table.guest is None):
                     new_guest = self.queue.get()
                     table.guest = new_guest
                     print(f"{new_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                     new_guest.start()
                 if (not table.guest is None) and (table.guest.is_alive()):
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()














