import requests
import json
from sklearn.feature_extraction.text import TfidfVectorizer
import re
from kiwipiepy import Kiwi
import numpy
import os
from dotenv import load_dotenv
load_dotenv()

def news_corpus(korean_word, display=100, start=1, sort="date"):


    url = "https://openapi.naver.com/v1/search/news.json"
    headers = {
        "Content-Type": "application/json",
        "X-Naver-Client-Id": os.getenv("NAVER_CLIENT_ID"),
        "X-Naver-Client-Secret": os.getenv("NAVER_CLIENT_SECRET")
    }
    data = {
        "query": korean_word,
        "display": display,
        "start": start,
        "sort": sort
    }

    response = requests.get(url, headers=headers, params=data)

    if response.status_code == 200:
        result = json.loads(response.text)
        return result
    else:
        print(f"API 요청 실패: {response.status_code}")
        print(response.text)
        return None

def get_top_tfidf_words(tfidf_dict, top_n=15):
    top_words = sorted(tfidf_dict.items(), key=lambda x: x[1], reverse=True)[:top_n]
    return top_words

def near_words(korean_input, top_n=15, display=100, start=1, sort="date"):
    results = news_corpus(korean_input, display, start, sort)
    kiwi = Kiwi()

    if results:
        corpus = []
        for result in results['items']:
            result['description'] = re.sub(r'<b>', '', result['description'])
            result['description'] = re.sub(r'</b>', '', result['description'])
            corpus.append(result['description'])

        tokens = []
        temp_tokens = ""
        for line in corpus:
            result = kiwi.tokenize(line)
            for token in result:
                if (token.tag).startswith("N"):
                    temp_tokens += token.form + " "
            tokens.append(temp_tokens)
            temp_tokens = ""
    
        vectorizer = TfidfVectorizer(dtype=numpy.float32)
        X = vectorizer.fit_transform(tokens)
        feature_names = vectorizer.get_feature_names_out()
        tfidf_scores = X.toarray().sum(axis=0)
        tfidf_dict = {word: score for word, score in zip(feature_names, tfidf_scores)}

        top_words = get_top_tfidf_words(tfidf_dict, top_n)
        return top_words
    else:
        return None

        
