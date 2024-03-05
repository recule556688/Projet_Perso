import sys
import os
import platform
import tkinter as tk
import requests
from PIL import Image, ImageTk
from io import BytesIO
from pytube import YouTube, exceptions
import zipfile
from customtkinter import (
    CTk,
    CTkLabel,
    CTkEntry,
    CTkProgressBar,
    CTkButton,
    set_appearance_mode,
    set_default_color_theme,
)

# Get the directory of the executable
base_dir = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))

# Construct the path to the icon files
icon_path_ico = os.path.join(base_dir, "app.ico")
icon_path_xbm = os.path.join(base_dir, "app.xbm")

# Constants
WINDOW_GEOMETRY = "1600x900"
IMAGE_SIZE = (500, int(500 / 16 * 9))


# Auto update function
def update_app():
    # GitHub API URL for your repository
    api_url = "https://api.github.com/repos/recule556688/Projet_Perso/releases/latest"

    # Get the latest release info
    response = requests.get(api_url)
    data = response.json()

    # Get the latest version number
    latest_version = data["tag_name"]

    # Get the current version number
    with open("version.txt", "r") as f:
        current_version = f.read().strip()

    # If the latest version is newer than the current version
    if latest_version > current_version:
        # Get the URL and name of the .exe file for the latest release
        exe_url = None
        exe_name = None
        for asset in data["assets"]:
            if asset["name"].endswith(".exe"):
                exe_url = asset["browser_download_url"]
                exe_name = asset["name"]
                break

        if exe_url is None:
            print("No new update found in the latest release.")
            return

        # Download the latest version of the application
        response = requests.get(exe_url)
        with open(exe_name, "wb") as f:
            f.write(response.content)

        # Replace the old .exe with the new one
        os.remove("myapp.exe")
        os.rename(exe_name, "myapp.exe")

        # Update the version number in the local version.txt file
        with open("version.txt", "w") as f:
            f.write(latest_version)


# Our app window
app = CTk()
app.geometry(WINDOW_GEOMETRY)
app.title("YouTube Downloader")

# Check the operating system
if platform.system() == "Windows":
    # On Windows, use the .ico file directly
    app.iconbitmap(icon_path_ico)
elif platform.system() == "Linux":
    # On Linux, use the .xbm file directly
    app.iconbitmap("@{}".format(icon_path_xbm))

# Thumbnail label
thumbnail_label = tk.Label(
    app, text="Thumbnail", fg="green", borderwidth=3, relief="solid"
)
# Initially hide the label
thumbnail_label.pack_forget()


# Download function
def startDownload():
    try:
        # Disable the download button
        download_button.configure(
            state="disabled",
            text="Downloading...",
            text_color="green",
            font=("Helvetica", 12, "bold"),
        )

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

        # Show the label
        thumbnail_label.pack(padx=10, pady=10)

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


# System settings
set_appearance_mode("System")
set_default_color_theme("green")


# Link input
link = CTkEntry(app, width=600, height=50, text_color="grey")
link.insert(0, "Insert the link of the video you want to download")


def clear_placeholder(event):
    current = link.get()
    if current == "Insert the link of the video you want to download":
        link.delete(0, tk.END)


link.bind("<FocusIn>", clear_placeholder)
link.pack(padx=10, pady=50)

# Title label
title = CTkLabel(app, text="")
title.pack(padx=10, pady=10)

# Finish Downloading
finish_label = CTkLabel(app, text="")
finish_label.pack(padx=10, pady=10)

# Progress percentage
pPercentage = CTkLabel(app, text="0 %")
pPercentage.pack(padx=10, pady=0)

progressBar = CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=5)

# Download button
download_button = CTkButton(
    app,
    text="Download",
    command=startDownload,
    text_color="darkgreen",
    font=("Helvetica", 12, "bold"),
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
