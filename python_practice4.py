counties = ["Arapahoe","Denver","Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is IN in the list of counties.")
# else:
#     print("El Paso IS NOT in the list of counties.")

# if "Arapahoe" in counties and "El Paso" in counties:
#     print("Arapahoe and El Paso ar ein the list of counties")
# else:
#     print("Arapahoe or El Paso is not in the list of counties")

# if "Arapahoe" in counties or "El Paso" in counties:
#     print("Arapahoe or El Paso are in the list of counties")
# else:
#     print("Arapahoe and El Paso are not in the list of counties")

# if "Arapahoe" in counties and "El paso" not in counties:
#     print("Only Arapahoe is in the list of counties")
# else:
#     print("Arapahoe is in the list of counties and El Paso is not in the list of counties")

# x = 0
# while x <= 5:
#     print(x)
#     x= x+1
   
# count = 7
# while count < 10:
#     print("Hello World")
#     count += 1

# for county in counties:
#     print(county)

# numbers = [0, 1, 2, 3, 4]
# for num in numbers:
#     print(num)

# for i in range(len(counties)):
#     print(counties[i])

counties_dict = {"Arapahoe":422826, "Denver": 463353, "Jefferson": 432438}



# for county in counties_dict.keys():
#     print(county)
# for voters in counties_dict.values():
#     print(voters)

# for county in counties_dict:
#     print(counties_dict[county])

#     for county in counties_dict:
#         print(counties_dict.get(county))

for county in counties_dict:
    print(county + " county has " + str(counties_dict.get(county)) + " registered voters.")

