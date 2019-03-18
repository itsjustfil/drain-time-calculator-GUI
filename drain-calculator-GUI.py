# GUI created to calcluate drain time out of a pipe

from tkinter import Tk, Label, Entry, Button, messagebox
top = Tk() # creates new window
top.title("Drain Time Calculator") # window title

LBLH = Label(top, text = "Height of the liquid above the hole").grid(row = 0)
ENTH = Entry(top)
ENTH.grid(row = 0, column = 1) # user entry for liquid height

LBLA = Label(top, text = "Horizontal cross section area").grid(row = 1)
ENTA = Entry(top)
ENTA.grid(row = 1, column = 1) # user entry for pipe horizontal cross section area

LBLa = Label(top, text = "Hole cross section area").grid(row = 2)
ENTa = Entry(top)
ENTa.grid(row = 2, column = 1) # user entry for cross section area of the hole

def DrainCalc(): # function that calculates the drain time to be assigned to a button
    try:
        # gets entries as strings from entry box
        H = ENTH.get() 
        A = ENTA.get()
        a = ENTa.get()

        # converts strings to float type
        H = float(H) 
        A = float(A)
        a = float(a)
        g = 9.80655 # gravity

        # assert entries are greater than zero
        assert H > 0
        assert A > 0
        assert a > 0
        
        drain  = ((2 * A) / a) * (2 * H / g) ** 0.5 # drain time equation, result in second

    except AssertionError:
        messagebox.showinfo("Calculate" , "Your entries must be greater than zero.")

    finally:
        hours = drain / 3600 # drain time in hours
        mins = drain / 60 - int(hours)*60 # drain time in mins
        sec = drain % 60 # drain time seconds left over

        if (hours < 1 and mins < 1):
            messagebox.showinfo("Calculate", "The time it takes for the liquid to drain is:" + str(int(sec)) + " seconds. ") # Will display only if the liquid trains in 59 seconds or less
        elif (hours < 1):
            messagebox.showinfo("Calculate" , "The time it takes for the liquid to drain is: " + str(int(mins)) + " minutes and " + str(int(sec)) + " seconds.") # Will display only if the liquid drains in less than an hour
        elif (mins < 1):
            messagebox.showinfo("Calculate" , "The time it takes for the liquid to drain is: " + str(int(hours)) + "hours and" + str(int(sec)) + " seconds.") # Displays only hours and second
        else:
            messagebox.showinfo("Calculate" , "The time it takes for the liquid to drain is: " + str(int(hours)) + " hours " + str(int(mins)) + " minutes and " + str(int(sec)) +  " seconds. ") # Displays hours, minutes, and seconds for drainage

BTN  = Button(top, text = "Calculate" , command = DrainCalc) # button that when clicked will calculate drain time
BTN.grid(row = 6, column = 1)
top.mainloop()
