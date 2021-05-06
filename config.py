
import os
root_dir = os.path.dirname(os.path.abspath(__file__))


'''<------------Word2Vec model path------------------------------>'''
word2vec_model_sm_path = os.path.join(root_dir,'models/word2vec_models/sabd2vec_sm','sabda_to_vec_model')
word2vec_model_md_path = os.path.join(root_dir,"models/word2vec_models/sabda_2_vec_md","sabda_to_vec_model_md")
word2vec_model_lg_path = os.path.join(root_dir,"models/word2vec_models/sabda2vec_lg","sabda_to_vec_model_lg")
nepali_nlp_gensim_model_path = os.path.join(root_dir,"models/word2vec_models/nepali_nlp_model","nepali_nlp_gensim_model")
fasttext_model_path = os.path.join(root_dir,"models/word2vec_models/fastetext_embedding_model","sabda2vecfasttext.np.txt")

'''<----------------Stanford Ner Model Path-------------------------->'''
stanford_jar_path = os.path.join(root_dir, "ner_devanagari/model/stanford-ner.jar")
stanford_model_path = os.path.join(root_dir, 'ner_devanagari/model/dummy-ner-model-nepali.ser.gz')
