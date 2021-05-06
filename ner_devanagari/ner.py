from nltk.tag import StanfordNERTagger
import sys
sys.path.append(".")
sys.path.append("..")
from config import stanford_jar_path,stanford_model_path
from sabda2vec.nepali_tokenizer import Tokenizer
tok = Tokenizer()



class DevanagriNER():
    def __init__(self):
        self.ner_tagger = StanfordNERTagger(stanford_model_path,stanford_jar_path)
    
    def tag_ner(self,tokens):
        tagged_tuples = self.ner_tagger.tag(tokens)
        return tagged_tuples


if __name__ == '__main__':
    print("Hello")
    dner_obj = DevanagriNER()
    test_text = "जित बहादुर खाम्चा आहिले सानेपा ललितपुरमा रहेको इन्फोदेवेलोपेर्स प्राइभेट लिमिटेडमा काम गर्दै हुनुहुन्छ"
    test_tokens = tok.word_tokenize(test_text)
    tagged_tuples = dner_obj.tag_ner(test_tokens)
    print(test_tokens)
    print(tagged_tuples)
