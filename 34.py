def count_syllables(phrase):
    vowels = "aeiouyAEIOUY"
    count = 0
    for word in phrase.split():
        for char in word:
            if char in vowels:
                count += 1
    return count

def has_rhyme(poem):
    phrases = poem.split()
    for i in range(len(phrases)-1):
        if count_syllables(phrases[i])!= count_syllables(phrases[i+1]):
            return False
    return True

poem = input()
if has_rhyme(poem):
    print("Парам пам-пам")
else:
    print("Пам парам")