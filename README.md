MapReduce Python Simulator

Quickstart
- Create venv and install requirements if needed.
- Run a sample job after scaffolding is complete:
  - python -m src.cli.main run --workers 4 --input data/input --output data/output/wordcount --job student_jobs.word_count.mapper:WordCountMapper,student_jobs.word_count.reducer:WordCountReducer --reducers 4
Завдання 1 (wordcount без пунктуації)

Запустити в PowerShell в одній папці з MapReduceLab:

python -m src.cli.main run --workers 2 --reducers 2 --input data/input --output data/output/wordcount --job src.student_jobs.word_count.mapper:WordCountMapper,src.student_jobs.word_count.reducer:WordCountReducer

Завдання 2 – тільки довгі слова (>5)
python -m src.cli.main run --workers 2 --reducers 2 --input data/input --output data/output/long_words --job src.student_jobs.word_count.mapper:LongWordCountMapper,src.student_jobs.word_count.reducer:LongWordCountReducer

Завдання 3 – відсоток голосних/приголосних по довжині слова
python -m src.cli.main run --workers 2 --reducers 2 --input data/input --output data/output/vowels_consonants --job src.student_jobs.word_count.mapper:LengthVowelConsonantMapper,src.student_jobs.word_count.reducer:LengthVowelConsonantReducer

