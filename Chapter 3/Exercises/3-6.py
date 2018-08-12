numbers = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,
49.9, 45, 44.9, 40, 39.9, 2, 5, 0]

grade = ["First", "Upper Second", "Second", "Third", "F1 Supp", "F2", "F3"]

for number in numbers:
    if number >= 75:
        print("Grade", grade[0], "- Mark:", number)
    if  70<= number <75:
        print("Grade", grade[1], "- Mark:", number)
    if  60<= number <70:
        print("Grade", grade[2], "- Mark:", number)
    if  50<= number <60:
        print("Grade", grade[3], "- Mark:", number)
    if  45<= number <50:
        print("Grade", grade[4], "- Mark:", number)
    if  40<= number <45:
        print("Grade", grade[5], "- Mark:", number)
    if number < 40:
        print("Grade", grade[6], "- Mark:", number)
