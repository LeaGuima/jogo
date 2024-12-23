 j o g o 
 // _O Jogo da Forca é um projeto desenvolvido em Python com o objetivo de recriar um dos jogos mais populares e simples, mas com uma abordagem que prioriza a organização e boas práticas de programação. O jogo oferece uma experiência interativa para o jogador, que precisa adivinhar uma palavra oculta, uma letra por vez, dentro de um número limitado de tentativas._

//#Funcionalidades do Projeto 
_Escolha Aleatória de Palavras 
O jogo inicia escolhendo automaticamente uma palavra de uma lista pré-definida. Essa seleção aleatória garante que cada partida seja diferente, proporcionando uma experiência variada para o jogador._

//#Interação com o Jogador
_O jogador interage diretamente com o jogo, inserindo palpites no formato de letras. O programa informa se a letra faz parte da palavra oculta ou não. Além disso, após quatro tentativas (certas ou erradas), o jogador pode tentar adivinhar a palavra inteira, oferecendo uma dinâmica adicional e mais opções para resolver o desafio._

//#Controle de Tentativas
_O jogador tem um limite inicial de seis tentativas. Cada erro resulta na redução desse número, e o jogo termina quando as tentativas se esgotam. Esse controle adiciona um elemento de tensão e estratégia, incentivando o jogador a pensar bem antes de fazer um palpite._

//#Feedback em Tempo Real
*Durante o jogo, o programa mantém o jogador informado sobre o progresso. Ele exibe:*

//#As letras corretas já descobertas.
*As letras erradas que foram tentadas.
A palavra oculta, com os espaços ainda não revelados destacados.
Além disso, mensagens claras indicam se o palpite foi válido, correto ou incorreto.
Finalização do Jogo
O jogo termina de duas formas possíveis:*

//#Vitória: o jogador descobre todas as letras da palavra ou adivinha a palavra inteira corretamente.
#Derrota: o jogador esgota todas as tentativas sem descobrir a palavra.
#Estrutura e Etapas de Desenvolvimento
//*Planejamento e Design
A primeira etapa foi definir a lógica principal do jogo e identificar as funcionalidades desejadas, como escolha aleatória de palavras, controle de tentativas e feedback para o jogador.*

//#Divisão do Código
_Para garantir um código organizado e reutilizável, o projeto foi dividido em dois arquivos:_

//#jogo_da_forca.py: Contém as funções responsáveis pela lógica do jogo, como a escolha da palavra e o processamento dos palpites do jogador.
*main.py: Gerencia o loop principal do jogo, lida com a interação do jogador e utiliza as funções do arquivo anterior.
Desenvolvimento do Código
Cada parte do código foi escrita para cumprir uma responsabilidade específica. Por exemplo:*

//#A função escolher_palavra é responsável por selecionar a palavra aleatória.
_A função processar_palpite lida com as regras de validação do palpite e atualiza o estado do jogo.
Testes e Ajustes
O jogo foi testado extensivamente para garantir que:_

//#Letras e palavras fossem validadas corretamente.
*O jogador recebesse feedback claro em todas as etapas.
A funcionalidade de adivinhar a palavra inteira após quatro tentativas funcionasse sem erros.
//Melhoria da Experiência do Jogador
Foram adicionadas mensagens informativas e ajustes na interface do jogo para tornar a experiência mais amigável e intuitiva.*

Conclusão
Este projeto não só recria o clássico Jogo da Forca, mas também demonstra a importância de uma abordagem estruturada no desenvolvimento de software. Com a separação do código em módulos e foco na organização, o projeto é fácil de manter e expandir, permitindo adicionar futuras melhorias, como carregar palavras de um arquivo externo ou criar um modo de dificuldade.
 
