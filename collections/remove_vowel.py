def disemvowel(word):
    result = ''
    for letter in word:
        if letter.lower() not in 'aeiou':
            result += letter
    return result

print(disemvowel("education"))