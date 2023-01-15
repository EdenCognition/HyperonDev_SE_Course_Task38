############################## Compulsory Task 1 ###############################

#################################### START #####################################

# imports NLP module
import spacy

# Loads Eng language pipline
nlp = spacy.load('en_core_web_md')

#------ Code extract from the pdf -----------------------------------

# Processes the text
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

# Calls function and displays the results
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Compulsory Task 1 vector
tokens = nlp('cat apple monkey banana')
for token1 in tokens: 
    for token2 in tokens: 
        print(token1.text, token2.text, token1.similarity(token2))

# Modified vector
tokens = nlp('cat paw monkey baboon')
for token1 in tokens: 
    for token2 in tokens: 
        print(token1.text, token2.text, token1.similarity(token2))


sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
                "Hello, there is my car",
                "I\'ve lost my car in my car", 
                "i\'d like my boat back", 
                "I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences: 
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

#---------- Observations - Cat & Monkey ----------------------------------------
#
# Cat & Monkey have similarity of 0.59, both share the same classification:
# Kingodom: Animalia, Phylum: Chordata and Class: Mammalia. 
# Monkey and banana rturned 0.40, both don't have liner similarity like cat 
# and monkey, but are used in similar context.
# Modified vector contains replacemets for apple and banane - paw and baboon
# cat paw & monkey baboon returned almost perfect similarity (0.99), because 
# cat has 4 paws and baboon is a primate just like monkey
#
# As per task requirment, run example file with 'en_core_web_sm' and got W007: 
"""
[W007] The model you're using has no word vectors loaded, so the result of 
the Doc.similarity method will be based on the tagger, parser and NER, 
which may not give useful similarity judgements. 
This may happen if you're using one of the small models, 
e.g. `en_core_web_sm`, which don't ship with word vectors 
and only use context-sensitive tensors. You can always add your own word 
vectors, or use one of the larger models instead if available.
"""
# 'en_core_web_sm' is a small version of the model and it contains smaller
# vocabulary, hence trained on less data than 'en_core_web_md'. As a result, 
# 'md' provides more accurate predictions, the'sm' is a small model and is 
# focused on tasks such as'tokenisation and part-of-speech tagging, name entity 
# recognition, the 'md' is trained on more data and has a larger vocabulary to 
# make more accurate predictions.
#-------------------------------------------------------------------------------

#################################### END #######################################

