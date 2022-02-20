from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from authorization import *





if __name__ == '__main__':

    # set title
    root = Tk()
    root.title("reddify")


    # set size
    root.geometry("825x325")
    root.resizable(width=False, height=False)
    root.iconbitmap("assets/icon.ico")


    # Display image on a Label widget.
    img = ImageTk.PhotoImage(Image.open("assets/backround.png").resize((900, 450), Image.ANTIALIAS))
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

        inputs['playlist name'] = playlist_name_textbox.get("1.0", "end-1c")
        inputs['number of tracks'] = number_of_tracks_textbox.get("1.0", "end-1c")
        inputs['subreddit name'] = subreddit_name_textbox.get("1.0", "end-1c")
        inputs['date_range'] = var.get()
        inputs['category'] = cat.get()


        #check for missing values;
        missing_values = ''

        for i in inputs:
            if len(inputs[i]) == 0:
                missing_values += str(i) + ' \n'

        if len(missing_values) > 0:
            messagebox.showinfo('Input Error',"Plese fill: " + '\n'  + missing_values)



        try:
            token = get_spotify_token(inputs['user name'],inputs['client id'],inputs['secret id'],inputs['redirect uri'])
        except:
            messagebox.showinfo('Input Error', "something went wrong with your spotify credentials")

        playlist_id = create_playlist(inputs['playlist name'],token,inputs['user name'])

        if playlist_id  == 0:
            messagebox.showinfo('Input Error', "Playlist already exists")


        add_tracks(inputs['user name'],inputs['subreddit name'],inputs['category'],int(inputs['number of tracks']),inputs['date_range'],token,playlist_id)

        messagebox.showinfo('Messege:',"Playlist Created!")


    #interface

    # spotify token
    spotify_header = Label(root, text = "Spotify token:",bg='#3b3b3b', fg='white')
    spotify_header.config(font=("arial", 12))
    username = Label(root, text = "Username:",bg='#3b3b3b', fg='white')
    username_textbox = Text(root, height = 1, width = 25)
    redirect_uri = Label(root, text = "Redirect_uri:",bg='#3b3b3b', fg='white')
    redirect_uri_textbox = Text(root, height = 1, width = 25)
    client_id = Label(root, text = "Client_id:",bg='#3b3b3b', fg='white')
    client_id_textbox = Text(root, height = 1, width = 25)
    secret_id = Label(root, text = "Secret_id:",bg='#3b3b3b', fg='white')
    secret_id_textbox = Text(root, height = 1, width = 25)



    # playlist filters:
    playlist_filters = Label(root, text = "Playlist_filters:",bg='#3b3b3b', fg='white')
    playlist_filters.config(font=("arial", 12))
    playlist_name = Label(root, text = "playlist_name:",bg='#3b3b3b', fg='white')
    playlist_name_textbox = Text(root, height = 1, width = 25)
    subreddit_name = Label(root, text="   subreddit_name:", bg='#3b3b3b', fg='white')
    subreddit_name_textbox = Text(root, height=1, width=25)
    number_of_tracks = Label(root, text = "Number_of_tracks:",bg='#3b3b3b', fg='white')
    number_of_tracks_textbox = Text(root, height = 1, width = 4)
    date_range = Label(root, text = "Date_range:",bg='#3b3b3b', fg='white')
    category = Label(root, text="Category:", bg='#3b3b3b', fg='white')

    # date_range_menubar:
    options = ["hour","day","week","month","year","all"]
    var = StringVar()
    var.set(options[0])
    omenu = OptionMenu(root, var, *options)
    omenu.configure(background="white",activeforeground='#fe7012',fg='black')

    # date_range_menubar:
    options_category = ["new", "hot", "top"]
    cat = StringVar()
    cat.set(options_category[0])
    omenu_cat = OptionMenu(root, cat, *options_category)
    omenu_cat.configure(background="white", activeforeground='#fe7012', fg='black')

    b = Button(root, text = " Create \n Playlist",command = lambda:Take_input(),bg='#fd6a12',height=3 ,width=12, fg='white')

    #error messege
    entryBox = Entry()




    # set widgets positions:

    spotify_header.grid(row=0, column=2,pady=15)
    username.grid(row=2, column=0,pady=10)
    username_textbox.grid(row=2, column=1)
    redirect_uri.grid(row=2, column=2,pady=10)
    redirect_uri_textbox.grid(row=2, column=3)
    client_id.grid(row=3, column=0,pady=10)
    client_id_textbox.grid(row=3, column=1)
    secret_id.grid(row=3, column=2,pady=10)
    secret_id_textbox.grid(row=3, column=3)

    playlist_filters.grid(row=4, column=2,pady=15)
    playlist_name.grid(row=6, column=0,pady=10)
    playlist_name_textbox.grid(row=6, column=1,padx=15)
    number_of_tracks.grid(row=5, column=4,pady=10, padx=5)
    number_of_tracks_textbox.grid(row=5, column=5)
    subreddit_name.grid(row=5, column=0, pady=10)
    subreddit_name_textbox.grid(row=5, column=1)
    date_range.grid(row=5, column=2,pady=15)
    omenu.grid(row=5, column=3,pady=15)
    category.grid(row=6, column=2, pady=15)
    omenu_cat.grid(row=6, column=3, pady=15)
    b.grid(row=6, column=4,columnspan = 1, sticky = W+E)


    root.mainloop()




