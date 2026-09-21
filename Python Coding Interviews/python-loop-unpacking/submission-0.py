from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    best_grade = 0
    best_student = ""

    for student, grade in scores:
        if grade > best_grade:
            best_grade = grade
            best_student = student
    
    return best_student


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
