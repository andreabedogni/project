import matplotlib.pyplot as ply

file = open("top5MensSalary.csv", "w")
file.write("Men, Women")
file.close()

file = open("top5MensSalary.csv", "r")
gender = file.read()
file.close()

genders = gender.split(",") 


file = open("top5WomenSalary.csv", "w")
file.write("373, 2.3")
file.close()

file = open("top5WomenSalary.csv", "r")
millions = file.read()
file.close()

million = millions.split(",") 
million = [float(item) for item in million]

colors = ['blue', 'red']
ply.bar(genders, million, color = colors)
ply.title("TOP 5 MOST PAID MEN VS WOMEN FOOTBALLERS")
ply.xlabel("GENDER")
ply.ylabel("MILLIONS")
ply.show()
