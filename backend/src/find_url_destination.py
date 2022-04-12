import re


async def find(url):
    if re.search(r"""(.*youtube)""", url):
        return "youtube"
    elif re.search(r"""(.*tiktok)""", url):
        return "tiktok"
    elif re.search(r"""(.*twitter)""", url):
        return "twitter"
    else:
        return None
