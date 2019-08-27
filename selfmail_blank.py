import smtplib
from email.mime.text import MIMEText
import os
from os.path import isfile, join

mypath = os.getcwd()
onlyfiles = [f for f in os.listdir(mypath) if isfile(join(mypath, f))]


def send_mail():
    try:
        print(onlyfiles)
        ListToSend = input("Which file do you want to send?\n")
        f = open(ListToSend, "r")
        data = f.read()
        print(data)
        f.close()
        msg = MIMEText(data)
        msg['From'] = "yourmail"
        msg['To'] = "yourmail"
        msg['Subject'] = "ToDo"
        password = input("pw: ")
        smtp_server = smtplib.SMTP(host='provider smtp server', port=587)
        smtp_server.starttls()
        smtp_server.login(msg['From'], password)
        smtp_server.sendmail(msg['From'], msg['To'], msg.as_string())
        print("success")
    except Exception as e:
        print(e)
    finally:
        smtp_server.quit()


def todo_input():
    todo = input("What are your next tasks: \n")
    file = open("ToDo.txt", "a")
    for i in range(1):
        file.write("new Task %s\r\n" % todo)
    file.close()
    send_mail()


def delete_list():
    print(onlyfiles)
    mylist = input("Enter list to delete: ")
    if os.path.exists(mylist):
        os.remove(mylist)
    else:
        print("File does not exist!")


def new_list():
    newlist = input("Listname: \n")
    todo = input("ToDo: \n")
    file = open(newlist, "a")
    for i in range(1):
        file.write("new Task %s\r\n" % todo)
    file.close()


def main():
    print("Option 1: Create new task (includes send_mail)\n")
    print("Option 2: Only send mail\n")
    print("Option 3: Delete list\n")
    print("Option 4: Create new list\n")
    print("Option 5: Show files in current folder\n")
    k = input("Option: \n")

    if k == '1':
        todo_input()
    elif k == '2':
        send_mail()
    elif k == '3':
        w = input("Delete list? y/n\n")
        if w == 'y':
            delete_list()
        else:
            print("List not deleted")
    elif k == '4':
        new_list()
    elif k == '5':
        print(onlyfiles)
    else:
        print("Wrong number input\n")


if __name__ == "__main__":
    main()
