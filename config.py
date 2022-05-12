import random
import requests
from bs4 import BeautifulSoup
import urllib
import json

EMO_POOL = [
    '😂', '👍', '🤙', '😎', '😳', 
    '💪', '👌', '🖖', '🈹',' ⚡', 
    '💦', '🤪', '🥵', '😡', '🐒', 
    '🐵', '🔥'
]

GAN_POOL = [
    ' skrskr🤙🤙 ', ' 很厲害欸😎😎 ', ' peace ', 
    ' 笑死😂😂 ', ' 哈哈是我啦 ', ' 好屌🍆喔 ', 
    ' 可以養嗎😳😳 ', ' 好像沒有變🙄🙄 ', ' 666起來 ', 
    ' 我是DJ~5555 ', ' 欸欸AAAA ', ' 牛逼🐂🐂 ', 
    ' ㄇㄉ ', ' 欸幹穿山甲欸🤩🤩 ', ' 你有頭緒嗎😰😰 '
]

FULL_COMMA = '，'
FULL_PERIOD = '。'
FULL_EXCLAMATION = '！'
HALF_COMMA = ','
HALF_PERIOD = '.'
HALF_EXCLAMATION = '!'
END_OF_LINE = '[[endl]]'

PUNCTUATION_POOL = [
    FULL_COMMA, FULL_PERIOD, FULL_EXCLAMATION, 
    HALF_COMMA, HALF_EXCLAMATION,
    END_OF_LINE
] 

def generate_random_emoji_sequence() -> str:
    emo = random.sample(EMO_POOL, 2) * 2
    emo[1], emo[2] = emo[2], emo[1]
    return f' {"".join(emo)} '

def generate_random_gan_text() -> str:
    return random.choice(GAN_POOL)

def convert(string: str) -> str:
    while string.count('[[endl]][[endl]]') > 0:
        string = string.replace('[[endl]][[endl]]', '[[endl]]')
    for punctuation in PUNCTUATION_POOL:
        punctuation_cnt = string.count(punctuation)
        for _ in range(punctuation_cnt):
            additive_gen = random.choice([generate_random_emoji_sequence]*2+[generate_random_gan_text]*3)
            string = string.replace(punctuation, additive_gen(), 1)
    return string

def random_wiki() -> dict:
    url = "https://zh.wikipedia.org/wiki/Special:%E9%9A%8F%E6%9C%BA%E9%A1%B5%E9%9D%A2"

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }

    rq = requests.get(url, headers=headers)
    soup = BeautifulSoup(rq.text, 'lxml')
    header = soup.find('div', id='content')
    body = soup.find('div', id='bodyContent')

    title = header.find('h1', id='firstHeading').text
    content = body.find(
        'div', class_='mw-parser-output'
    ).find('p').text.replace(' ', '')
    link = 'https://zh.wikipedia.org/wiki/' + urllib.parse.quote(title)
    return {
        'title': title,
        'content': content,
        'link': link
    }

def get_bs(topic, min_len=50):

    data = json.dumps({"Topic": topic, "MinLen": min_len})

    response = requests.post(
        "https://api.howtobullshit.me/bullshit", data=data).text.replace('&nbsp;', '').replace('<br>', '\n').replace('Bad Request', '')

    return response

print(get_bs('這段日子以來，我一直想對你說三個字，但又怕說了連普通朋友也做不成，可我控制不住，還是想說：「借點錢！」', 50))