from gensim.models.word2vec import Word2Vec
import json

def load_model(mocked: bool = False) -> Word2Vec:
    if mocked:
        with open("mocked_word2vec.json", "r") as file:
            return json.load(file)
    return Word2Vec.load("word2vec-google-news-300.model").wv