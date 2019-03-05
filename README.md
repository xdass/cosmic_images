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
```
NOTE: You can change images dir in util.py load_image function
### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).