class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_mark(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached and 0<grade<=10:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            print('Error input')

    def __avg_mark(self):
        """служебный метод расчета средней оценки за ДЗ студентов"""
        total_mark = []
        for mark in self.grades.values():
            total_mark += mark
        return sum(total_mark)/len(total_mark)

    def __str__(self):
        inf_s = f'Имя: {self.name}\n'\
                  f'Фамилия: {self.surname}\n'\
                  f'Средняя оценка за домашние задания: {self.__avg_mark()}\n'\
                  f'Курсы в процессе обучения:, {", ".join(self.courses_in_progress)}'\
                  f'Завершенные курсы:', {", ".join(self.finished_courses)}
        return inf_s

    def __lt__(self, other):
        """служебный метод сравнения студентов по оценкам за ДЗ по изучаемым курсам"""
        if not isinstance(other, Student):
            print('Это не студент!')
            return
        return self.__avg_mark() < other.__avg_mark()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def __get_avr_mark(self):
        """служебный метод расчета средней оценки лектора"""
        total_m = []
        for marks in self.grades.values():
            total_m += marks
            avr = sum(total_m)/len(total_m)
        return avr

    def __str__(self):
        lector = f'Имя: {self.name}\n'\
                 f'Фамилия: {self.surname}\n'\
                 f'Средняя оценка за лекции - {self.__get_avr_mark()}'
        return lector

    def __lt__(self, other):
        """служебный метод сравнения двух лекторов"""
        if not isinstance(other, Lecturer):
            print('Это не лектор!')
            return
        return self.__get_avr_mark() < other.__get_avr_mark()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('такого нет!')

    def __str__(self):
        revier = f'Имя: {self.name}\n'\
                 f'Фамилия: {self.surname}'
        return revier



student_1 = Student('Bryan', 'Philips', 'М')
student_2 = Student('Rayn', 'Morris', 'Ж')
lector_1 = Lecturer('Oleg', 'Filimonovich')
lector_2 = Lecturer('Dima', 'Batanov')
lector_2.courses_attached.append('Python')
lector_1.courses_attached.append('Python')
lector_2.courses_attached.append('Git')
lector_1.courses_attached.append('Git')
student_1.courses_in_progress.append('Python')
student_1.courses_in_progress.append('Git')
student_2.courses_in_progress.append('Git')
student_2.courses_in_progress.append('Python')
student_1.rate_mark(lector_1, 'Python', 10)
student_1.rate_mark(lector_1, 'Python', 9)

student_1.rate_mark(lector_2, 'Python', 10)
student_1.rate_mark(lector_2, 'Python', 10)
student_1.rate_mark(lector_1, 'Git', 9)
student_1.rate_mark(lector_2, 'Git', 8)
print(lector_1.grades)
print(lector_2.grades)
#                   Сравнение двух лекторов
print(lector_1 < lector_2)

revier_1 = Reviewer('Ivan', 'Ivanov')
revier_1.courses_attached.append('Python')
revier_1.courses_attached.append('Git')
revier_1.rate_hw(student_1, 'Python', 10)
revier_1.rate_hw(student_1, 'Python', 8)
revier_1.rate_hw(student_1, 'Git', 10)
revier_1.rate_hw(student_2, 'Git', 9)
print(student_1.grades)

revier_1.rate_hw(student_2, 'Python', 8)
revier_1.rate_hw(student_2, 'Python', 7)
print(student_2.grades)
#               Сравнение двух студентов
print(student_2 < student_1)


all_students = [student_1, student_2]
def avg_mark_hw(list_students, course_name):
    """Функция, определяющая общую оценку всех студентов за определенный курс"""
    all_marks = []
    sum_all_marks = 0
    for student in list_students:
        for key, values in student.grades.items():
            if key == course_name:
                all_marks += values
                sum_all_marks += sum(values)
                avg_mark = sum_all_marks / len(all_marks)
    return f" Средняя оценка всех студентов за курс по '{course_name}' -{avg_mark: .1f}"
a = avg_mark_hw(all_students, 'Python')
print(a)


all_lectors = [lector_1, lector_2]
def avr_mark_lector(list_lector, course_name):
    """Функция, определяющая общую оценку всех лекторов за определенный курс"""
    all_marks = []
    sum_all_marks = 0
    for lector in list_lector:
        for key, values in lector.grades.items():
            if key == course_name:
                all_marks += values
                sum_all_marks += sum(values)
                avr_mark = sum_all_marks / len(all_marks)
    return f"Средняя оценка всех лекторов за курс по '{course_name}' - {avr_mark: .1f}"
b = avr_mark_lector(all_lectors, 'Git')
print(b)