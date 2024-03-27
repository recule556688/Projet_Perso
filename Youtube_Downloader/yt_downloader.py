from pathlib import Path
from tkinter import Tk, Canvas, Entry, StringVar, Button, PhotoImage, filedialog, ttk
from pytube import YouTube, exceptions
from PIL import Image, ImageTk
from io import BytesIO
import requests
import platform
import sys


# Get the directory of the executable
base_dir = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))

# Define the base directory as the Applications folder in the script directory
root_dir = base_dir / "Applications"

# Construct the path to the assets files
icon_path_ico = base_dir / "assets" / "app.ico"
icon_path_xbm = base_dir / "assets" / "app.xbm"
button_1_dir = base_dir / "assets" / "frame0" / "button_1.png"
entry_image_1_dir = base_dir / "assets" / "frame0" / "entry_1.png"
image_image_1_dir = base_dir / "assets" / "frame0" / "image_1.png"

# Construct the path to the version file
version_file_path = base_dir / "assets" / "version.txt"


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
    with open(version_file_path, "r") as f:
        current_version = f.read().strip()

    # If the latest version is newer than the current version
    if latest_version > current_version:
        # Get the URL and name of the file for the latest release
        file_url = None
        file_name = None
        for asset in data["assets"]:
            if platform.system() == "Windows" and asset["name"].endswith(".exe"):
                file_url = asset["browser_download_url"]
                file_name = asset["name"]
                break
            elif platform.system() == "Linux" and not asset["name"].endswith(".exe"):
                file_url = asset["browser_download_url"]
                file_name = asset["name"]
                break

        if file_url is None:
            print("No new update found in the latest release.")
            return

        # Download the latest version of the application
        response = requests.get(file_url)
        with open(file_name, "wb") as f:
            f.write(response.content)

        # Rename the new downloaded version with its version number
        new_file_name = "YoutubeDownloader " + latest_version + (".exe" if platform.system() == "Windows" else "")
        Path(file_name).rename(new_file_name)

        # Move the new downloaded version to Applications folder in the current directory
        new_path = root_dir / new_file_name
        new_path.parent.mkdir(parents=True, exist_ok=True)
        Path(new_file_name).replace(new_path)

        # Update the version number in the local version.txt file
        with open(version_file_path, "w") as f:
            f.write(latest_version)


# Create the window
window = Tk()

# Check the operating system
if platform.system() == "Windows":
    # On Windows, use the .ico file directly
    window.iconbitmap(icon_path_ico)
elif platform.system() == "Linux":
    # On Linux, use the .xbm file directly
    window.iconbitmap("@{}".format(icon_path_xbm))

window.geometry("720x1280")
window.configure(bg="#1E1E1E")

window.title("YouTube Downloader" + " v" + open(version_file_path, "r").read().strip())

# Create variables to store the IDs of the text items
title_id = None
author_id = None
publish_date_id = None
views_id = None
length_id = None


def center_text(item_id):
    button_center_x = button_1.winfo_x() + button_1.winfo_width() / 2
    canvas.coords(item_id, button_center_x, canvas.coords(item_id)[1])


def update_text(item_id, new_text):
    canvas.itemconfig(item_id, text=new_text)
    center_text(item_id)


canvas = Canvas(
    window,
    bg="#1E1E1E",
    height=1280,
    width=720,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)

canvas.place(x=0, y=0)

def on_progress(stream, _, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100

    # Update the progress bar
    progressBar["value"] = percentage_of_completion
    window.update_idletasks()  # Use window instead of root


def StartDownload():
    try:
        ytlink = entry_1.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)

        # Update the text items with video information
        update_text(title_id, ytObject.title)
        update_text(author_id, ytObject.author)
        update_text(publish_date_id, ytObject.publish_date)
        update_text(views_id, ytObject.views)
        update_text(length_id, ytObject.length)

        # Get the video information
        ytObject = YouTube(ytlink)
        minutes, seconds = divmod(ytObject.length, 60)

        # Update the text items with video information
        window.after(1, lambda: update_text(title_id, "Video Title: " + ytObject.title))
        window.after(1, lambda: update_text(author_id, "Author of the Video: " + ytObject.author))
        window.after(1, lambda: update_text(publish_date_id, "Publish Date: " + str(ytObject.publish_date)))
        window.after(1, lambda: update_text(views_id, "Views: " + str(ytObject.views)))
        window.after(1, lambda: update_text(length_id, f"Duration: {minutes} minutes {seconds} seconds"))

        video = ytObject.streams.get_highest_resolution()
        video.download(output_path=select_path())

        # Get the URL of the thumbnail
        thumbnail_url = ytObject.thumbnail_url

        # Download the image data
        response = requests.get(thumbnail_url)
        img_data = response.content

        # Open the image and convert it to a format that Tkinter can display
        img = Image.open(BytesIO(img_data))

        # Calculate the size of the black bars
        bar_height = int(img.height * 0.14)  # Adjust this value as needed

        # Crop the image to remove the black bars
        img = img.crop((0, bar_height, img.width, img.height - bar_height))

        tk_img = ImageTk.PhotoImage(img)

        # Display the image
        canvas.create_image(360, 880, image=tk_img)

        # Keep a reference to the image object
        global thumbnail
        thumbnail = tk_img

    except exceptions.VideoPrivate:
        print("Video is private")
    except exceptions.VideoRegionBlocked:
        print("Video is region blocked")
    except exceptions.VideoUnavailable:
        print("Video is unavailable")
    except exceptions.RegexMatchError:
        print("Invalid URL")


# Create text items using these variables
title_id = canvas.create_text(
    360, 433.0, anchor="center", text="", fill="#FFFFFF", font=("Inter", 20 * -1)
)
author_id = canvas.create_text(
    360, 492.0, anchor="center", text="", fill="#FFFFFF", font=("Inter", 20 * -1)
)
publish_date_id = canvas.create_text(
    360, 549.0, anchor="center", text="", fill="#FFFFFF", font=("Inter", 20 * -1)
)
views_id = canvas.create_text(
    360, 608.0, anchor="center", text="", fill="#FFFFFF", font=("Inter", 20 * -1)
)
length_id = canvas.create_text(
    360, 666.0, anchor="center", text="", fill="#FFFFFF", font=("Inter", 20 * -1)
)


button_image_1 = PhotoImage(file=button_1_dir)
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=StartDownload,
    relief="flat",
)
button_1.place(x=238.0, y=360.0, width=251.98098754882812, height=40.28776931762695)

entry_image_1 = PhotoImage(file=entry_image_1_dir)
entry_bg_1 = canvas.create_image(360.0, 166.0, image=entry_image_1)
entry_1 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_1.place(x=50.0, y=146.0, width=620.0, height=38.0)

image_image_1 = PhotoImage(file=image_image_1_dir)
image_1 = canvas.create_image(359.0, 67.0, image=image_image_1)


# Create the progress bar
progressBar = ttk.Progressbar(window, length=641, mode="determinate")
progressBar.place(x=39, y=244, width=641, height=10)


def select_path():
    output_path = filedialog.askdirectory()  # opens dialog to select directory
    return output_path

if __name__ == "__main__":
    # Update the Application
    update_app()
    # Run the Application
    window.mainloop()
