class Student:
    """Student"""
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f'\nИмя {self.name} ' \
               f'\nФамилия {self.surname} ' \
               f'\nСредняя оценка за домашние задания {self.average_estimate()}' \
               f'\nЗавершенные курсы {self.finished_courses}' \
               f'\nКурсы в прогрессе {self.courses_in_progress}\n'

    def Reflection(self, lector, course, *args):
        if isinstance(lector,
                      Lecturer) and course in self.courses_in_progress or course in self.finished_courses and \
                course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [*args]
            else:
                lector.grades[course] = [*args]
        else:
            return "Ошибка"

    def average_estimate(self):
        if not self.grades:
            return 0
        all_estimates = []
        for value in self.grades.values():
            all_estimates.extend(value)
        return round(sum(all_estimates) / len(all_estimates), 2)

    def __eq__(self, other):
        return self.average_estimate() == other.average_estimate()

    def __lt__(self, other):
        return self.average_estimate() < other.average_estimate()

    def __le__(self, other):
        return self.average_estimate() > other.average_estimate()



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Reviewer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname)
        self.courses_attached = courses_attached


    def __str__(self):
        return f'\n Имя {self.name}' \
               f'\n Фамилия {self.surname}' \


    def Makes_estimates_to_student(self, student, course, *args):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [*args]
            else:
                student.grades[course] = [*args]
        else:
            return "Ощибка"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []

    def __str__(self):
        return f'\nЛектор' \
               f'\nИмя {self.name}' \
               f'\nФамилия {self.surname}' \
               f'\nПрикрепленные курсы {self.courses_attached}' \
               f'\nОценки {self.grades}' \
               f'\nСредняя оценка {self.average_estimate()}\n'

    def average_estimate(self):
        if not self.grades:
            return 0
        all_estimates = []
        for value in self.grades.values():
            all_estimates.extend(value)
        return round(sum(all_estimates) / len(all_estimates), 2)

    def __eq__(self, other):
        return self.average_estimate() == other.average_estimate()

    def __lt__(self, other):
        return self.average_estimate() < other.average_estimate()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return 'have no'
        return self.average_estimate() > other.average_estimate()


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.finished_courses += ['Git']
best_student.courses_in_progress += ['Python', 'php']
best_student.grades['Git'] = [10, 10, 10, 10, 10]
best_student.grades['Python'] = [10, 10]

the_worst_student = Student('Joe', 'Swonson', 'man')
the_worst_student.grades['Git'] = [2, 3, 4, 6, 10]
the_worst_student.courses_in_progress += ['Python']

strict_rewiewer = Reviewer('Stewe', 'Griffin', 'Python')

lector1 = Lecturer('Piter', 'Griffin')
lector1.courses_attached += ['Git', 'Python', 'php']
lector3 = Lecturer('Ravil', 'Barber')
lector3.courses_attached += ['Barber_courses']


lector2 = Lecturer('Megatron', 'Griffin')
lector2.courses_attached += ['php']

best_student.courses_in_progress += ['php']
best_student.Reflection(lector3, 'php', 10, 9)
best_student.Reflection(lector2, 'php', 1, 8, 1)
best_student.Reflection(lector1, 'php', 10, 8, 10)
best_student.Reflection(lector1, 'Git', 1, 6, 1)
strict_rewiewer.Makes_estimates_to_student(the_worst_student, 'Python', 2, 3, 7)
strict_rewiewer.Makes_estimates_to_student(best_student, 'php', 2, 3, 7)
the_worst_student.Reflection(lector1, 'Python', 10, 1, 2)


lecturers = [lector1, lector2, lector3]
students = [best_student, the_worst_student]
course = input('enter a course: - Python, Assembler or php: ')

def compare_students(students, course):
    grades_list = []
    for i in students:
        grades_list.extend(i.grades.get(course, []))
    if not grades_list:
        return " i have no any grades"
    return round(sum(grades_list) / len(grades_list), 2)

def compare_lecturers(lecturers, course):
  return compare_students(lecturers, course)

print(f'Сравнениe студентов по средним оценкам за домашние задания: '
      f'{best_student.name} {best_student.surname} {"<" if best_student < the_worst_student else (">" if best_student > the_worst_student else "=")} {the_worst_student.name} {the_worst_student.surname}')
print()

print(f'Сравнение лекторов по средним оценкам за лекции: '
      f'{lector1.name} {lector1.surname} {"<" if lector1 < lector2  else (">" if lector1 > lector2 else "=")} {lector2.name} {lector2.surname}')
print()
print(f"Средняя оценка студентов по курсу {course}: {compare_students(students, course)}")
print()

print(f"Средняя оценка лекторов по курсу {course}: {compare_lecturers(lecturers, course)}")
print()
