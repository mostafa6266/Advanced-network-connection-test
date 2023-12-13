import wmi
class Apepa():
    def __init__(self) -> None:
        wmi_obj = wmi.WMI()
        wmi_sql = "select IPAddress,DefaultIPGateway from Win32_NetworkAdapterConfiguration where IPEnabled=TRUE"
        wmi_out = wmi_obj.query( wmi_sql )
        try:
            wmi_out[0].DefaultIPGateway[0]
            self.result = False
        except:
            self.result=True


