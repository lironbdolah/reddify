from tkinter import *
from tkinter import scrolledtext

x = 0

# gives varriable an input
def Take_input():
    INPUT = T.get("1.0", "end-1c")
    print(INPUT)
    x = INPUT



# set title
root = Tk()
root.title("Code Generator")


# set size
root.geometry("700x450")
root.resizable(width=False, height=False)

#interface

# spotify token
spotify_header = Label(root, text = "spotify token:").grid(row=0, column=2,pady=15)

username = Label(root, text = "Username:").grid(row=2, column=0,pady=10)
username_textbox = Text(root, height = 1, width = 25).grid(row=2, column=1)

redirect_uri = Label(root, text = "Redirect_uri:").grid(row=2, column=2,pady=10)
redirect_uri_textbox = Text(root, height = 1, width = 25).grid(row=2, column=3)

client_id = Label(root, text = "Client_id:").grid(row=3, column=0,pady=10)
client_id_textbox = Text(root, height = 1, width = 25).grid(row=3, column=1,padx=15)

secret_id = Label(root, text = "Secret_id:").grid(row=3, column=2,pady=10)
secret_id_textbox = Text(root, height = 1, width = 25).grid(row=3, column=3)

# reddit token
reddit_header = Label(root, text = "reddit token:").grid(row=4, column=2,pady=15)

user_agent = Label(root, text = "User_agent:").grid(row=5, column=0,pady=10)
user_agent_textbox = Text(root, height = 1, width = 25).grid(row=5, column=1)

reddit_client_id = Label(root, text = "Client_id:").grid(row=6, column=0,pady=10)
reddit_client_id_textbox = Text(root, height = 1, width = 25).grid(row=6, column=1)

reddit_secret_id = Label(root, text = "Secret_id:").grid(row=6, column=2,pady=15)
reddit_secret_id_textbox = Text(root, height = 1, width = 25).grid(row=6, column=3)


# playlist filters:

playlist_filters = Label(root, text = "Playlist_filters:").grid(row=7, column=2,pady=15)

number_of_tracks = Label(root, text = "Number_of_tracks:").grid(row=8, column=0,pady=10)
number_of_tracks_textbox = Text(root, height = 1, width = 25).grid(row=8, column=1)

date_range = Label(root, text = "Date_range:").grid(row=8, column=2,pady=15)
text_area = Scrollbar(root)
mylist = Listbox(root,yscrollcommand = text_area.set(0.0,2.0))
lis = ['week','month']
mylist.insert(END,'week')
mylist.insert(END,'month')
text_area.config(command = mylist.yview)
text_area.grid(row=8, column=3)
b = Button(root, text = "Select",command = lambda:Take_input()).grid(row = 10, column = 2)



root.mainloop()