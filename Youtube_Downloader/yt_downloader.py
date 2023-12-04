import tkinter as tk
import requests
from PIL import Image, ImageTk
from io import BytesIO
from pytube import YouTube, exceptions
from customtkinter import (
    CTk,
    CTkLabel,
    CTkEntry,
    CTkProgressBar,
    CTkButton,
    set_appearance_mode,
    set_default_color_theme,
)

# Constants
WINDOW_GEOMETRY = "1600x900"
IMAGE_SIZE = (500, int(500 / 16 * 9))

# Our app window

app = CTk()
app.geometry(WINDOW_GEOMETRY)
app.title("YouTube Downloader")


# Download function
def startDownload():
    try:
        # Disable the download button
        download_button.configure(state="disabled")

        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="red")
        finish_label.configure(text="")

        # Update video info labels
        author_label.configure(text="Author: " + ytObject.author, text_color="red")
        publish_date_label.configure(
            text="Publish Date: " + str(ytObject.publish_date), text_color="red"
        )
        views_label.configure(text="Views: " + str(ytObject.views), text_color="red")

        # Update video duration label
        minutes, seconds = divmod(ytObject.length, 60)
        duration_label.configure(
            text=f"Duration: {minutes} minutes {seconds} seconds", text_color="red"
        )

        # Get the thumbnail URL
        thumbnail_url = ytObject.thumbnail_url

        # Download the image
        response = requests.get(thumbnail_url)
        img_data = response.content
        img = Image.open(BytesIO(img_data))

        # Resize the image to a larger fixed size
        img = img.resize(IMAGE_SIZE, Image.LANCZOS)

        # Convert the image to PhotoImage
        photo_image = ImageTk.PhotoImage(img)

        # Update the label with the image
        thumbnail_label.configure(image=photo_image)
        thumbnail_label.image = photo_image

        video.download()
        finish_label.configure(text="Download finished", text_color="green")

        # Re-enable the download button
        download_button.configure(state="normal")
    except exceptions.PytubeError as e:
        print(e)  # Print the exception
        finish_label.configure(
            text="Download failed: Invalid YouTube link", text_color="red"
        )

        # Re-enable the download button
        download_button.configure(state="normal")
    except Exception as e:
        print(e)  # Print the exception
        finish_label.configure(
            text="Download failed: An unexpected error occurred", text_color="red"
        )

        # Re-enable the download button
        download_button.configure(state="normal")


# Initialize the pPercentage label with green color
pPercentage = CTkLabel(app, text="0%")


def on_progress(stream, _, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + "%")
    pPercentage.update()

    # Update the progress bar
    progressBar.set(float(percentage_of_completion) / 100)


# Thumbnail label
thumbnail_label = tk.Label(app, text="Thumbnail", fg="green")
thumbnail_label.pack(padx=10, pady=10)

# System settings

set_appearance_mode("System")
set_default_color_theme("green")

# Adding ui elements

title = CTkLabel(
    app, text="Insert the link of the video you want to download", text_color="green"
)
title.pack(padx=10, pady=10)

# Link input

url_var = tk.StringVar()
link = CTkEntry(app, width=600, height=50, textvariable=url_var, text_color="grey")
link.pack(padx=10, pady=10)

# Finish Downloading

finish_label = CTkLabel(app, text="")
finish_label.pack(padx=10, pady=10)

# Progress pourcentage
pPercentage = CTkLabel(app, text="0%")
pPercentage.pack(padx=10, pady=10)

progressBar = CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download button

download_button = CTkButton(
    app, text="Download", command=startDownload, text_color="darkgreen"
)
download_button.pack(padx=10, pady=10)

# Video info labels
author_label = CTkLabel(app, text="")
author_label.pack(padx=10, pady=10)

publish_date_label = CTkLabel(app, text="")
publish_date_label.pack(padx=10, pady=10)

views_label = CTkLabel(app, text="")
views_label.pack(padx=10, pady=10)

duration_label = CTkLabel(app, text="")
duration_label.pack(padx=10, pady=10)

# Run the app

app.mainloop()
