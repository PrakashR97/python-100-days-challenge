

student_heights = [180, 124, 165, 173, 189, 169, 146]

_stud_list=input("List of student heights?")
_k=_stud_list.split(' ')
print(_k)

avg=0
for i in _k:
    avg=avg+int(i)


print(int(avg/ len(_k)))
