import tkinter as tk
from tkinter import filedialog
from pygame import mixer
import os

root = tk.Tk()
root.title("Music Player")
root.geometry("400x400")  

mixer.init()
def play():
    # Get the filename of the song.
    filename = filedialog.askopenfilename()

    # Load the song.
    mixer.music.load(filename)

    # Update the currently playing song.
    songtitle.set(os.path.basename(filename))

    # Play the song.
    mixer.music.play()

# Define the stop function.
def stop():
    # Stop the song.
    mixer.music.stop()
    songtitle.set("")

# Define the pause function.
def pause():
    # Pause the song.
    mixer.music.pause()

# Define the resume function.
def resume():
    # Resume the song.
    mixer.music.unpause()

# Create the LabelFrames.
topframe = tk.Frame(root)
middleframe = tk.Frame(root)
bottomframe = tk.Frame(root)

# Create the StringVar variables.
songtitle = tk.StringVar()
status = tk.StringVar()

# Create the Labels with custom styling.
toplabel = tk.Label(topframe, text="Music Player", font=("Helvetica", 16), fg="blue")
middlelabel = tk.Label(middleframe, text="Song Title:", font=("Helvetica", 12), fg="green")
bottomlabel = tk.Label(bottomframe, text="Status:", font=("Helvetica", 12), fg="red")

# Create the Buttons with custom styling.
playbutton = tk.Button(topframe, text="Play", command=play, bg="green", fg="white")
stopbutton = tk.Button(topframe, text="Stop", command=stop, bg="red", fg="white")
pausebutton = tk.Button(topframe, text="Pause", command=pause, bg="orange", fg="white")
resumebutton = tk.Button(topframe, text="Resume", command=resume, bg="blue", fg="white")

# Place the Labels and Buttons.
toplabel.pack()
middlelabel.pack()
bottomlabel.pack()
playbutton.pack(side="left", padx=10)
stopbutton.pack(side="left", padx=10)
pausebutton.pack(side="left", padx=10)
resumebutton.pack(side="left", padx=10)

# Create a list to manage the playlist.
playlist = []

# Create a ListBox for the playlist.
playlistbox = tk.Listbox(middleframe, selectbackground="light gray", selectmode=tk.SINGLE)
playlistbox.pack()

# Create a function to add songs to the playlist.
def add_to_playlist():
    filename = filedialog.askopenfilename()
    playlistbox.insert(tk.END, os.path.basename(filename))
    playlist.append(filename)

# Create a Button to add songs to the playlist.
add_button = tk.Button(middleframe, text="Add to Playlist", command=add_to_playlist, bg="blue", fg="white")
add_button.pack()

# Create a function to play a selected song from the playlist.
def play_selected_song():
    index = playlistbox.curselection()
    if index:
        index = index[0]
        play_song = playlist[int(index)]
        mixer.music.load(play_song)
        mixer.music.play()
        songtitle.set(os.path.basename(play_song))

# Create a Button to play the selected song.
play_selected_button = tk.Button(middleframe, text="Play Selected", command=play_selected_song, bg="green", fg="white")
play_selected_button.pack()

# Place the LabelFrames.
topframe.pack(pady=10)
middleframe.pack(pady=10)
bottomframe.pack(pady=10)

# Run the app.
root.mainloop()
