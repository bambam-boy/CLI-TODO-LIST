import os
import json
import sys

rootPath = "/home/kushan/.CLI_TODOLIST"
rootFile = rootPath + "/tasks.json"
OKCYAN = "\033[96m"
OKGREEN = "\033[92m"
ENDC = "\033[0m"
WARNING = "\033[93m"


def main():
    while True:
        if os.path.exists(rootPath):
            print("Welcome back to your CLI TODO LIST")
        else:
            print("We are so happy to see you here for first time")
            os.mkdir(rootPath)
            open(rootFile, "w").close()
        choice = int(
            input(
                "1. View Tasks\n2. Add Task\n3. Delete Task\n4. Exit\nEnter your choice: "
            )
        )
        match choice:
            case 1:
                viewTasks()
                break
            case 2:
                addTask()
                break
            case 3:
                deleteTask()
                break
            case 4:
                print("Thank you for using CLI TODO LIST. See you next time!")
                sys.exit(0)
                break
            case _:
                print("invalid choice try again")
                break


def deleteTask():
    final: dict = {}
    keyname = input("enter the title of task that you want to change: ")
    if keyname != "":
        if keyname != None:
            with open(rootFile) as f2:
                data2 = (
                    f2.read()
                    .replace('"', "")
                    .replace("\\", "")
                    .replace("{", "")
                    .replace("}", "")
                    .replace(" ", "")
                )
                f2.close()
            filtereditems = []
            for itemchecker in data2.split(","):
                filtereditems.append({itemchecker})

            for filtereditem in filtereditems:
                castfilter = (
                    str(filtereditem)
                    .replace("{", "")
                    .replace("}", "")
                    .replace('"', "")
                    .replace("'", "")
                    .split(":")
                )
                isfounded = False
                indexFindeditem = -1
                need_To_Add = []
                for item in castfilter:
                    if item == keyname:
                        indexFindeditem = castfilter.index(item)
                        isfounded = True
                    elif isfounded == True:
                        if castfilter.index(item) == indexFindeditem + 2:
                            isfounded = False
                        else:
                            continue
                    else:
                        need_To_Add.append(item)
                for i in range(0, len(need_To_Add)):
                    if i % 3 == 0 and i != len(need_To_Add) - 1:
                        final.update(
                            {need_To_Add[i]: {need_To_Add[i + 1]: need_To_Add[i + 2]}}
                        )
            if final != None:
                with open(rootFile, "w") as w:
                    w.write(json.dumps(final))
                    w.close()
        else:
            print("doesnt found that item try again")
    else:
        print("you can not leave the name of item that you want to change")


def addTask():
    while True:
        title = input("enter the title of your task: ")
        task = input("enter your task: ")
        if os.path.exists(rootFile):
            if task == "":
                print("you can not add empty task")
            else:
                with open(rootFile, "r") as f:
                    datadummy = json.load(f)
                    f.close()

                new_data = {title: {"task": task}}
                datadummy.update(new_data)

                filewriter = open(rootFile, "w")
                try:
                    filewriter.write(json.dumps(datadummy))
                finally:
                    filewriter.close()
                    break
        else:
            open(rootFile, "w").close()
            if task == "":
                print("you can not add empty task")

            else:
                data = json.dumps({title: {"task": task}})
                filewriter = open(rootFile, "a")
                try:
                    filewriter.write(data)
                finally:
                    filewriter.close()
                    break


def viewTasks():
    with open(rootFile, "r") as f:
        data = (
            f.read()
            .replace('"', "")
            .replace("\\", "")
            .replace("{", "")
            .replace("}", "")
            .replace(":", "")
            .replace(" ", "")
        )
        f.close()

    valid_Data = []
    new_valid_Data = []
    for items in data.split(","):
        for item in items.split("task"):
            valid_Data.append(item)

    for i in range(len(valid_Data)):
        if i == len(valid_Data) - 1:
            break
        elif i % 2 == 0:
            new_valid_Data.append(
                OKCYAN
                + valid_Data[i]
                + WARNING
                + ": "
                + OKGREEN
                + valid_Data[i + 1]
                + ENDC
            )
    for item in new_valid_Data:
        print(item)


if __name__ == "__main__":
    main()
