class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_lectur(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def average_rating_hw(self, course):
        average_rating = []
        for key, value in self.grades.items():
            if key == course:
                average_rating.extend(value)
        return round(sum(average_rating)/len(average_rating), 2)
    
    def __str__(self, course):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {self.average_rating_hw(course)}\nЗавершенные курсы: {",".join(self.finished_courses)}'
    
    def __lt__(self, student, course):
        if isinstance(student, Student) and course in self.courses_in_progress and course in student.courses_in_progress:
                return self.average_rating_hw(course) < student.average_rating_hw(course)
        else:
            return 'Ошибка'

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

    def average_rating(self, course):
        average = []
        for key, value in self.grades.items():
            if key == course:
                average.extend(value)
        return round(sum(average)/len(average), 2)
    
    def __str__(self, course):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating(course)}'
    
    def __lt__(self, lecturer, course):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_attached:
                return self.average_rating(course) < lecturer.average_rating(course)
        else:
            return 'Ошибка'
    
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
            return 'Ошибка'
        
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

def total_average_for_students(students, course):
    all_grades = []
    for student in students:
        for key, value in student.grades.items():
            if key == course:
                all_grades.extend(value)
    return round(sum(all_grades)/len(all_grades), 2)

def total_average_for_lecturers(lecturers, course):
    all_grades = []
    for lecturer in lecturers:
        for key, value in lecturer.grades.items():
            if key == course:
                all_grades.extend(value)
    return round(sum(all_grades)/len(all_grades), 2)
    
student_1 = Student('Максим', 'Кожин', 'Мужской')
student_1.finished_courses = ['Git']
student_1.courses_in_progress += ['Основы программирования на Python', 'ООП']

student_2 = Student('Татьяна', 'Иванова', 'Женский')
student_2.finished_courses = ['C++']
student_2.courses_in_progress += ['Основы программирования на Python']

students = [student_1, student_2]

lecturer_1 = Lecturer('Екатерина', 'Орлова')
lecturer_1.courses_attached = ['Основы программирования на Python', 'Git']

lecturer_2 = Lecturer('Олег', 'Булыгин')
lecturer_2.courses_attached = ['Основы программирования на Python', 'Git', 'C++']

lecturers = [lecturer_1, lecturer_2]

reviewer_1 = Reviewer('Федор', 'Достаевский')
reviewer_1.courses_attached = ['Основы программирования на Python', 'Git', 'Литература']

reviewer_2 = Reviewer('Стив', 'Джобс')
reviewer_2.courses_attached = ['Основы программирования на Python', 'Git', 'Маркетинг']

student_1.rate_lectur(lecturer_2, 'Основы программирования на Python', 10)
student_2.rate_lectur(lecturer_1, 'Основы программирования на Python', 8)

reviewer_1.rate_hw(student_1, 'Основы программирования на Python', 7)
reviewer_1.rate_hw(student_2, 'Основы программирования на Python', 9)
reviewer_2.rate_hw(student_2, 'Основы программирования на Python', 10)
reviewer_2.rate_hw(student_1, 'Основы программирования на Python', 8)
print('Эксперты, проверяющие домашние задания:')
print(reviewer_1)
print(reviewer_2)

student_1.average_rating_hw('Основы программирования на Python')
student_2.average_rating_hw('Основы программирования на Python')
student_1.rate_lectur(lecturer_1, 'Основы программирования на Python', 9)
student_1.rate_lectur(lecturer_2, 'Основы программирования на Python', 8)
student_2.rate_lectur(lecturer_2, 'Основы программирования на Python', 10)
student_2.rate_lectur(lecturer_1, 'Основы программирования на Python', 7)
print('Студенты:')
print(student_1.__str__('Основы программирования на Python'))
print(student_2.__str__('Основы программирования на Python'))
print(student_2.__lt__(student_1, 'Основы программирования на Python'))

lecturer_1.average_rating('Основы программирования на Python')
lecturer_2.average_rating('Основы программирования на Python')
print('Лекторы:')
print(lecturer_1.__str__('Основы программирования на Python'))
print(lecturer_2.__str__('Основы программирования на Python'))
print(lecturer_1.__lt__(lecturer_2, 'Основы программирования на Python'))

print('Средняя оценка по всем студентам:')
print(total_average_for_students(students, 'Основы программирования на Python'))

print('Средняя оценка по всем лекторам:')
print(total_average_for_lecturers(lecturers, 'Основы программирования на Python'))

