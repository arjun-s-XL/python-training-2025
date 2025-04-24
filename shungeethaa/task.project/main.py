from task import display_task,addtask,remove_tasks

def main():
    print("Task manager app")
    display_task()
    print(addtask("Develop"))
    print(addtask("Write unit test"))
    print(addtask("Deploy"))
    display_task()
    print(remove_tasks(0))
    display_task()
    print(remove_tasks(0))
    display_task()
    print(remove_tasks(0))
    display_task()
    print(remove_tasks(0))

if __name__=="__main__":
    main()
