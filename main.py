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

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        middle_grade_stud = 0
        if len(self.grades):
            middle_grade_stud = avg_grade(self.grades)
        str_ = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {middle_grade_stud}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return str_

    def __lt__(self, other):
        return self.grades < other.grades


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        middle_grade_lecturer = 0
        if len(self.grades):
            middle_grade_lecturer = avg_grade(self.grades)
        str_ = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {middle_grade_lecturer}'
        return str_

    def __lt__(self, other):
        return avg_grade(self.grades) < avg_grade(other.grades)


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        str_ = f'Имя: {self.name}\nФамилия: {self.surname}'
        return str_


def avg_grade(dict_grades):
    grades_list = [x for el in list(dict_grades.values()) for x in el]
    # middle_grade_stud = sum(sum(self.grades.values(), [])) / len(self.grades)
    return round(sum(grades_list) / len(grades_list), 2)


def avg_grade_student(students_list, course):
    avg_students = 0
    index = 0
    for student in students_list:
        print(student.name, student.grades)
        grades_list = student.grades.get(course)
        if grades_list is not None:
            avg_students += (sum(grades_list) / len(grades_list))
            index += 1
    print(course, round(avg_students / index, 2))


def avg_grade_lecturer(lecturer_list, course):
    pass


one_student = Student('Mickey', 'Silver', 'M')
one_student.courses_in_progress += ['Python']
one_student.finished_courses += ['QA']
two_student = Student('Kath', 'Gold', 'F')
two_student.courses_in_progress += ['QA', 'Python']
three_student = Student('Richard', 'Silver', 'M')
three_student.add_courses(['Python'])
three_student.add_courses(['Java'])
three_student.courses_in_progress += ['QA']

cool_lecturer = Lecturer('Marty', 'Friedman')
cool_lecturer.courses_attached += ['Python']
awesome_lecturer = Lecturer('Dave', 'Mustaine')
awesome_lecturer.courses_attached += ['QA']
awesome_lecturer.courses_attached += ['Python']

cool_reviewer = Reviewer('Steve', 'Manfried')
cool_reviewer.courses_attached += ['QA']
awesome_reviewer = Reviewer('Ozzy', 'Osbourne')
awesome_reviewer.courses_attached += ['Python']

awesome_reviewer.rate_hw(one_student, 'Python', 7)
awesome_reviewer.rate_hw(two_student, 'Python', 8)
awesome_reviewer.rate_hw(three_student, 'Python', 9)
cool_reviewer.rate_hw(one_student, 'QA', 10)
cool_reviewer.rate_hw(two_student, 'QA', 8)
cool_reviewer.rate_hw(three_student, 'QA', 10)

one_student.rate_lecture(awesome_lecturer, 'Python', 9)
one_student.rate_lecture(awesome_lecturer, 'QA', 10)
one_student.rate_lecture(cool_lecturer, 'Python', 10)
two_student.rate_lecture(cool_lecturer, 'Python', 7)
two_student.rate_lecture(awesome_lecturer, 'QA', 10)
three_student.rate_lecture(cool_lecturer, 'Python', 10)
three_student.rate_lecture(awesome_lecturer, 'QA', 5)

print(f' --- Студент --- \n{one_student}')
print(f' --- Студент --- \n{two_student}')
print(f' --- Ревьювер --- \n{awesome_reviewer}')
print(f' --- Ревьювер --- \n{cool_reviewer}')
print(f' --- Лектор --- \n{awesome_lecturer}')
print(f' --- Лектор --- \n{cool_lecturer}')
print(f' --- Сравнение лекторов --- \n{awesome_lecturer < cool_lecturer}')

students_list = [one_student, two_student, three_student]
lecturer_list = [awesome_lecturer, cool_lecturer]
print('--- Средние оценки студентов ---')
avg_grade_student(students_list, 'QA')
# avg_grade_lecturer(lecturer_list, 'Python')
print('--- Средние оценки лекторов ---')
avg_grade_student(lecturer_list, 'Python')
