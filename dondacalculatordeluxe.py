import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

ver = "v1.5.0"

def commenseGUI():
    #window section
    window = tk.Tk()
    window.geometry("400x400") #widthxheight
    window.title("Donda Calculator Deluxe")
    window.resizable(False, False)
    window.iconbitmap("donda.ico")
    kanye = ImageTk.PhotoImage(Image.open("kanye.png"))

    #frames section
    frame = tk.Frame(height=200, width=400)
    infoFrame = tk.Frame(height=200, width=200)
    kanyeFrame = tk.Frame(height=200, width=200)

    #button section
    amPm = tk.StringVar(window, "0")
    amButton = ttk.Radiobutton(window, text="AM", variable=amPm, value="AM")
    pmButton = ttk.Radiobutton(window, text="PM", variable=amPm, value="PM")
    tfourButton = ttk.Radiobutton(window, text="24 Hour Time", variable=amPm, value="24")

    #label section
    instrLabel = tk.Label(frame, text="Enter information in each field, then click DONDA")
    timeLabel = tk.Label(frame, text="What is the current time?")
    kanyeLabel = tk.Label(kanyeFrame, image=kanye)
    credz1 = tk.Label(infoFrame, text="Anthony Salierno (calculations)")
    credz2 = tk.Label(infoFrame, text="Christian Giampapa (GUI)")
    vLab = tk.Label(infoFrame, text=ver)
    hour = tk.Entry(width=20)
    answerLabel = tk.Label(frame)
    answerLabelTwo = tk.Label(frame)
    answerLabelThree = tk.Label(frame)
    button = ttk.Button(frame, text="DONDA", command=lambda: update(hour.get(), amPm.get(),answerLabel,answerLabelTwo,answerLabelThree))


    frame.place(x=0, y=0)
    instrLabel.place(x=0, y=0)
    timeLabel.place(x=0, y=40)
    hour.place(x=150, y=40)
    amButton.place(x=0,y=80)
    pmButton.place(x=40, y=80)
    tfourButton.place(x=80, y=80)
    button.place(x=190, y=78)
    answerLabel.place(x=0,y=140)
    answerLabelTwo.place(x=0,y=160)
    answerLabelThree.place(x=0,y=180)


    infoFrame.place(x=0, y=200)
    credz1.place(x=0, y=140)
    credz2.place(x=0, y=160)
    vLab.place(x=0, y=180)

    kanyeFrame.place(x=200, y=200)
    kanyeLabel.pack()

    window.mainloop()

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

def update(hour,amPm,answerLabel,answerLabelTwo,answerLabelThree):
    time = hour.split(":")
    data = [amPm, time[0], time[1]]
    answerList = commenseDonda(data)
    answerLabel["text"] = answerList[0]
    answerLabelTwo["text"] = answerList[1]
    answerLabelThree["text"] = answerList[2]

commenseGUI()