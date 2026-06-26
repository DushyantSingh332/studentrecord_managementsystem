def add_students():
    std = input("ENTER THE STUDENT NAME")
    rec = input("ENTER THE STUDENT MAKRS")

    with open("students.txt","a") as file:
        file.write(std + "," + rec + "\n")

    print("STUDENT RECORD ADDED SUCCESFULLY.")


def view_students():
    try:
        with open("students.txt","r") as file:
            print("\n-------- Student Record ----------")
            for line in file:
                name, marks = line.strip().split(",")
                print(f"Name: {name}, Marks: {marks}")
    except FileNotFoundError:
        print("No Record Found.")

while True:
    print("\n1.Add Student " 
          "2.View student " \
          "3.Exit ")
    choice = input("Enter Your Choice")

    if choice == "1":
        add_students()

    elif choice == "2":
        view_students()

    elif choice == "3":
        print("--------EXITED SUCCESFULLY-----------------")
        break

    else:
        print("INVALID CHOICE")

    

                

   