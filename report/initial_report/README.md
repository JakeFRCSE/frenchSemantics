[[Kor]](#국가의-의미-분석을-통한-한국과-프랑스의-국가-구성원-정의-비교) [[Eng]](#comparative-analysis-of-the-meaning-of-nation-defining-national-constituents-in-south-korea-and-france)


# 정치성향에 따른 "국민"의 의미 분석

### 1. 주제 선정 동기

#### 1-1. 대한민국의 정치적 양극화 심화


|<img src="https://www.eai.or.kr/Upload/UserFile_20250401125745395414470.JPG"       alt="EAI 동아시아연구원에서 실시한 2025년 양극화 인식 조사. 더불어민주당에 대한 국민의힘 지지자 호감도는 58.8%가 매우 싫다로 답변하였다." >|<img src="https://www.eai.or.kr/Upload/UserFile_20250401125753395414470.JPG"         alt="EAI 동아시아연구원에서 실시한 2025년 양극화 인식 조사. 국민의힘에 대한 민주당 지지자 호감도는 69%가 매우 싫다로 답변하였다." >|
|:--:|:--:|
|<figcaption>출처 : <a href="https://www.eai.or.kr/new/ko/pub/view.asp?intSeq=22687&board=kor_issuebriefing&keyword_option=kor_workingpaper&keyword=kor_special&more=kor_multimedia"> EAI 동아시아연구원 </a></figcaption>|<figcaption>출처 : <a href="https://www.eai.or.kr/new/ko/pub/view.asp?intSeq=22687&board=kor_issuebriefing&keyword_option=kor_workingpaper&keyword=kor_special&more=kor_multimedia">EAI 동아시아연구원</a></figcaption>|



#### 최근 대통령의 계엄령 선포와 대통령 탄핵으로 인해 대한민국의 정치적 양극화가 심화되었습니다. 정치적 양극화는 EAI 동아시아연구원에서 실시한 2025년 양극화 인식 조사에서 잘 드러납니다. 해당 자료는 특정 정당을 지지하는 유권자의 타 정당에 대한 인식을 드러내고 있습니다. 자료를 통해 90% 이상의 응답자들이 타 정당에 대해 부정적 인식을 가지고 있음을 알 수 있고, 이를 통해 정치적 양극화가 심화되었음을 알 수 있습니다.


#### 1-2. 정치적 양극화 속 "국민"의 의미

>"헌재가 국민을 배신했다. 3000만 명 이상 모여 국민 혁명을 일으키자."

>"국민 저항권이 발동되었기 때문에..."

#### 이러한 상황 속에서 위와 같은 문장들을 접하며 특정 집단이 "국민"이라는 단어를 동일한 정치 이념을 공유하는 집단의 의미로 사용하는 경향이 생겨나고 있다는 생각을 하게 되었습니다. 인용문들 속의 "국민"은 표면적으로는 전체 국가 구성원을 지칭하는 듯 보이지만, 실제로는 특정 정치적 성향을 가진 집단만을 의미하는 용례로 해석될 여지가 있기 때문입니다.

#### 1-3. 국가 구성원으로서의 "국민"의 정의 분석 필요성

#### 앞서 살펴본 정치적 양극화 속 "국민" 용례를 통해, 저는 "국민"이라는 단어가 본래 의미하는 국가 구성원 전체를 충분히 포괄하지 못하게 될 위험성을 느꼈습니다. 따라서 이러한 문제의식을 바탕으로, 해당 단어의 사용 양상을 통계적으로 분석하여 "국민"이라는 단어가 사용 주체에 따라 얼마나 다른 의미로 사용되고 있는지를 확인하고자 합니다.


### 2. 주제 탐구 방법

#### 본 프로젝트에서는 "국민"이라는 단어를 분석하기 위해 다음과 같은 방법을 사용할 예정입니다.

1. **사전적 정의 분석** : 한국어 "국민"의 사전적 정의를 분석합니다. 
   
2. **통계적 분석** : 뉴스 미디어에서 사용되는 분석 대상 단어들의 의미를 통계적으로 분석할 예정입니다. `Python`을 사용하여 뉴스 미디어의 내용을 크롤링하여 데이터베이스에 저장할 예정입니다. 이후 해당 단어들이 들어있는 문장/문단/문서를 분석하여 `Streamlit`으로 시각화 하는 방식으로 접근해볼 예정입니다.

3. **참고 자료** : 사전적 정의는 표준국어대사전, 고려대한국어사전, 우리말 샘을 참고할 예정입니다. 통계적 분석은 대통령 탄핵 전후 시점을 중심으로 보수성향 언론사인 조선일보와 진보성향 언론사인 경향신문에서 데이터를 확보할 예정입니다. 단, 원활한 데이터 수집을 위해 언론사가 바뀔 수 있습니다. 

#### 이러한 과정을 통해 정치성향에 따라 달라지는 단어 의미의 차이를 분석해볼 예정입니다.


### 3. 문제 및 한계

#### 본 프로젝트는 정치적 중립을 유지한 상태로 진행되어야 합니다. 이를 위해 각 정치성향별 데이터의 수를 동일하게 유지할 예정입니다. 아직 통계적 분석을 위한 방법론을 확정하지 않은 상태입니다. 분석을 위한 방법론 확정이 필요합니다.


### 4. 향후 계획 및 일정

|주차|연구 계획|달성 여부|비고| 
|:--:|:--:|:--:|:--:|
|1주차|사전적 정의 분석 + 데이터 수집| [ ] ||
|2주차|데이터 전처리 + 통계적 분석| [ ] ||
|3주차|통계적 분석| [ ] ||
|4주차|통계적 분석 결과 시각화| [ ] ||

# Political polarization and the meaning of "gukmin"

### 1. Motivation

#### 1-1. Deepening Political Polarization in South Korea

|<img src="https://www.eai.or.kr/Upload/UserFile_20250401125745395414470.JPG"       alt="EAI East Asia Institute's 2025 Survey on Polarization Perception. 58.8% of People Power Party supporters answered that they 'strongly dislike' the Democratic Party of Korea." >|<img src="https://www.eai.or.kr/Upload/UserFile_20250401125753395414470.JPG"         alt="EAI East Asia Institute's 2025 Survey on Polarization Perception. 69% of Democratic Party supporters answered that they 'strongly dislike' the People Power Party." >|
|:--:|:--:|
|<figcaption>Source: <a href="https://www.eai.or.kr/new/ko/pub/view.asp?intSeq=22687&board=kor_issuebriefing&keyword_option=kor_workingpaper&keyword=kor_special&more=kor_multimedia"> EAI East Asia Institute </a></figcaption>|<figcaption>Source: <a href="https://www.eai.or.kr/new/ko/pub/view.asp?intSeq=22687&board=kor_issuebriefing&keyword_option=kor_workingpaper&keyword=kor_special&more=kor_multimedia">EAI East Asia Institute</a></figcaption>|

Recent events, including the president's declaration of martial law and impeachment, have deepened political polarization in South Korea. This polarization is evident in the EAI East Asia Institute's 2025 survey on polarization perception. The data reveals the perceptions of voters supporting a particular political party towards the opposing party. The survey indicates that over 90% of respondents hold negative perceptions of the opposing party, highlighting the severity of political polarization.

#### 1-2. The Meaning of "Gukmin" (國民 - Nation/People) Amidst Political Polarization

> "The Constitutional Court betrayed the gukmin. Let's gather over 30 million people and start a national revolution."

> "Because the gukmin's right to resistance has been invoked..."

In this context, encountering sentences like the above has led me to believe that certain groups tend to use the word "gukmin" to refer to a collective sharing the same political ideology. While "gukmin" seemingly refers to all national constituents, there is a possibility that it is being used to denote only a specific politically aligned group.

#### 1-3. The Necessity of Analyzing the Definition of "Gukmin" as National Constituents

Through the observed usage of "gukmin" in the context of political polarization, I recognized the potential risk of this term failing to fully encompass all members of the national community, which is its original meaning. Therefore, based on this concern, I aim to statistically analyze the usage patterns of this word to determine how differently "gukmin" is used depending on the speaker/source.

### 2. Research Methodology

In this project, the following methods will be used to analyze the word "gukmin":

1. **Analysis of Dictionary Definitions**: Analyze the dictionary definitions of the Korean word "gukmin."

2. **Statistical Analysis**: The meaning of the target word ("gukmin") as used in news media will be statistically analyzed. Python will be used to crawl news media content and store it in a database. Subsequently, sentences/paragraphs/documents containing the word will be analyzed, and the findings will be visualized using Streamlit.

3. **Reference Materials**: For dictionary definitions, the Standard Korean Language Dictionary (표준국어대사전), Korea University Korean Dictionary (고려대한국어사전), and Woori Mal Saem (우리말샘) will be consulted. For statistical analysis, data will be collected from the conservative news outlet Chosun Ilbo(조선일보) and the progressive news outlet Kyunghyang Shinmun(경향신문), focusing on the period around the presidential impeachment. However, the news outlets may change for ease of data collection.

Through this process, the analysis will aim to examine the differences in the word's meaning based on political orientation.

### 3. Issues and Limitations

This project must be conducted while maintaining political neutrality. To achieve this, the amount of data for each political orientation will be kept equal. The methodology for statistical analysis has not yet been finalized. Finalizing this methodology is necessary.

### 4. Future Plans and Schedule

|Week|Research Plan|Completion Status|Notes|
|:--:|:--:|:--:|:--:|
|Week 1|Analysis of Dictionary Definitions + Data Collection| [ ] ||
|Week 2|Data Preprocessing + Statistical Analysis| [ ] ||
|Week 3|Statistical Analysis| [ ] ||
|Week 4|Visualization of Statistical Analysis Results| [ ] ||