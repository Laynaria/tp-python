import csv

all_ages: list[float] = []
age_average: float = 0

with open("titanic_survival.csv", "r") as csv_file:
    csv_file_reader = csv.DictReader(csv_file)


    for line in csv_file_reader:
        # pclass,survived,name,sex,age,sibsp,parch,ticket,fare,cabin,embarked,boat,body,home.dest
        
        pclass = line["pclass"]
        survived = line["survived"]
        age = line["age"]
        boat = line["boat"]

        if age :
            all_ages.append(float(age))
    

for age in all_ages :
    age_average += age

age_average = age_average / len(all_ages)

print(f"Average Age is : {age_average}") # Average Age is : 29.8811345124283