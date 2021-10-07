root = Tk()
root.title("ProjectGurukul Alarm Clock")
root.geometry("270x300")
root.resizable(False, False)
# Creating and placing all the components of the window
Label(root, text='When do you want to wake up?\n(Enter in 24-hour format)', font=("Comic Sans MS", 13), wraplength=root.winfo_width()).place(x=0, y=0)
Label(root, text='Hour', font=("Book Antiqua", 11), wraplength=root.winfo_width()).place(x=50, y=70)
Label(root, text='Minute', font=("Book Antiqua", 11), wraplength=root.winfo_width()).place(x=100, y=70)
Label(root, text='Second', font=("Book Antiqua", 11), wraplength=root.winfo_width()).place(x=160, y=70)
hours = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09']
minutes = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09']
seconds = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09']
for i in range(10, 24):
  hours.append(i)
for i in range(10, 61):
  minutes.append(i)
  seconds.append(i)
hour = StringVar(root)
hour.set(hours[0])
OptionMenu(root, hour, *hours).place(x=40, y=100)
minute = StringVar(root)
minute.set(minutes[0])
OptionMenu(root, minute, *minutes).place(x=100, y=100)
second = StringVar(root)
second.set(seconds[0])
OptionMenu(root, second, *seconds).place(x=160, y=100)
submit_btn = Button(root, text='Submit', bg='CadetBlue4', command=lambda: alarm_clock(hour.get()[:2], minute.get()[:2], second.get()[:2]))
submit_btn.place(x=100, y=150)
