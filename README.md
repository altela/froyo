# froyo
is a python script to remove background of the image, shrinking its file size, and merge multiple image into one.
this needs `rembg` library, thus you need to install it first by running `pip3 install rembg`

## How To

First, put your image into `images` folder, and run the script with : 
```
python3 -m froyo.py
```

or, if you are using windows you can edit the `run_froyo.bat` file, you need to edit it and identify where your python folder located.
Just follow the instruction inisde that file.

This will combine your image inside `images` folder with `twibbon.png`, which the result will be saved into `result` folder.
This script support multiple images, just put it inside `images` folder
