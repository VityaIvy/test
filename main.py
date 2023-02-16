class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) \
                and course in self.courses_attached \
                and course in student.courses_in_progress:

            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_rating(self):
        if not self.grades:
            return 0

        estimations = []
        for estimation in self.grades.values():
            estimations.extend(estimation)

        return sum(estimations) / len(estimations)

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {self.average_rating()}'

    def __eq__(self, other):
        return self.average_rating() == other.average_rating()

    def __lt__(self, other):
        return self.average_rating() < other.average_rating()

    def __le__(self, other):
        return self.average_rating() <= other.average_rating()


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

    def put_2(self, lecturer: object, course: object, grade: object) -> object:
        if isinstance(lecturer, Lecturer) \
                and course in lecturer.courses_attached \
                and course in self.courses_in_progress:

            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating(self):
        if not self.grades:
            return 0

        estimations = []
        for estimation in self.grades.values():
            estimations.extend(estimation)

        return sum(estimations) / len(estimations)

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашнее задание: {self.average_rating()}\n' \
               f'Курсы в процесе изучения: {self.courses_in_progress}\n' \
               f'Завершённые курсы: {self.finished_courses}\n'

    def __eq__(self, other):
        return self.average_rating() == other.average_rating()

    def __lt__(self, other):
        return self.average_rating() < other.average_rating()

    def __le__(self, other):
        return self.average_rating() <= other.average_rating()


def course_average(course_name: str, person_list: list) -> float:
    all_grades = []
    for person in person_list:

        all_grades.extend(person.grades[course_name])

    return sum(all_grades) / len(all_grades)
