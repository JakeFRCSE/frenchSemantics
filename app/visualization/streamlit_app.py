import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os
import sys

# 프로젝트 루트 디렉토리를 Python 경로에 추가
project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(project_root)

from app.utils import get_file_paths, split_before_after

def create_slope_chart(df_before, df_after, top_n=20, newspaper="조선일보"):
    # 각 데이터프레임에서 상위 N개 단어 선택 (정확히 N개만)
    df_before_top = df_before.nlargest(top_n, 'tfidf_score')
    df_after_top = df_after.nlargest(top_n, 'tfidf_score')
    
    # 각 시점의 상위 단어 목록
    words_before = df_before_top['word'].tolist()
    words_after = df_after_top['word'].tolist()
    
    # 데이터 준비
    data = []
    
    # 1. Before 시점의 상위 N개 단어 처리
    for word in words_before:
        rank_before = df_before_top[df_before_top['word'] == word].index[0] + 1
        score_before = df_before_top[df_before_top['word'] == word]['tfidf_score'].values[0]
        
        # After 시점에서의 순위와 점수 (있는 경우에만)
        if word in words_after:
            rank_after = df_after_top[df_after_top['word'] == word].index[0] + 1
            score_after = df_after_top[df_after_top['word'] == word]['tfidf_score'].values[0]
            
            # 순위가 변한 경우 (빨간색 또는 파란색)
            if rank_after < rank_before:  # 순위가 상승한 경우 (빨간색)
                line_color = 'red'
            elif rank_after > rank_before:  # 순위가 하락한 경우 (파란색)
                line_color = 'blue'
            else:  # 순위가 같은 경우 (검은색)
                line_color = 'black'
                
            data.append({
                'word': word,
                'rank_before': rank_before,
                'rank_after': rank_after,
                'score_before': score_before,
                'score_after': score_after,
                'line_color': line_color,
                'type': 'both'
            })
        else:
            # Before 시점에만 있는 단어
            data.append({
                'word': word,
                'rank_before': rank_before,
                'rank_after': None,
                'score_before': score_before,
                'score_after': 0,
                'line_color': 'gray',
                'type': 'before'
            })
    
    # 2. After 시점에만 있는 상위 N개 단어 처리
    for word in words_after:
        if word not in words_before:  # Before 시점에 없는 단어만
            rank_after = df_after_top[df_after_top['word'] == word].index[0] + 1
            score_after = df_after_top[df_after_top['word'] == word]['tfidf_score'].values[0]
            
            data.append({
                'word': word,
                'rank_before': None,
                'rank_after': rank_after,
                'score_before': 0,
                'score_after': score_after,
                'line_color': 'gray',
                'type': 'after'
            })
    
    # Plotly 그래프 생성
    fig = go.Figure()
    
    # 선과 점 추가 - 양쪽에 있는 단어 먼저 (겹치는 것 방지)
    for item in data:
        if item['type'] == 'both':
            # 선 추가 (매핑된 단어만)
            fig.add_trace(go.Scatter(
                x=[0, 1],
                y=[item['rank_before'], item['rank_after']],
                mode='lines+markers+text',
                name=item['word'],
                line=dict(color=item['line_color'], width=2),
                text=[item['word'], item['word']],
                textposition=["middle left", "middle right"],  # 텍스트를 좌우로 이동
                textfont=dict(size=14),
                marker=dict(size=10),
                hovertemplate=f"<b>{item['word']}</b><br>순위: %{{y}}<br>점수: {item['score_before']:.2f} / {item['score_after']:.2f}<extra></extra>"
            ))
    
    # Before 시점에만 있는 단어 추가
    for item in data:
        if item['type'] == 'before':
            fig.add_trace(go.Scatter(
                x=[0],
                y=[item['rank_before']],
                mode='markers+text',
                name=item['word'],
                marker=dict(color='gray', size=10),
                text=[item['word']],
                textposition="middle left",  # 텍스트를 왼쪽으로 이동
                textfont=dict(size=14, color='gray'),
                hovertemplate=f"<b>{item['word']}</b><br>순위: %{{y}}<br>점수: {item['score_before']:.2f}<extra></extra>"
            ))
    
    # After 시점에만 있는 단어 추가
    for item in data:
        if item['type'] == 'after':
            fig.add_trace(go.Scatter(
                x=[1],
                y=[item['rank_after']],
                mode='markers+text',
                name=item['word'],
                marker=dict(color='gray', size=10),
                text=[item['word']],
                textposition="middle right",  # 텍스트를 오른쪽으로 이동
                textfont=dict(size=14, color='gray'),
                hovertemplate=f"<b>{item['word']}</b><br>순위: %{{y}}<br>점수: {item['score_after']:.2f}<extra></extra>"
            ))
    
    # 레이아웃 설정
    title_text = f'{newspaper} 단어 순위 비교 (Before vs After)'
    
    # x축 레이블 설정
    left_label = "Before"
    right_label = "After"
    
    fig.update_layout(
        title=dict(
            text=title_text,
            font=dict(size=24)
        ),
        xaxis=dict(
            title=dict(text='시간 흐름', font=dict(size=18)),
            ticktext=[left_label, right_label],
            tickvals=[0, 1],
            range=[-0.2, 1.2],  # 텍스트가 더 잘 보이도록 범위 확장
            tickfont=dict(size=16)
        ),
        yaxis=dict(
            title=dict(text='순위', font=dict(size=18)),
            autorange='reversed',  # 순위가 위로 갈수록 높은 순위
            tickfont=dict(size=14),
            range=[0, top_n+1]  # Y축 범위를 1부터 top_n까지로 설정
        ),
        showlegend=False,  # 범례 숨기기 (너무 많은 항목이 있어서)
        height=900,  # 그래프 높이 크게 설정
        width=1200,  # 그래프 너비 설정
        margin=dict(l=100, r=100, t=80, b=50),  # 여백 넓게 설정
        plot_bgcolor='white',
        hovermode='closest'
    )
    
    return fig

def main():
    st.set_page_config(
        page_title="신문사 단어 빈도 비교",
        page_icon="📰",
        layout="wide"
    )
    
    st.title("신문사 단어 빈도 비교 분석")
    
    # 사이드바에 설정 추가
    st.sidebar.header("설정")
    
    # 파일 선택
    file_option = st.sidebar.radio(
        "비교할 파일 선택",
        ["TF-IDF", "Co-occurrence"],
        help="비교할 분석 결과를 선택하세요"
    )
    
    # 신문사 선택
    newspaper_option = st.sidebar.radio(
        "신문사 선택",
        ["조선일보", "경향신문"],
        help="분석할 신문사를 선택하세요"
    )
    
    # 상위 단어 수 선택
    top_n = st.sidebar.slider(
        "표시할 상위 단어 수",
        min_value=5,
        max_value=50,
        value=20,
        step=5,
        help="각 시점에서 표시할 상위 단어의 수를 선택하세요"
    )
    
    try:
        # 데이터프레임 가져오기
        chosun_df, kyunghyang_df = get_file_paths(file_option)
        
        # 신문사 선택에 따라 데이터셋 필터링
        if newspaper_option == "조선일보":
            # 조선일보 Before/After 데이터 분리
            df_before, df_after = split_before_after(chosun_df)
        else:  # 경향신문
            # 경향신문 Before/After 데이터 분리
            df_before, df_after = split_before_after(kyunghyang_df)
        
        # 데이터 프리뷰
        with st.sidebar.expander("데이터 프리뷰"):
            st.write(f"**{newspaper_option} Before 데이터**")
            st.dataframe(df_before.head(3))
            
            st.write(f"**{newspaper_option} After 데이터**")
            st.dataframe(df_after.head(3))
            
            # 데이터 정보 표시
            st.write(f"**{newspaper_option} 데이터셋 정보**")
            st.write(f"Before 단어 수: {len(df_before)}")
            st.write(f"After 단어 수: {len(df_after)}")
        
        # 슬로프 차트 생성
        fig = create_slope_chart(df_before, df_after, top_n, newspaper_option)
        
        # 표시된 단어 수
        common_words = len(set(df_before.nlargest(top_n, 'tfidf_score')['word']).intersection(
                        set(df_after.nlargest(top_n, 'tfidf_score')['word'])))
        
        # 차트 위에 정보 추가
        st.info(f"{newspaper_option}: Before와 After에서 각각 상위 {top_n}개 단어 표시 (공통 단어: {common_words}개)")
        
        # 차트 표시
        st.plotly_chart(fig, use_container_width=True)
        
        # 색상 범례 만들기
        st.markdown("<h3 style='text-align: center;'>차트 색상 설명</h3>", unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown('<div style="background-color: red; height: 20px; width: 20px; display: inline-block; margin-right: 5px;"></div> <span style="font-size: 16px;">순위 상승</span>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div style="background-color: blue; height: 20px; width: 20px; display: inline-block; margin-right: 5px;"></div> <span style="font-size: 16px;">순위 하락</span>', unsafe_allow_html=True)
        with col3:
            st.markdown('<div style="background-color: black; height: 20px; width: 20px; display: inline-block; margin-right: 5px;"></div> <span style="font-size: 16px;">순위 유지</span>', unsafe_allow_html=True)
        with col4:
            st.markdown('<div style="background-color: gray; height: 20px; width: 20px; display: inline-block; margin-right: 5px;"></div> <span style="font-size: 16px;">한 시점에만 존재</span>', unsafe_allow_html=True)
        
        # 설명 추가
        with st.expander("차트 사용법 및 주의사항"):
            st.markdown("""
            ### 차트 사용법
            - **빨간색 실선**: 순위가 상승한 단어 (After에서 더 높은 순위)
            - **파란색 실선**: 순위가 하락한 단어 (After에서 더 낮은 순위) 
            - **검은색 실선**: 순위가 동일한 단어
            - **회색 점**: 한 시점에만 나타나는 단어 (텍스트도 회색으로 표시)
            - 그래프 위에 마우스를 올리면 단어의 정확한 순위와 점수를 볼 수 있습니다.
            - 원하는 영역을 드래그하여 확대할 수 있습니다.
            - 더블 클릭하면 그래프를 초기화할 수 있습니다.
            
            ### 주의사항
            - 슬라이더로 각 시점별 상위 N개 단어만 표시됩니다.
            - 각 시점에서 상위 N개 단어만 표시되므로, 실제 순위가 N보다 낮은 단어는 표시되지 않습니다.
            - 단어가 많을 경우 텍스트가 겹칠 수 있습니다. 이 경우 상위 단어 수를 줄여보세요.
            """)
        
    except Exception as e:
        st.error(f"오류가 발생했습니다: {str(e)}")
        st.exception(e)

if __name__ == "__main__":
    main() 