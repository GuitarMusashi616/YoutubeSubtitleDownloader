from selenium import webdriver

def save_subtitles(browser, url):
    browser.get(url)
    browser.implicitly_wait(30)
    title = get_title(browser)
    browser.implicitly_wait(30)
    content = get_content(browser)
    browser.implicitly_wait(30)
    save_file(title, content)
    browser.implicitly_wait(30)

def get_content(browser):
    script = """document.querySelector("#primary-button > ytd-button-renderer > yt-button-shape > button").click()"""
    script2 = """return Array.from(document.querySelectorAll("#segments-container yt-formatted-string")).map(x => x.textContent.trim()).join(" ")"""
    browser.execute_script(script)
    browser.implicitly_wait(5)
    return browser.execute_script(script2)

def get_title(browser):
    script3 = """return document.querySelector("#above-the-fold > #title").textContent.trim()"""
    return browser.execute_script(script3)

def save_file(title, content):
    with open(title + ".txt", 'w') as file:
        file.write(content)

def main():
    browser = webdriver.Chrome()
    links = [
        "https://www.youtube.com/watch?v=G_iczjkh-Lw&list=PLAwxTw4SYaPm4vV1XbFV93ZuT2saSq1hO&index=129&pp=iAQB",
        "https://www.youtube.com/watch?v=fcFth2DM7tc&list=PLAwxTw4SYaPm4vV1XbFV93ZuT2saSq1hO&index=130&pp=iAQB",
        "https://www.youtube.com/watch?v=gQ3CWXL7lsU&list=PLAwxTw4SYaPm4vV1XbFV93ZuT2saSq1hO&index=131&pp=iAQB",
        "https://www.youtube.com/watch?v=FfzDgvsCNQM&list=PLAwxTw4SYaPm4vV1XbFV93ZuT2saSq1hO&index=132&pp=iAQB",
        "https://www.youtube.com/watch?v=HX_EA8_nG54&list=PLAwxTw4SYaPm4vV1XbFV93ZuT2saSq1hO&index=133&pp=iAQB",
        "https://www.youtube.com/watch?v=QgWz_s7uugE&list=PLAwxTw4SYaPm4vV1XbFV93ZuT2saSq1hO&index=134&pp=iAQB",
        "https://www.youtube.com/watch?v=VIgMnexiH9g&list=PLAwxTw4SYaPm4vV1XbFV93ZuT2saSq1hO&index=135&pp=iAQB",
        "https://www.youtube.com/watch?v=7fEO3nlwXjc&list=PLAwxTw4SYaPm4vV1XbFV93ZuT2saSq1hO&index=136&pp=iAQB",
        "https://www.youtube.com/watch?v=KuVtFLatJAI&list=PLAwxTw4SYaPm4vV1XbFV93ZuT2saSq1hO&index=137&pp=iAQB",
        "https://www.youtube.com/watch?v=N6nHv1BDPPQ&list=PLAwxTw4SYaPm4vV1XbFV93ZuT2saSq1hO&index=138&pp=iAQB",
        "https://www.youtube.com/watch?v=_iuwVTNdJiI&list=PLAwxTw4SYaPm4vV1XbFV93ZuT2saSq1hO&index=139&pp=iAQB",
        "https://www.youtube.com/watch?v=_gWc2Ikq9aA&list=PLAwxTw4SYaPm4vV1XbFV93ZuT2saSq1hO&index=140&pp=iAQB",
        "https://www.youtube.com/watch?v=4V1ynaj6dq8&list=PLAwxTw4SYaPm4vV1XbFV93ZuT2saSq1hO&index=141&pp=iAQB",
        "https://www.youtube.com/watch?v=eSigjhE9S78&list=PLAwxTw4SYaPm4vV1XbFV93ZuT2saSq1hO&index=142&pp=iAQB",
        "https://www.youtube.com/watch?v=qDljciDJSw0&list=PLAwxTw4SYaPm4vV1XbFV93ZuT2saSq1hO&index=143&pp=iAQB",
        "https://www.youtube.com/watch?v=Q2fkck7s07Q&list=PLAwxTw4SYaPm4vV1XbFV93ZuT2saSq1hO&index=144&pp=iAQB",
        "https://www.youtube.com/watch?v=QK227Ey8Cu4&list=PLAwxTw4SYaPm4vV1XbFV93ZuT2saSq1hO&index=145&pp=iAQB",
        "https://www.youtube.com/watch?v=1R08yxconDs&list=PLAwxTw4SYaPm4vV1XbFV93ZuT2saSq1hO&index=146&pp=iAQB",
        "https://www.youtube.com/watch?v=cQTmqz5Nxgo&list=PLAwxTw4SYaPm4vV1XbFV93ZuT2saSq1hO&index=147&pp=iAQB",
        "https://www.youtube.com/watch?v=YZ_WmKyKEUs&list=PLAwxTw4SYaPm4vV1XbFV93ZuT2saSq1hO&index=148&pp=iAQB",
        "https://www.youtube.com/watch?v=6WzjlVw_b-g&list=PLAwxTw4SYaPm4vV1XbFV93ZuT2saSq1hO&index=149&pp=iAQB",
        "https://www.youtube.com/watch?v=OwoMVYt1XUQ&list=PLAwxTw4SYaPm4vV1XbFV93ZuT2saSq1hO&index=150&pp=iAQB"
    ]       

    for url in links:
        save_subtitles(browser, url)

    browser.quit()

if __name__ == "__main__":
    main()