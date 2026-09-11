# To-Do-List

task_list = []

while True:
    try:
        user_input = int(
            input("Enter '1' to ADD \nEnter '2' to VIEW \nEnter '3' to QUIT \n: ")
        )
        if user_input > 3 or user_input < 1:
            print("Invalid Input. Please Enter 1,2 or 3\n")
        
        elif user_input == 1:
            add_to_list = input("\nAdd a task to your To-Do-List : ")
            task_list.append(add_to_list)
            print()

        elif user_input == 2:
            print()
            for index, item in enumerate(task_list, start=1):
                print(f"{index}: {item}")
            print()
            
        elif user_input == 3:
            break
                
    except ValueError:
        print("Error: Please Enter 1,2 or 3\n")