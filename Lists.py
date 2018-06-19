myinfo = ["Ozil Jersey","Aubameyang Jersey","Nintendo Switch Pro Controller","Let's Go Pikachu"]
for name in myinfo:
    print(name)
    
myinfo.append("Life")
print(myinfo)

myinfo.remove("Life")
print(myinfo)
print (len(myinfo))

colors = ["Red", "Orange","Yellow","Green","Blue","Indigo","Violet"]
print(colors.index("Red"))
colors.insert(2, "Yellows")
print (colors)



careers = ["Doctor", "Lawyer", "Athlete", "Coach"]
print careers.index("Athlete")
careers.insert (2, "Web Designer")
print careers

c = raw_input("What is your job? ")
careers.append(c)
print careers