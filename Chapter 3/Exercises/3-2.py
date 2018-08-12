days = [
    (0, "Monday"),
    (1, "Tuesday"),
    (2, "Wednesday"),
    (3, "Thursday"),
    (4, "Friday"),
    (5, "Saturday"),
    (6, "Sunday")
]

for date, day in days:
    starting_day = int(input("Enter the current day."))
    stay_length = int(input("Enter the length of your stay."))
    return_day = starting_day + (stay_length % 7)

    if return_day > 6:
        return_day -= 6

    if return_day == 0:
        print("Monday")
    if return_day == 1:
        print("Tuesday")
    if return_day == 2:
        print("Wednesday")
    if return_day == 3:
        print("Thursday")
    if return_day == 4:
        print("Friday")
    if return_day == 5:
        print("Saturday")
    if return_day == 6:
        print("Sunday")

#This looks really, really bad.
#Other ver @https://src-code.simons-rock.edu/git/jyang13/HW4/raw/master/Ch.5E2.py