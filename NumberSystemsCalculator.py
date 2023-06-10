print("Добро пожаловать в Калькулятор систем счисления!")
c = input('Укажите систему счисления вашего числа: b - bin, o - oct, h - hex, d - dec ')

def dec_to_bin(n):
    res = ''
    while n > 0:
        res += str(n % 2)
        n = n // 2
    return res[-1::-1]

def dec_to_oct(n):
    res = ''
    while n > 0:
        res += str(n % 8)
        n = n // 8
    return res[-1::-1]

def dec_to_hex(n):
    abc = 'ABCDEF'
    num = [10, 11, 12, 13, 14, 15]
    res = ''
    while n > 0:
        if n % 16 > 9:
            res += abc[num.index(n % 16)]
        else:
            res += str(n % 16)
        n = n // 16
    return res[-1::-1]

def bin_to_dec(n ):
    res = 0
    i = 0
    while n > 0:
        res += (n % 10) * 2**i
        n = n // 10
        i += 1
    return res

def oct_to_dec(n):
    res = 0
    i = 0
    while n > 0:
        res += (n % 10) * 8 ** i
        n = n // 10
        i += 1
    return res


def hex_to_dec(n):
    abc = 'ABCDEF'
    num = [10, 11, 12, 13, 14, 15]
    res = 0
    i = 0
    while len(n) > 0:
        if n[-1].isdigit():
            res += int(n[-1]) * 16**i
        else:
            if n[-1] in abc:
                res += num[abc.index(n[-1])] * 16**i
        n = n[:len(n)-1]
        i += 1
    return res


if c == 'b':
    n = int(input('Укажите число в  системе счисления: '))
    print(bin_to_dec(n))
elif c == 'o':
    n = int(input('Укажите число в  системе счисления: '))
    print(oct_to_dec(n))
elif c == 'h':
    n = input('Укажите число в  16 системе счисления: ')
    print(hex_to_dec(n))
elif c == 'd':
    c = input('Укажите систему счисления вашего десятичного числа: b - bin, o - oct, h - hex ')
    n = int(input('Укажите число в  системе счисления: '))
    if c == 'b':
        print(dec_to_bin(n))
    elif c == 'o':
        print(dec_to_oct(n))
    elif c == 'h':
        print(dec_to_hex(n))