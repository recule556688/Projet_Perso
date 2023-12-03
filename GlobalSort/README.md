<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=144px src="https://github.com/recule556688/Projet_Perso/blob/main/GlobalSort/Assets/logo.png?raw=true" alt="Project logo"></a>
</p>

<h3 align="center">🌍 GlobalSort</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/recule556688/Projet_Perso)](https://github.com/recule556688/Projet_Perso/issues)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> 🗂️ GlobalSort is a Python-based utility tool designed to organize files in your computer's directories...

# 📚 Table of Contents

- [About](#about)
- [Getting Started](#getting-started)
- [Features](#features)
- [Supported Extensions](#supported-extensions)
- [Supported Languages](#supported-languages)
- [Installation](#installation)
- [Usage](#usage)
- [Built With](#built-with)
- [Authors](#authors)
- [License](#license)

# 📖 About

"GlobalSort is my first project developed in Python. I decided to create this powerful file organization tool as a means to learn Python and simultaneously find a solution to organize my files efficiently."

# 🚀 Getting Started

These instructions will get you a copy of the project up and running on your local machine.

# 🌟 Features
This tool allows you to:
- Sort music files
- Sort video files
- Sort image files
- Sort document files
- Sort download files
- Sort files from a specific directory
- Sort all directories
- Undo last operation
- Display an helping menu
- Quit the program

# Supported Extensions

### Music 🎵
- .mp3, .wav, .flac, .ogg, .wma, .m4a, .aac, .aiff, .ape

### Video 🎥
- .mp4, .avi, .gif, .mkv, .wmv, .mov

### Image 🖼️
- .bmp, .png, .jpg, .jpeg, .heic, .svg

### Document 📄
- .txt, .pptx, .csv, .xls, .odp, .pages, .pdf, .doc, .zip, .docx

### Download 📥
- All the extensions mentioned above and:

   .exe, .bat, .sh, .py, .pyw, .msi, .apk, .app, .deb, .rpm, .bin, .dmg, .run, .jar

# Supported Languages 🌐

The program currently supports the following languages:

- 🇬🇧 English
- 🇫🇷 French
- 🇪🇸 Spanish
- 🇩🇪 German
- 🇮🇹 Italian

# Installation

## Prerequisites
- Git. You can download Git from its [official website](https://git-scm.com/downloads).
- Python 3.6 or higher. You can download Python from the [official website](https://www.python.org/downloads/).

```
import sys  # To interact with the Python interpreter
import locale  # To set the locale for your program
import logging  # To enable logging of events for debugging
import shutil  # To perform high-level file operations
import os  # To interact with the operating system
from pathlib import Path # For handling filesystem paths in a way that is compatible with all OS
```
## Installation guide


```bash
# Clone the repo
git clone https://github.com/recule556688/Projet_Perso.git

# Go into the repo
cd GlobalSort
```

## Run the Program
```py
python GlobalSort.py
```


##  🔧 Running the tests <a name = "tests"></a>

### Run tests

```py
python -m unittest test_GlobalSort.py
```

# 🎈 Usage <a name="usage"></a>

### Run the program with the following command:

```py
python GlobalSort.py
```

A graphical user interface (GUI) will appear in your terminal. Here's how to navigate it:

- **Use the numpad for quick navigation**: GlobalSort supports numpad inputs. For example:
  - Press '1' on your numpad and then 'Enter' to select the first option.
  - Select the '10' option to display the help menu.

Remember to press **'Enter'** after your selection.

![Usage Example](https://github.com/recule556688/Projet_Perso/blob/main/GlobalSort/Assets/usage.gif?raw=true)
## ⛏️ Built Using <a name = "built_using"></a>

- <img src="https://img.icons8.com/color/30/000000/python.png">[Python](https://www.python.org/) - Language

## ✍️ Authors <a name = "authors"></a>

- [@recule556688](https://github.com/recule556688) - Idea & Initial work
