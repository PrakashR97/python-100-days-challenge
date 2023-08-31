student_scores = [78, 65, 89, 86, 55, 91, 64, 89]


_max_score=0

for i in student_scores:
    if _max_score<i:
        _max_score=i



print(f"The highest score in the class is {_max_score}")
