from Question_2_classes import Countdown
from datetime import datetime

target_datetime_1 = datetime(2025, 10, 1, 11, 0)
target_datetime_2 = datetime(2022, 10, 1, 11, 0)
target_datetime_3 = datetime(2021, 9, 30, 20, 0)

countdown1 = Countdown(target_datetime_1)
countdown2 = Countdown(target_datetime_2)
countdown3 = Countdown(target_datetime_3)

print(countdown1.time_left)
print(countdown1.is_expired)
print()
print(countdown2.time_left)
print(countdown2.is_expired)
print()
print(countdown3.time_left)
print(countdown3.is_expired)
