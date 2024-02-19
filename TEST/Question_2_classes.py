from datetime import datetime


class Countdown:
    def __init__(self, target_datetime: datetime):
        self.target_datetime = target_datetime

    @property
    def time_left(self):
        current_datetime = datetime(2024, 2, 16, 10, 10)
        elapsed_time = self.target_datetime - current_datetime
        days = elapsed_time.days
        minutes = elapsed_time.seconds // 60
        seconds = elapsed_time.seconds % 60
        hours = minutes // 60
        if days > 0:
            print(f"{days} days, {hours}:{minutes}:{seconds}")
        else:
            print(f"{hours}:{minutes}:{seconds}")

    @property
    def is_expired(self):
        current_datetime = datetime(2024, 2, 16, 10, 10)
        elapsed_time = self.target_datetime - current_datetime
        minutes = elapsed_time.seconds // 60
        hours = minutes // 60
        if hours < 0:
            return True
        else:
            return False
