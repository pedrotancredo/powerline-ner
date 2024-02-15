import base64
import streamlit as st
import requests
from annotated_text import annotated_text
from streamlit_mic_recorder import speech_to_text

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def agrupar_entidades_adjacentes(dados):
    resultado = []
    grupo_atual = None

    for item in dados:
        if grupo_atual is None or (
            item["entity_group"] == grupo_atual["entity_group"]
            and item["start"] == grupo_atual["end"]
        ):
            if grupo_atual is None:
                grupo_atual = {
                    "entity_group": item["entity_group"],
                    "start": item["start"],
                    "end": item["end"],
                }
            else:
                grupo_atual["end"] = item["end"]
        else:
            resultado.append(grupo_atual)
            grupo_atual = {
                "entity_group": item["entity_group"],
                "start": item["start"],
                "end": item["end"],
            }

    if grupo_atual is not None:
        resultado.append(grupo_atual)

    return resultado

# Função para agrupar entidades adjacentes
def aplicar_agrupamento_na_string(resultado_agrupado, texto_original):
    saida = []

    posicao_atual = 0

    for grupo in resultado_agrupado:
        start = grupo["start"]
        end = grupo["end"]
        entity_group = grupo["entity_group"]

        if start > posicao_atual:
            # Adiciona a parte não mapeada à lista
            nao_mapeado = texto_original[posicao_atual:start]
            saida.append(nao_mapeado)

        if isinstance(entity_group, str):
            # Se a entidade tem uma "word" associada, adiciona à lista como uma tupla
            palavra = texto_original[start:end]
            saida.append((palavra, entity_group))
        else:
            # Se não tem uma "word" associada, adiciona à lista como uma string simples
            saida.append(texto_original[start:end])

        posicao_atual = end

    # Adiciona o restante não mapeado à lista, se houver
    if posicao_atual < len(texto_original):
        nao_mapeado_final = texto_original[posicao_atual:]
        saida.append(nao_mapeado_final)

    return saida


API_TOKEN = st.secrets["API_TOKEN"]
API_URL = st.secrets["API_URL"]

headers = {"Authorization": f"Bearer {API_TOKEN}"}

# Inicializnado o endpoint
query("Inspeção detalhada torre 123, esfera desbotada, necessita substituição. Linha palmares campo grande, para-raios esquerdo")

state = st.session_state

st.markdown("# Demonstração")
st.markdown(
    """<div align="justify"><p>No exemplo é possível testar o modelo fazendo
    envio de texto transcrito a partir de gravação de audio:</p></div>""",
    unsafe_allow_html=True,
)

if "text_input" not in state:
    state.text_input = ""

if "text" not in state:
    state.text = ""

c1, c2 = st.columns((2, 1))
with c1:
    st.write("Gravar áudio:")

with c2:
    text = speech_to_text(
        "🔴 Gravar",
        "🟩 Parar",
        language="pt-BR",
        use_container_width=True,
        just_once=True,
        key="STT",
    )
if state.get("STT",False):
    state.text = state["STT_output"]
    state.audio = state.STT["audio_base64"]

if state.get("audio", False):
    audio_data = base64.b64decode(state.audio)
    st.audio(audio_data, format="audio/wav")

state["text_input"] = st.text_input("Caso seja necessário, corrigir ou alterar a transcrição:", value=state.text)


if state.text_input:

    dados = query(state.text_input)

    resultado_agrupado = agrupar_entidades_adjacentes(dados)
    texto_original = state.text_input

    # Aplicar agrupamento na string
    saida = aplicar_agrupamento_na_string(resultado_agrupado, texto_original)

    # Exibir resultado
    st.markdown('### Resultado da Análise:')
    annotated_text(saida)