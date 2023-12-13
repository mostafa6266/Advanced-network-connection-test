
import subprocess
class Trust:
    def __init__(self) -> None:
        
        command = 'Test-ComputerSecureChannel -Server "asuh.local"'
        p = subprocess.Popen(["powershell.exe", "-Command", command], stdout=subprocess.PIPE)
        output, errors = p.communicate()
        self.result = output.decode('utf-8')
        
        


