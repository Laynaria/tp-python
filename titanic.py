import csv

all_ages: list[float] = []

first_class = []
second_class = []
third_class = []

boats_that_saved = []

with open("titanic_survival.csv", "r") as csv_file:
    csv_file_reader = csv.DictReader(csv_file)


    for line in csv_file_reader:
        # pclass,survived,name,sex,age,sibsp,parch,ticket,fare,cabin,embarked,boat,body,home.dest
        
        pclass = line["pclass"]
        survived = line["survived"]
        age = line["age"]
        boat = line["boat"]

        # part 1
        if age :
            all_ages.append(float(age))

        # part 2
        if pclass == "1":
            first_class.append(int(survived))
        elif pclass == "2":
            second_class.append(int(survived))
        elif pclass == "3":
            third_class.append(int(survived))
        
        # part 3
        if survived == "1" and boat:
            boats_that_saved.append(boat)
    

# Part 1 Logic
age_average: float = 0

for age in all_ages :
    age_average += age

age_average = age_average / len(all_ages)

print(f"Average Age is : {age_average}") # Average Age is : 29.8811345124283

# Part 2 Logic
# First Class
number_saved_first_class = 0

for is_alive in first_class:
    if is_alive:
        number_saved_first_class += 1

percent_saved_first_class = number_saved_first_class / len(first_class) * 100
print(f"First class: {percent_saved_first_class} % survivor") # First class: 61.91950464396285 % survivor

# Second class
number_saved_second_class = 0

for is_alive in second_class:
    if is_alive:
        number_saved_second_class += 1

percent_saved_second_class = number_saved_second_class / len(second_class) * 100
print(f"Second class: {percent_saved_second_class} % survivor") # Second class: 42.96028880866426 % survivor

# Third Class
number_saved_third_class = 0

for is_alive in third_class:
    if is_alive:
        number_saved_third_class += 1

percent_saved_third_class = number_saved_third_class / len(third_class) * 100
print(f"Third class: {percent_saved_third_class} % survivor") # Third class: 25.52891396332863 % survivor

# Part 3 Logic
# for boat in boats_that_saved:
existing_saving_boats = set(boats_that_saved)
existing_saving_boats = list(existing_saving_boats)
valueArray = []

for boat in existing_saving_boats:
    valueArray.append(0)

dictionnary = dict(zip(existing_saving_boats, valueArray))

for boat in boats_that_saved:
    dictionnary[boat] +=1

boats_that_saved_the_most = max(dictionnary, key=dictionnary.get)
max_saved_number_from_a_boat = max(dictionnary.values())

print(f"The boat that saved the most people is the {boats_that_saved_the_most}. It saved {max_saved_number_from_a_boat} people.")
# The boat that saved the most people is the 13. It saved 39 people.