import csv

data = []

with open("dataset_1.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        data.append(row)

headers = data[0]
star_data = data[1:]
df = df[df['column_name'].notna()]

#Converting mass and radius 
for mass in star_data:
    mass = df['mass']*0.000954588
    

for radius in star_data:
    radius = df['radius']*0.102763

#Sorting planet names in alphabetical order
star_data.sort(key=lambda star_data: star_data[2])


with open("dataset_2_sorted.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)