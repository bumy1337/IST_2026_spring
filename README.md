# IST_2026_spring
В этом репозитории будут домашние работы по предмету Интелектуальные системы и технологии.

<img width="1542" height="784" alt="image" src="https://github.com/user-attachment
Структура файлов
homework-02/
├── caesar.py        # Шифр Цезаря (шифрование / дешифрование / брутфорс)
├── vigenere.py      # Шифр Виженера (шифрование / дешифрование)
├── rsa.py           # RSA (генерация ключей, шифрование, дешифрование)
├── cipher.txt       # Зашифрованный текст (шифр Виженера)
├── cracked.txt      # Расшифрованный текст
└── crack_cipher.py  # Скрипт взлома шифра брутфорсом

Реализованные шифры
1. Шифр Цезаря (caesar.py)
Каждая буква сдвигается на shift позиций в алфавите.
pythonencrypt_caesar("PYTHON", shift=3)  # → 'SBWKRQ'
decrypt_caesar("SBWKRQ", shift=3)  # → 'PYTHON'
Также реализован брутфорс (caesar_breaker_brute_force) — перебирает все 26 сдвигов и выбирает тот, при котором расшифрованный текст содержит больше всего слов из словаря.
2. Шифр Виженера (vigenere.py)
Улучшенный шифр Цезаря: сдвиг меняется для каждой буквы согласно ключевому слову.
pythonencrypt_vigenere("ATTACKATDAWN", "LEMON")  # → 'LXFOPVEFRNHR'
decrypt_vigenere("LXFOPVEFRNHR", "LEMON")  # → 'ATTACKATDAWN'
3. RSA (rsa.py)
Асимметричное шифрование с открытым и закрытым ключом.
pythonpublic, private = generate_keypair(17, 19)
encrypted = encrypt(private, "Hello")
decrypted = decrypt(public, encrypted)  # → 'Hello'

Взлом cipher.txt
Что за текст
cipher.txt — отрывок из книги "Surely You're Joking, Mr. Feynman!" Ричарда Фейнмана, зашифрованный шифром Виженера.
Метод взлома
Использован брутфорс с частотным анализом:

Перебираем все возможные ключи длиной от 1 до N букв
Для каждого ключа расшифровываем текст
Считаем количество встречающихся английских слов
Выбираем ключ с максимальным количеством совпадений

Найденный ключ
hellawes
Как запустить взлом самостоятельно
bashpython crack_cipher.py
Скрипт автоматически найдёт ключ и сохранит результат в cracked.txt



Ниже представлены скриншоты, на которых все тесты пройдены 

Тест Caesar
<img width="1568" height="744" alt="image" src="https://github.com/user-attachments/assets/d2d5d20f-6b57-4a00-8d99-b2f638eee7f7" />

Тест Rsa
<img width="1512" height="794" alt="image" src="https://github.com/user-attachments/assets/ed22332c-22ea-4eb3-9c75-ad4ffa8d8b9d" />

Тест Vigeneres/assets/4d1a6b12-eb2c-4ee3-9e3e-059e4ae61374" />
