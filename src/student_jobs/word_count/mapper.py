from src.core.job.mapper import Mapper
import string

# Додаткові знаки пунктуації, які будемо видаляти
EXTRA_PUNCT = "«»—…„“”№"
PUNCTUATION = string.punctuation + EXTRA_PUNCT

# Голосні (укр + англ)
VOWELS = set("aeiouаеєиіїоуюяAEIOUАЕЄИІЇОУЮЯ")


def _clean_text(text: str) -> str:
    """Замінює знаки пунктуації на пробіли, щоб легше ділити на слова."""
    table = str.maketrans({ch: " " for ch in PUNCTUATION})
    return text.translate(table)


def _count_vowels_consonants(word: str) -> tuple[int, int]:
    """Рахує кількість голосних і приголосних у слові."""
    vowels = 0
    consonants = 0

    for ch in word:
        if not ch.isalpha():
            continue
        if ch in VOWELS:
            vowels += 1
        else:
            consonants += 1

    return vowels, consonants


class WordCountMapper(Mapper):

    def map(self, record, emit):
        text = _clean_text(str(record))

        for token in text.split():
            word = token.lower()
            # залишаємо тільки токены, де є хоча б одна буква
            if any(ch.isalpha() for ch in word):
                emit(word, 1)



class LongWordCountMapper(Mapper):

    MIN_LENGTH = 6

    def map(self, record, emit):
        text = _clean_text(str(record))

        for token in text.split():
            word = token.lower()
            if word and len(word) >= self.MIN_LENGTH:
                emit(word, 1)


class LengthVowelConsonantMapper(Mapper):

    def map(self, record, emit):
        text = _clean_text(str(record))

        for token in text.split():
            word = token.lower()
            if not word:
                continue

            vowels, consonants = _count_vowels_consonants(word)
            length = len(word)

            # усього голосних, усього приголосних, кількість слів цієї довжини
            emit(length, (vowels, consonants, 1))
