import pandas as pd
import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

def load_excel(file_path):
    df = pd.read_excel(file_path)
    df['일자'] = pd.to_datetime(df['일자'], format='%Y%m%d').dt.strftime('%Y-%m-%d')
    return df


def split_by_date(df, date = '2025-04-04'):
    before_date = df[df['일자'] < date]
    after_date = df[df['일자'] >= date]
    return before_date, after_date

def bag_of_words(df):
    all_words = set()
    word_freq = {}
    
    for keywords in df['키워드']:
        cell_words = set(str(keywords).split(','))
        all_words.update(cell_words)
        for word in cell_words:
            word_freq[word] = word_freq.get(word, 0) + 1
    
    return {
        'unique_words': all_words,
        'word_frequency': word_freq,
        'total_words': sum(word_freq.values())
    }

def n_gram(df, bag_of_words, n, keyword = '국민'):
    # 동시발생 행렬 초기화
    co_occurrence = {word: 0 for word in bag_of_words}
    
    for keywords in df['키워드']:
        # 각 셀의 키워드를 리스트로 변환
        words = str(keywords).split(',')
        
        # 타겟 키워드의 모든 위치 찾기
        target_indices = [i for i, word in enumerate(words) if word == keyword]
        
        if not target_indices:
            continue
            
        # 각 타겟 키워드 위치에 대해
        for target_idx in target_indices:
            # 좌우 n개 단어 범위 계산
            start_idx = max(0, target_idx - n)
            end_idx = min(len(words), target_idx + n + 1)
            
            # 동시발생 단어 카운트
            for i in range(start_idx, end_idx):
                if i != target_idx:  # 타겟 키워드 자신은 제외
                    co_occurrence[words[i]] = co_occurrence.get(words[i], 0) + 1
    
    # 결과를 데이터프레임으로 변환
    result_df = pd.DataFrame({
        'word': list(co_occurrence.keys()),
        'co_occurrence_count': list(co_occurrence.values())
    })
    
    # 빈도수 기준으로 정렬
    result_df = result_df.sort_values('co_occurrence_count', ascending=False)
    result_df.reset_index(drop=True, inplace=True)
    return result_df

def tfidf(df, top_n=20):
    # 각 셀의 키워드를 공백으로 구분된 문자열로 변환
    documents = df['키워드'].apply(lambda x: ' '.join(str(x).split(',')))
    
    # TF-IDF 벡터화
    vectorizer = TfidfVectorizer(
        tokenizer=lambda x: x.split(),  # 이미 토큰화된 단어들을 그대로 사용
        preprocessor=None,  # 전처리 필요 없음
        token_pattern=None  # 토큰 패턴 비활성화
    )
    
    # TF-IDF 계산
    tfidf_matrix = vectorizer.fit_transform(documents)  
    
    # 단어 목록 가져오기
    feature_names = vectorizer.get_feature_names_out()
    
    # 각 단어의 평균 TF-IDF 점수 계산
    avg_tfidf = np.mean(tfidf_matrix.toarray(), axis=0)
    
    # 단어와 점수를 튜플 리스트로 변환
    word_scores = list(zip(feature_names, avg_tfidf))
    
    # 점수 기준으로 정렬
    word_scores.sort(key=lambda x: x[1], reverse=True)
    
    # 상위 N개 단어 선택
    top_words = word_scores[:top_n]
    
    # 결과를 데이터프레임으로 변환
    result_df = pd.DataFrame(top_words, columns=['word', 'tfidf_score'])
    
    return result_df    


def tdidf_analysis(file_path, save_path, top_n=20):
    df = load_excel(file_path)

    before_date, after_date = split_by_date(df)

    before_bag_of_words = bag_of_words(before_date)
    before_n_gram = n_gram(before_date, before_bag_of_words['unique_words'], 2)
    before_tfidf = tfidf(before_date, 100)
    after_tfidf = tfidf(after_date, 100)

    #concat before_tfidf and after_tfidf and save to csv
    df_to_save = pd.concat([before_tfidf, after_tfidf], axis=1)
    df_to_save.to_csv(save_path)

def n_gram_analysis(file_path, save_path, n=2):
    df = load_excel(file_path)

    before_date, after_date = split_by_date(df)

    before_bag_of_words = bag_of_words(before_date)
    before_n_gram = n_gram(before_date, before_bag_of_words['unique_words'], n)
    before_n_gram.columns = ['before_word', 'before_count']

    after_bag_of_words = bag_of_words(after_date)
    after_n_gram = n_gram(after_date, after_bag_of_words['unique_words'], n)
    after_n_gram.columns = ['after_word', 'after_count']

    df_to_save = pd.concat([before_n_gram, after_n_gram], axis=1)
    longer_column = 'after_count' if len(after_n_gram) > len(before_n_gram) else 'before_count'
    df_to_save[longer_column] = df_to_save[longer_column].astype(float)
    df_to_save.to_csv(save_path)