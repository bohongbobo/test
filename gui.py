import tkinter as tk
from tkinter import ttk
import event_states

1111

1

1

1
1
1
1

1
1
1
1
11

1
1
1
1

1

window = tk.Tk()
window.title("event_states")
window.geometry("500x500")

test_descriptions = [["Car is ready", "Car is moving", "Car is finished"],
                        ["Car is not turning", "Car is turning left", "Car is turning right"],
                        ["Car is not avoiding", "Car is avoiding left car", "Car is avoiding right car"],
                        ["Normal course", "Shortcut Course"]]

event_descriptions = [["Red Light","Green Light"],
                      ["Start Line","Both Lines","Only Left Line","Only Right line","Left Line Close", "Right Line Close"],
                      ["No shortcut","Shortcut Entrance","Shortcut Exit"],
                      ["Horizontal Line","Finish Line","Horizontal Line Right","Horizontal Line Left"],
                      ["No Other Cars","Other Car Right","Other Car Left","Other Car Front"]]

def run():
    current_state = event_states.state([0,0,0,0,0,0], "State",test_descriptions)
    show = event_states.state.get_state(current_state)

    return show

def command():
    current_event = event_states.event([0,0,0,0,0],event_descriptions)
    output = event_states.begin_menu(current_state, current_event)

    return output

def get():
    input = str(en.get())
    t.insert(tk.END, input)

def close_window():
    window.destroy()
    exit()

but1 = ttk.Button(text = "run", command = run)

label1 = tk.Label(text="Type a command: ")

but0 = ttk.Button(text="command",command=command)

but2 = ttk.Button(text="show",command=get)

label0 = tk.Label(window, text="Your input shows here: ")

en = tk.Entry(window, bd=5)

t = tk.Text(master=window, height=10, width=28)

but3 = ttk.Button(text="Exit", command=close_window)

but1.pack()
label1.pack()
en.pack()
but0.pack()
but2.pack()
label0.pack()
t.pack()
but3.pack()

window.mainloop()
