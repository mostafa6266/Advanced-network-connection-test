
import urllib.request
class Connect:
    def __init__(self) -> None:
        try:
            urllib.request.urlopen("http://test_connectivity_to_localnetwork.asuh.local/")  # Python 3.x
            self.result = True
        except:
            self.result= False

    