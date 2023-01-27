def sort_words(sentence):
    words = sentence.split("-")
    words.sort()
    return "-".join(words)

sentence = input("enter a sentence which is hyphen seperated: ")
sorted_sentence = sort_words(sentence)
print("sorted sentence", sorted_sentence)
