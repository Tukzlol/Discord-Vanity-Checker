import requests
import random


def headers(token: str = ""):
    return {
        "authority": "discord.com",
        "x-discord-locale": "en-US",
        "x-debug-options": "bugReporterEnabled",
        "accept-language": "en-US",
        "authorization": token,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9007 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36",
        "accept": "*/*",
        "origin": "https://discord.com",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
    }


def check(vanity: str = "", token: str = ""):
    proxy = open("./data/proxies.txt", "r").read().splitlines()
    proxy = random.choice(proxy)
    proxies = {
      "http://": f"http://{proxy}", 
      "https://": f"http://{proxy}"
    }
    with requests.Session() as session:
        check_res = session.get(
            f"https://discord.com/api/v9/invites/{vanity}",
            headers=headers(token),
            proxies=proxies,
        ).text

        if "vanity_url_code" in check_res:
            pass

        elif "Unknown Invite" in check_res:
            print(f">> [{vanity}] available")
            open("./data/available.txt", "a").write(f"{vanity}\n")


def _():
    while True:
        ok = open("./data/vanitys.txt", "r").read().splitlines()
        check(
          vanity=random.choice(ok), 
          token=""
        )


_()
