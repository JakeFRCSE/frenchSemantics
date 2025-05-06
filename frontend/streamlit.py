import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import streamlit as st
from backend.crawling import near_words
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import random
import pandas as pd


def main(): 
    st.title("French Semantics")
    st.write("This is a web app for French semantics.")
    st.write("Enter a Korean word (e.g. 국민) and click Submit Korean to get a word cloud and dataframe.")
    korean_word = st.text_input("Enter a Korean word.")
    top_n = st.slider("Set the number of words to display if you want.", 1, 100, 30)
    if st.button("Submit Korean"):
        if korean_word:
            with st.spinner("Processing..."):
                extracted_words = near_words(korean_word, top_n=top_n)
            if extracted_words:
                df = pd.DataFrame(extracted_words, columns=['단어(Word)', '중요도(Score)'])
                extracted_words = {word[0]:word[1]*10 for word in extracted_words}
                font_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'NanumFontSetup_TTF_GOTHIC', 'NanumGothic.ttf')
                font_path = os.path.abspath(font_path)
                palettes = ['spring', 'summer', 'seismic','PuBu', 'Accent', 'Blues', 'BrBG', 'CMRmap']
                wc = WordCloud(font_path=font_path, width=800, height=400, background_color='black', colormap=random.choice(palettes)).fit_words(extracted_words)
                plt.figure(figsize=(10, 5))
                plt.imshow(wc, interpolation='bilinear')
                plt.axis('off')
                st.pyplot(plt)
                plt.clf()
                st.dataframe(df)
            else:
                st.write("No words extracted.")
        else:
            st.write("Please enter a Korean word.")

if __name__ == "__main__":
    main()