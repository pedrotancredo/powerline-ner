import streamlit as st
from PIL import Image
import streamlit as st

# Set config to expanded sidebar
st.set_page_config(initial_sidebar_state="expanded")


image = Image.open("images/banner.png")
st.image(image, use_column_width=True)


st.header(
    "Modelo para reconhecimento de entidades nomeadas (NER) em transcrições de audios de inspeção aérea de linhas de transmissão"
)
st.markdown(
    '<div align="right">Pedro Henrique Tancredo Campos</div>', unsafe_allow_html=True
)

tabs = st.tabs(["Introdução", "Dataset", "Modelo"])

with tabs[0]:
    st.subheader("Inspeção Aérea de Linhas de Transmissão")
    st.markdown(
        """<div align="justify"><p>A infraestrutura elétrica é a espinha dorsal
        de qualquer sociedade moderna, impulsionando o desenvolvimento e
        sustentando o modo de vida contemporâneo. No cerne dessa infraestrutura,
        as linhas de transmissão de energia desempenham um papel crucial,
        transportando eletricidade de usinas geradoras para comunidades e empresas.
        Para garantir a confiabilidade e a eficiência dessas linhas, a inspeção
        aérea emerge como uma prática essencial.</p></div>""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """<div align="justify">
        <p>A inspeção aérea de linhas de transmissão envolve o uso de aeronaves
        especializadas equipadas com tecnologias capazes de avaliar a condição
        física e operacional das estruturas. Esta abordagem oferece vantagens
        significativas em comparação com métodos terrestres, permitindo uma
        análise abrangente e eficiente em grandes extensões de território.</p>
        <p>Um dos benefícios fundamentais da inspeção aérea é a capacidade de
        identificar de forma rápida e precisa qualquer anomalia ou desgaste nas
        estruturas das linhas de transmissão. Os helicópteros equipados com
        câmeras de alta resolução e sensores específicos podem detectar sinais
        de corrosão, danos mecânicos ou outros problemas que podem comprometer
        a integridade da linha.</p>
        <p>Além disso, a inspeção aérea facilita a identificação precoce de
        vegetação excessiva nas proximidades das linhas. A vegetação nãogerenciada
        pode representar riscos substanciais, incluindo interrupções no fornecimento
        de energia. Com a capacidade de sobrevoar grandes áreas rapidamente, a
        inspeção aérea permite a pronta detecção e mitigação desses riscos
        ambientais.</p>
        <p>A rapidez na identificação e resolução de problemas é crucial para
        garantir a confiabilidade operacional das linhas de transmissão. A inspeção
        aérea, ao fornecer uma visão panorâmica e detalhada, acelera o processo
        de manutenção, reduzindo significativamente o tempo de inatividade e os
        custos associados.</p></div>""",
        unsafe_allow_html=True,
    )

    st.subheader("Instrumentalização")

    st.markdown(
        """<div align="justify"><p>Como uma evolução dos métodos tradicionais de
        inspeção aérea, a instrumentalização, utilizando câmeras e áudio,
        representou um avanço significativo na manutenção e monitoramento dessa
        infraestrutura. Ao incorporar tecnologias audiovisuais, esta abordagem
        não apenas proporcionou uma análise visual detalhada, mas também ofereceu
        informações auditivas valiosas que podem ser exploradas de maneiras
        inovadoras.</p></div>""",
        unsafe_allow_html=True,
    )
    st.markdown(
        """<div align="justify"><p>O uso de câmeras de alta resolução montadas
        em drones ou helicópteros permite a captura de registros em vídeo
        durante a inspeção. Essas imagens não apenas fornecem uma visão clara
        e detalhada do estado físico das linhas, mas também possibilitam uma
        revisão mais minuciosa posteriormente. A análise de vídeos pode revelar
        nuances que podem escapar à observação instantânea, facilitando a
        identificação de desgastes, danos ou potenciais pontos de falha.</p>
        <p>A verdadeira inovação surge quando exploramos o potencial da transcrição
        automática do áudio. Ao converter os registros de áudio em texto, obtemos
        um recurso adicional para a análise e documentação. Essa transcrição não
        apenas facilita a catalogação e indexação eficientes das inspeções, mas
        também permite a aplicação de técnicas de processamento de linguagem
        natural para identificar padrões e tendências ao longo do tempo.</p>
        <p>Ao combinar dados visuais e auditivos, as empresas de energia podem
        desenvolver estratégias mais abrangentes de manutenção preditiva. A
        análise conjunta de imagens e transcrições permite uma compreensão mais
        holística da saúde das linhas de transmissão, capacitando as equipes de
        manutenção a antecipar problemas potenciais e agir proativamente. Em
        última análise, a inspeção instrumentalizada, incorporando elementos
        visuais e auditivos, não apenas eleva a eficiência da manutenção de
        linhas de transmissão, mas também abre portas para a implementação de
        soluções inovadoras e inteligentes, fundamentadas na análise integrada
        de dados multimodais.</p></div>""",
        unsafe_allow_html=True,
    )
with tabs[1]:
    st.subheader("Dataset")
    st.markdown(
        """<div align="justify"><p>Durante as missões instrumentalizadas para a
        inspeção aérea das linhas de transmissão, foram produzidas aproximadamente
        1500 horas de vídeos georreferenciados que abrangem o registro completo
        das inspeções realizadas pela Eletrobras Furnas de 2019 a 2021. Nessas
        missões, além do registro em vídeo, há a opção de utilizar a funcionalidade
        push-to-talk para adicionar áudio às gravações. Devido a essa abordagem
        ativa, existe a garantia de que os áudios contêm informações valiosas
        sobre as situações observadas durante as inspeções. Ao longo desses três
        anos de inspeção, foram gravadas cerca de 30 horas de áudio, abrangendo
        mais de 30.000 sentenças.</p>
        <p>O conjunto de dados utilizado para o Reconhecimento de Entidades
        Nomeadas (NER) é composto pelas transcrições destas senteças nas quais
        os mais de 20 inspetores, de diferentes estados do país, relatam as anomalias
        identificadas. Com base na análise de diversos exemplos dessas transcrições,
        foram definidas as seguintes categorias:</p></div>""",
        unsafe_allow_html=True,
    )
    st.markdown(
        """<div align="justify"><p>
        <li><b>Componente</b>: Partes que compõem a estrutura da linha de transmissão.
        <ul><b>Exemplos:</b> Isolador, Espaçador, Esfera, Cone, Amortecedor,
        Faixa de Servidão</ul></li>
        <li><b>Anomalia</b>: Possíveis defeitos ou anomalias que podem ser
        identificados durante a inspeção aérea.
        <ul><b>Exemplos:</b> Quebrado, Caído, Ninho, Frouxo</ul></li>
        <li><b>Posição</b>: Posição relativa das anomalias em relação à estrutura da
        linha de transmissão.
        <ul><b>Exemplos:</b> Ré, Vante, Fase Central, Fase Superior, Mísula</ul></li>
        <li><b>Linha de Transmissão</b>: Nome específico da linha de transmissão
        sob inspeção.
        <ul><b>Exemplos:</b> Furnas - Pimenta, Campos - Rio Novo do Sul 1</ul></li>
        <li><b>Evento</b>: Eventos específicos relacionados à inspeção.
        <ul><b>Exemplos:</b>Inspeção Detalhada</ul></li>
        <li><b>Localização</b>: Localização exata das entidades identificadas.
        <ul><b>Exemplos:</b> Torre 247, Torre 123, Vão 210, Vão 109</ul></li>
        </p></div>""",
        unsafe_allow_html=True,
    )

    st.markdown("#### Exemplos de Transcrições:")

    st.markdown(
        """|   #   |                              Transcrição                              |                        Audio                       | 
| :---: | :-------------------------------------------------------------------: | :---------------------------------------------------:  | 
|   1   |                264 cordoalha, lateral direita rompido.                | <audio controls><source src="https://polis.azureedge.net/mp4/examples/ex1.wav" type="audio/wav"></audio> | 
|   2   |                Torre 886, brotos de eucalipto no vão.                 | <audio controls><source src="https://polis.azureedge.net/mp4/examples/ex2.wav" type="audio/wav"></audio> | 
|   3   |                   Esfera aberta. Vão da torre 575.                    | <audio controls><source src="https://polis.azureedge.net/mp4/examples/ex3.wav" type="audio/wav"></audio> | 
|   4   |     Torre 009 da linha Rio Verde Rondonópolis, hortaliças no vão.     | <audio controls><source src="https://polis.azureedge.net/mp4/examples/ex4.wav" type="audio/wav"></audio> | 
|   5   |             Torre 403, ninho de pássaro da fase central.              | <audio controls><source src="https://polis.azureedge.net/mp4/examples/ex5.wav" type="audio/wav"></audio> | 
|   6   |              Fundação da torre 173, Furnas, pimenta um.               | <audio controls><source src="https://polis.azureedge.net/mp4/examples/ex6.wav" type="audio/wav"></audio> | 
|   7   | Invasão não vão da torre 225, muro de alvenaria faz lateral esquerda. | <audio controls><source src="https://polis.azureedge.net/mp4/examples/ex7.wav" type="audio/wav"></audio> | 
|   8   | Torre 32 para 33, faltando uma esfera de sinalização de um para raio. | <audio controls><source src="https://polis.azureedge.net/mp4/examples/ex8.wav" type="audio/wav"></audio> """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """<div align="justify"><p></p><p>É importante destacar que o conjunto de dados
        foi gerado a partir das transcrições automáticas dos áudios de inspeções
        aéreas sem a imposição de orientações específicas para os inspetores.
        Dessa forma, o conjunto de dados incorpora uma variedade de desafios
        decorrentes da abordagem diversificada de cada inspetor ao relatar as
        anomalias observadas. Este aspecto introduz diferentes nuances na maneira
        como as inspeções são documentadas e apresenta desafios valiosos para o
        desenvolvimento do modelo de Reconhecimento de Entidades Nomeadas (NER).</p>
        <p><b>Diversidade nas Descrições:</b> A diversidade nas descrições das
        anomalias é uma característica fundamental do conjunto de dados. Cada
        inspetor tem sua própria abordagem ao relatar, resultando em uma gama
        abrangente de expressões e terminologias.</p>
        <p><b>Desafios de Consistência:</b> A ausência de orientações prévias
        para os inspetores pode gerar inconsistências nas transcrições. Essas
        inconsistências são valiosas para entender como diferentes abordagens
        impactam a qualidade e uniformidade das informações registradas.</p>
        <p>Espera-se que, ao analisar o conjunto de dados sob essa perspectiva
        diversificada, seja possível estabelecer diretrizes específicas e melhores
        práticas para a padronização e aprimoramento do processo de transcrição.
        A compreensão dessas nuances não apenas contribuirá para a melhoria contínua
        do conjunto de dados, mas também fortalecerá a robustez do modelo de NER
        em lidar com a variabilidade natural das inspeções aéreas.</p></div>""",
        unsafe_allow_html=True,
    )
with tabs[2]:
    st.subheader("Modelo")
    st.markdown(
        """<div align="justify"><p>O Reconhecimento de Entidade Nomeada
         (Named Entity Recognition - NER) refere-se à identificação de entidades
         com categorias específicas (geralmente substantivos) do texto, como
         nomes de pessoas, nomes de lugares, nomes de organizações, etc. O
         reconhecimento de entidades nomeadas é uma tarefa básica de recuperação
         de informações, classificação de consulta, pergunta e resposta, etc.
         Seu efeito afeta diretamente o processamento subsequente, por isso é um
         problema recorrente de pesquisa em processamento de linguagem natural.
         </p></div>""",
        unsafe_allow_html=True,
    )
