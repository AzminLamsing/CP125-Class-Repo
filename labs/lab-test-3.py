import csv
def read_and_calculate(file_name) :
    file = open(file_name,"r",newline = "")
    reader = csv.reader(file)

    next(reader)
    #print(header)
  

    total_height = 0
    count = 0
    for row in reader :
        print(row)
        height = int(row[1])
        total_height += height
        count += 1

    average = total_height / count
    print(f" Average Heigt : {average}")
    file.close()

def add_new_data(file_name):
    gender = input("Enter your gender : ")
    height = int(input("Enter your height : "))
    weight = int(input("Enter your weight : "))
    bmi = float(input("Enter your "))

    file = open(file_name,"a",newline = "")
    writer = csv.writer(file)
    writer.writerow([gender,height,weight,bmi])
    file.close()
    print("\n New Data Added \n")

    file = open(file_name,"r",newline = "")
    reader = csv.reader(file)
    print("\n Update Content File \n")
    for row in reader :
        print(row)

    file.close()


file_name = "CP125-Class-Repo/labs/bmi.csv"
print("Function 1")
print(read_and_calculate(file_name))

print("\n Function 2 ")
#print(add_new_data(file_name))


