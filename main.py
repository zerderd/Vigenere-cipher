def code():
    key = (key_1 * 1000)[:len(text)]
    encrypted_text = ''
    if text[1] in ru_alphabet_lower or text[1] in ru_alphabet_upper:
        if action == 'enc':
            for i in range(len(text)):
                if text[i] in ru_alphabet_lower or text[i] in ru_alphabet_upper:
                    number = ru_alphabet_lower.index(text[i].lower()) + ru_alphabet_lower.index(key[i].lower())
                    if number > 32:
                        number -= 33
                    if text[i].islower():
                        encrypted_text += ru_alphabet_lower[number]
                    if text[i].isupper():
                        encrypted_text += ru_alphabet_upper[number]
                if text[i] not in ru_alphabet_lower and text[i] not in ru_alphabet_upper:
                    encrypted_text += text[i]
            return encrypted_text
        if action == 'dec':
            for j in range(len(text)):
                    if text[j] in ru_alphabet_lower or text[j] in ru_alphabet_upper:
                        number = ru_alphabet_lower.index(text[j].lower()) - ru_alphabet_lower.index(key[j].lower())
                        if text[j].isupper():
                            encrypted_text += ru_alphabet_upper[number]
                        if text[j].islower():
                            encrypted_text += ru_alphabet_lower[number]
                    if text[j] not in ru_alphabet_lower and text[j] not in ru_alphabet_upper:
                        encrypted_text += text[j]
            return encrypted_text

    if text[1] in en_alphabet_lower or text[1] in en_alphabet_upper:
        if action == 'enc':
            for i in range(len(text)):
                if text[i] in en_alphabet_lower or text[i] in en_alphabet_upper:
                    number = en_alphabet_lower.index(text[i].lower()) + en_alphabet_lower.index(key[i].lower())
                    if number > 25:
                        number -= 26
                    if text[i].islower():
                        encrypted_text += en_alphabet_lower[number]
                    if text[i].isupper():
                        encrypted_text += en_alphabet_upper[number]
                if text[i] not in en_alphabet_lower and text[i] not in en_alphabet_upper:
                    encrypted_text += text[i]
            return encrypted_text
        if action == 'dec':
            for j in range(len(text)):
                    if text[j] in en_alphabet_lower or text[j] in en_alphabet_upper:
                        number = en_alphabet_lower.index(text[j].lower()) - en_alphabet_lower.index(key[j].lower())
                        if text[j].isupper():
                            encrypted_text += en_alphabet_upper[number]
                        if text[j].islower():
                            encrypted_text += en_alphabet_lower[number]
                    if text[j] not in en_alphabet_lower and text[j] not in en_alphabet_upper:
                        encrypted_text += text[j]
            return encrypted_text



text = input('Введите текст: ')
key_1 = input('Введите ключ: ')
action = input('enc/dec ') # Выбор действия encryption/decryption

en_alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ru_alphabet_lower = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
en_alphabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ru_alphabet_upper = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
print(code())