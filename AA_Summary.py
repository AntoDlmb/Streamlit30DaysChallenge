import streamlit as st


st.set_page_config(layout='wide',page_title='Sommaire')
st.title('Sommaire du 30 Days challenge')

with st.expander('Table des matières du 30 days challenge Streamlit'):
    st.write('Vous trouverez toutes les notions vues durant le 30 Days challenge de streamlit. Pour voir le code associé, sélectionné au moins une des notions dans le menu à gauche' )

affiliation_day = {'Test streamlit installé':'Day1.py',
                   'Streamlit hello world':'Day2.py',
                   'Button':'Day3.py',
                   'Project : Plotly / Streamlit':'Day4.py',
                   'Tous types d\'écriture (write, markdown...)':'Day5.py',
                   'Sliders':'Day8.py',
                   'Graphiques':'Day9.py',
                   'Select Box':'Day10.py',
                   'Multiselection':'Day11.py',
                   'CheckBox':'Day12.py',
                   'Pandas profiling':'Day14.py',
                   'Latex':'Day15.py',
                   'Theme de l\'app avec .config':'Day16.py',
                   'Secrets':'Day17.py',
                   'Upload file':'Day18.py',
                   'Layout':'Day19.py',
                   'Progress bar':'Day21.py',
                   'Formulaire':'Day22.py',
                   'Paramètre de requête':'Day23.py',
                   'Cache et ressource':'Day24.py',
                   'Variables de session':'Day25.py',
                   'Project : Elements streamlit':'Day27.py',
                   'Project : Analyse shap':'Day28.py',
                   'Project : Hugging face':'Day29.py',
                   'Project : Miniature yt' : 'Day30.py',
                   'Utils':'URL'
                   }

def get_content_of_file(name_file):
    with open(name_file,'r',encoding=('utf-8')) as pythonfile:
        content = pythonfile.read()
    return content

with st.sidebar:
    st.header('Chapitres')
    l_notions = st.multiselect('30 days challenge',affiliation_day.keys())
    if len(l_notions)>0:
        st.subheader('Notions affichées : ')
        for notion in l_notions:
            st.markdown(notion)

for notion in l_notions:
    if notion!='Utils':
        st.subheader(notion)
        st.code(get_content_of_file(affiliation_day[notion]),language='python')
    else:
        st.subheader('Ressources utiles')
        c1,c2,c3 = st.columns([0.25,0.5,0.25])
        with c1 :
            st.markdown('**API Documentation**')
            st.markdown('https://docs.streamlit.io/')
        with c2: 
            st.markdown('**Cheat sheet**')
            st.markdown('https://docs.streamlit.io/develop/quick-reference/cheat-sheet')
        with c3:
            st.markdown('**Deployment**')
            st.markdown('https://streamlit.io/cloud')