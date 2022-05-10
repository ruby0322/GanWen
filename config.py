import random

EMO_POOL = ['😂', '👍', '🤙', '😎', '😳', '💪', '👌', '🖖', '🈹',' ⚡', '💦']
GAN_POOL = [' skrskr🤙🤙 ', ' 很厲害欸😎😎 ', ' peace ', ' 笑死😂😂 ', ' 哈哈是我啦 ']

FULL_COMMA = '，'
FULL_PERIOD = '。'
FULL_EXCLAMATION = '！'
HALF_COMMA = ','
HALF_PERIOD = '.'
HALF_EXCLAMATION = '!'
END_OF_LINE = '[[endl]]'

PUNCTUATION_POOL = [
    FULL_COMMA, FULL_PERIOD, FULL_EXCLAMATION, 
    HALF_COMMA, HALF_PERIOD, HALF_EXCLAMATION,
    END_OF_LINE
] 

def generate_random_emoji_sequence() -> str:
    return ' ' + ''.join([random.choice(EMO_POOL)*2 for _ in range(2)]) + ' '

def generate_random_gan_text() -> str:
    return random.choice(GAN_POOL)

def convert(string: str) -> str:
    for punctuation in PUNCTUATION_POOL:
        punctuation_cnt = string.count(punctuation)
        for _ in range(punctuation_cnt):
            additive_gen = random.choice([generate_random_emoji_sequence, generate_random_gan_text])
            string = string.replace(punctuation, additive_gen(), 1)
    return string
