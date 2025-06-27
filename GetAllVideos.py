# pyright: strict

import time
from selenium.webdriver import Chrome
from selenium.common.exceptions import JavascriptException
from typing import Any, List

class GetAllVideos:
    def __init__(self, browser: Chrome, secs_implicit_wait: int = 30, secs_per_retry: int = 3):
        self.browser = browser
        self.secs_implicit_wait = secs_implicit_wait
        self.secs_per_retry = secs_per_retry
    
    def get_all_videos_from_url(self, url: str) -> List[str]:
        """Get all the videos from a channels 'videos' page eg. https://www.youtube.com/@TradersHelpingTraders/videos"""
        self.browser.get(url)
        self.browser.implicitly_wait(self.secs_implicit_wait)

        result = self.execute_script("""return Array.from(document.querySelectorAll("#video-title-link")).map(a => a.href)""") # type: ignore
        self.browser.implicitly_wait(self.secs_implicit_wait)

        return result # type: ignore

    def execute_script(self, script: str) -> Any:
        tries_left = 3
        while tries_left > 0:
            try:
                result = self.browser.execute_script(script) # type: ignore
                return result # type: ignore
            except JavascriptException: 
                tries_left -= 1
                time.sleep(self.secs_per_retry)

        
