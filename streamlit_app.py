import streamlit as st
from PIL import Image
import streamlit as st


image = Image.open('images/banner.png')
st.image(image, use_column_width=True)


st.header('Modelo para reconhecimento de entidades nomeadas em transcrições de audios de inspeção aérea de linhas de transmissão')
st.markdown('<div align="right">Pedro Henrique Tancredo Campos</div>', unsafe_allow_html=True)

tabs = st.tabs(['Introdução', 'Modelo', 'Classes'])

with tabs[0]:
    st.subheader('Inspeção Aérea de Linhas de Transmissão')
    st.markdown('''<div align="justify"><p>A infraestrutura elétrica é a espinha dorsal de qualquer sociedade moderna, impulsionando o desenvolvimento e sustentando o modo de vida contemporâneo. No cerne dessa infraestrutura, as linhas de transmissão de energia desempenham um papel crucial, transportando eletricidade de usinas geradoras para comunidades e empresas. Para garantir a confiabilidade e a eficiência dessas linhas, a inspeção aérea emerge como uma prática essencial.</p></div>''', unsafe_allow_html=True)

    # with st.expander(label="O que é inspeção aérea de linhas de transmissão?"):
    st.markdown('''<div align="justify">
    <p>A inspeção aérea de linhas de transmissão envolve o uso de aeronaves especializadas equipadas com tecnologias capazes de avaliar a condição física e operacional das estruturas. Esta abordagem oferece vantagens significativas em comparação com métodos terrestres, permitindo uma análise abrangente e eficiente em grandes extensões de território.</p>
    <p>Um dos benefícios fundamentais da inspeção aérea é a capacidade de identificar de forma rápida e precisa qualquer anomalia ou desgaste nas estruturas das linhas de transmissão. Os helicópteros equipados com câmeras de alta resolução e sensores específicos podem detectar sinais de corrosão, danos mecânicos ou outros problemas que podem comprometer a integridade da linha.</p>
    <p>Além disso, a inspeção aérea facilita a identificação precoce de vegetação excessiva nas proximidades das linhas. A vegetação não gerenciada pode representar riscos substanciais, incluindo interrupções no fornecimento de energia. Com a capacidade de sobrevoar grandes áreas rapidamente, a inspeção aérea permite a pronta detecção e mitigação desses riscos ambientais.</p>
    <p>A rapidez na identificação e resolução de problemas é crucial para garantir a confiabilidade operacional das linhas de transmissão. A inspeção aérea, ao fornecer uma visão panorâmica e detalhada, acelera o processo de manutenção, reduzindo significativamente o tempo de inatividade e os custos associados.</p>
    </div>
    ''', unsafe_allow_html=True)

    st.subheader('Inspeção instrumentalizada')

    st.markdown('''<div align="justify"><p>Como uma evolução dos métodos tradicionais de inspeção aérea, a instrumentalização, utilizando câmeras e áudio, representou um avanço significativo na manutenção e monitoramento dessa infraestrutura. Ao incorporar tecnologias audiovisuais, esta abordagem não apenas proporcionou uma análise visual detalhada, mas também ofereceu informações auditivas valiosas que podem ser exploradas de maneiras inovadoras.</p></div>''', unsafe_allow_html=True)
    st.markdown('''<div align="justify"><p>O uso de câmeras de alta resolução montadas em drones ou helicópteros permite a captura de registros em vídeo durante a inspeção. Essas imagens não apenas fornecem uma visão clara e detalhada do estado físico das linhas, mas também possibilitam uma revisão mais minuciosa posteriormente. A análise de vídeos pode revelar nuances que podem escapar à observação instantânea, facilitando a identificação de desgastes, danos ou potenciais pontos de falha.</p>
    <p>A verdadeira inovação surge quando exploramos o potencial da transcrição automática do áudio. Ao converter os registros de áudio em texto, obtemos um recurso adicional para a análise e documentação. Essa transcrição não apenas facilita a catalogação e indexação eficientes das inspeções, mas também permite a aplicação de técnicas de processamento de linguagem natural para identificar padrões e tendências ao longo do tempo.</p>
    <p>Ao combinar dados visuais e auditivos, as empresas de energia podem desenvolver estratégias mais abrangentes de manutenção preditiva. A análise conjunta de imagens e transcrições permite uma compreensão mais holística da saúde das linhas de transmissão, capacitando as equipes de manutenção a antecipar problemas potenciais e agir proativamente.
    Em última análise, a inspeção instrumentalizada, incorporando elementos visuais e auditivos, não apenas eleva a eficiência da manutenção de linhas de transmissão, mas também abre portas para a implementação de soluções inovadoras e inteligentes, fundamentadas na análise integrada de dados multimodais.</p></div>''', unsafe_allow_html=True)

# with st.expander("A inspeção instrumentalizada em Furnas"):

with tabs[2]:
    st.subheader('Classes')
    st.markdown('''
    Pensei em dividir da seguinte forma, vou colocar uns exemplos também:

    - componente: isolador, espaçador, esfera, cone, amortecedor, faixa de servidão
    - anomalia: quebrado, caído, ninho, frouxo
    - posição: ré, vante, fase central, fase superior, mísula
    - linha de transmissão: Furnas - Pimenta, Campos - Rio Novo do Sul 1
    - subestação: Campos, Adrianópolis, Pimenta, Angra, Marimbondo
    - evento: Inspeção Detalhada
    - localização: Torre 247, Torre 123, Vão 210, Vão 109''')