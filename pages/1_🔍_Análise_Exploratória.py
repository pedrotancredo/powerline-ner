from nltk.corpus import stopwords
import streamlit as st
import pandas as pd
from datetime import datetime
import altair as alt
import nltk
import re

def replace_words(text):

    WORDS_TO_REPLACE = {
        r'\d+': '',                 # Remove digitos
        r'[-_!.,?\\\/*%+]+': ' ',    # Remove caracteres especiais
        r'[áàãâä]': 'a',            # Substitui acentuação por letra a
        r'[éèêë]': 'e',             # Substitui acentuação por letra e
        r'[íìîï]': 'i',             # Substitui acentuação por letra i
        r'[óòõôö]': 'o',            # Substitui acentuação por letra o
        r'[úûùü]': 'u',             # Substitui acentuação por letra u
        r'ç': 'c',                  # Substitui ç
        r'\s+': ' ',                # Substitui espaços multiplos por simples
        r'\binspe\b': 'inspecao',
        'inspeccao': 'inspecao',
        'impressao': 'inspecao',
        'expressao': 'inspecao',
        r'\bpressao\b': 'inspecao',
        r'\bfaz\b': 'fase',
        'cadeias': 'cadeia',
        'coragem': 'ancoragem',
        'esferas': 'esfera',
        'iitutinga': 'itutinga',
        r'\btalhada\b' : 'detalhada',
        r'\bum\b': '1',
        r'\bdois\b': '2',
        r'\btrês\b': '3',
        r'\bquatro\b': '4',
        r'\bcinco\b': '5',
        r'\bseis\b': '6',
        r'\bsete\b': '7',
        r'\boito\b': '8',
        r'\bnove\b': '9',
        r'\bzero\b': '0',
        r'\b\w{1,2}\b': '',         # Palavras de comprimento um ou dois caracteres
    }
    for pattern, replacement in WORDS_TO_REPLACE.items():
        text = re.sub(pattern, replacement, text)
    return text

st.markdown("# Análise exploratória")

st.markdown('## Carga do Arquivo de Entrada')


@st.cache_data
def load_data(uploaded_transcript):
    if uploaded_transcript is not None:
        try:
            df = pd.read_csv(uploaded_transcript, sep=';')

        except Exception:
            st.error('CSV Inválido')
            return None
        return df

uploaded_transcript = st.file_uploader('Transcrições:',type=['csv'])


df = load_data(uploaded_transcript)

if df is None:
    st.stop()



# Exclui colunas não utilizadas na avaliação
COLUMNS = {
    'id': 'str',
    'ciclo': 'category',
    'regional': 'category',
    # 't_azure': 'str',
    # 't_humana': 'str',
    # 'status': 'int64',
    # 'audio': 'str',
    # 'date': 'datetime64',
    # 't_model_texto': 'str',
    't_model_audio': 'str',
}

df = df[COLUMNS]

df = df[df['id'] != 'A02843']
df = df[df['t_model_audio'] != 'NAO_FOI_EXTRAIDO_TEXTO']

df = df.astype(dict(COLUMNS)).set_index('id')
df = df.rename(columns={'t_model_audio': 'transcript'})
#filtered df

filter = st.text_input('Filtrar palavra:', value='')
# filter = st.multiselect('oi',st.session_state['wordslist'])
filtered_df = df[df['transcript'].str.contains(filter)]
# filtered_df = df[df['transcript'].str.lower().apply(lambda x: all(word in x for word in filter))]
st.metric('Quantidade de registros:', len(filtered_df))
st.dataframe(filtered_df)
st.markdown('## Histograma de frequência de cada palavra')

# Faz a limpeza nas palavras:
filtered_df['transcript'] = filtered_df['transcript'].str.lower()

# filtered_df['transcript'] = filtered_df['transcript'].replace(WORDS_TO_REPLACE, regex=True)
filtered_df['transcript'] = filtered_df['transcript'].apply(replace_words)


# Palavras para remover
@st.cache_data
def load_stopwords():

    nltk.download('stopwords')

    sw = stopwords.words('portuguese')

    STOP_WORDS = ['das', 'dos', 'sim', 'nao', 'foi',
                'com', 'nas', 'nos', 'que', 'dia',
                'meu', 'ano', 'ela', 'ele', 'era', 'pra',
                'por', 'seu', 'sua', 'nan', 'ate',
                'nesse', 'desse', 'nessa', 'essa',
                'este', 'esta', 'estas', 'estes', 'esse', 'essa', 'esses', 'essas'
                'estou', 'estava', 'estava', 'estou',
                'ali', 'aqui', 'bem', 'bom', 'sem', 'agora', 'vai', 'uma', 'para',
                'partir', 'vamos', 'entao', 'quem', 'voce', 'onde']

    STOP_WORDS.extend(sw)

    return set(STOP_WORDS)

STOP_WORDS = load_stopwords()
# Remove stopwords da coluna 'transcript'
filtered_df['transcript'] = filtered_df['transcript'].apply(lambda x: ' '.join(
    [word for word in x.split() if word not in STOP_WORDS]))


# Divide coluna em palavras e agrupa por frequência:
words = filtered_df['transcript'].str.split().explode(
).value_counts().sort_values(ascending=False)

words = words.reset_index()

col1, col2 = st.columns([4,1])

with col2:
    threshold = st.number_input('Frequência mínima:', value=1,key='threshold', min_value=1)
    words = words[words['transcript'] >= threshold]

with col1:
    words_quantity = st.slider('Filtro de palavras:', 1,
                           words.shape[0], [0, int(words.shape[0]/2)], key='words_quantity')

# Remove frequencia inferior a limite


# words
filtered_words = words.iloc[words_quantity[0]:words_quantity[1]]

hist = alt.Chart(filtered_words).mark_bar().encode(
    x=alt.X('index', sort='-y'),
    y='transcript'
)

st.altair_chart(hist, use_container_width=True)
st.markdown('### Lista de palavras:')
st.session_state['wordslist'] = list(filtered_words['index'])
st.write(', '.join(filtered_words['index']))
