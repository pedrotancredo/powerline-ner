import streamlit as st

st.markdown('# Pré anotação:')
st.markdown('''Para agilizar o processo de anotação, utilizaremos como premissa
            algumas expressões regulares. Para isso, vamos criar o dicionário
            indicado abaixo:''')

TABLE = {'Descrição': {
    'Localização:': 'torre ou vão seguido de número',
    'Evento': 'inspeção seguido ou não de detalhada ou aérea',
    'Componente (esfera)': 'esferas ou esfera seguido ou não de sinalização',
    'Componente (espaçador)': 'espaçador ou espaçadores',
    'Componente (cadeia)': 'cadeia opcional seguido por isolador(es)',
    'Componente (faixa)': 'faixa seguido opcionalmente por de servidão',
    'Componente (eucalipto)': 'eucalipto ou eucaliptos',
    'Anomalia (quebrado)': 'quebrado ou quebrados',
    'Anomalia (ninho)': 'ninho ou ninhos seguido por: pássaro, curicaca, gavião ou gaviões',
    'Posição (fase)': 'fase seguido opcionalmente por lateral esquerda ou direita ou central ou do meio ou de baixo ou de cima ou ré ou a vante',
},
    'REGEX': {
        'Localização:': r'(?:[Tt]orre|[Vv]ão)\s+\d+\b[.,]?',
        'Evento': r'\b[Ii]nspeção[,.]?(?:\s[dD]etalhada|\s[aA]érea)?\b[.,]?',
        'Componente (esfera)': r'\b[Ee]sferas?[,.]?(?:\sde[.,]?\s[sS]inalização)\b?[,.]?',
        'Componente (espaçador)': r'\b[Ee]spaçador(?:es)?\b[.,]?',
        'Componente (cadeia)': r'\b(?:[Cc]adeia de )?[Ii]solador(?:es)?\b[.,]?',
        'Componente (faixa)': r'\b[Ff]aixa[.,]?(?: de servidão)?\b[.,]?',
        'Componente (eucalipto)': r'\b[Ee]ucaliptos?\b[.,]?',
        'Anomalia (quebrado)': r'\b[Qq]uebrad(?:o|a)s?\b[.,]?',
        'Anomalia (ninho)': r'\b[Nn]inhos?(?: de (?:[Pp]assarinho|[Pp]ássaro|[Cc]uricaca|[Gg]avião|[Gg]aviões))?\b[.,?]?',
        'Posição (fase)': r'(?:\b[Ff]ases?(?:[,.]? ?lateral)?(?: (?:esquerd[ao]|direit[ao]))?(?: central| do meio| de baixo| de cima| inferior| superior)?[.,]?(?: ré| a?vante)?\b[.,]?)|(?:\b(?:lateral)(?: (?:esquerd[ao]|direit[ao]))?(?: central| do meio| de baixo| de cima| inferior| superior)?[.,]?(?: ré| a?vante)?\b[.,]?)',
}
}

st.dataframe(TABLE)
