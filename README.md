# Froyo
is a python script to remove background of the image, shrinking its file size, and merge multiple image into one.

# Requirements
this needs several library such as 
- rembg
- PIL
- pillow_heif

Open your terminal, `cd` to the folder and type `pip install -r requirements.txt`.
Make sure python3 and pip is already installed.

## How To

First, put your image into `images` folder, and run the script with : 
```
python3 -m froyo.py
```

Second, run the command below to merge images inside result folder with white.bg
```
python3 -m froyo_bg.py
```

Finally, to enhance the brightness, use
```
python3 -m brightness.py
```

## Todo
Make this script compatible for windows through run_froyo.bat
