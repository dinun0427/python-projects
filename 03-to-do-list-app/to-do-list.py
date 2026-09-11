# To-Do-List

task_list = []

while True:
    try:
        user_input = int(
            input("Enter '1' to ADD \nEnter '2' to VIEW \nEnter '3' to QUIT \nEnter '4' to DELETE: \nEnter '5' to COMPLETE \n")
        )
        if user_input > 5 or user_input < 1:
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
        
        elif user_input == 4:
            while True:
                try:
                    index = int(input("\nEnter the index you want to Delete : "))
                    if index <= len(task_list) and index > 0:
                        task_list.pop(index-1)
                        print("Sucessfully Deleted.\n")
                        break
                    else:
                        print("Enter a valid index.")
                except ValueError:
                    print("Enter a valid integer input")
        
        elif user_input == 5:
            while True:
                try:
                    index = int(input("\nEnter the index you Completed : "))
                    if index <= len(task_list) and index > 0:
                        task_list[index-1] = "[DONE] " + task_list[index-1]
                        print("Sucessfully Updated.\n")
                        break
                    else:
                        print("Enter a valid index.")
                except ValueError:
                    print("Enter a valid integer input") 
                               
    except ValueError:
        print("Error: Please Enter 1,2 or 3\n")