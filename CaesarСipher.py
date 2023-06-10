eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

print("Добро пожаловать в числовую угадайку!")
ans = input("Хотите шифровавать или дешифровать? (encryption - e/ decryption - d): ").lower()
language = input("Выберите язык: (english - en/ русский - рус): ").lower()
word = input('Напиши предложение или слово: ')

def encription(word, k, language):
    encrypted = ''
    if language == 'en':
        for i in range(len(word)):
            if word[i] in eng_lower_alphabet:
                if eng_lower_alphabet.index(word[i]) + k > 25:
                    encrypted += eng_lower_alphabet[k - 25 + eng_lower_alphabet.index(word[i]) - 1]
                else:
                    encrypted += eng_lower_alphabet[eng_lower_alphabet.index(word[i]) + k]
            elif word[i] in eng_upper_alphabet:
                if eng_upper_alphabet.index(word[i]) + k > 25:
                    encrypted += eng_upper_alphabet[k - 25 + eng_upper_alphabet.index(word[i]) - 1]
                else:
                    encrypted += eng_upper_alphabet[eng_upper_alphabet.index(word[i]) + k]
            else:
                encrypted += word[i]
        return encrypted
    elif language == 'рус':
        for i in range(len(word)):
            if word[i] in rus_lower_alphabet:
                if rus_lower_alphabet.index(word[i]) + k > 31:
                    encrypted += rus_lower_alphabet[k - 31 + rus_lower_alphabet.index(word[i]) - 1]
                else:
                    encrypted += rus_lower_alphabet[rus_lower_alphabet.index(word[i]) + k]
            elif word[i] in rus_upper_alphabet:
                if rus_upper_alphabet.index(word[i]) + k > 31:
                    encrypted += rus_upper_alphabet[k - 31 + rus_upper_alphabet.index(word[i]) - 1]
                else:
                    encrypted += rus_upper_alphabet[rus_upper_alphabet.index(word[i]) + k]
            else:
                encrypted += word[i]
        return encrypted

def encryption_ave(word, language):
    word = word + ' '
    encrypted = ''
    if language == 'en':
            while word != '':
                index = word.find(' ')
                wlen = ''
                for k in range(0, index):
                    if word[k].isalpha():
                        wlen += word[k]
                k = len(wlen)
                for i in range(len(word[0:index + 1])):
                    if word[i] in eng_lower_alphabet:
                        if eng_lower_alphabet.index(word[i]) + k > 25:
                            encrypted += eng_lower_alphabet[k - 25 + eng_lower_alphabet.index(word[i]) - 1]
                        else:
                            encrypted += eng_lower_alphabet[eng_lower_alphabet.index(word[i]) + k]
                    elif word[i] in eng_upper_alphabet:
                        if eng_upper_alphabet.index(word[i]) + k > 25:
                            encrypted += eng_upper_alphabet[k - 25 + eng_upper_alphabet.index(word[i]) - 1]
                        else:
                            encrypted += eng_upper_alphabet[eng_upper_alphabet.index(word[i]) + k]
                    else:
                        encrypted += word[i]
                word = word[index + 1:]
            encrypted = encrypted[0:len(encrypted) - 1]
            return encrypted
    elif language == 'рус':
        while word != '':
            index = word.find(' ')
            wlen = ''
            for k in range(0, index):
                if word[k].isalpha():
                    wlen += word[k]
            k = len(wlen)
            for i in range(len(word[0:index + 1])):
                if word[i] in rus_lower_alphabet:
                    if rus_lower_alphabet.index(word[i]) + k > 31:
                        encrypted += rus_lower_alphabet[k - 31 + rus_lower_alphabet.index(word[i]) - 1]
                    else:
                        encrypted += rus_lower_alphabet[rus_lower_alphabet.index(word[i]) + k]
                elif word[i] in rus_upper_alphabet:
                    if rus_upper_alphabet.index(word[i]) + k > 31:
                        encrypted += rus_upper_alphabet[k - 31 + rus_upper_alphabet.index(word[i]) - 1]
                    else:
                        encrypted += rus_upper_alphabet[rus_upper_alphabet.index(word[i]) + k]
                else:
                    encrypted += word[i]
            word = word[index + 1:]
        encrypted = encrypted[0:len(encrypted) - 1]
        return encrypted

def decryption(word, k, language):
    decrypted = ''
    if language == 'en':
        for i in range(len(word)):
            if word[i] in eng_lower_alphabet:
                if eng_lower_alphabet.index(word[i]) - k < 0:
                    decrypted += eng_lower_alphabet[25 + eng_lower_alphabet.index(word[i]) - k + 1]
                else:
                    decrypted += eng_lower_alphabet[eng_lower_alphabet.index(word[i]) - k]
            elif word[i] in eng_upper_alphabet:
                if eng_upper_alphabet.index(word[i]) - k < 0:
                    decrypted += eng_upper_alphabet[25 + eng_upper_alphabet.index(word[i]) - k + 1]
                else:
                    decrypted += eng_upper_alphabet[eng_upper_alphabet.index(word[i]) - k]
            else:
                decrypted += word[i]
        return decrypted
    elif language == 'рус':
        for i in range(len(word)):
            if word[i] in rus_lower_alphabet:
                if rus_lower_alphabet.index(word[i]) - k < 0:
                    decrypted += rus_lower_alphabet[31 + rus_lower_alphabet.index(word[i]) - k + 1]
                else:
                    decrypted += rus_lower_alphabet[rus_lower_alphabet.index(word[i]) - k]
            elif word[i] in rus_upper_alphabet:
                if rus_upper_alphabet.index(word[i]) - k < 0:
                    decrypted += rus_upper_alphabet[31 + rus_upper_alphabet.index(word[i]) - k + 1]
                else:
                    decrypted += rus_upper_alphabet[rus_upper_alphabet.index(word[i]) - k]
            else:
                decrypted += word[i]
        return decrypted

def decryption2(word,k ,  language):
    decrypted = ''
    if language == 'en':
        for i in range(len(word)):
            if word[i] in eng_lower_alphabet:
                if eng_lower_alphabet.index(word[i]) - k < 0:
                    decrypted += eng_lower_alphabet[25 + eng_lower_alphabet.index(word[i]) - k + 1]
                else:
                    decrypted += eng_lower_alphabet[eng_lower_alphabet.index(word[i]) - k]
            elif word[i] in eng_upper_alphabet:
                if eng_upper_alphabet.index(word[i]) - k < 0:
                    decrypted += eng_upper_alphabet[25 + eng_upper_alphabet.index(word[i]) - k + 1]
                else:
                    decrypted += eng_upper_alphabet[eng_upper_alphabet.index(word[i]) - k]
            else:
                decrypted += word[i]
        return decrypted
    elif language == 'рус':
        for i in range(len(word)):
            if word[i] in rus_lower_alphabet:
                if rus_lower_alphabet.index(word[i]) - k < 0:
                    decrypted += rus_lower_alphabet[31 + rus_lower_alphabet.index(word[i]) - k + 1]
                else:
                    decrypted += rus_lower_alphabet[rus_lower_alphabet.index(word[i]) - k]
            elif word[i] in rus_upper_alphabet:
                if rus_upper_alphabet.index(word[i]) - k < 0:
                    decrypted += rus_upper_alphabet[31 + rus_upper_alphabet.index(word[i]) - k + 1]
                else:
                    decrypted += rus_upper_alphabet[rus_upper_alphabet.index(word[i]) - k]
            else:
                decrypted += word[i]
        return decrypted

def which_one(ans):
    if ans == 'd':
        key = input('У тебя есть ключ? (y/n) ')
        if key == 'y':
            k = int(input('Напиши число передвига: '))
            print(decryption(word, k, language))
        else:
            for k in range(25):
                print(decryption2(word, k,  language))
    elif ans == 'e':
            key = input('У тебя есть ключ? (y/n) ')
            if key == 'y':
                k = int(input('Напиши число передвига: '))
                print(encription(word, k, language))
            else:
                print(encryption_ave(word, language))
    else:
        ans = input("Выберите (encryption - e/ decryption - d): ")

which_one(ans)