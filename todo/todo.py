import os
class Task:
    def __init__(self,title):
        self.title = title
        self.content = ""
        self.priority = 0
    def view(self):
        print(f" {self.title}: priority {self.priority}: content: {self.content}")

    def change_note(self, new_content, new_priority):
        self.content = new_content
        self.priority = new_priority

tasks = []
repeat = True
choice = ""

os.system("clear")
while repeat == True:
    print("current notes:\n")
    for task in tasks:
        task.view()
    choice = int(input("\n1: enter a note \n2: remove a note \n3: revise a note \n4: sort priority \n5: exit\n"))


    if choice == 1:
        tasks.append(Task(input("Enter a title for your note ")))
        os.system("clear")

    elif choice == 2:
        task_to_remove = input("enter a note number to remove: ")
        for task in tasks:
            if task.title == task_to_remove:
                tasks.remove(task)
            else:
                print("Error: no such note")

    elif choice == 3:
        task_to_revise = input("Enter a note to revise: ")
        for task in tasks:
            if task.title == task_to_revise:
                task.content = input("Enter the content of the note: ")
                task.priority = int(input("Enter the priority of this note: "))
                os.system("clear")
    elif choice == 4:
        for slot in range(len(tasks)-1,0,-1):
            largest = 0
            print(tasks[slot].priority)
            for index in range(1,slot+1):
                if tasks[index].priority < tasks[largest].priority:
                    largest = index

            temp = tasks[slot]
            tasks[slot] = tasks[largest]
            tasks[largest] = temp

    elif choice == 5:
        break
    else:
        print("try again my dude\n")
