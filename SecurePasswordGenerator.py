import string, random

digits = string.digits
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
punctuation = '!#$%&*+-=?@^_'
chars = ''
n = int(input('Укажите количество паролей для генерации: '))
len = int(input('Укажите длину одного пароля: '))
digOn = input('Включать ли цифры 0123456789? (y/n)')
ABCon = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)')
abcOn = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)')
chOn = input('Включать ли символы !#$%&*+-=?@^_? (y/n)')
excOn = input('Исключать ли неоднозначные символы il1Lo0O? (y/n)')

if digOn.lower() == 'y':
    chars += digits
if ABCon.lower() == 'y':
    chars += uppercase_letters
if abcOn.lower() == 'y':
    chars += lowercase_letters
if chOn.lower() == 'y':
    chars += punctuation
if excOn.lower() == 'y':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')


def generate_password(len, chars):
    password = ''
    for j in range(len):
        password += random.choice(chars)
    return password
    #generate = random.sample(chars, len)
    #print('Ваш пароль:', end=' ')
    #print(*generate, sep='')


for _ in range(n):
    generate_password(len, chars)
