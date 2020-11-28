from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

st.set_option('deprecation.showPyplotGlobalUse', False)

def cloud(image, text, max_word, max_font, random):
    stopwords = set(STOPWORDS)
    stopwords.update(['us', 'one', 'will', 'said', 'now', 'well', 'man', 'may',
    'little', 'say', 'must', 'way', 'long', 'yet', 'mean',
    'put', 'seem', 'asked', 'made', 'half', 'much',
    'certainly', 'might', 'came'])


    wc = WordCloud(background_color="white", colormap="hot", max_words=max_word, mask=image,
                stopwords=stopwords, max_font_size=max_font, random_state=random)
    # generate word cloud
    wc.generate(text)

    # create coloring from image
    image_colors = ImageColorGenerator(image)

    # show
    plt.figure(figsize=(80,80))
    fig, ax = plt.subplots()
    im = ax.imshow(wc)
    ax.axis('off')
    plt.show()
    #fig, axes = plt.subplots(1,2, gridspec_kw={'width_ratios': [3, 2]})
    #axes[0].imshow(wc, interpolation="bilinear")
    # recolor wordcloud and show
    # we could also give color_func=image_colors directly in the constructor
   # axes[1].imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
    #axes[1].imshow(image, cmap=plt.cm.gray, interpolation="bilinear")
    #for ax in axes:
    #    ax.set_axis_off()
    
    st.pyplot()
    


def main():
    st.write("# WordCloud Text Summary")
    max_word = st.sidebar.slider("Max words", 50, 1000, 50)
    max_font = st.sidebar.slider("Max Font Size", 50, 200, 50)
    random = st.sidebar.slider("Random State", 20, 100, 40 )
    #image = st.file_uploader("Choose a file(preferably a silhouette)")
    image = './cloud.jpg'
    text = st.text_area("Add text ..")
    if image and text is not None:
        if st.button("Plot"):
            #st.write("### Original image")
            image = np.array(Image.open(image))
            #st.image(image, width=100, use_column_width=True)
       
            st.write("### Word cloud")
            st.write(cloud(image, text, max_word, max_font, random), use_column_width=True)


if __name__=="__main__":
    main()