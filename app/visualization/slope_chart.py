import pandas as pd
import plotly.graph_objects as go

def create_slope_chart(file1, file2, top_n=20, title_prefix="", newspaper_option="조선일보"):
    # CSV 파일 읽기
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    
    # 상위 N개 행 선택 및 count 기준 내림차순 정렬
    if newspaper_option == "조선일보":
        df1 = df1.sort_values(by='before_count', ascending=False).reset_index(drop=True)
        df1_top = df1.head(top_n).reset_index(drop=True)
        df2_top = df2.head(top_n).reset_index(drop=True)
    elif newspaper_option == "경향신문":
        df2 = df2.sort_values(by='before_count', ascending=False).reset_index(drop=True)
        df1_top = df1.head(top_n).reset_index(drop=True)
        df2_top = df2.head(top_n).reset_index(drop=True)
    else:
        df1 = df1.sort_values(by='before_count', ascending=False).reset_index(drop=True)
        df2 = df2.sort_values(by='before_count', ascending=False).reset_index(drop=True)
        df1_top = df1.head(top_n).reset_index(drop=True)
        df2_top = df2.head(top_n).reset_index(drop=True)
    
    # Plotly 슬로프 차트 생성
    fig = go.Figure()
    
    # 신문사 선택에 따른 처리
    if newspaper_option == "조선일보":
        before_words = df1_top['before_word'].tolist()
        after_words = df1_top['after_word'].tolist()
        before_counts = df1_top['before_count'].tolist()
        after_counts = df1_top['after_count'].tolist()
        
        for i in range(len(before_words)):
            if before_words[i] in after_words:
                after_rank = after_words.index(before_words[i])
                before_rank = i
                # y축은 0이 상위, 값이 커질수록 하위이므로, after_rank < before_rank면 순위 상승(빨간), after_rank > before_rank면 순위 하락(파란)
                if after_rank < before_rank:
                    color = 'red'    # 순위 상승
                elif after_rank > before_rank:
                    color = 'blue'   # 순위 하락
                else:
                    color = 'black'  # 순위 유지
                fig.add_trace(go.Scatter(
                    x=[0, 1],
                    y=[before_rank, after_rank],
                    mode='lines+markers+text',
                    line=dict(color=color, width=2),
                    marker=dict(size=10, color=color),
                    text=[f"{before_words[i]} ({before_counts[i]})", f"{after_words[after_rank]} ({after_counts[after_rank]})"],
                    textposition=['middle right', 'middle left'],
                    name=f'Pair {i+1}'
                ))
            else:
                # 매핑되지 않은 단어: 점+텍스트만 표시 (회색)
                fig.add_trace(go.Scatter(
                    x=[0],
                    y=[i],
                    mode='markers+text',
                    marker=dict(size=10, color='gray'),
                    text=[f"{before_words[i]} ({before_counts[i]})"],
                    textposition=['middle right'],
                    showlegend=False
                ))
        # after 쪽에만 있는 단어도 점+텍스트만 표시
        for j in range(len(after_words)):
            if after_words[j] not in before_words:
                fig.add_trace(go.Scatter(
                    x=[1],
                    y=[j],
                    mode='markers+text',
                    marker=dict(size=10, color='gray'),
                    text=[f"{after_words[j]} ({after_counts[j]})"],
                    textposition=['middle left'],
                    showlegend=False
                ))
        title = f'{title_prefix} 분석: 조선일보 Before/After 단어 비교 (상위 {top_n}개)'
        x_labels = ['Before 단어', 'After 단어']
    elif newspaper_option == "경향신문":
        before_words = df2_top['before_word'].tolist()
        after_words = df2_top['after_word'].tolist()
        before_counts = df2_top['before_count'].tolist()
        after_counts = df2_top['after_count'].tolist()
        for i in range(len(before_words)):
            if before_words[i] in after_words:
                after_rank = after_words.index(before_words[i])
                before_rank = i
                if after_rank < before_rank:
                    color = 'red'
                elif after_rank > before_rank:
                    color = 'blue'
                else:
                    color = 'black'
                fig.add_trace(go.Scatter(
                    x=[0, 1],
                    y=[before_rank, after_rank],
                    mode='lines+markers+text',
                    line=dict(color=color, width=2),
                    marker=dict(size=10, color=color),
                    text=[f"{before_words[i]} ({before_counts[i]})", f"{after_words[after_rank]} ({after_counts[after_rank]})"],
                    textposition=['middle right', 'middle left'],
                    name=f'Pair {i+1}'
                ))
            else:
                fig.add_trace(go.Scatter(
                    x=[0],
                    y=[i],
                    mode='markers+text',
                    marker=dict(size=10, color='gray'),
                    text=[f"{before_words[i]} ({before_counts[i]})"],
                    textposition=['middle right'],
                    showlegend=False
                ))
        for j in range(len(after_words)):
            if after_words[j] not in before_words:
                fig.add_trace(go.Scatter(
                    x=[1],
                    y=[j],
                    mode='markers+text',
                    marker=dict(size=10, color='gray'),
                    text=[f"{after_words[j]} ({after_counts[j]})"],
                    textposition=['middle left'],
                    showlegend=False
                ))
        title = f'{title_prefix} 분석: 경향신문 Before/After 단어 비교 (상위 {top_n}개)'
        x_labels = ['Before 단어', 'After 단어']
    else:
        chosun_words = df1_top['before_word'].tolist()
        kyunghyang_words = df2_top['before_word'].tolist()
        chosun_counts = df1_top['before_count'].tolist()
        kyunghyang_counts = df2_top['before_count'].tolist()
        for i in range(len(chosun_words)):
            if chosun_words[i] in kyunghyang_words:
                kyunghyang_rank = kyunghyang_words.index(chosun_words[i])
                chosun_rank = i
                if kyunghyang_rank < chosun_rank:
                    color = 'red'
                elif kyunghyang_rank > chosun_rank:
                    color = 'blue'
                else:
                    color = 'black'
                fig.add_trace(go.Scatter(
                    x=[0, 1],
                    y=[chosun_rank, kyunghyang_rank],
                    mode='lines+markers+text',
                    line=dict(color=color, width=2),
                    marker=dict(size=10, color=color),
                    text=[f"{chosun_words[i]} ({chosun_counts[i]})", f"{kyunghyang_words[kyunghyang_rank]} ({kyunghyang_counts[kyunghyang_rank]})"],
                    textposition=['middle right', 'middle left'],
                    name=f'Pair {i+1}'
                ))
            else:
                fig.add_trace(go.Scatter(
                    x=[0],
                    y=[i],
                    mode='markers+text',
                    marker=dict(size=10, color='gray'),
                    text=[f"{chosun_words[i]} ({chosun_counts[i]})"],
                    textposition=['middle right'],
                    showlegend=False
                ))
        for j in range(len(kyunghyang_words)):
            if kyunghyang_words[j] not in chosun_words:
                fig.add_trace(go.Scatter(
                    x=[1],
                    y=[j],
                    mode='markers+text',
                    marker=dict(size=10, color='gray'),
                    text=[f"{kyunghyang_words[j]} ({kyunghyang_counts[j]})"],
                    textposition=['middle left'],
                    showlegend=False
                ))
        title = f'{title_prefix} 분석: 조선일보 vs 경향신문 Before 단어 비교 (상위 {top_n}개)'
        x_labels = ['조선일보', '경향신문']
    # 레이아웃 설정
    fig.update_layout(
        title=dict(
            text=title,
            y=0.95,
            x=0.5,
            xanchor='center',
            yanchor='top',
            font=dict(size=20)
        ),
        xaxis=dict(
            showticklabels=False,
            range=[-0.1, 1.1]
        ),
        yaxis=dict(
            showticklabels=False,
            range=[top_n-1, -1]
        ),
        showlegend=False,
        height=800,
        width=1000,
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(size=12),
        margin=dict(t=100)
    )
    
    fig.add_annotation(
        x=0, y=-1,
        text=x_labels[0],
        showarrow=False,
        font=dict(size=14, color='#1f77b4')
    )
    fig.add_annotation(
        x=1, y=-1,
        text=x_labels[1],
        showarrow=False,
        font=dict(size=14, color='#1f77b4')
    )
    return fig

if __name__ == "__main__":
    # 테스트용 파일 경로
    file1 = "src/data/cooc_chosun.csv"
    file2 = "src/data/cooc_kyunghyang.csv"
    # 슬로프 차트 생성
    fig = create_slope_chart(file1, file2)
    # HTML 파일로 저장
    fig.write_html("src/visualization/slope_chart.html") 