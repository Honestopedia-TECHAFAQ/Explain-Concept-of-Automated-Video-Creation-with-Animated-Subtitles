# Automated Video Creation with Animated Subtitles

## Overview

This project uses MoviePy to add animated blue boxes with subtitles to a video. It requires the ImageMagick tool for creating and manipulating text clips.

## Requirements

1. **Python 3.10 or higher**
2. **MoviePy**: A Python module for video editing.
3. **ImageMagick**: A software suite to create, edit, compose, or convert bitmap images.

## Installation

### Install Python

Make sure you have Python 3.10 or higher installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Install MoviePy

Install MoviePy using pip:

```bash
pip install moviepy
```




### 1. **Install ImageMagick**

You need to install ImageMagick if it's not already installed. Follow these steps:

1. **Download ImageMagick:**
   * Go to the [ImageMagick download page]() and download the version for Windows.
2. **Install ImageMagick:**
   * Run the installer and follow the prompts. Ensure you select the option to install the "legacy utilities (e.g., convert)" during installation.

### 2. **Add ImageMagick to System PATH**

To ensure that MoviePy can find ImageMagick, you need to add its installation directory to your system's PATH.

1. **Find the Installation Directory:**
   * Typically, ImageMagick is installed in `C:\Program Files\ImageMagick-<version>` or a similar directory.
2. **Add to PATH:**
   * Right-click on `This PC` or `Computer` on your desktop or File Explorer and select `Properties`.
   * Click on `Advanced system settings`.
   * Click on the `Environment Variables` button.
   * Under `System variables`, find the `Path` variable, select it, and click `Edit`.
   * Add the path to the directory where ImageMagick is installed (e.g., `C:\Program Files\ImageMagick-<version>`). Make sure to separate it from other entries with a semicolon.
   * Click `OK` to close all dialogs.
