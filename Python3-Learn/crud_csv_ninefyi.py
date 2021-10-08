#AUTHOR: Piti (Fyi) Champeethong
#Python3 Concept: CRUD for CSV file
#GITHUB: https://github.com/ninefyi

import csv

def create_mobile():
    name = str(input("Enter mobile contact:"))
    mobile = str(input("Enter mobile number:"))
    headers = ['name', 'mobile']
    with open("mobile.csv", "a+", encoding='UTF8', newline='') as f:
        writer  = csv.DictWriter(f,fieldnames=headers)
        writer.writerow({'name':name, 'mobile':mobile})

def read_mobile():
    headers = ['name', 'mobile']
    with open("mobile.csv", "r+", encoding='UTF8') as f:
        reader = csv.DictReader(f,fieldnames=headers)
        print("Row\tName\t\tMobile")
        print("-" * 30)
        row_index = 1
        for line in reader:
            print(row_index, "\t", line['name'],"\t\t",line["mobile"])
            row_index = row_index + 1

def update_mobile():
    row_number = int(input("Enter row number for updating:"))
    headers = ['name', 'mobile']
    update_list = []
    with open("mobile.csv", "r+", encoding='UTF8') as f:
        reader = csv.DictReader(f,fieldnames=headers)
        row_index = 1
        for line in reader:
            if(row_index == row_number):
                name = str(input("Enter new mobile contact ({}):".format(line['name'])))
                mobile = str(input("Enter new mobile number ({}):".format(line["mobile"])))
                line['name'] = name
                line['mobile'] = mobile
            update_list.append(line)
            row_index = row_index + 1
    update_csv(update_list)

def delete_mobile():
    row_number = int(input("Enter row number for deleting:"))
    headers = ['name', 'mobile']
    update_list = []
    with open("mobile.csv", "r+", encoding='UTF8') as f:
        reader = csv.DictReader(f,fieldnames=headers)
        row_index = 1
        for line in reader:
            if(row_index != row_number):
                update_list.append(line)
            row_index = row_index + 1
    update_csv(update_list)

def update_csv(new_list):
    headers = ['name', 'mobile']
    with open("mobile.csv", "w+", encoding='UTF8', newline='') as f:
        writer  = csv.DictWriter(f,fieldnames=headers)
        writer.writerows(new_list)
    
def display_menu():
    print("-" * 30)
    print("1. Create a new mobile number on CSV")
    print("2. Read all mobile numbers from CSV")
    print("3. Update a mobile numbers from CSV")
    print("4. Delete a mobile numbers from CSV")
    print("0. Exit")
    menu = int(input("Enter you menu number [0,1,2,3,4]:"))
    print("-" * 30)
    return menu

menu = display_menu()

while menu != 0:
    if menu == 1:
        create_mobile()
    elif menu == 2:
        read_mobile()
    elif menu == 3:
        update_mobile()
    elif menu == 4:
        delete_mobile()
    elif menu == 0:
        exit
    menu = display_menu()