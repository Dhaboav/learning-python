from datetime import datetime as time
from random import randint


class Times:
    def __init__(self):
        self.date = time.now()

    def log_time(self):
        time_log = f"{self.date:%h-%d-%Y}, {self.date:%H:%M:%S}"
        return time_log
    
    def date_time(self):
        year = self.date.year
        months = [
            "January", "February", "March",
            "April", "May", "June", 
            "July", "August", "September", 
            "October", "November", "December"
        ]
        return months, year


def random_number(length):
    if length <= 0:
        raise ValueError("Negative length")  
    lower_bound = 10 ** (length - 1)
    upper_bound = (10 ** length) - 1
    return randint(lower_bound, upper_bound)


def generate_password(length, categories, months, year):
    for category in categories:
        print(f"{category}:")
        for month in months:
            number = random_number(length)
            print(f"{month}_{number}_{year}X_{category}")
        print()




if __name__ == "__main__":
    clock = Times()
    month, year = clock.date_time()
    categories = ["Private", "Schools", "Microsoft"]
    generate_password(6, categories, month, year)