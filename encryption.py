
lis = {
    "q":0,"Q":26,
    "w":1,"W":27,
    "e":2,"E":28,
    "r":3,"R":29,
    "t":4,"T":30,
    "y":5,"Y":31,
    "u":6,"U":32,
    "i":7,"I":33,
    "o":8,"O":34,
    "p":9,"P":35,
    "a":10,"A":36,
    "s":11,"S":37,
    "d":12,"D":38,
    "f":13,"F":39,
    "g":14,"G":40,
    "h":15,"H":41,
    "j":16,"J":42,
    "k":17,"K":43,
    "l":18,"L":44,
    "z":19,"Z":45,
    "x":20,"X":46,
    "c":21,"C":47,
    "v":22,"V":48,
    "b":23,"B":49,
    "n":24,"N":50,
    "m":25,"M":51,

    "й":52,"Й":85,
    "ц":53,"Ц":86,
    "у":54,"У":87,
    "к":55,"К":88,
    "е":56,"Е":89,
    "н":57,"Н":90,
    "г":58,"Г":91,
    "ш":59,"Ш":92,
    "щ":60,"Щ":93,
    "з":61,"З":94,
    "х":62,"Х":95,
    "ъ":63,"Ъ":96,
    "ф":64,"Ф":97,
    "ы":65,"Ы":98,
    "в":66,"В":99,
    "а":67,"А":100,
    "п":68,"П":101,
    "р":69,"Р":102,
    "о":70,"О":103,
    "л":71,"Л":104,
    "д":72,"Д":105,
    "ж":73,"Ж":106,
    "э":74,"Э":107,
    "я":75,"Я":108,
    "ч":76,"Ч":109,
    "с":77,"С":110,
    "м":78,"М":111,
    "и":79,"И":112,
    "т":80,"Т":113,
    "ь":81,"Ь":114,
    "б":82,"Б":115,
    "ю":83,"Ю":116,
    "ё":84,"Ё":117,

    "0":118,
    "1":119,
    "2":120,
    "3":121,
    "4":122,
    "5":123,
    "6":124,
    "7":125,
    "8":126,
    "9":127,
    "0":128,

    "!":129,
    "@":130,
    "#":131,
    "$":132,
    "%":133,
    "^":134,
    "&":135,
    "*":136,
    "(":137,
    ")":138,
    "-":139,
    "_":140,
    "=":141,
    "+":142,
    "`":143,
    "~":144,
    ",":145,
    "<":146,
    ".":147,
    ">":148,
    "/":149,
    "?":150,
    ";":151,
    ":":152,
    "'":153,
    "\"":154,
    "[":155,
    "]":156,
    "{":157,
    "}":158,
    "\\":159,
    "|":160,
    " ":161,
    "\n":162,
    '"':163,

    "∶":252, "∴":253, "∵":254, "∷":255
}


def encryption_letter_10(files):
    rets = []
    for i in files:
        for x in lis:
            if i == x:
                rets.append(lis[x])

    return rets

def encryption_10_2(files):
    retur = []

    for i in files:
        num = i
        codes = ''
        
        if num < 256 and num >= 128:
            codes += '1'
            num -= 128
            
        else:
            codes += '0'

        if num < 128 and num >= 64:
            codes += '1'
            num -= 64
            
        else:
            codes += '0'

        if num < 64 and num >= 32:
            codes += '1'
            num -= 32
            
        else:
            codes += '0'


        if num < 32 and num >= 16:
            codes += '1'
            num -= 16
            
        else:
            codes += '0'


        if num < 16 and num >= 8:
            codes += '1'
            num -= 8
            
        else:
            codes += '0'

        if num < 8 and num >= 4:
            codes += '1'
            num -= 4
            
        else:
            codes += '0'

        if num < 4 and num >= 2:
            codes += '1'
            num -= 2
        else:
            codes += '0'

        if num < 2 and num >= 1:
            codes += '1'
            num -= 1
            
        else:
            codes += '0'

        retur.append(codes)

    return retur


def encryption_2_sumbol(files):

    file_work = ''
    for y in files:
        file_work += y

    sumbol = '∶∴∵∷'
    sumbol_res = ''
    file_len = len(files)*4

    for i in range(file_len):
        numbers = f'{file_work[i*2:(i*2)+2]}'

        if numbers == "00":
            sumbol_res += sumbol[0]
        elif numbers == "01":
            sumbol_res += sumbol[1]
        elif numbers == "10":
            sumbol_res += sumbol[2]
        elif numbers == "11":
            sumbol_res += sumbol[3]
        else:
            sumbol_res += '❌'

    return sumbol_res

        

def unencryption_sumbol_2(files):

    sumbol = '∶∴∵∷'
    sumbol_res = ''

    for i in files:
        if i == sumbol[0]:
            sumbol_res += "00"
        elif i == sumbol[1]:
            sumbol_res += "01"
        elif i == sumbol[2]:
            sumbol_res += "10"
        elif i == sumbol[3]:
            sumbol_res += "11"
        else:
            sumbol_res += '❌'

    return sumbol_res


def unencryption_2_10(files):

    ret = []    # ▓░░▒▒██▓ == '10 00 00 01', '01 11 11 10' == 129, 126 == !8

    dones = []

    for i in range(len(files)//8):
        ret.append(files[i*8:(i+1)*8])

    for f in ret:
        nums = 0
        if f[0] == '1':
            nums += 128
        if f[1] == '1':
            nums += 64
        if f[2] == '1':
            nums += 32
        if f[3] == '1':
            nums += 16
        if f[4] == '1':
            nums += 8
        if f[5] == '1':
            nums += 4
        if f[6] == '1':
            nums += 2
        if f[7] == '1':
            nums += 1

        dones.append(nums)

    return dones
            

def unencryption_10_letter(files):

    letter = ''

    for i in files:
        for x in lis:
            if i == lis[x]:
                letter += x

    return letter




    


def encryption(text):
    step1 = encryption_letter_10(text)
    step2 = encryption_10_2(step1)
    step3 = encryption_2_sumbol(step2)

    return step3

def unencryption(text):

    step1 = unencryption_sumbol_2(text)
    step2 = unencryption_2_10(step1)
    step3 = unencryption_10_letter(step2)

    return step3
