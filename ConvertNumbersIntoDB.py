file = "kordy bolcik.txt"

with open(file, "r") as file:
    fixed_line = []
    for line in file:
        char = line.strip("\n").split(" ")
        print(char[0], char[1], char[2])
        fixed_line.append("    [" + char[0] + ", " + char[1] + ", " + char[2] + "]," + "\n")
        with open("kordy bolcik poprawione.txt", "w") as file_w:
            for i in range(len(fixed_line)):
                file_w.write(fixed_line[i])
