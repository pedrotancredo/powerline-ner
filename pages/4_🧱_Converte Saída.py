import json
import streamlit as st
from utils.labelstudio2iob import labelstudio2iob

st.markdown("# Converte Saída:")
st.markdown(
    """Converte a saída do Label Studio para o formato IOB utilizado para treinamento
    do modelo:"""
)

annotations_file = st.file_uploader("Carregar arquivo de anotação", type=["json"])

if annotations_file is not None:
    data = json.load(annotations_file)
    df = labelstudio2iob(data)

    st.dataframe(df)

    # download button to download dataframe as csv using streamlit
    st.download_button(
        "Press to Download",
        df.to_csv(sep="\t").encode("utf-8"),
        "file.csv",
        "text/csv",
        key="download-csv",
    )
