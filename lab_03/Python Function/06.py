def reversed_sentences(sentence):
    words = sentence.split()
    words.reverse()
    return ' '.join(words)

sentence = input("Enter a sentence: ")
print(reversed_sentences(sentence))