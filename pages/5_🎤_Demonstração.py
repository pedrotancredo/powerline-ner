import streamlit as st
from streamlit_mic_recorder import mic_recorder, speech_to_text
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline


@st.cache_data
def load_model():
    model_name = "recursos/base_m3/"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForTokenClassification.from_pretrained(
        model_name, use_safetensors=True
    )
    pipe = pipeline(
        task="token-classification",
        model=model.to("cpu"),
        tokenizer=tokenizer,
        aggregation_strategy="simple",
    )

    return pipe


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


# pipe("inspeção detalhada na torre 37 da ibntpr1, isolador quebrado na fase lateral esquerda")
teste = load_model()

state = st.session_state

st.write("Texto descritivo sobre como utilizar a ferramenta")

if "text_received" not in state:
    state.text_received = []

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
# st.write(text)
if text:
    state.text_received = text
    # state.text_received.append(text)

    # for text in state.text_received:
    # st.write(text)

    # st.button("Clear", on_click=lambda: state.clear())

    # dados = teste("inspeção detalhada não sei o quê torre 233 isolador quebrado na fase lateral esquerda")
    dados = teste(text)

    resultado_agrupado = agrupar_entidades_adjacentes(dados)
    texto_original = text

    # Aplicar agrupamento na string
    saida = aplicar_agrupamento_na_string(resultado_agrupado, texto_original)

    # Exibir resultado
    print(saida)
    from annotated_text import annotated_text, annotation

    annotated_text(saida)
    # annotation(saida)


# st.write()
# st.write("Record your voice, and play the recorded audio:")
# audio=mic_recorder(start_prompt="⏺️",stop_prompt="⏹️",key='recorder')

# if audio:
#     st.audio(audio['bytes'])
