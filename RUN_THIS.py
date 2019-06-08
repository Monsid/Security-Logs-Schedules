import os
import subprocess
from subprocess import PIPE, run
import time
import sys

"""The purpose of function view_and_delete_schedules is to view the schedules created by this script only, there are 
function within this one which serve for the purpose of input validation as well allowing for more functionality like 
deleting the viewed schedules from the console in the running script"""
def view_and_delete_schedules():

    from subprocess import PIPE, run

    def loop_try():
        answerinorino = input('Retry? (y/n) - ')
        if answerinorino == "y":
            view_and_delete_schedules()
        elif answerinorino == 'n':
            menu()
        else:
            print("invalid input")
        loop_try()
    """The deletor function serves the view_and_delete_schedules function in deleting the schedules"""
    def deletor():
        mustAsk = (input("Type the number(0,1,2,3,etc) of the item you would like to delete then press enter - "))
        if mustAsk == '':
            print("Invalid Input - you didn't actually type anything mate...")
            loop_try()

        elif int(mustAsk) <= maxi:
            set_it_up = (tug[int(mustAsk)])
            cmd_appendage = (set_it_up[0:22])
            os.system('schtasks /delete /tn "' + cmd_appendage + '" /f')
        else:
            print("Invalid Input not in index")
            loop_try()

        AltReRun2()

    """This out(command) function is simply a subprocess for querying task scheduler for schedules with the word 
    'created'"""
    def out(command):
        result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
        return result.stdout

    my_output = out('schtasks /query | findstr /i "Created"')
    clean = "".join(my_output)
    tug = clean.splitlines(False)

    maxi = 0

    for c, value in enumerate(tug, 0):
        print(c, value)
        if maxi < c:
            maxi = c

    main_or_delete = input("(1)Delete Schedules or (2)Return to Main Menu - ")

    while True:
        if main_or_delete == "1":
            print("okay")
            deletor()
            AltReRun2()
            break
        elif main_or_delete == "2":
            menu()
            break
        else:
            print("Invalid Input")
            loop_try()
            break


"""The function log_scheduler's purpose is to create a task schedule for a specific time that will create a log file
of the l0 latest security audit event IDs 4624 and 4625, it does this by creating a powershell .ps1 file with CMD prompt
 and then opening it with powershell as a local admin, this kind of makes the script location specific - if the script 
 is run from any directory other than 'C:\Security-Logs-Schedules' it wont be able to call the powershell .ps1 file"""
def log_scheduler():

    print("WARNING: Creating this Schedule will shutdown other instances of Powershell!")
    print("What time would you like the script to run everyday?")
    xariable = input("0:00 - 24:00<- insert time - ").lower().replace(" ", "")
    Rinow = time.strftime('%d%m%Y%H%M%S')  # in the format DMYHMS
    newnames = "Created " + Rinow
    xyz = "TaskSchedule_Code" + Rinow + ".ps1"
    lines = ["Start-Process powershell -Verb runAs \n"
        "$action = New-ScheduledTaskAction -Execute 'C:\Security-Logs-Schedules\SCHEDULED.bat'\n",
        "$trigger = New-ScheduledTaskTrigger -Daily -At " + xariable + "\n",
        "Register-ScheduledTask -Action $action -Trigger $trigger -TaskName '" + newnames +
        "' -Description 'This creates logs of the latest authentications recorded at the set time in the Python script Folder'\n"]
    os.system("cd C:\Security-Logs-Schedules")
    os.system("type nul >" + xyz + "\n")

    file = open(xyz, mode="a+", encoding="utf-8")
    file.writelines(lines)
    for i in file:
        print(i)
    file.close()
    print(xariable)

    os.system("cd C:\Security-Logs-Schedules")
    os.system("powershell Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine")
    os.system('powershell "& ""C:\Security-Logs-Schedules\\' + xyz + '"""')
    os.system(('taskkill /IM "powershell.exe" /F'))


"""This function - da_file_eyes was created to view the script directory files, but only show whats relevant - the log
authentication .txt files"""
def da_file_eyes():
    def loop_try():
        answerinorino = input('Retry? (y/n)')
        if answerinorino == "y":
            da_file_eyes()
        elif answerinorino == 'n':
            menu()
        else:
            print("invalid input")
        loop_try()

    files = [f for f in os.listdir('.') if f.endswith(".txt")
             if os.path.isfile(f)]

    maxi = 0
    for num, line in enumerate(files):
        print(num, line)
        if maxi < num:
            maxi = num

    user_turn = (input("Which line (1,2,3etc) would you like to read(top to bottom): "))

    if user_turn == '':
        print("Invalid Input - you didn't actually type anything mate...")
        loop_try()

    elif int(user_turn) <= maxi:
        set_var = (files[int(user_turn)])
        print("You have selected: " + set_var)
        file_object = open(set_var, mode="r+")
        file_object.seek(0)
        print(file_object.read())

    else:
        print("Invalid Input, that number is not in index")
        loop_try()

    AltReRun()


"""This function - da_file_genie creates the latest 10 login security audit logs"""
def da_file_genie():
    emptylogfile = []
    Rinow = time.strftime('%d%m%Y%H%M%S')  # in the format DMYHMS
    with open("AuthenticationLog" + Rinow + ".txt", "w") as f:
        for i in emptylogfile:
            f.write(i)
    x = "AuthenticationLog" + Rinow + ".txt"
    os.system("powershell Get-EventLog -logname security -instanceid 4625,4624 -newest 10 >" + x)

"""This is my main menu, to give it a basic menu feel I have been a bit silly and added some fat spacing, manually attempting
to allign text to center. The function serves as a menu with if and elifs as options for the above functions."""
def menu():

    print(" ")
    print(" ")
    print("                                Hello and Welcome to the Main Menu of Security-Logs-Schedules")
    print(" ")
    print("*IMPORTANT PLEASE READ*   This script is designed for windows cmd prompt run as administrator with python installed   *IMPORTANT PLEASE READ*")
    print(" ")
    print("                                    Please Select a number corresponding with the function:")
    print(" ")
    print("                                                  Through Event Viewer")
    print("                      1 = 5 latest successful login logs   |    2 = 5 latest unsuccessful login logs")
    print(" ")
    print("                                                     Export to File")
    print("              3 = Save 10 latest authentication attempts to a text file  |  4 = File Viewer (views all text files)")
    print(" ")
    print("                                                       Scheduler")
    print("           5 = Schedule option 3 to run at a particular time    |    6 = Schedule Viewer (views and deletes schedules)")
    print(" ")
    print("Exit:")
    print("7 = Close")
    print(" ")
    MainMenu = (input("input number and press enter - "))

    while True:

        if MainMenu == "1":
            os.system("powershell get-winevent -FilterHashtable @{Logname='Security';ID=4624}  -MaxEvents 5")
            ReRun()
            break
        elif MainMenu == "2":
            os.system("powershell get-winevent -FilterHashtable @{Logname='Security';ID=4625}  -MaxEvents 5")
            ReRun()
            break
        elif MainMenu == "3":
            da_file_genie()

            ReRun()
            break
        elif MainMenu == "4":
            da_file_eyes()


            break
        elif MainMenu == "5":
            log_scheduler()
            answerino = input("Would you like to go to the Schedule Viewer? (y/n) - ")
            if answerino == "n":
                ReRun()
                break
            elif answerino == "y":
                view_and_delete_schedules()
                break
            else:
                print("Invalid Input")
            ReRun()
            break
        elif MainMenu == "6":
            view_and_delete_schedules()
            break


        elif MainMenu == "7":
            print("goodbye")
            break
        else:
            print("Invalid Input")
            ReRun()
            break


"""The functions ReRun, AltReRun2, alt_invalid and AltReRun all serve as input validation and will prevent invalid user 
 input from breaking the scripts functionality."""
def ReRun():
    while True:
        answer = str(input('Return to Main Menu? (y/n): '))
        if answer == 'y':
            menu()
            break
        elif answer == 'n':
            print('goodbye')
            break
        else:
            print('Invalid Input')
            ReRun()
            break

def AltReRun2():
    while True:
        answer = str(input('Return to Schedule Viewer? (y/n): '))
        if answer == 'y':
            view_and_delete_schedules()
            break
        elif answer == 'n':
            print('Returning to Main Menu')
            menu()
            break
        else:
            print('Invalid Input')
            AltReRun2()
            break


def alt_invalid():
    while True:
        answer = str(input('Invalid Input, would you like to try again from the Main Menu? (y/n): '))
        if answer == 'y':
            menu()
            break
        elif answer == 'n':
            print('Returning to Main menu')
            break
        else:
            print("I don't understand!")
            alt_invalid()
            break



def AltReRun():
    while True:
        answer = str(input('Return to File Viewer? (y/n): '))
        if answer == 'y':
            da_file_eyes()
            break
        elif answer == 'n':
            print('Returning to Main menu')
            menu()
            break
        else:
            print('Invalid Input')
            AltReRun()
            break

menu()
