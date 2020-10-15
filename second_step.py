ciphertext = "HUKXOMWEAQMMHVKFPWVSNQCXHVNEWPIWPKSWAIBIZQDXPVQMUICXYMOXZQNIJIPIDIDGOQXKWMYTSMQSPVQMUIXHJWWMUOYYAWPEOWEWLWXXOMYXOMBWPLOSMBRIZBBILBPMYADXOMIWLMDAVXOSWTOKVQXKPVDSAPOLVCCIAQWIWICWLAKJAMBEDPSPLBRIFVYXPKOXOZOIWMBWVVCGVUSRNWEXVNDLLPYYZMDLLXRCZQMMZBCEFADLLQXMAQKPTMKWBZOQLVDAHAXXHKMYYIDIAPOFPWVSNQCXZIIWAPOCOIFIYMZVVLEGLLDLLUKXOMWEAQMMHVCEFASJLFKGATISUMZIYAYRLVDIYADLLPYYZMDLLVSXDQVPIMOQWBIENISRDPOROMXVFSSWZQXKLZVIMBREYDKVKIXHDMXXAWGEZPSRNBYRAWCIYDOMUBRIUQHSUINQPVSWAZKXPWXLLEKWHAUIKJISUMRMZVOAJWVPLIQYLAKFVCDXOMZSSBSGHTSRMQQLAQXKPVKGHLOQPISRDICLPVQXVVGIYMPETWEWMWBTVTSXPKKPPVDVPOEIPBCSBZTSIAYQLWXIHAUIKJEXDMBIWQUIYAMSTXKVLLDSAPOFHKUWAILFPVQEULNMYBITVTSXPKCEACXMCMBWPBSIZERCKWISBXOSWTOJPORXSQUIAPKXRQCWPVQIYQCWHQNXVPKZLZOWWWXHLLSROQCPVEQVHDOPSGFSPKOMAALIJIEWLBRIZBKOLAKVLAYPVE"
english_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def count_frequency(s):
    frequency = {}
    for letter in s:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1
    return frequency


def get_ciphertext_nth(s, start, length):
    ciphertext_nth = ""
    x = start
    while x <= len(ciphertext) - length:
        ciphertext_nth = ciphertext_nth + ciphertext[x]
        x += length
    return ciphertext_nth


def sort_frequency(f):
    return sorted(f.items(), key=lambda kv: kv[1], reverse=True)


def get_frequency_value(c, s):
    z = 0
    freq = 0
    while z < len(c):
        freq += ((c[z][1] * (c[z][1] - 1.0)) / (len(s) * (len(s) - 1)))
        z += 1
    return freq


for x in range(4):
    ciph = get_ciphertext_nth(ciphertext, x, 4)
    sort_ciph = sort_frequency(count_frequency(ciph))
    print("[+] Line", x + 1, ciph)
    print("[+] IC", get_frequency_value(sort_ciph, ciph))

