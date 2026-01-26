from module_usererror import  UserError

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student is not None:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def count_students(self):
        if len(self.group) > 10:
            raise UserError("More than 10 students!", len(self.group))
        return len(self.group)

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += f'{student.first_name} {student.last_name}\n '
        return f'Number: {self.number}\n {all_students} '