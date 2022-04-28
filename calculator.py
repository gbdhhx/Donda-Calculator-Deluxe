import tkinter as tk
from tkinter import ttk

ver = "v1.4.0"


def commenseDonda(data):
    amPm = data[0].lower()
    hour = int(data[1])
    if amPm == "am" and hour == 12:
        hour -= 12
    if amPm == "pm" and hour != 12:
        hour += 12
    dondaUnit = ((hour * 60) + int(data[2])) / 108
    answerOne = "It is " + str(dondaUnit) + " Dondas"

    dondaLeft = 13.23529412 - dondaUnit

    answerTwo = "You have " + str(dondaLeft) + " dondas Left in the day. "
    answerThree = statement(dondaLeft)
    return [answerOne, answerTwo, answerThree]


def statement(x):
    if x > 13:
        return "Go To bed before Ye thinks about murdering you. "
    elif x > 12:
        return "Donda, Donda, DondaDonda, Donda, Donda, Donda, Donda,Donda,Donda, Donda, Donda, Donda ,Donda, Donda, Donda, Donda, Donda, Donda, Donda, Donda, Donda, Donda, Donda, Donda, DondaDonda, Donda, Donda, Donda, DondaDonda, Donda, Donda, Donda, Donda, DondaDonda, Donda, Donda, DondaDonda, Donda,Donda, Donda, Donda, Donda, Donda, Donda, Donda, Donda, DondaDonda, Donda, Donda, Donda, Donda, Donda, Donda, Donda. "
    elif x > 11:
        return "No one man should have all that power. The clock's ticking, I just count the hours."
    elif x > 10:
        return "Okay I scratched your corolla. "
    elif x > 9:
        return "Go To bed before Ye thinks about murdering you. "
    elif x > 8:
        return "She got a light skinned friend look like Michael Jackson. Got a dark skinned friend look like Michael Jackson "
    elif x > 7:
        return "Guess who's goin' to jail tonight? "
    elif x > 6:
        return "I stopped buying Louis bags after Virgil passed. "
    elif x > 5:
        return "No hard feelings, but my feelings harder. "
    elif x > 4:
        return "I'm too black, I'm too vocal, I'm too flagrant. "
    elif x > 3:
        return "This generation's closest thing to Einstein. "
    elif x > 2:
        return "I feel like me and Taylor might still have sex. "
    elif x > 1:
        return "Choke a South Park writer with a fishstick."
    elif x == 1:
        return "You still have enough time to listen to Donda today."
    # It's 10:16 PM if you're Curious
    else:
        return "Find God."


window = tk.Tk()
instrLabel = tk.Label(text="Enter information in each field, then click DONDA")

amPm = tk.StringVar(window, "0")
amButton = ttk.Radiobutton(window, text="AM", variable=amPm, value="AM")
pmButton = ttk.Radiobutton(window, text="PM", variable=amPm, value="PM")
tfourButton = ttk.Radiobutton(window, text="24 Hour Time", variable=amPm, value="24")

hourLabel = tk.Label(text="What is the current time?")
hour = tk.Entry(width=50)

answerLabel = tk.Label()
answerLabelTwo = tk.Label()
answerLabelThree = tk.Label()
credz1 = tk.Label(text="Anthony Salierno (calculations)")
credz2 = tk.Label(text="Christian Giampapa (GUI)")
vLab = tk.Label(text=ver)


def update():
    time = hour.get().split(":")
    data = [amPm.get(), time[0], time[1]]
    answerList = commenseDonda(data)
    answerLabel["text"] = answerList[0]
    answerLabelTwo["text"] = answerList[1]
    answerLabelThree["text"] = answerList[2]


button = ttk.Button(window, text="DONDA", command=update)

window.title("Donda Calculator Deluxe")
window.iconbitmap("donda.ico")
instrLabel.pack()
hourLabel.pack()
hour.pack()
amButton.pack()
pmButton.pack()
tfourButton.pack()
button.pack()
answerLabel.pack()
answerLabelTwo.pack()
answerLabelThree.pack()
credz1.pack(side=tk.LEFT)
credz2.pack(side=tk.LEFT)
vLab.pack(side=tk.LEFT)
window.mainloop()
