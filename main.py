from selenium import webdriver

from GetAllVideos import GetAllVideos
from SaveSubtitles import SaveSubtitles

def simple_example():
    browser = webdriver.Chrome()
    links = [
        "https://www.youtube.com/watch?v=gDbXJzRhgKg&list=PLAwxTw4SYaPk5-YaXFkWY4UXdv6pVdiYg&index=73&pp=iAQB",
        "https://www.youtube.com/watch?v=LTVbD9_t4iE&list=PLAwxTw4SYaPk5-YaXFkWY4UXdv6pVdiYg&index=110&pp=iAQB",
    ]

    bot = SaveSubtitles(browser)
    for url in links:
        bot.save_subtitles(url)

    browser.quit()


def all_video_links_example():
    browser = webdriver.Chrome()

    video_bot = GetAllVideos(browser)

    result = video_bot.get_all_videos_from_url('https://www.youtube.com/@TradersHelpingTraders/videos')

    print(result)


def all_subtitles_from_channel_example():
    browser = webdriver.Chrome()

    video_bot = GetAllVideos(browser)
    links = video_bot.get_all_videos_from_url('https://www.youtube.com/@TradersHelpingTraders/videos')
    print(links)

    subtitle_bot = SaveSubtitles(browser, 'traders_helping_traders')
    for url in links:
        subtitle_bot.save_subtitles(url)

    browser.quit()

def main():
    simple_example()

if __name__ == "__main__":
    main()
    