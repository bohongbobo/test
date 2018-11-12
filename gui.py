import tkinter as tk
from tkinter import ttk
import event_states
#from event_states import event
#from event_states import state
asdfasd




2

2

2
2

2

2
2
22
2
2

2



window = tk.Tk()
window.title("event_states")
window.geometry("500x500")

test_descriptions = [["Car is ready", "Car is moving", "Car is finished"],
                        ["Car is not turning", "Car is turning left", "Car is turning right"],
                        ["Car is not avoiding", "Car is avoiding left car", "Car is avoiding right car"],
                        ["Car is not chasing", "Car is chasing"],
                        ["Normal course", "Shortcut Course"]]

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
