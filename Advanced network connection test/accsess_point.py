# import wmi
# import os
# class Acess_point:
    
#     def __init__(self ) -> None:
#         def gat ():
#             try:    
#                 wmi_obj = wmi.WMI()
#                 wmi_sql = "select IPAddress,DefaultIPGateway from Win32_NetworkAdapterConfiguration where IPEnabled=TRUE"
#                 wmi_out = wmi_obj.query( wmi_sql )
#                 return wmi_out[0].DefaultIPGateway[0]
#             except:
#                 return "erorr"
#         ip = gat()
#         gateway  = ["192.168.1.1","192.168.0.1","192.168.1.254","192.168.0.254","192.168.254.254","10.10.1.1","192.168.2.1","192.168.254.2","192.168.254.1","192.168.3.1",]
        
#         if ip in gateway:
#             self.result =True
#             test = os.popen("arp -a").read()
#             with open("arp_file", "w") as file:
#                 file.write(test)
#         else: 
#             self.result = False   
import os
import subprocess
class Acess_point:
    def __init__(self ) -> None:
# Run the 'ipconfig' command to get network information
        result2 = subprocess.run(["ipconfig"], capture_output=True, text=True)

        # Check if the command was successful
        if result2.returncode == 0:
            self.result = False
            # Split the output into lines and find the line with the Wi-Fi interface
            lines = result2.stdout.split('\n')
            for line in lines:
                if "wi" in line.lower() or "eth" in line.lower() or "area" in line.lower() :
                    # Look for the line that contains the Default Gateway
                    for line in lines[lines.index(line):]:
                        if "Default Gateway" in line:
                            default_gateway = line.split(':')[-1].strip()
                            gateway = ["192.168.1.1","192.168.0.1","192.168.1.254","192.168.0.254","192.168.254.254","10.10.1.1","192.168.2.1","192.168.254.2","192.168.254.1","192.168.3.1"]
                            if default_gateway in gateway:
                                test = os.popen("arp -a").read()
                                with open("arp_file", "w") as file:
                                    file.write(test)
                                self.result = True
                            break
        else:
            self.result = False
