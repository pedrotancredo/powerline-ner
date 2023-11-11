import streamlit as st
import pandas as pd
import json
import altair as alt

@st.cache_data
def load_data(uploaded_file):
    if uploaded_file is not None:
        try:
            json_content = json.load(uploaded_file)

        except json.JSONDecodeError:
            st.error('Arquivo JSON inválido')
            return None
        return json_content

uploaded_file = st.file_uploader(
    'Carregar arquivo de exportação JSON do Label Studio', type=['json'])


json_content = load_data(uploaded_file)

if json_content is None:
    st.stop()

# data_label = [item['label'] for item in json_content if 'label' in item.keys()]
data_label = [item['label'] for item in json_content if 'label' in item.keys()]
# st.write(data_label)


# labels_list = [label_item["labels"][0] for item in json_content for label_item in item.get(
#     "label", []) if label_item.get("labels")]

label_text_list = [(label_item["labels"][0], label_item["text"]) for item in json_content for label_item in item.get("label", []) if label_item.get("labels")]
# individual_label = [item['labels'] for item in data_label if 'labels' in item.keys()]
# st.write(labels_list)

# label_frequency = {label: labels_list.count(label) for label in set(labels_list)}
# label_frequency = {label: label_text_list.count((label, text)) for label, text in label_text_list}

labels_list = [label_item["labels"][0] for item in json_content for label_item in item.get("label", []) if label_item.get("labels")]
label_frequency = {label: labels_list.count(label) for label in set(labels_list)}

st.title("Histograma dos rótulos")
st.bar_chart(label_frequency)

# st.write(label_text_list)

st.title("Histograma dos textos associados")

# Selectbox to filter by label
selected_label = st.selectbox("Escolha um rótulo:", list(set(labels_list)),)

# Filter the label_text_list based on selected label
filtered_label_text_list = [(label, text) for label, text in label_text_list if label == selected_label]

# Filter the label_text_list based on selected label
filtered_texts = [text for label, text in label_text_list if label == selected_label]

# Sort the words alphabetically and join them into a single string
sorted_and_joined_text = ','.join(sorted(filtered_texts))
# Display the sorted and joined text
# st.write("Associated Texts (Alphabetically Sorted):")
# st.write(sorted_and_joined_text)

# Display the sorted and joined text
# st.write(sorted_and_joined_text)

# Calculate word frequency by counting occurrences in filtered_texts
word_frequency = {text: filtered_texts.count(text) for text in filtered_texts}
word_frequency_df = pd.DataFrame(word_frequency.items(), columns=['Texto', 'Frequência'])
#Max lengh Texto
max_len = 140*word_frequency_df['Texto'].str.len().max()
max_height = max_len if max_len < 30000 else 30000
label_lim = 5*max_len
st.write(max_height)
# Create an Altair bar chart
chart = alt.Chart(word_frequency_df).mark_bar().encode(
    x='Frequência:Q',
    y=alt.Y('Texto:O', sort='-x', axis=alt.Axis(labelLimit=250)),
    color=alt.value('steelblue')
).properties(
    width=600,
    height=max_height
)

# Display the Altair chart using Streamlit
st.altair_chart(chart, use_container_width=True)
