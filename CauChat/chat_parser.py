from konlpy.tag import Kkma


def get_best_key(content):
    lib = Kkma()
    nouns = lib.nouns(content)
    for noun in nouns:
        print(noun)

