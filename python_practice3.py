counties = ["Arapahoe","Denver","Jefferson"]
len(counties)
if counties[1] == "Denver":
    print(counties[1])
len(counties)
print(len(counties))
if counties[2] == "Jefferson":
    print(counties[2])

temperature = int(input("What is the temperature outisde?"))
if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the window.")


score = int(input("What is your test score?"))
# Determine the grade
if score >= 90:
    print("Your grade is an A.")
else:
    if score >= 80:
        print("Your grade is a B.")
    else:
        if score >= 70:
            print("Your grade is a C.")
        else:
            if score >= 60:
                print("Your grade is a D.")
            else:
                print("Your grade i a F'")

if score >= 90:
    print("Your grade is an A.")
elif score >= 80:
    print("Your grade is a B.")
elif score >= 70:
    print("Your grade is a C.")
elif score >= 60:
    print("Your grade is a D.")
else:
    print("Your grade is a F'")

counties

