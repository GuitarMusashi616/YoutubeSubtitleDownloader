# Youtube Subtitle Downloader

## Setup

1) Install Google Chrome
2) Setup [Selenium](https://pypi.org/project/selenium/)

## Install

1) git clone https://github.com/GuitarMusashi616/YoutubeSubtitleDownloader.git
2) py -m venv .venv
3) py -m pip install -r requirements.txt
4) py main.py

## How to make it work

- Change the list of links in the main function
- Put breakpoints on line 6, 10, & 18 so you can manually wait for the selenium browser to load the pages before continuing
- Put breakpoints where self.get_title, self.open_content, and self.get_content are called and run in debug to manually wait for selenium to load / execute javascript before continuing

