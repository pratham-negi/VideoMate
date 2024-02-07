import streamlit as st
from shortVideo import shortVideoFun as SVF
from subtitle import subtitleFun as SubF
from translator import translatedFile
from summary import summarizationTextFun

import os
from objectDetection import faceList

st.set_page_config(layout="wide")

st.markdown( "<style > div.stButton > button:first-child {color:black; width : 100% ; margin-top : 20px } </style>", unsafe_allow_html=True)

st.markdown( "<style > div.stApp { margin-top : -90px body ; background: linear-gradient(-40deg, #4158D0, #C850C0, #FFCC70, #B7F804);} </style>", unsafe_allow_html=True)

st.markdown( "<style > div.st-emotion-cache-k7vsyb { margin-top : -40px } </style>", unsafe_allow_html=True)


@st.cache_data
def bind_socket(uploaded_filed):
    SVF(uploaded_filed)
    text,timestamp = SubF("temp_file_1.mp4")
    textSum = summarizationTextFun('output.srt')

    with open('text.txt', 'w') as f :
        f.write(textSum)
    translatedFile(text,timestamp)




_, imageCont , _ = st.columns([45,15,45])
imageCont.image('J2fZlf01 (2).svg', use_column_width= True)
st.markdown("# <div align = 'center' > VidSnap </div>", unsafe_allow_html=True)
st.markdown("<hr style='border:2px solid gray'>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Choose a video...", type=["mp4", "mpeg"])
if uploaded_file is not None:
    _, container1, timer = st.columns([20, 60,   20])
    container1.video(uploaded_file)
    with st.spinner('Wait for it...'):
        import time 
        start = time.time()
        print("starting")
        try:
            bind_socket(uploaded_file)
        except:
            timer.write("cache Full")
        
        end = time.time() 
        print(end - start)
        
        
        
    st.success('Done!')


_ , summaryBtn, subtitleBtn, translatedBtn , objectBtn , _ = st.columns([10, 20,20,20,20,   10])


if summaryBtn.button('Summary' , type = 'primary'):
    _, container, _ = st.columns([20, 60,   20])
    container.video("final.mp4")
    fileSum = open("text.txt", "r")
    container.write(fileSum.read())
        


if subtitleBtn.button('Subtitle File' , type = 'primary'):
    _, container, _ = st.columns([20, 60,   20])
    fileSub = open("output.srt", "r")
    data = fileSub.read()
    container.download_button(
    label="Download file",
    data= data,
    file_name='subtitle.srt',
    mime='text/srt',
)
    container.code(data)

if translatedBtn.button("Translate",type = 'primary'):
    _, container, _ = st.columns([20, 60,   20])
    transfileSub = open("translation.srt", "r",encoding="utf8")
    data = transfileSub.read()
    container.download_button(
    label="Download file",
    data= data,
    file_name='subtitle.srt',
    mime='text/srt',
)
    container.code(data)


if objectBtn.button('Characters' , type = 'primary' ):
    _, container, _ = st.columns([20, 60,   20])
    with st.spinner('Wait for it...'):

        listOfImage = faceList()
        container.image(listOfImage)
        
        
    st.success('Done!')



    

            
            

            
        

