current_time = int(input("Enter the current time.")) % 24
hours_timer = int(input("Enter the number of hours you want to wait."))
days_trigger = hours_timer // 24
hour_alarm_trigger = hours_timer % 24
print("The alarm will be triggered in ", days_trigger, " days at ", hour_alarm_trigger + current_time, "hours.")

# add if statement for AM/PM later