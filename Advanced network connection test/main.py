import tkinter as tk
from tkinter import ttk
from passive import Passiv
import requests
import connectivity
from accsess_point import Acess_point
from trust import Trust
from apepa import Apepa

def perform_task():
    def test_conect():
        test_conect = connectivity.Connect().result
        return test_conect
    
    def ipaddress_for_acess_point():
        ipaddress_for_acess = Acess_point().result
        return ipaddress_for_acess
        
    def passive_problem():
        passive_problem = Passiv().result
        return passive_problem

    def test_trust():
        test_trust = Trust().result 
        return test_trust
    
    def test_apepa():
        test_apepa = Apepa().result
        return test_apepa

    if test_conect() == True:
        my_lable = tk.Label(text="\u2713", foreground="#D3D9E9", font=("hsn ibtisam", 100, "bold"), background="#627497")
        my_lable1 = tk.Label(text="انت متصل بنجاح ", foreground="#D3D9E9", font=("Calibri", 50, "bold"), background="#627497")

    elif passive_problem():
        my_lable1 = tk.Label(text="Error 445", foreground="#D3D9E9", font=("Calibri", 30, "bold"), background="#627497")
        my_lable = tk.Label(text="\u2717", foreground="#D3D9E9", font=("Calibri", 130, "bold"), background="#627497")
    elif requests.utils.getproxies() != {}:
        my_lable1 = tk.Label(text="Error 443 ", foreground="#D3D9E9", font=("Arial", 30, "bold"), background="#627497")
        my_lable = tk.Label(text="\u2717", foreground="#D3D9E9", font=("Arial", 130, "bold"), background="#627497")
    elif test_apepa() == True:
        my_lable1 = tk.Label(text="Error 442", foreground="#D3D9E9", font=("Arial", 30, "bold"), background="#627497")
        my_lable = tk.Label(text="\u2717", foreground="#D3D9E9", font=("Arial", 130, "bold"), background="#627497")
    
    elif ipaddress_for_acess_point() == True:
        my_lable1 = tk.Label(text="Error 400", foreground="#D3D9E9", font=("Arial", 30, "bold"), background="#627497")
        my_lable = tk.Label(text="\u2717", foreground="#D3D9E9", font=("Arial", 130, "bold"), background="#627497")
    else:
        my_lable1 = tk.Label(text="Error 412", foreground="#D3D9E9", font=("Arial", 30, "bold"), background="#627497")
        my_lable = tk.Label(text="\u2717", foreground="#D3D9E9", font=("Arial", 130, "bold"), background="#627497")
        
    if test_trust() == False:
        my_lable1 = tk.Label(text="Error 415", foreground="#D3D9E9", font=("Arial", 30, "bold"), background="#627497") 
        my_lable = tk.Label(text="\u2717", foreground="#D3D9E9", font=("Arial", 130, "bold"), background="#627497")
  

    my_lable.pack()
    my_lable1.pack()

def show_loading_screen():
    loading_screen = tk.Toplevel(root)
    loading_screen.minsize(width=750, height=250)
    loading_screen.title("Loading...")    
    label = ttk.Label(loading_screen, text="جاري التحميل الرجاء الانتظار ", font=("Calibri", 40), style='TLabel')
    label.pack(pady=50 )
    loading_screen.update()
    perform_task()
    loading_screen.destroy()

def start():
    show_loading_screen()

def disable_button():
    button.pack_forget()  # This will remove the button completely

root = tk.Tk()
style = ttk.Style()
root.title("اختبار الاتصال الشبكه")
root.configure(bg='#627497')

# Calculate the center coordinates of the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 900
window_height = 500
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Set the window size and position
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

frame = tk.Frame(root)
frame.pack()
frame.configure(bg='#627497')

button_frame = tk.Frame(frame, bg='#627497')
button_frame.pack(padx=20, pady=20)

button = tk.Button(
    button_frame,
    text="ابدأ",
    command=lambda: [start(), disable_button()],
    width=15,
    padx=0,
    pady=5,
    bg='#D3D9E9',
    fg='black',
    font=("Calibri", 25, "bold"),
)
style = ttk.Style()
sentence_label = tk.Label(root, text="dev by eng. Mostafa Mohamed", font=("Forte", 12), bg="#627497", fg="#D3D9E9", anchor="w", justify="left")
sentence_label.pack(side="bottom", fill="x")

button.pack(padx=20, pady=20)
root.mainloop()