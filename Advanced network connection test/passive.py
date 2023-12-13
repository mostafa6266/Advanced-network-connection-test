import psutil
class Passiv:
    def check_cable_connection_status(self):
        interfaces = psutil.net_if_stats()
        disconnected_ethernet = []
        disconnected_wifi = []

        for interface, stats in interfaces.items():
            if stats.isup == True:
                if "eth" in interface.lower() or "area" in interface.lower() :
                    disconnected_ethernet.append(interface)

        # Check for the presence of Wi-Fi interface

        for interface, stats in interfaces.items():
            if stats.isup == True:
                if "wi" in interface.lower():
                    disconnected_wifi.append(interface)

        return disconnected_ethernet, disconnected_wifi
    def __init__(self) -> None:
        
        disconnected_ethernet, disconnected_wifi = self.check_cable_connection_status()
        print(f"et is {disconnected_ethernet}")
        print(f"wi fi is {disconnected_wifi}")
        if not disconnected_ethernet and not disconnected_wifi:
             self.result = True
        elif disconnected_wifi and  disconnected_ethernet:
            self.result = False
        elif disconnected_wifi and  not disconnected_ethernet:
            self.result = False
        elif not disconnected_wifi and  disconnected_ethernet:
            self.result = False
        elif disconnected_wifi and disconnected_ethernet: 
             self.result = True
        elif not disconnected_ethernet:
            self.result = True
        elif  not disconnected_wifi :
            self.result = True
        else:
            self.result = False