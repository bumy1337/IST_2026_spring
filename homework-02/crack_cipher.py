import string
import itertools
import vigenere


def score(text: str) -> int:
    """Считаем сколько английских слов встречается в тексте."""
    words = [
        'the', 'and', 'was', 'that', 'for', 'his', 'her', 'not', 'with', 'this',
        'they', 'have', 'from', 'were', 'been', 'are', 'had', 'but', 'all',
        'would', 'there', 'their', 'said', 'what', 'she', 'you', 'him', 'when',
        'which', 'could', 'into', 'than', 'then', 'who', 'now', 'did',
        'like', 'time', 'know', 'just', 'very', 'how', 'more', 'think',
    ]
    t = text.lower()
    return sum(t.count(w) for w in words)


def find_key(ciphertext: str, max_key_len: int = 8) -> str:
    """
    Брутфорс: перебирает все ключи длиной 1..max_key_len
    и возвращает тот, при котором расшифрованный текст
    содержит больше всего английских слов.
    """
    best_score = 0
    best_key = 'a'

    for key_len in range(1, max_key_len + 1):
        print(f"Проверяем ключи длиной {key_len} ({26 ** key_len} вариантов)...")

        for combo in itertools.product(string.ascii_lowercase, repeat=key_len):
            key = ''.join(combo)
            decrypted = vigenere.decrypt_vigenere(ciphertext, key)
            s = score(decrypted)
            if s > best_score:
                best_score = s
                best_key = key
                print(f"Новый лучший ключ: '{key}' (score={s})")

    return best_key


if __name__ == '__main__':
    # Читаем зашифрованный текст
    with open('cipher.txt', 'r', encoding='windows-1252') as f:
        ciphertext = f.read()

    print("Взлом шифра Виженера\n")

    # Ищем ключ (перебираем до 8 символов включительно)
    key = find_key(ciphertext, max_key_len=8)

    print(f"\nНайден ключ: '{key}'")

    # Расшифровываем
    plaintext = vigenere.decrypt_vigenere(ciphertext, key)

    print(f"\nНачало расшифрованного текста:")
    print(plaintext[:300])

    # Сохраняем результат
    with open('cracked.txt', 'w', encoding='utf-8') as f:
        f.write(plaintext)

    print(f"\nРезультат сохранён в cracked.txt")