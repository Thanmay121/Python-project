import random, wx, datetime

k = random.randint(1, 1000)  # for a current session save a random value which will be used in the code
data = {}
failedatm = []
sucessatm = []

def caesar_encrypt(text, k):  # The data hiding process used in this code.
    result = ""
    k = k % 26
    for ch in text:
        if 'a' <= ch <= 'z':
            base = ord('a')
            result += chr(base + (ord(ch) - base + k) % 26)
        elif 'A' <= ch <= 'Z':
            base = ord('A')
            result += chr(base + (ord(ch) - base + k) % 26)
        else:
            result += ch
    return result

def caesar_decrypt(text, k):
    return caesar_encrypt(text, -k)

def signin(event):  # The sign in process, saves a username and password combination
    dlg = wx.TextEntryDialog(frame, "Enter username:", "Sign in")  # pops out a dialogue box
    if dlg.ShowModal() != wx.ID_OK:  # If user closes the window, end the function early
        dlg.Destroy()
        return
    username = dlg.GetValue()  # save the username entered by the user
    dlg.Destroy()  # close the tab
    dlg2 = wx.TextEntryDialog(frame, "Enter password:", "Sign in")
    if dlg2.ShowModal() != wx.ID_OK:  # same as previous
        dlg2.Destroy()
        return
    password = dlg2.GetValue()
    dlg2.Destroy()
    data[username] = caesar_encrypt(password, k)  # encrypting the data
    wx.MessageBox("User registered", "Info")

def login(event):
    dlg = wx.TextEntryDialog(frame, "Enter username:", "Login")
    if dlg.ShowModal() != wx.ID_OK:
        dlg.Destroy()
        return
    username = dlg.GetValue()
    dlg.Destroy()
    if username not in data:
        wx.MessageBox("Username not found", "Error")
        failedatm.append((datetime.datetime.now()))
        return
    dlg2 = wx.TextEntryDialog(frame, "Enter password:", "Login")
    if dlg2.ShowModal() != wx.ID_OK:
        dlg2.Destroy()
        return
    password = dlg2.GetValue()
    dlg2.Destroy()
    if caesar_encrypt(password, k) != data[username]:  # if passwords dont match
        wx.MessageBox("Wrong password", "Error")
        failedatm.append((datetime.datetime.now()))
        return
    wx.MessageBox("Login success", "Success")
    sucessatm.append((datetime.datetime.now()))

def Tracker(event):
    msg = "\n".join(str(x) for x in failedatm)  # each attempt on a new line
    wx.MessageBox(msg, "Failed attempts")
    msg = "\n".join(str(x) for x in sucessatm)
    wx.MessageBox(msg, "Sucessful attempts")

app = wx.App()
frame = wx.Frame(None, title="Basic Window", size=(400, 300))
panel = wx.Panel(frame, style=wx.SIMPLE_BORDER)
btn1 = wx.Button(panel, label="Sign in", pos=(100, 100))
btn1.Bind(wx.EVT_BUTTON, signin)
btn2 = wx.Button(panel, label="Login", pos=(180, 100))
btn2.Bind(wx.EVT_BUTTON, login)
btn3 = wx.Button(panel, label="log Tracker", pos=(250, 100))
btn3.Bind(wx.EVT_BUTTON, Tracker)
frame.Show()
app.MainLoop()
