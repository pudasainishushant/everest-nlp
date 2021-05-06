# coding: utf-8
import nltk
from nltk.tag.stanford import StanfordNERTagger
# Optional
import os
java_path = "/usr/lib/jvm/default-java"
os.environ['JAVA_HOME'] = java_path
sentence = u"नेपाल सरकारले  नेपालमा राम सिता दुबइ जन्मेको भन्छ"
jar = '/home/shushant/Documents/everest_nlp/models/ner/stanford-ner.jar'
model = '/home/shushant/Documents/everest_nlp/models/ner/dummy-ner-model-nepali.ser.gz'
ner_tagger = StanfordNERTagger(model, jar, encoding='utf8')
words = nltk.word_tokenize(sentence)
print(ner_tagger.tag(words))