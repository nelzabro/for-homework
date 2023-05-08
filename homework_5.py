import datetime
import time
class Parrot:
    biology_class = 'birds'
    def __init__(self, name, colour, superability, age):
        self._name = name
        self.colour = colour
        self.superability = superability
        self.age = age


    def greeting(self):
        return f'Hi, my name is {self._name}, I am {self.colour} colour. I can {self.superability} ' \
               f'Will you play with me?'



    def time_to_speak(self):
        return f' I want to tell you {datetime.date.today()} , {time.strftime("%H:%M:%S")}' \
               f' is time to speak with me'

parrot_1 = Parrot('Pururu', 'green','loudly cry', 3 )
print(parrot_1.age)
print(parrot_1.greeting())
print(parrot_1.time_to_speak())
