sleep_hours_A = int(input())
excess_hours_B = int(input())
ann_sleep_H = int(input())

if ann_sleep_H > excess_hours_B:
    print("Excess")
elif ann_sleep_H < sleep_hours_A:
    print("Deficiency")
else:
    print("Normal")
