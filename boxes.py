from ppadb.client import Client as AdbClient
from rply.token import BaseBox
import time

#Check if android devices is attached
client = AdbClient(host="127.0.0.1", port=5037) # Default is "127.0.0.1" and 5037
devices = client.devices()
if len(devices) == 0:
    print('No devices')
    quit()
device = devices[0]
''' some commands to use adb
device.shell('input keyevent 27')
time.sleep(15)
#device.shell('input keyevent 24')
print('Taken a photo!')
device.shell(f'input text 5245')
'''

class MainBox(BaseBox):
    def __init__(self, statements,expressions):
        self.expressions = expressions
        self.statements = statements

    def eval(self):
        for statement in self.statements.getlist():
            a = int(statement.eval())
            for i in range(a):
                for expression in self.expressions.getlist():
                    expression.eval()

class StatementBox(BaseBox):
    def __init__(self, word, number):
        self.word = word
        self.number = number

    def eval(self):
        return self.number.getstr()



class StatementsBox(BaseBox):
    def __init__(self, statements=None, statement=None):
        self.statements = statements
        self.statement = statement

    def getlist(self):
        if self.statements:
            return self.statements.getlist() + [self.statement]
        return []


class ActionBox(BaseBox):
    def __init__(self, value):
        self.value = value

    def getstr(self):
        return self.value.getstr()


class WordBox(BaseBox):
    def __init__(self, value):
        self.value = value

    def getstr(self):
        return self.value.getstr()

class StringBox(BaseBox):
    def __init__(self, value):
        self.value = value

    def getstr(self):
        return self.value.getstr()

class IntBox(BaseBox):
    def __init__(self, value):
        self.value = value

    def getstr(self):
        return self.value.getstr()

class ExpressionBox(BaseBox):
    def __init__(self, action, wordnum):
        self.action = action
        self.wordnum = wordnum

    def eval(self):
        print(self.action.getstr())
        print(self.wordnum.getstr())
        if self.action.getstr() == "start":
            if self.wordnum.getstr() == "whatsapp":
                device.shell(f'input keyevent KEYCODE_HOME')
                device.shell(f'am start -n com.whatsapp/.Main')
                time.sleep(0.5)
            elif self.wordnum.getstr() == "settings":
                device.shell(f'monkey -p com.android.settings -c android.intent.category.LAUNCHER 1')
            elif self.wordnum.getstr() == "facebook":
                device.shell(f'input keyevent KEYCODE_HOME')
                device.shell(f'am start -a android.intent.action.VIEW -d facebook://facebook.com/inbox')
                time.sleep(0.5)
            elif self.wordnum.getstr() == "spotify":
                device.shell(f'input keyevent KEYCODE_HOME')
                device.shell(f'am start -n com.spotify.music/.MainActivity')
                time.sleep(0.5)
            elif self.wordnum.getstr() == "shazam":
                device.shell(f'input keyevent KEYCODE_HOME')
                device.shell(f'am start -n com.shazam.android/.activities.SplashActivity')
                time.sleep(0.5)
            elif self.wordnum.getstr() == "twitter":
                device.shell(f'input keyevent KEYCODE_HOME')
                device.shell(f'am start -n com.twitter.android/.StartActivity')
                time.sleep(0.5)
        elif self.action.getstr() == "stop":
            if self.wordnum.getstr() == "whatsapp":
                device.shell(f'am force-stop com.whatsapp')
                device.shell(f'input keyevent KEYCODE_HOME')
            elif self.wordnum.getstr() == "spotify":
                device.shell(f'am force-stop com.spotify.music')
                device.shell(f'input keyevent KEYCODE_HOME')
            elif self.wordnum.getstr() == "shazam":
                device.shell(f'am force-stop com.shazam.android')
                device.shell(f'input keyevent KEYCODE_HOME')
            elif self.wordnum.getstr() == "twitter":
                device.shell(f'am force-stop com.twitter.android')
                device.shell(f'input keyevent KEYCODE_HOME')
        elif self.action.getstr() == "wait":
            time.sleep(int(self.wordnum.getstr()))
        elif self.action.getstr() == "unlockpw":
            device.shell(f'input keyevent 26')
            device.shell(f'input keyevent 82') 
            device.shell(f'input text {int(self.wordnum.getstr())}')
            device.shell(f'input keyevent 66')
        elif self.action.getstr() == "write":
            #time.sleep(1)
            device.shell(f'input tap 900 1488')
            device.shell(f'input text {self.wordnum.getstr()}')
            #device.shell(f'input tap 900 178')
            #print(self.wordnum.getstr())
            #time.sleep(1)
        elif self.action.getstr() == "search":
            time.sleep(1)
            device.shell(f'input tap 890 188')
            device.shell(f'input text {self.wordnum.getstr()}')
            device.shell(f'input tap 570 440')
        elif self.action.getstr() == "lock":
            device.shell(f'input keyevent 26')
            time.sleep(1)



class ExpressionSBox(BaseBox):
    def __init__(self, expressions=None, expression=None):
        self.expressions = expressions
        self.expression = expression

    def getlist(self):
        if self.expressions:
            return self.expressions.getlist() + [self.expression]
        return []
        