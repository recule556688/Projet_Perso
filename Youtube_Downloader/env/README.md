# 🎥 YouTube Downloader

## 📚 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Prerequisites](#prerequisites)
- [Installing](#installing)
- [Usage](#usage)

## 📖 About <a name = "about"></a>

This project is a YouTube downloader built in Python using the pytube library and tkinter for the GUI. It allows users to download and save videos from YouTube. It also displays video information such as the author, publish date, views, and duration.

## 🚀 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine and start downloading Youtube Videos

## 📋 Prerequisites <a name = "prerequisites"></a>

To run this project, you will need:

- [Python 3.6 or later](https://www.python.org/downloads/)
- pip (Python package installer)

#### Python and pip

If you're using Python 3.4 or later downloaded from python.org, pip is already installed. If you're working in a Virtual Environment created by virtualenv or pyvenv, pip is also available.

#### Python Packages

Here's a list of the Python packages you'll need:

- charset-normalizer
- certifi
- tkinter
- customtkinter
- darkdetect
- idna
- packaging
- Pillow
- pytube
- requests
- urllib3

## 🔧 Installing <a name = "installing"></a>

1. Clone the repository to your local machine:

```bash
git clone https://github.com/recule556688/Projet_Perso.git

cd Youtube_Downloader

python3 -m venv env

source env/bin/activate # go directly here if the env/ is already setup

pip install -r requirements.txt

python yt_downloader.py
```
### 🎬 Usage

```py
python yt_downloader.py

# now copy paste a valid Youtube link in the GUI
```