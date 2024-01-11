<!-- antes de enviar a versão final, solicitamos que todos os comentários, colocados para orientação ao aluno, sejam removidos do arquivo -->
# Modelo para reconhecimento de entidades nomeadas (NER) em transcrições de audios de inspeção aérea de linhas de transmissão

#### Aluno: [Pedro Henrique Tancredo Campos](https://github.com/pedrotancredo)
#### Orientadora:  [Evelyn Batista](https://github.com/evysb)
---

Trabalho apresentado ao curso [BI MASTER](https://ica.puc-rio.ai/bi-master) como pré-requisito para conclusão de curso e obtenção de crédito na disciplina "Projetos de Sistemas Inteligentes de Apoio à Decisão".

<!-- para os links a seguir, caso os arquivos estejam no mesmo repositório que este README, não há necessidade de incluir o link completo: basta incluir o nome do arquivo, com extensão, que o GitHub completa o link corretamente -->
- [Link para o código](https://github.com/pedrotancredo/powerline-ner). <!-- caso não aplicável, remover esta linha -->

- [Link para a monografia](https://powerlines.streamlit.app/). <!-- caso não aplicável, remover esta linha -->

<!-- - Trabalhos relacionados: caso não aplicável, remover estas linhas
    - [Nome do Trabalho 1](https://link_do_trabalho.com).
    - [Nome do Trabalho 2](https://link_do_trabalho.com).
-->
---

### Resumo

<!-- trocar o texto abaixo pelo resumo do trabalho, em português -->

Este artigo apresenta um modelo de Reconhecimento de Entidades Nomeadas (NER) aplicado à inspeção aérea de linhas de transmissão. Ao analisar transcrições automáticas de áudios provenientes dessas inspeções, o NER categoriza entidades como Componente, Anomalia e Posição, enriquecendo significativamente o conjunto de dados. Destaca-se a capacidade do NER em proporcionar uma análise integrada, oferecendo bases sólidas para estratégias avançadas de manutenção preditiva. Além disso, este estudo ressalta a perspectiva de aprimoramento do modelo através da integração de seus resultados com os modelos já em desenvolvimento de análise das imagens da inspeção, bem como as informações geográficas das linhas, potencialmente complementando e expandindo suas capacidades analíticas. A diversidade nas descrições e os desafios de consistência introduzidos pelos diferentes inspetores fortalecem o modelo, contribuindo para diretrizes de padronização e preparando-o para evoluções tecnológicas que visem uma análise ainda mais abrangente nas inspeções aéreas.

### Abstract <!-- Opcional! Caso não aplicável, remover esta seção -->

<!-- trocar o texto abaixo pelo resumo do trabalho, em inglês -->

This article introduces a Named Entity Recognition (NER) model applied to aerial inspection of transmission lines. By analyzing automatic transcriptions of audio recordings from these inspections, the NER categorizes entities such as Component, Anomaly, and Position, significantly enriching the dataset. The NER's capability to provide an integrated analysis is emphasized, laying a solid foundation for advanced predictive maintenance strategies. Furthermore, this study highlights the prospect of enhancing the model by integrating its results with ongoing image analysis models of inspections, as well as geographical information about the lines. This potential integration aims to complement and expand the analytical capabilities of the NER. The diversity in descriptions and consistency challenges introduced by various inspectors strengthen the model, contributing to standardization guidelines and preparing it for technological advancements aimed at even more comprehensive analysis in aerial inspections.

### 1. Introdução

#### 1.1. Inspeção Aérea de Linhas de Transmissão

A infraestrutura elétrica é a espinha dorsal de qualquer sociedade moderna, impulsionando o desenvolvimento e sustentando o modo de vida contemporâneo. No cerne dessa infraestrutura, as linhas de transmissão de energia desempenham um papel crucial, transportando eletricidade de usinas geradoras para comunidades e empresas. Para garantir a confiabilidade e a eficiência dessas linhas, a inspeção aérea emerge como uma prática essencial.

A inspeção aérea de linhas de transmissão envolve o uso de aeronaves especializadas equipadas com tecnologias capazes de avaliar a condição física e operacional das estruturas. Esta abordagem oferece vantagens significativas em comparação com métodos terrestres, permitindo uma análise abrangente e eficiente em grandes extensões de território.

Um dos benefícios fundamentais da inspeção aérea é a capacidade de identificar de forma rápida e precisa qualquer anomalia ou desgaste nas estruturas das linhas de transmissão. Os helicópteros equipados com câmeras de alta resolução e sensores específicos podem detectar sinais de corrosão, danos mecânicos ou outros problemas que podem comprometer a integridade da linha.

Além disso, a inspeção aérea facilita a identificação precoce de vegetação excessiva nas proximidades das linhas. A vegetação nãogerenciada pode representar riscos substanciais, incluindo interrupções no fornecimento de energia. Com a capacidade de sobrevoar grandes áreas rapidamente, a inspeção aérea permite a pronta detecção e mitigação desses riscos ambientais.

A rapidez na identificação e resolução de problemas é crucial para garantir a confiabilidade operacional das linhas de transmissão. A inspeção aérea, ao fornecer uma visão panorâmica e detalhada, acelera o processo de manutenção, reduzindo significativamente o tempo de inatividade e os custos associados.

#### 1.2. Instrumentalização

Como uma evolução dos métodos tradicionais de inspeção aérea, a instrumentalização, utilizando câmeras e áudio, representou um avanço significativo na manutenção e monitoramento dessa infraestrutura. Ao incorporar tecnologias audiovisuais, esta abordagem não apenas proporcionou uma análise visual detalhada, mas também ofereceu informações auditivas valiosas que podem ser exploradas de maneiras inovadoras.

O uso de câmeras de alta resolução montadas em drones ou helicópteros permite a captura de registros em vídeo durante a inspeção. Essas imagens não apenas fornecem uma visão clara e detalhada do estado físico das linhas, mas também possibilitam uma revisão mais minuciosa posteriormente. A análise de vídeos pode revelar nuances que podem escapar à observação instantânea, facilitando a identificação de desgastes, danos ou potenciais pontos de falha.

A verdadeira inovação surge quando exploramos o potencial da transcrição automática do áudio. Ao converter os registros de áudio em texto, obtemos um recurso adicional para a análise e documentação. Essa transcrição não apenas facilita a catalogação e indexação eficientes das inspeções, mas também permite a aplicação de técnicas de processamento de linguagem natural para identificar padrões e tendências ao longo do tempo.

Ao combinar dados visuais e auditivos, as empresas de energia podem desenvolver estratégias mais abrangentes de manutenção preditiva. A análise conjunta de imagens e transcrições permite uma compreensão mais holística da saúde das linhas de transmissão, capacitando as equipes de manutenção a antecipar problemas potenciais e agir proativamente. Em última análise, a inspeção instrumentalizada, incorporando elementos visuais e auditivos, não apenas eleva a eficiência da manutenção de linhas de transmissão, mas também abre portas para a implementação de soluções inovadoras e inteligentes, fundamentadas na análise integrada de dados multimodais.

### 2. Modelagem

#### 2.1. Dataset

O modelo foi treinado através do fine-tuning do modelo [BERTimbau Base](https://huggingface.co/neuralmind/bert-base-portuguese-cased) que consiste em um modelo BERT pré-treinado na língua portuguesa 

O conjunto de dados utilizado para o NER constitui-se das transcrições dos audios das inspeções aéreas de linhas de transmissão onde os inspetores relatam as anomalias encontradas. Com base na observação de diversos exemplos destas transcrições, foram definidas as seguintes classes:

Componente: Partes que compõem a estrutura da linha de transmissão.

    Isolador, Espaçador, Esfera, Cone, Amortecedor, Faixa de Servidão

Anomalia: Possíveis defeitos ou anomalias que podem ser identificados durante a inspeção aérea.

    Quebrado, Caído, Ninho, Frouxo

Posição: Posição relativa das anomalias em relação à estrutura da linha de transmissão.

    Exemplos: Ré, Vante, Fase Central, Fase Superior, Mísula

Linha de Transmissão: Nome específico da linha de transmissão sob inspeção.

    Exemplos: Furnas - Pimenta, Campos - Rio Novo do Sul 1

Evento: Eventos específicos relacionados à inspeção.

    Exemplos:Inspeção Detalhada

Localização: Localização exata das entidades identificadas.

    Exemplos: Torre 247, Torre 123, Vão 210, Vão 109

As transcrições contaram com um modelo customizado construído a partir de ferramentas do serviço [Azure AI Speech](https://azure.microsoft.com/en-us/products/ai-services/ai-speech)

A seguir alguns exemplos do tipo de audio produzido pelo sistema:

| # | Transcrição | Download |
| :-: | :-: | :-: |
| 1 | 264 cordoalha, lateral direita rompido. | <audio controls><source src="https://polis.azureedge.net/mp4/examples/ex1.wav" type="audio/wav"></audio> 
| 2 | Torre 886, brotos de eucalipto no vão. | <audio controls><source src="https://polis.azureedge.net/mp4/examples/ex2.wav" type="audio/wav"></audio> 
| 3 | Esfera aberta. Vão da torre 575. | <audio controls><source src="https://polis.azureedge.net/mp4/examples/ex3.wav" type="audio/wav"></audio> 
| 4 | Torre 009 da linha Rio Verde Rondonópolis, hortaliças no vão. | <audio controls><source src="https://polis.azureedge.net/mp4/examples/ex4.wav" type="audio/wav"></audio> 
| 5 | Torre 403, ninho de pássaro da fase central. | <audio controls><source src="https://polis.azureedge.net/mp4/examples/ex5.wav" type="audio/wav"></audio> 
| 6 | Fundação da torre 173, Furnas, pimenta um. | <audio controls><source src="https://polis.azureedge.net/mp4/examples/ex6.wav" type="audio/wav"></audio> 
| 7 | Invasão não vão da torre 225, muro de alvenaria faz lateral esquerda. | <audio controls><source src="https://polis.azureedge.net/mp4/examples/ex7.wav" type="audio/wav"></audio> 
| 8 | Torre 32 para 33, faltando uma esfera de sinalização de um para raio. | <audio controls><source src="https://polis.azureedge.net/mp4/examples/ex8.wav" type="audio/wav"></audio> 



#### 2.2. Treinamento

Para o treinamento utilizou-se 2.206 setenças totalizando mais de 20.000 palavras
anotadas manualmente com auxílio da ferramenta [Label Studio](https://labelstud.io/), no entanto, embora a utilização dessa ferramenta gere um arquivo estruturado, houve a
necessidade de se construir um conversor do arquivo de saída para que fosse 
ajustada ao formato específico necessário para o treinamento.

O esquema de anotação, utilizado na aplicação foi o [IOB-tagging](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)), que significa Inside-Outside-Beginning. Neste formato cada tag indica se a palavra correspondente está dentro, fora ou no início de uma entidade nomeada específica. A razão para isso é que entidades nomeadas podem ser formadas por mais de uma palavra.

### 3. Resultados

#### 3.1. Primeiro Treinamento

Os resultados obtidos na primeira etapa do treinamento tiveram os seguintes valores
para os hiperparâmetros

**Modelo Base:** neuralmind/bert-base-portuguese-cased
**MAX_LEN:** 32
**TRAIN_BATCH_SIZE:** 8
**VALID_BATCH_SIZE:** 8
**EPOCHS:** 6
**LEARNING_RATE:** 5e-06
**MAX_GRAD_NORM:** 10

|  | Precision | Recall | F1-Score | Support |
|:-:|:-:|:-:|:-:|:-:|
| ANOMALIA  | 0.65  | 0.83 | 0.73 | 271 |
| COMPONENTE  | 0.77 | 0.64 | 0.70 | 208 |
| EVENTO  | 0.92 | 0.99 | 0.95 | 492 |
| LINHA  | 0.64 | 0.80 | 0.71 | 217 |
| LOCALIZACAO  | 0.66  | 0.76 | 0.70 | 579 |
| POSICAO  | 0.58  | 0.67 | 0.62 | 48 |
|   |   |   |   |   |
| **Micro Avg**  | **0.73**  | **0.82** | **0.77** | **1815** |
| **Macro Avg**  | **0.70**  | **0.78** | **0.74** | **1815** |
| **Weighted Avg**  | **0.74**  | **0.82** | **0.77** | **1815** |

#### 3.2. Segundo Treinamento

E o último resultado, públicado em [Hugging-Face](https://huggingface.co/pedrotancredo/powerlines-ner) :

**Modelo Base:** neuralmind/bert-base-portuguese-cased
**MAX_LEN:** 64
**TRAIN_BATCH_SIZE:** 16
**VALID_BATCH_SIZE:** 16
**EPOCHS:** 6
**LEARNING_RATE:** 5e-05
**MAX_GRAD_NORM:** 10

|  | Precision | Recall | F1-Score | Support |
|:-:|:-:|:-:|:-:|:-:|
| ANOMALIA  | 0.77  | 0.80 | 0.79 | 361 |
| COMPONENTE  | 0.83 | 0.88 | 0.85 | 391 |
| EVENTO  | 0.97 | 1.00 | 0.98 | 664 |
| LINHA  | 0.77 | 0.79 | 0.78 | 268 |
| LOCALIZACAO  | 0.96  | 0.96 | 0.96 | 734 |
| POSICAO  | 0.83  | 0.86 | 0.85 | 133 |
|   |   |   |   |   |
| **Micro Avg**  | **0.89**  | **0.91** | **0.90** | **2551** |
| **Macro Avg**  | **0.86**  | **0.88** | **0.87** | **2551** |
| **Weighted Avg**  | **0.89**  | **0.91** | **0.90** | **2551** |

### 4. Conclusões

**TODO**
**INCLUIR COMENTÁRIO SOBRE IMPORTÂNCIA DO MODELO DE TRANSCRIÇÃO**
**INCLUIR ARQUIVOS DE AUDIO COM EXEMPLOS DO DADO**
**INCLUIR IMAGEM DO SISTEMA DE COLETA**
**INCLUIR IMAGEM DO SISTEMA DE PESQUISA POR COORDENADA?**

O avanço significativo na abordagem de manutenção preditiva e monitoramento da infraestrutura crítica das linhas de transmissão é evidenciado pelo desenvolvimento e implementação do modelo de Reconhecimento de Entidades Nomeadas (NER). É importante destacar que, devido às características intrínsecas desse tipo de missão, onde o tempo disponível para anotações estruturadas é limitado, a utilização do NER se mostra particularmente valiosa. Ao examinar automaticamente as transcrições de áudios provenientes das inspeções aéreas, o NER classifica entidades como Componente, Anomalia, Posição, Linha de Transmissão, Evento e Localização. Isso resulta em uma visão integrada e abrangente do estado operacional das linhas, contribuindo para a eficiência e confiabilidade na manutenção preditiva desse componente crítico da infraestrutura elétrica.

O treinamento do modelo, baseado no BERTimbau Base, incorporou um conjunto de dados diversificado e desafiador, capturando a variabilidade natural das descrições feitas por diferentes inspetores durante as inspeções. A aplicação do esquema de anotação IOB-tagging permitiu uma categorização precisa das entidades nomeadas, levando a resultados promissores nos indicadores de precisão, recall e F1-score.

Os resultados dos dois treinamentos realizados mostram uma evolução significativa no desempenho do modelo. A segunda iteração, contou com ajustes nos hiperparâmetros e no próprio dataset onde, através de anotações manuais, buscou-se melhorar o balancemento das categorias. Tais ajustes demonstraram melhorias notáveis em todas as categorias, evidenciando a sensibilidade do modelo a otimizações específicas.

A integração potencial dos resultados do NER com modelos de análise de imagem e informações geográficas das linhas abre perspectivas para uma análise ainda mais abrangente e inteligente. Essa sinergia permitirá estratégias de manutenção preditiva mais robustas, capacitando as equipes a antecipar e abordar proativamente potenciais problemas operacionais.

O desafio da diversidade nas descrições e a consistência variável introduzida pelos diferentes inspetores foram transformados em pontos fortes, contribuindo para a construção de diretrizes de padronização e aprimoramento contínuo do modelo. A capacidade do modelo em lidar com nuances e variações na linguagem utilizada pelos inspetores é fundamental para sua aplicabilidade em cenários do mundo real.

Em suma, o modelo de NER desenvolvido não apenas enriquece significativamente o conjunto de dados da inspeção aérea, mas também estabelece bases sólidas para a evolução contínua da análise integrada de dados multimodais. Este trabalho representa um passo crucial na direção de sistemas inteligentes de apoio à decisão na manutenção de linhas de transmissão, promovendo eficiência operacional e confiabilidade na infraestrutura elétrica essencial para o funcionamento da sociedade moderna.

---

Matrícula: 212.100.500

Pontifícia Universidade Católica do Rio de Janeiro

Curso de Pós Graduação *Business Intelligence Master*
