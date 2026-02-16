# tasks
# a simple string entered by the user
# tasks will be stored using lists in the memory
# tasks will be saved in a text file in each line
tasks = []
f = open("tasks.txt")

for task in f:
    tasks.append(task.strip())


print("1. View tasks\n2. Add task\n3. Remove Task\n4. Exit")

while True:
    choice = input("Enter choice: ")
    if choice == "1":
        print(tasks)
    elif choice == "2":
        t = input("What task do you want to add: \n")
        tasks.append(t)
        file = open("tasks.txt","w")
        for task in tasks:
            file.write(task+ "\n")
        file.close()
    elif choice == "3":
        r = input("What task do you want to remove: \n")
        tasks.remove(r)
        file = open("tasks.txt","w")
        for task in tasks:
            file.write(task+ "\n")
        file.close()
    elif choice == "4":
        break
    else:
        print("invalid input")
