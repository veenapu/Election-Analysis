# print("Hello World!")
# counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])
# if counties[3] != 'Jefferson':
#     print(counties[2])
    
counties = ["Arapahoe","Denver","Jefferson"]

if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")

if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print('Arapahoe is in the list of counties and El Paso is not in the list of counties')

for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)

for i in range(len(counties)):
     print(counties[i])

counties_dict = {"Arapahoe":422829,"Denver":463353,"Jefferson":432438}

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

for key, value in counties_dict.items():
    print(key,value)

for key, value in counties_dict.items():
    print("Arapahoe county has 422829 registered voters.")
    print("Denver county has 463353 registered voters.")
    print("Jefferson county has 432438 registered voters")
    