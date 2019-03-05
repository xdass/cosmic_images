# Space Instagram

This project created to help you download images from spacex and hubble API.
All images you can upload to your Instagram account.

### How to install

1. You need to register Instagram account or you can exist account.
2. Create .env file and add USER=instagram_username, PASSWORD=instagram_password
3. Install dependencies (written below)

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### How to use

1. If you have images, go to item 3
2. Download images from spacex
```
python fetch_spacex.py
```
3. Download images from hubble
```
python fetch_hubble.py
```
4. Upload images to Instagram account.  The default dir uploaded images is 'images'
```
python main.py <images dir>
2019-03-05 16:47:55,488 - INFO - Instabot Started
2019-03-05 16:47:57,348 - INFO - Logged-in successfully as 'username'!
Analizing `images\3861.png`
No exif info found (ERR: 'PngImageFile' object has no attribute '_getexif')
FOUND w:2000, h:960, ratio=2.0833333333333335
Horizontal image
Cropping image
Resizing image
Saving new image w:1080 h:565 to `images\3861.png.CONVERTED.jpg`
FOUND: w:1080 h:565 r:1.9115044247787611
2019-03-05 16:48:08,691 - INFO - Photo 'images\3861.png' is uploaded.
......
2019-03-05 16:53:41,349 - INFO - Bot stopped. Worked: 17:40:53.610984
2019-03-05 16:53:41,349 - INFO - Total requests: 151

```
NOTE: You can change images dir in util.py load_image function
### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).