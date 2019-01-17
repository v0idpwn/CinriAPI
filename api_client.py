# Cinri API client library
import requests
import json

class CinriConn:
    """This class has methods to access the most important parts of
        Cinri's data. Every connection requires a token and a key
        given by the sysadmin
    """
    def __init__(self, token, key):
        self.token = token
        self.key = key
        self.baseurl = 'https://inri.ct.ufsm.br/cinri/api/'

    def check_login(self, user, password):
        result = requests.get(self.baseurl + 'login.php?token='
                            + self.token + '&key=' + self.key
                            + '&u=' + user + '&p=' + password)

    def get_user_info(self, u_name="", u_id=""):
        if(u_id != ""):
            result = requests.get(self.baseurl + 'get_user_info.php?token='
                                + self.token + '&key=' + self.key
                                + '&id=' + str(u_id))
        elif(u_name != ""):
            result = requests.get(self.baseurl + 'get_user_info.php?token='
                                + self.token + '&key=' + self.key
                                + '&name=' + u_name)
        else:
            result = requests.get(self.baseurl + 'get_user_info.php?token='
                                + self.token + '&key=' + self.key)
        return result.json()

