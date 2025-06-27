# pyright: strict
from typing import Any
from selenium.webdriver import Chrome
from selenium.common.exceptions import JavascriptException
from pathlib import Path
import re
import time

class SaveSubtitles:
    def __init__(self, browser: Chrome, save_folder: str = '.', secs_implicit_wait: int = 30, secs_per_retry: int = 3):
        self.browser = browser
        self.save_folder = self.parse_folder(save_folder)

        self.secs_implicit_wait = secs_implicit_wait
        self.secs_per_retry = secs_per_retry
    
    @classmethod
    def parse_folder(cls, save_folder: str) -> Path:
        path = Path(save_folder)
        assert path.is_dir(), f"{save_folder} is not a valid folder to save subtitles text files"
        return path

    def save_subtitles(self, url: str):
        self.browser.get(url)
        self.browser.implicitly_wait(self.secs_implicit_wait)

        title = self.get_title()
        self.browser.implicitly_wait(self.secs_implicit_wait)

        self.open_content()
        self.browser.implicitly_wait(self.secs_implicit_wait)

        content = self.get_content()
        self.browser.implicitly_wait(self.secs_implicit_wait)

        self.save_file(title, content)
        self.browser.implicitly_wait(self.secs_implicit_wait)

    def open_content(self):
        script = """document.querySelector("#primary-button > ytd-button-renderer > yt-button-shape > button").click()"""
        self.execute_script(script) # type: ignore

    def get_content(self) -> str:
        script = """return Array.from(document.querySelectorAll("#segments-container yt-formatted-string")).map(x => x.textContent.trim()).join(" ")"""
        return self.execute_script(script) # type: ignore

    def get_title(self) -> str:
        script = """return document.querySelector("#above-the-fold > #title").textContent.trim()"""
        return self.execute_script(script) # type: ignore
    
    def execute_script(self, script: str) -> Any:
        tries_left = 3
        while tries_left > 0:
            try:
                result = self.browser.execute_script(script) # type: ignore
                return result # type: ignore
            except JavascriptException: 
                tries_left -= 1
                time.sleep(self.secs_per_retry)
                


    def save_file(self, title: str, content: str):
        dest = self.save_folder / f"{self.sanitize_filename(title)}.txt"
        with dest.open('w') as file:
            file.write(content)

    @classmethod
    def sanitize_filename(cls, filename: str, replacement: str = '') -> str:
        invalid_chars = r'[<>:"/\\|?*\x00-\x1F]'

        filename = re.sub(invalid_chars, replacement, filename)
        filename = filename.rstrip('. ')
        return filename