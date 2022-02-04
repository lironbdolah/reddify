from tkinter import *
from tkinter import messagebox
from authorization import *
from PIL import Image, ImageTk




if __name__ == '__main__':
    # set title
    root = Tk()
    root.title("reddify")


    # set size
    root.geometry("775x450")
    root.resizable(width=False, height=False)
    root.iconbitmap("assets/icon.ico")


    # Display image on a Label widget.
    img = ImageTk.PhotoImage(Image.open("assets/backround.gif").resize((775, 450), Image.ANTIALIAS))
    lbl = Label(root, image=img)
    lbl.img = img  # Keep a reference in case this code put is in a function.
    lbl.place(relx=0.5, rely=0.5, anchor='center')  # Place label in center of parent.


    # gives varriable an input
    def Take_input():

        inputs = {}

        #recive inputs:
        inputs['user name'] = username_textbox.get("1.0", "end-1c")
        inputs['redirect uri'] = redirect_uri_textbox.get("1.0", "end-1c")
        inputs['client id'] = client_id_textbox.get("1.0", "end-1c")
        inputs['secret id'] = secret_id_textbox.get("1.0", "end-1c")
        inputs['user agent'] = user_agent_textbox.get("1.0", "end-1c")
        inputs['reddit client id'] = reddit_client_id_textbox.get("1.0", "end-1c")
        inputs['reddit secret id'] = reddit_secret_id_textbox.get("1.0", "end-1c")
        inputs['playlist name'] = playlist_name_textbox.get("1.0", "end-1c")
        inputs['number of tracks'] = number_of_tracks_textbox.get("1.0", "end-1c")
        inputs['subreddit name'] = subreddit_name_textbox.get("1.0", "end-1c")
        inputs['date_range'] = var.get()


        #check for missing values;
        missing_values = ''

        for i in inputs:
            if len(inputs[i]) == 0:
                missing_values += str(i) + ' \n'

        if len(missing_values) > 0:
            messagebox.showinfo('Input Error',"Plese fill: " + '\n'  + missing_values)

        try:
            songs = reddit_tracks(inputs['reddit client id'],inputs['reddit secret id'],
                                  inputs['user agent'],inputs['date_range'],int(inputs['number of tracks']),inputs['subreddit name'])
        except:
            messagebox.showinfo('Input Error', "something went wrong with your reddit credentials")
        try:
            token = get_spotify_token(inputs['user name'],inputs['client id'],inputs['secret id'],inputs['redirect uri'])
        except:
            messagebox.showinfo('Input Error', "something went wrong with your spotify credentials")

        playlist_id = create_playlist(inputs['playlist name'],token,inputs['user name'])
        if playlist_id  == 0:
            messagebox.showinfo('Input Error', "Playlist already exists")

        add_tracks(playlist_id,songs,token,inputs['user name'])

        messagebox.showinfo('Messege:',"Playlist Created!")

        # interface

        # spotify token


    spotify_header = Label(root, text="Spotify token:", bg='#3b3b3b', fg='white')
    spotify_header.config(font=("arial", 12))
    username = Label(root, text="Username:", bg='#3b3b3b', fg='white')
    username_textbox = Text(root, height=1, width=25)
    redirect_uri = Label(root, text="Redirect_uri:", bg='#3b3b3b', fg='white')
    redirect_uri_textbox = Text(root, height=1, width=25)
    client_id = Label(root, text="Client_id:", bg='#3b3b3b', fg='white')
    client_id_textbox = Text(root, height=1, width=25)
    secret_id = Label(root, text="Secret_id:", bg='#3b3b3b', fg='white')
    secret_id_textbox = Text(root, height=1, width=25)

    # reddit token
    reddit_header = Label(root, text="Reddit token:", bg='#3b3b3b', fg='white')
    reddit_header.config(font=("arial", 12))
    user_agent = Label(root, text="User_agent:", bg='#3b3b3b', fg='white')
    user_agent_textbox = Text(root, height=1, width=25)
    reddit_client_id = Label(root, text="Client_id:", bg='#3b3b3b', fg='white')
    reddit_client_id_textbox = Text(root, height=1, width=25)
    reddit_secret_id = Label(root, text="Secret_id:", bg='#3b3b3b', fg='white')
    reddit_secret_id_textbox = Text(root, height=1, width=25)

    # playlist filters:
    playlist_filters = Label(root, text="Playlist_filters:", bg='#3b3b3b', fg='white')
    playlist_filters.config(font=("arial", 12))
    playlist_name = Label(root, text="playlist_name:", bg='#3b3b3b', fg='white')
    playlist_name_textbox = Text(root, height=1, width=25)
    subreddit_name = Label(root, text="   subreddit_name:", bg='#3b3b3b', fg='white')
    subreddit_name_textbox = Text(root, height=1, width=25)
    number_of_tracks = Label(root, text="Number_of_tracks:", bg='#3b3b3b', fg='white')
    number_of_tracks_textbox = Text(root, height=1, width=8)
    date_range = Label(root, text="Date_range:", bg='#3b3b3b', fg='white')

    # menubar:
    options = ["hour", "day", "week", "month", "year", "all"]
    var = StringVar()
    var.set(options[0])
    omenu = OptionMenu(root, var, *options)
    omenu.configure(background="white", activeforeground='#fe7012', fg='black')

    b = Button(root, text=" Create \n Playlist", command=lambda: Take_input(), bg='#fd6a12', height=3, width=10,
               fg='white')

    # error messege
    entryBox = Entry()

    # set widgets positions:

    spotify_header.grid(row=0, column=2, pady=15)
    username.grid(row=2, column=0, pady=10)
    username_textbox.grid(row=2, column=1)
    redirect_uri.grid(row=2, column=2, pady=10)
    redirect_uri_textbox.grid(row=2, column=3)
    client_id.grid(row=3, column=0, pady=10)
    client_id_textbox.grid(row=3, column=1)
    secret_id.grid(row=3, column=2, pady=10)
    secret_id_textbox.grid(row=3, column=3)
    reddit_header.grid(row=4, column=2, pady=15)
    user_agent.grid(row=5, column=0, pady=10)
    user_agent_textbox.grid(row=5, column=1)
    reddit_client_id.grid(row=6, column=0, pady=10)
    reddit_client_id_textbox.grid(row=6, column=1)
    reddit_secret_id.grid(row=6, column=2, pady=15)
    reddit_secret_id_textbox.grid(row=6, column=3)
    playlist_filters.grid(row=7, column=2, pady=15)
    playlist_name.grid(row=8, column=0, pady=10)
    playlist_name_textbox.grid(row=8, column=1, padx=15)
    number_of_tracks.grid(row=8, column=2, pady=10)
    number_of_tracks_textbox.grid(row=8, column=3)
    subreddit_name.grid(row=9, column=0, pady=10)
    subreddit_name_textbox.grid(row=9, column=1)
    date_range.grid(row=9, column=2, pady=15)
    omenu.grid(row=9, column=3, pady=15)
    b.grid(row=8, column=4, columnspan=2, sticky=W + E)

    root.mainloop()





