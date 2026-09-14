# To-Do-List

import json


def load_tasks():
    try:
        with open("03-to-do-list-app/tasks.json", "r") as f:
            tasks = json.load(f)

    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
        
    return tasks

def save_tasks(tasks):
    with open("03-to-do-list-app/tasks.json", "w") as f:
        json.dump(tasks, f)
        
        
def add_tasks(tasks):
    add_to_list = input("\nAdd a task to your To-Do-List : ")
    tasks.append({"text": add_to_list, "done": False})
    print()
                    
    save_tasks(tasks)
    
def view_tasks(tasks):
    print()
    for index, item in enumerate(tasks, start=1):
        if item["done"]:
            print(f"[x]: {index}. {item['text']}")
        else:
            print(f"[ ]: {index}. {item['text']}")
    print()
        
def delete_tasks(tasks):
    while True:
        try:
            index = int(input("\nEnter the index you want to Delete : "))
            if is_valid_index(index, tasks):
                tasks.pop(index-1)
                print("Sucessfully Deleted.\n")
                            
                save_tasks(tasks)
                                                    
                break
            else:
                print("Enter a valid index.")
                            
        except ValueError:
            print("Enter a valid integer input")
            
def complete_task(tasks):
    while True:
        try:
            index = int(input("\nEnter the index you Completed : "))
            if is_valid_index(index, tasks):
                tasks[index-1]["done"] = True
                print("Sucessfully Updated.\n")
                            
                save_tasks(tasks)  
                                                    
                break
            else:
                print("Enter a valid index.")
                    
        except ValueError:
            print("Enter a valid integer input")
            
def is_valid_index(index, tasks):
    return index > 0 and index <= len(tasks)
    

def main():
    
    task_list = load_tasks()

    while True:
        try:
            user_input = int(
                input("Enter '1' to ADD \nEnter '2' to VIEW \nEnter '3' to QUIT \nEnter '4' to DELETE: \nEnter '5' to COMPLETE \n")
            )
            if user_input > 5 or user_input < 1:
                print("Invalid Input. Please Enter 1,2 or 3\n")
            
            elif user_input == 1:
                add_tasks(task_list)

            elif user_input == 2:
                view_tasks(task_list)
                
            elif user_input == 3:
                break
            
            elif user_input == 4:
                
                delete_tasks(task_list)
            
            elif user_input == 5:
                
                complete_task(task_list)
                                
        except ValueError:
            print("Error: Please Enter 1,2 or 3\n")
        
if __name__ == "__main__":
    main()