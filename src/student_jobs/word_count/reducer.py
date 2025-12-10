from src.core.job.reducer import Reducer


class WordCountReducer(Reducer):

    def reduce(self, key, values, emit):
        emit(key, sum(values))


class LongWordCountReducer(Reducer):

    def reduce(self, key, values, emit):
        emit(key, sum(values))


class LengthVowelConsonantReducer(Reducer):

    def reduce(self, key, values, emit):
        total_vowels = 0
        total_consonants = 0
        total_words = 0

        for v, c, cnt in values:
            total_vowels += v
            total_consonants += c
            total_words += cnt

        total_letters = total_vowels + total_consonants
        if total_letters == 0:
            return  

        vowels_pct = round(total_vowels / total_letters * 100, 2)
        consonants_pct = round(total_consonants / total_letters * 100, 2)

        result_str = (
            f"{key} символів – {vowels_pct}% голосних, "
            f"{consonants_pct}% приголосних (слів: {total_words})"
        )

        emit(key, result_str)
