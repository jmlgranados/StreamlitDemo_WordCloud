from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

st.set_option('deprecation.showPyplotGlobalUse', False)

def cloud(image, text, max_word, max_font, random):
    stopwords = set(STOPWORDS)
    wc = WordCloud(background_color="white", colormap="hot", max_words=max_word, mask=image,
                stopwords=stopwords, max_font_size=max_font, random_state=random)

    wc.generate(text)

    image_colors = ImageColorGenerator(image)

    plt.figure(figsize=(80,80))
    fig, ax = plt.subplots()
    im = ax.imshow(wc)
    ax.axis('off')
    plt.show()
    st.pyplot()
    
def main():
    st.write("# WordCloud Text Summary")
    max_word = st.sidebar.slider("Max words", 50, 1000, 50)
    max_font = st.sidebar.slider("Max Font Size", 50, 200, 50)
    random = st.sidebar.slider("Random State", 20, 100, 40 )
    image = './cloud.jpg'
    text = st.text_area("Add your text...")
    if image and text is not None:
        if st.button("Plot"):
            image = np.array(Image.open(image))
       
            st.write("### Word Cloud")
            st.write(cloud(image, text, max_word, max_font, random), use_column_width=True)


if __name__=="__main__":
    main()
