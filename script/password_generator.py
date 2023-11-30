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


class Save:
    def log(self, path, log_time):
        with open(path, "w") as file:
            file.write(f"{log_time}")

    def write_data(self, file_name, data):
        with open(file_name, "a") as file:
            file.write("\n" + data)


def random_number(length):
    if length <= 0:
        raise ValueError("Negative length")  
    lower_bound = 10 ** (length - 1)
    upper_bound = (10 ** length) - 1
    return randint(lower_bound, upper_bound)

def generate_password(length, categories, months, year):
    passwords = []
    for category in categories:
        passwords.append(f"\n{category}:")
        for month in months:
            number = random_number(length)
            generated_password = f"{month}_{number}_{year}X_{category}"
            passwords.append(generated_password)
    return passwords



if __name__ == "__main__":

    # Generating password
    clock = Times()
    month, year = clock.date_time()
    log_time = clock.log_time()
    categories = ["Private", "Schools", "Microsoft"]
    passwords = generate_password(5, categories, month, year)

    # Save the generated password to txt
    file_folder = r"script\password.txt"
    database = Save()
    database.log(file_folder, log_time)
    for password in passwords:
        database.write_data(file_folder, password)