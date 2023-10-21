from datetime import datetime


class BacaData:
    def __init__(self) -> None:
        pass

    def open_file(self, file_name):
        with open(file_name, "r") as file:
            return file.read()

    def detail(self, data, dict_data):
        for x in data:
            print(f"name: {x}, age: {dict_data[x][0]}")


class TulisData:
    def __init__(self) -> None:
        pass

    def times(self):
        now = datetime.now()
        log_waktu = f"{now:%h-%d-%Y}, {now:%H:%M:%S}"
        return log_waktu

    def write_data_line(self, file_name, line, data):
        with open(file_name, "r") as file:
            lines = file.readlines()

        # Jika line lebih besar dari jumlah baris dalam file,
        if line > len(lines):
            # tambahkan baris kosong hingga mencapai baris yang diinginkan
            for _ in range(len(lines), line):
                lines.append("\n")

        lines[line - 1] = data + "\n"  # Tulis data pada baris yang spesifik
        with open(file_name, "w") as file:
            file.writelines(lines)

    def write_last(self, file_name, data):
        with open(file_name, "a") as file:
            file.write("\n" + data)



# =====================================================================================
if __name__ == "__main__":
    database = r"script/logger.txt"
    print("0 for read, 1 for write")
    user_input = int(input("Your choice: "))
    if user_input == 0:
        data_mahasiswa = {}
        reader = BacaData()
        content = reader.open_file(database)
        for line in content.split("\n"):
            data = line.strip().split(", ")
            if len(data) != 3:
                continue

            name = data[0]
            age = int(data[1])
            gender = data[2]
            data_mahasiswa[name] = (age, gender)
            

        # Class
        man = []
        woman = []
        unknown = []
        for name in data_mahasiswa:
            age_data, gender_data = data_mahasiswa[name]
            if gender_data == "man":
                man.append(name)
            elif gender_data == "woman":
                woman.append(name)
            else:
                unknown.append(name)
        
        print(f"man: {len(man)}, women: {len(woman)}, Unknown: {len(unknown)}")
        reader.detail(unknown, data_mahasiswa)

    elif user_input == 1:
        writer = TulisData()
        time = f"Last Log: {writer.times()}"
        writer.write_data_line(database, 1, time)

        total_data = int(input("How much data? "))
        for write in range(total_data):
            name = input("Name: ").title()
            age = int(input("Age: "))
            gender = input("Gender: ").lower()
            summary = f"{name}, {age}, {gender}"
            writer.write_last(database, summary)
            print("\n")
        else:
            print("\nDone!")

    else:
        print("Choose 0 or 1!")