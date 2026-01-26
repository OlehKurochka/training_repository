# 2. Створення власних модулів

from module_student import Student
from module_group import Group
from module_usererror import UserError


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
assert gr.find_student('Jobs2') is None

gr.delete_student('Taylor')
print(gr) # Only one student


try:
    print(gr.count_students())
except UserError as err:
    print(f'Error: {err.get_exception_message()} (number: {err.num})')

assert gr.find_student('Jobs') == st1
