# HW 13.1
class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}"

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record Book: {self.record_book}"

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student): # добавление студента в группу
        self.group.add(student)

    def delete_student(self, last_name): # удаление студента из группы
        for student in self.group:
            if student.last_name == last_name:
                self.group.remove(student)
                return  # Прекращаем после удаления, так как студент найден

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None  # Если студент не найден, возвращаем None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f"Number: {self.number}\nStudents:\n{all_students}"

# HW 13.2
class Counter:

    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start): # проверка допустимых границ
        if self.min_value <= start <= self.max_value:
            self.current = start
        else:
            raise ValueError("Start value is out of bounds.")

    def set_max(self, max_max): # Установка максимального значения
        if max_max >= self.min_value:
            self.max_value = max_max
            if self.current > self.max_value:
                self.current = self.max_value
        else:
            raise ValueError("Max value cannot be less than min value.")

    def set_min(self, min_min): # Установка минимального значения
        if min_min <= self.max_value:
            self.min_value = min_min
            if self.current < self.min_value:
                self.current = self.min_value
        else:
            raise ValueError("Min value cannot be more than max value.")

    def step_up(self): # + 1, если оно ниже максимума.
        if self.current < self.max_value:
            self.current += 1
        else:
            raise ValueError("Maximum limit reached.")

    def step_down(self):  # - 1, если  не меньше мин
        if self.current > self.min_value:
            self.current -= 1
        else:
            raise ValueError("Minimum limit reached.")

    def get_current(self):
        return self.current
print ("13.1")
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!

print ("13.2")

counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()
except ValueError as e:
    print(e)
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()
except ValueError as e:
    print(e)
assert counter.get_current() == 7, 'Test4'

