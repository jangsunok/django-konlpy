from konlpy.tag import Kkma

from CauChat.models import Key


def get_best_key(content):
    lib = Kkma()
    nouns = lib.nouns(content)
    best_key = None
    for noun in nouns:
        print(noun)
        try:
            key = Key.objects.get(label=noun)
            if best_key is None or best_key.priority < key.priority:
                best_key = key
        except Key.DoesNotExist:
            key = None
    return best_key

