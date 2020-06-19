import streamlit as st

def main():
    st.title("Hello World")
    st.header('This is a header')
    st.subheader('This is a subheader') 
    st.text('isto é um texto')
    st.subheader("Logo do Python")
    st.image('python.png')
    #st.audio('arquivo.extensão')  #tras um arquivo em audio
    #st.video('video') #traz arquivo em video

    

if __name__=='__main__':
    main()