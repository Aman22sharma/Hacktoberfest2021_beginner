import names
import pyperclip
def name():
    a = names.get_full_name()
    print(f"how is {a}")
    ra = int(input("how many names you want to generate"))

    ii = 0
    while True:
        print(f"Name: {names.get_full_name()}")
        if ra == ii:
              input("press enter to exit")
              break
        else:
            continue


from tkinter import *

# splash_root = Tk()
# splash_root.title("Password Generator")
# splash_img = PhotoImage(file="splash_img.png")
# splash_bg = Label(image=splash_img)
# splash_bg.place(x=0, y=0, relheight=1, relwidth=1)
# splash_root.geometry("580x470")


def main():
    # splash_root.destroy()
    root = Tk()

    def name_generator():
        global a
        entry_label.delete(0, END)
        a = names.get_full_name()
        entry_label.insert(0, a)

    def copy_command():
        pyperclip.copy(a)

    root.geometry("580x470")
    root.config(bg="black")
    root.title("Name Generator")
    f1 = Frame(root, borderwidth=14, bg="red", relief=SUNKEN)
    f1.pack()

    label = Label(f1, text="Name Generator", bg='yellow', fg="red", font="Arial 39 bold", borderwidth=3)
    label.pack(pady=21)
    pass_val = StringVar()
    entry_label = Entry(f1, bg="yellow", fg="red", font="arial 35 bold", borderwidth=3, textvariable=pass_val)
    entry_label.pack(pady=20)
    generate_button = Button(f1, text="generate name", bg="yellow", fg="red", font="arial 30 bold", borderwidth=3,
                             command=name_generator)
    generate_button.pack(pady=20)
    copy_button = Button(f1, text="copy", bg="yellow", fg="red", font="arial 30 bold", borderwidth=3,
                         command=copy_command)
    copy_button.pack(pady=20)
    root.mainloop()
# splash_root.after(3000, main)
main()
mainloop()
