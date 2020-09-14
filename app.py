import streamlit as st
import os 
import base64
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.tokenizers import Tokenizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from collections import Counter
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import random
nltk.download('punkt')
nltk.download('stopwords')

file_ = open("./1.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

lang = 'english'
count = 10

    
st.header("NLP For CyberCrime and The Law Class Readings")    

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" style="width: 100%;max-width: 400px;height: auto;display: block;margin-left: auto;margin-right: auto;" alt="robobootcamp gif">',
    unsafe_allow_html=True,
)

keys = {
    '08/13/2020': './day/08-13-2020/txt',
    '08/18/2020': './day/08-18-2020/txt',
    '08/20/2020': './day/08-20-2020/txt',
    '08/25/2020': './day/08-25-2020/txt',
    '08/27/2020': './day/08-27-2020/txt',
    '09/01/2020': './day/09-01-2020/txt',
    '09/03/2020': './day/09-03-2020/txt',
    '09/08/2020': './day/09-08-2020/txt',
    '09/22/2020': './day/09-22-2020/txt',
    '09/24/2020': './day/09-24-2020/txt',
    'Others': './day/Others/txt',
            } 
            

st.subheader("Syllabus Readings")
pick = st.selectbox("Select a Day: ", list(keys.keys()))





def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)






if pick != 'hello':
    
    
    folder = keys[pick]+"/"
    txt_files = os.listdir(keys[pick])
    
    for i in txt_files:
        words_list = []
        words_corpus = []
        corpus = []
        with open(folder+ i ,encoding='utf8') as f_input:
            corpus.append(f_input.read()) 
        
        new_string = corpus[0].replace('.', '. ').strip()
        lsa = LsaSummarizer(Stemmer(lang))
        lsa.stop_words = get_stop_words(lang)
        parser = PlaintextParser.from_string(new_string, Tokenizer(lang))
        lsa_summary = lsa(parser.document, count)
        lsa_s = [str(sent) for sent in lsa_summary]
        summary = ' '.join(lsa_s)
        st.write("")
        st.write("")
        st.header("Summary of " + i[8:-4] + " Reading")
        st.write(summary)
        
        

        for phrase in corpus:
            words_list.append((str(phrase)).split())

        
        for words in words_list:
            for word in words:
                words_corpus.append(word)
        
        
        clean_tokens = []
 
        sr = stopwords.words('english')
        sr.extend(['From:', "Don't", 'No.','GEORGE','[|',"anything", "/", 'v.','I,','didn’t','9','was,', 'say', 'Do', 'here.', 'put','3','make','statement', 'go', 'point.','going','Clockwise', 'the,','‘cause', 'IN','This','first','the','may','that', "that,", "Speaker2:", "I'm","don't", 'sir.', 'hmm.', 'Yes', 'When', 'saw', 'still','THE', 'gonna', 'I', 'and,', 'anything', 'OK.', 'Okay','back'," ___ ", "Serino:", "John","Kevin","Okay,", "If", "AND", "2","Martin","Speaker:", "sir", "point", "Other", "He", ":", "tell", "went", "looked", "Mm", "Singleton:","John","Serino","Kevin","I'm","|'ll",'—','____','___','I','Okay.','||', '|__|', '———','______', 'David', "O'Rourke", "Singleton", "O'Rourke:",'Firefighter', "I'm", 'right', 'Mr.','think','It','get','one','time','PHOTO','must','would',"don't","that's","Okay.","you,",'Bachelor:','top','Special','The','um,','Lee:','said','Uh,','said,','got','****','could','guy',"I'm",'I’m','don’t','that’s','So','.', '2:','Um,', 'see', 'know' ,'person','Yes,', 'You', "ma'am.",'Zimmerman:','And', '1:', 'like', 'OF','uh,', 'Okay_','|_|','know,','Speaker','--','___','--,', '-', '-,', '_','__','West', 'To:', 'js', 'Cc', '|', 'Wl', 'Subject:'])
        for token in words_corpus:
            if token not in sr:
                clean_tokens.append(token)
        clean_word_count = Counter(clean_tokens)
        st.header("Word Cloud of " + i[8:-4] + " Reading")
        
        wordcloud = WordCloud(background_color='black', collocations=False, width = 1000, height = 500).generate_from_frequencies(clean_word_count)
        plt.figure(figsize=(15,8))

        plt.imshow(wordcloud.recolor(color_func=grey_color_func, random_state=3), interpolation="bilinear")
        plt.axis("off")
        st.pyplot()
        st.write("")
        st.write("")
        #st.write(clean_tokens)

    