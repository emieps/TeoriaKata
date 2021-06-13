morse = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----'}

def morseTiming(words):
    words = str(words)
    dot = 1000
    dash = dot * 3
    words_pause = dot * 7 
    total = 0
    for s in words: 
        for c in s: 
            c = c.upper()
            if c in morse: 
                for sng in morse[c]: 
                     if sng == '.': 
                         total += dot + dash
                     else: 
                         total += dash + dash 
            elif(c == ' '): 
                total += words_pause    
    return total

if __name__ == '__main__':
    t = morseTiming("emily")
    print(str(t) + "m/s")