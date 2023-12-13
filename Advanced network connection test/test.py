# # import tkinter as tk
# # from tkinter import ttk
# # from tkinter.ttk import Button, Style, Frame

# # root = tk.Tk()
# # style = ttk.Style()
# # style.configure('TButton', foreground='red', relief='sunken', padding=20)
# # mainframe = Frame(root)
# # button = Button(mainframe, text='test')
# # button.pack(padx=20, pady=20)
# # mainframe.pack()
# # root.mainloop()
# import subprocess

# # Run the 'ipconfig' command to get network information
# result = subprocess.run(["ipconfig"], capture_output=True, text=True)

# # Check if the command was successful
# if result.returncode == 0:
#     # Split the output into lines and find the line with the Wi-Fi interface
#     lines = result.stdout.split('\n')
#     for line in lines:
#         if "wi" in line.lower() or "eth" in line.lower() or "area" in line.lower() :
#             # Look for the line that contains the Default Gateway
#             for line in lines[lines.index(line):]:
#                 if "Default Gateway" in line:
#                     default_gateway = line.split(':')[-1].strip()
#                     print(default_gateway)
#                     gateway = ["192.168.1.1","192.168.0.1","192.168.1.254","192.168.0.254","192.168.254.254","10.10.1.1","192.168.2.1","192.168.254.2","192.168.254.1","192.168.3.1"]
#                     if default_gateway in gateway:
#                         print ("test")
#                     break
# else:
#     print("Error running 'ipconfig'.")

import psutil

def check_cable_connection_status():
    interfaces = psutil.net_if_stats()
    disconnected_ethernet = []
    disconnected_wifi = []

    for interface, stats in interfaces.items():
        if not stats.isup:
            if "eth" in interface.lower() or "area" in interface.lower() :
                disconnected_ethernet.append(interface)

    # Check for the presence of Wi-Fi interface
    all_interfaces = psutil.net_if_addrs()
    wifi_present = any("fi" in interface.lower() for interface in all_interfaces)
    if wifi_present:
        for interface, stats in interfaces.items():
            if not stats.isup and "fi" in interface.lower():
                disconnected_wifi.append(interface)

    return disconnected_ethernet, disconnected_wifi
    
        
disconnected_ethernet, disconnected_wifi = check_cable_connection_status()

if disconnected_ethernet and not disconnected_wifi:
    result = False
elif disconnected_wifi and not disconnected_ethernet:
    result = False
elif disconnected_wifi and disconnected_ethernet: 
       result = True
elif disconnected_ethernet:
    result = True
elif  disconnected_wifi :
    result = True
else:
   result = False