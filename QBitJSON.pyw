# Version 0.1
# Author: Jagjamin

import tkinter as tk
import json

window = tk.Tk()

hostvar = tk.StringVar()
portvar = tk.StringVar()
usernamevar = tk.StringVar()
passwordvar = tk.StringVar()
settings = {}
def submit():
    host=hostvar.get()
    port=portvar.get()
    username=usernamevar.get()
    password=passwordvar.get()

    global settings
    settings = {
        "host": host,
        "port": int(port),
        "username": username,
        "password": password
    }
    try:
        with open("host.json", "w") as json_file:
            json.dump(settings, json_file, indent=4)
        print("File created/updated")
    except IOError:
        print("Error writing file")

def testset():
    with open("host.json", "r") as file:
        data = json.load(file)
    TestText.delete("1.0", tk.END)
    host=data["host"]
    port=data["port"]
    username=data["username"]
    password=data["password"]
    TestText.insert("1.0", "Host is: ")
    TestText.insert(tk.END, host)
    TestText.insert("2.0", "\nPort is: ")
    TestText.insert(tk.END, port)
    TestText.insert("3.0", "\nUsername is: ")
    TestText.insert(tk.END, username)
    TestText.insert("4.0", "\npassword is: ")
    TestText.insert(tk.END, password)


HostLabel = tk.Label(text="Host IP address", width=30)
HostLabel.pack()
HostEntry = tk.Entry(width=25, textvariable= hostvar)
HostEntry.insert(tk.END, "localhost")
HostEntry.pack()
PortLabel = tk.Label(text="Port number", width=30)
PortLabel.pack()
PortEntry = tk.Entry(width=25, textvariable= portvar)
PortEntry.insert(tk.END, 8080)
PortEntry.pack()
UsernameLabel = tk.Label(text="Username", width=30)
UsernameLabel.pack()
UsernameEntry = tk.Entry(width=25, textvariable= usernamevar)
UsernameEntry.insert(tk.END, "admin")
UsernameEntry.pack()
PasswordLabel = tk.Label(text="Password", width=30)
PasswordLabel.pack()
PasswordEntry = tk.Entry(width=25, textvariable= passwordvar)
PasswordEntry.insert(tk.END, "adminadmin")
PasswordEntry.pack()
SubmitButton = tk.Button(text="Save Settings", width=25, height=5, bg="white", fg="black", command = submit)
SubmitButton.pack()
TestButton = tk.Button(text="View Settings", width=25, height=5, bg="white", fg="black", command = testset)
TestButton.pack()
TestText= tk.Text(height=10, width=50)
TestText.pack()
window.mainloop()
