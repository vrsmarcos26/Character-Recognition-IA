# Real-Time Object Detection and People Counting with YOLOv8

Este projeto é um laboratório prático de Visão Computacional que utiliza o modelo **YOLOv8** para detecção de objetos em tempo real. A atividade explora desde a inferência básica em imagens e vídeos até a implementação de um sistema inteligente para contar pessoas que cruzam linhas virtuais pré-definidas em um vídeo.

Foram utilizadas as bibliotecas `ultralytics` para a execução do modelo YOLOv8 e `supervision` para o processamento e anotação dos resultados.

## 🎥 Demonstração Final: Contador de Pessoas

O principal resultado do projeto é um sistema que processa um vídeo, detecta todas as pessoas em cada quadro e conta quantas cruzam duas linhas virtuais, registrando as entradas e saídas.

![Resultado do Contador de Pessoas com YOLOv8](https://i.imgur.com/gKj3O5H.gif)

## 🧠 Conceitos Aplicados

### 1. YOLOv8 (You Only Look Once)
YOLOv8 é um modelo de detecção de objetos de última geração, conhecido por seu alto desempenho que equilibra velocidade e precisão. Ele é capaz de identificar e localizar múltiplos objetos em uma imagem ou vídeo em uma única passagem, tornando-o ideal para aplicações em tempo real. A biblioteca `ultralytics` é a ferramenta oficial para utilizar o YOLOv8.

### 2. Supervision
`supervision` é uma biblioteca Python que oferece um conjunto de utilitários para acelerar o desenvolvimento de projetos de Visão Computacional. Neste projeto, ela foi essencial para:
-   **Anotar os frames**: Desenhar caixas delimitadoras (bounding boxes) e rótulos sobre os objetos detectados.
-   **Implementar a lógica de contagem**: Utilizar a funcionalidade `sv.LineZone` para criar "linhas-gatilho" e `sv.LineZoneAnnotator` para visualizar as linhas e a contagem de cruzamentos.

## 🛠️ Funcionalidades Implementadas

O projeto foi desenvolvido em etapas, adicionando complexidade a cada passo:

1.  **Detecção em Imagens**: Execução inicial do modelo YOLOv8 em imagens estáticas (`zidane.jpg` e `people.jpg`) para identificar objetos diversos.
2.  **Detecção em Vídeo**: Aplicação do modelo em um arquivo de vídeo (`video.mp4`), processando-o quadro a quadro para detecção contínua.
3.  **Filtragem de Classes**: Modificação do código para detectar e rastrear apenas objetos de uma classe específica. Neste caso, a classe **'pessoa' (ID 0)** foi isolada para a tarefa de contagem.
4.  **Sistema de Contagem por Linha**: Implementação de duas linhas virtuais na cena do vídeo. O sistema incrementa um contador sempre que o centro de uma caixa delimitadora de uma 'pessoa' cruza uma dessas linhas.

## 🚀 Como Executar o Projeto

Este projeto foi projetado para ser executado no **Google Colab**.

### Passo 1: Configurar o Ambiente
Execute a primeira célula do notebook `yolo_people_counter.ipynb` para instalar as bibliotecas `ultralytics` e `supervision`:
```bash
!pip install ultralytics supervision
```

### Passo 2: Baixar os Arquivos de Teste
Execute as células que contêm os comandos `!wget` para baixar a imagem de teste (`zidane.jpg`), a imagem de pessoas (`people.jpg`) e o vídeo (`video.mp4`) para o ambiente do Colab.

### Passo 3: Executar a Análise
Execute todas as células do notebook em sequência.
-   As primeiras células realizarão a detecção nas imagens.
-   A última célula executará o processo completo de análise de vídeo e contagem de pessoas, gerando um arquivo de saída chamado **`people_counting.mp4`** no ambiente do Colab.

Você pode então baixar o vídeo `people_counting.mp4` para visualizar o resultado final.

## Licença

Este projeto está sob a licença MIT.
