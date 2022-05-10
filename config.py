import random

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
    return ''.join(emo)

def generate_random_gan_text() -> str:
    return random.choice(GAN_POOL)

def convert(string: str) -> str:
    while string.count('[[endl]][[endl]]') > 0:
        string = string.replace('[[endl]][[endl]]', '[[endl]]')
    for punctuation in PUNCTUATION_POOL:
        punctuation_cnt = string.count(punctuation)
        for _ in range(punctuation_cnt):
            additive_gen = random.choice([generate_random_emoji_sequence, generate_random_gan_text])
            string = string.replace(punctuation, additive_gen(), 1)
    return string
