import itertools

ciphertext = "HUKXOMWEAQMMHVKFPWVSNQCXHVNEWPIWPKSWAIBIZQDXPVQMUICXYMOXZQNIJIPIDIDGOQXKWMYTSMQSPVQMUIXHJWWMUOYYAWPEOWEWL" \
             "WXXOMYXOMBWPLOSMBRIZBBILBPMYADXOMIWLMDAVXOSWTOKVQXKPVDSAPOLVCCIAQWIWICWLAKJAMBEDPSPLBRIFVYXPKOXOZOIWMBWVV" \
             "CGVUSRNWEXVNDLLPYYZMDLLXRCZQMMZBCEFADLLQXMAQKPTMKWBZOQLVDAHAXXHKMYYIDIAPOFPWVSNQCXZIIWAPOCOIFIYMZVVLEGLLD" \
             "LLUKXOMWEAQMMHVCEFASJLFKGATISUMZIYAYRLVDIYADLLPYYZMDLLVSXDQVPIMOQWBIENISRDPOROMXVFSSWZQXKLZVIMBREYDKVKIXH" \
             "DMXXAWGEZPSRNBYRAWCIYDOMUBRIUQHSUINQPVSWAZKXPWXLLEKWHAUIKJISUMRMZVOAJWVPLIQYLAKFVCDXOMZSSBSGHTSRMQQLAQXKP" \
             "VKGHLOQPISRDICLPVQXVVGIYMPETWEWMWBTVTSXPKKPPVDVPOEIPBCSBZTSIAYQLWXIHAUIKJEXDMBIWQUIYAMSTXKVLLDSAPOFHKUWAI" \
             "LFPVQEULNMYBITVTSXPKCEACXMCMBWPBSIZERCKWISBXOSWTOJPORXSQUIAPKXRQCWPVQIYQCWHQNXVPKZLZOWWWXHLLSROQCPVEQVHDO" \
             "PSGFSPKOMAALIJIEWLBRIZBKOLAKVLAYPVE"
start = 0
stop = len(ciphertext)
step = 3

# https://www.geeksforgeeks.org/gcd-two-array-numbers/
def find_gcd(x, y):
    while (y):
        x, y = y, x % y
    return x

def get_final_gcd(l):
    num1 = l[0]
    num2 = l[1]
    gcd = find_gcd(num1, num2)

    for i in range(2, len(l)):
        gcd = find_gcd(gcd, l[i])
    return gcd


# https://www.geeksforgeeks.org/gcd-two-array-numbers/

# create all possible trigrams from english alphabet
perm = itertools.permutations('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 3)
all_existing_ciphertext_trigrams = []

# split ciphertext into trigrams
while step <= stop:
    ciphertext_trigram = ciphertext[start:step]
    all_existing_ciphertext_trigrams.append(ciphertext_trigram)
    start += 1
    step += 1

trigram_occurences = {}
trigram_occurences_more_than_two = {}

# count occurences
for ciphertext in perm:
    for ciphertext_trigrams in all_existing_ciphertext_trigrams:
        ciphertext = ''.join(ciphertext)
        if ciphertext_trigrams == ciphertext:
            if ciphertext_trigrams in trigram_occurences:
                trigram_occurences[ciphertext_trigrams] += 1
            else:
                trigram_occurences[ciphertext_trigrams] = 1

# more than two occurences
for z in trigram_occurences:
    if trigram_occurences[z] > 2:
        trigram_occurences_more_than_two[z] = trigram_occurences[z]

print("[+] Trigrams occuring more than two times",trigram_occurences_more_than_two)

trig_steps = 1
first_occurence = 1

steps_inbetween_trigrams = []
for trig in trigram_occurences_more_than_two:
    for nextrig in all_existing_ciphertext_trigrams:
        if trig == nextrig and trig_steps > 0:
            if first_occurence == 1:
                first_occurence = 0
                trig_steps = 1
            else:
                steps_inbetween_trigrams.append(trig_steps)
                trig_steps += 1
        else:
            trig_steps += 1
    print("[+] Trigram",trig, "steps in between them",steps_inbetween_trigrams, "GCD", get_final_gcd(steps_inbetween_trigrams))
    steps_inbetween_trigrams.clear()
    trig_steps = 1
    first_occurence = 1

