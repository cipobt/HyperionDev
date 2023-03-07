import spacy

nlp = spacy.load("en_core_web_sm")

print("Example 1: Cat Monkey Banana\n")

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1, word2, word1.similarity(word2))
print(word3, word2, word3.similarity(word2))
print(word3, word1, word3.similarity(word1))

# It was interesting to see how high the score was between cat and monkey whe using en_core_web_md in comparison with the
# other two similarities. A bit aginst the popular image and stating the fact that both cat and monkey are animals.

print("\nMy Own Example\n")

word1 = nlp("lion")
word2 = nlp("king")
word3 = nlp("jungle")

print(word1, word2, word1.similarity(word2))
print(word3, word2, word3.similarity(word2))
print(word3, word1, word3.similarity(word1))

# When running my own example based on a popular expression, I was a bit surprised that the similarities scored so low.
# I can imagine that if I've put two words of a same category like savannah rather king, the similarity between savannah
# and jungle will score much higher. So I did and the result was 0.5002993524370793. This was with en_core_web_md

print("\nExample 2 (tokens): Cat Apple Monkey Banana\n")

tokens = nlp('cat apple monkey banana ')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print("\nExample 3 (sentences)\n")

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
             "Hello, there is my car",
             "I've lost my car in my car",
             "I'd like my boat back",
             "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

# When running the code with en_core_web_sm two things were inmediately obvious: that this model does not have
# word vectors loaded, which I understand are numerical representations of words that capture their semantic meaning
# and can be used to determine the similarity between words or documents; and that the similiraty scores between words
# were noticeable much higher than when using the medium size en_core_web model
