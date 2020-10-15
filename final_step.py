english_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

b = "XEMFSXEWWIXMXXIIGKTSMHMYEWXXWSIIMXWASKKSLIIWJEPIXXIWGRXLYLCMELMPWQAXYIFSXWCIVGLXEMEJGSIRILYLXPQERRVWKIEVHXERRIMISQWXLWISMAPYFXSGRLKGQRLXIEWTXPVISSQIIXIISVSFWFEMTXEMWICSSJXIXWIWXZWHRPVPSMIWIOV"
a = "KWMKVCNISBDQCONPDXYQQXWYPEXYBORBPDIDOOXDOCWCKBSRYOOBCSEDYDRMCDXKKODXMDOVCIOFZEDKWMCSKIZYDDYDSVOISOXSXVRKXXGSYCORHNSKXKUIROVQKDZSSQXKOSCQGPEBSKDECTYXUEBUMKDOULQNISCXBSRIOORUKCQCNKOXSCQOFOLERKKY"

def decrypt(key, string):
    temp_string = ""
    place = english_alphabet.find(key)
    for c in string:
        char_place = english_alphabet.find(c) - place
        temp_string += english_alphabet[char_place]
    return temp_string, place

def get_mutual_ic(string1, string2):
    string1_dictionary = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0,
                          'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0,
                          'W': 0,
                          'X': 0, 'Y': 0, 'Z': 0}
    string2_dictionary = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0,
                          'L': 0,
                          'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0,
                          'X': 0, 'Y': 0, 'Z': 0}

    for letter in english_alphabet:
        if letter in string1:
            for string2_letter in string2:
                if string2_letter == letter:
                    string2_dictionary[letter] += 1

    for letter in english_alphabet:
        if letter in string2:
            for string1_letter in string1:
                if string1_letter == letter:
                    string1_dictionary[letter] += 1

    freqsum = 0
    for letter in english_alphabet:
        freqsum += (string1_dictionary[letter] * string2_dictionary[letter])
    mutuall_ic = freqsum / (len(string1) * len(string2))

    return round(mutuall_ic, 3)

for l in english_alphabet:
    ddd = decrypt(l, b)
    # print(get_mutual_ic(a,ddd[0]),"steps",ddd[1])
    tempt_mic = get_mutual_ic(a, ddd[0])
    if tempt_mic > 0.06:
        print("[+] Mutual IC",tempt_mic, "steps in between", ddd[1])

