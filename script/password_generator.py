from datetime import datetime as time
from random import randint


def random_number(length):
    if length <= 0:
        raise ValueError("Negative length")  
    lower_bound = 10 ** (length - 1)
    upper_bound = (10 ** length) - 1
    return randint(lower_bound, upper_bound)


def generate_password(rand_int):
    date = time.now()
    year = date.year
    categories = ["Private", "School", "Microsoft"]
    months = [
        "January", "February", "March",
        "April", "May", "June", 
        "July", "August", "September", 
        "October", "November", "December"
    ]
    

    for category in categories:
        print(f"{category}:")
        for month in months:
            number = random_number(rand_int)
            print(f"{month}_{number}_{year}X_{category}")
        print()




if __name__ == "__main__":
    generate_password(10)