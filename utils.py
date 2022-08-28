import requests
from bs4 import BeautifulSoup as bs

def get_word_data(word):
    response = requests.get("https://dict.youdao.com/search?q={}&keyfrom=new-fanyi.smartResult".format(word))
    if response.status_code == 200:
        try:
            soup = bs(response.text, "html.parser")
            data = soup.find("div", {"class": "trans-container"})
            explain = [i.text for i in data.find_all("li")]
            additiona = data.p.text if data.p else ""
        except:
            return {"explain": "未找到", "url": None}
        else:
            return {
                "explain": explain,
                "additiona": additiona,
                "url": "http://dict.youdao.com/dictvoice?audio="+word
            }
    else:
        return {"explain": "未找到", "url": None}



if __name__ == '__main__':
    print(get_word_data("apple"))