import streamlit as st

def main():
    st.title("Hello World")
    st.markdown('Botão')
    botao = st.button('Botão')
    if botao:
        st.markdown("Clicado")

    st.markdown('Checkbox')
    check = st.checkbox('Checkbox')
    if check:
        st.markdown('Checado')
    
    st.markdown('Radio')
    radio = st.radio("Escolha as opções", ('Option 1', 'Option 2', 'Option 3'))
    if radio == 'Option 1':
        st.markdown('Opção 1') 
    if radio == 'Option 2':
        st.markdown('Opção 2')
    if radio == 'Option 3':
        st.markdown('Opção 3')

    st.markdown("Selctbox")
    select = st.selectbox("Choose opt", ("Opt 1", "Opt 2", "Opt 3"))
    if select == 'Opt 1':
        st.markdown("Selecionou opt 1")
    if select == 'Opt 2':
        st.markdown("Selecionou opt 2")
    if select == 'Opt 3':
        st.markdown("Selecionou opt 3")
    
    st.markdown("Multiselect")
    mult = st.multiselect('Choose:', ("Opt 1", "Opt 2", "Opt 3"))
    if mult == 'Opt 1':
        st.markdown('Opt 1')
    if mult == 'Opt 2':
        st.markdown('Opt 2')
    if mult == 'Opt 3':
        st.markdown('Opt 3')

    st.markdown('File Uploader')
    file = st.file_uploader('Choose your file', type='csv') #verificar documentação para as possibilidades
    if file is not None:
        st.markdown('Não está vazio')

if __name__=='__main__':
    main()
