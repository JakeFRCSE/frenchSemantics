import pandas as pd
import os

def modify_tfidf_columns(df):
    """TF-IDF 데이터프레임의 컬럼을 수정합니다."""
    # 필요한 컬럼만 선택
    df = df[['word', 'tfidf_score', 'word.1', 'tfidf_score.1']]
    # 컬럼 이름 변경 - 첫 번째 쌍을 before로, 두 번째 쌍을 after로 매핑
    df.columns = ['word_before', 'tfidf_score_before', 'word', 'tfidf_score']
    return df

def get_file_paths(file_option):
    """선택된 옵션에 따라 파일 경로를 반환합니다."""
    # app 디렉토리 내의 data 폴더 경로
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    
    if file_option == "TF-IDF":
        chosun_path = os.path.join(data_dir, "tfidf_chosun.csv")
        kyunghyang_path = os.path.join(data_dir, "tfidf_kyunghyang.csv")
        
        # TF-IDF 파일 처리
        chosun_df = pd.read_csv(chosun_path)
        kyunghyang_df = pd.read_csv(kyunghyang_path)
        
        chosun_modified = modify_tfidf_columns(chosun_df)
        kyunghyang_modified = modify_tfidf_columns(kyunghyang_df)
        
        return chosun_modified, kyunghyang_modified
    else:  # Co-occurrence
        chosun_path = os.path.join(data_dir, "cooc_chosun.csv")
        kyunghyang_path = os.path.join(data_dir, "cooc_kyunghyang.csv")
        
        try:
            # Co-occurrence 파일 로드
            chosun_df = pd.read_csv(chosun_path)
            kyunghyang_df = pd.read_csv(kyunghyang_path)
            
            # 필요한 정보를 직접 추출하여 새 데이터프레임 생성
            # 컬럼 이름이 'before_word', 'before_count', 'after_word', 'after_count'인 경우
            if 'before_word' in chosun_df.columns and 'after_word' in chosun_df.columns:
                # 컬럼 매핑
                chosun_df = chosun_df[['after_word', 'after_count', 'before_word', 'before_count']]
                chosun_df.columns = ['word', 'tfidf_score', 'word_before', 'tfidf_score_before']
                
                kyunghyang_df = kyunghyang_df[['after_word', 'after_count', 'before_word', 'before_count']]
                kyunghyang_df.columns = ['word', 'tfidf_score', 'word_before', 'tfidf_score_before']
            
            return chosun_df, kyunghyang_df
            
        except Exception as e:
            print(f"Error processing Co-occurrence files: {e}")
            # 오류 발생 시 빈 데이터프레임 반환
            return pd.DataFrame(columns=['word', 'tfidf_score', 'word_before', 'tfidf_score_before']), \
                   pd.DataFrame(columns=['word', 'tfidf_score', 'word_before', 'tfidf_score_before'])


def split_before_after(df):
    """하나의 데이터프레임을 Before/After 데이터로 분리합니다."""
    # After 데이터프레임
    after_df = df[['word', 'tfidf_score']].copy()
    
    # Before 데이터프레임
    before_df = pd.DataFrame({
        'word': df['word_before'],
        'tfidf_score': df['tfidf_score_before']
    })
    
    # NaN 값 제거
    before_df = before_df.dropna()
    after_df = after_df.dropna()
    
    return before_df, after_df 