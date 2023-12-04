
# 🎥 YouTube Downloader

## 📚 Table of Contents

- [📖 About](#about)
- [🚀 Getting Started](#getting_started)
- [📋 Prerequisites](#prerequisites)
- [🔧 Installing](#installing)
- [🎬 Usage](#usage)

## 📖 About <a name = "about"></a>

This project is a YouTube downloader built in Python using the pytube library and tkinter for the GUI. It allows users to download and save videos from YouTube. It also displays video information such as the author, publish date, views, thumbnail and duration.

## 🚀 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine and start downloading YouTube Videos.

## 📋 Prerequisites <a name = "prerequisites"></a>

To run this project, you will need:

- <img src="https://www.python.org/static/favicon.ico" width="15"> [Python 3.6 or later](https://www.python.org/downloads/)
- 📦 pip (Python package installer)

### 🐍 Python and pip

If you're using Python 3.4 or later downloaded from python.org, pip is already installed. If you're working in a Virtual Environment created by virtualenv or pyvenv, pip is also available.

#### 📚 Python Packages

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

### 1. 📥 Clone the repository to your local machine

```bash
git clone https://github.com/recule556688/Projet_Perso.git
```

### 2. 🗂️ Navigate to the project directory

```bash
cd Youtube_Downloader
```

### 3. 🌐 Create the virtual environment

```python
python -m venv env  # This command creates the virtual environment named `env`.
```

### 4. 🚀 Activate the virtual environment

On Windows:

```bash
.\env\Scripts\activate

# or sometimes you need to use this command:

source env/bin/activate
```

On Unix or MacOS:

```bash
source env/bin/activate
```

### 5. 📦 Install the dependencies

Install all the necessary dependencies using pip:

```bash
pip install -r requirements.txt # Install all the dependencies
```

### 6. ▶️ Run the program

Run the Python program:

```python
python yt_downloader.py # The Graphical User Interface will be launched
```

### 🎬 Usage <a name = "usage"></a>

```python
python yt_downloader.py  # now copy paste a valid YouTube link in the GUI
```
