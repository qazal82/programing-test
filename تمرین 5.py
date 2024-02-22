names = ["qazal", "mobina", "tarane", "fanaz"]
name="0"
while name != 'tooo':

    counter=0
    name = input("Enter a name: ")
    for user_name in names:
        if user_name==name :
            counter +=1

    if counter>0 :
        print("name is already in DB")

    else:
        names.append(name)
        print(name, "has been added to the database.")