def sort_word_in_sentence(sentence):
    words = sentence.split()
    sorted_words = sorted(words, key=lambda x: x.lower())
    return ' '.join(sorted_words)
sentence = "this is a man world"
sorted_sentence = sort_word_in_sentence(sentence)
print("sorted sentence:", sorted_sentence)