# portscan

### Nome: Pedro Vaz de Moraes Pertusi 

### Semestre: 6º

### Curso: Ciência da Computação

### Matéria: Cibersegurança

## Descrição

Este é um projeto de escaneamento de portas desenvolvido como parte do Desafio 5 (APS) do curso de Ciência da Computação. A aplicação permite escanear portas de comunicação em um host especificado, verificando se elas estão abertas ou fechadas, e também fornece uma breve descrição do serviço associado para portas conhecidas.

## Como Usar

### Requisitos

- Python 3.x
- Módulos padrão do Python (`socket`, `tkinter`)

### Instruções

1. **Clone o repositório ou baixe os arquivos do projeto.**
2. **Execute o arquivo principal do programa.**

``` python port_scan.py```

### Interface Gráfica:

Host: Insira o endereço do host que deseja escanear.

Range de Portas: Insira um intervalo de portas (por exemplo, 20-80) ou uma única porta (80).

Clique em "Começar Scan" para iniciar o escaneamento.

Resultados:
A saída mostrará o status de cada porta (aberta ou fechada) e o serviço associado (se conhecido) ou "Serviço desconhecido".

## Estrutura do Projeto

`port_scan.py`: Código principal da aplicação que inclui a lógica de escaneamento de portas e a interface gráfica com Tkinter.

`common-ports.txt`: Arquivo contendo as portas conhecidas e os serviços associados, que é lido pelo programa para fornecer informações adicionais.


### Enunciado do Desafio 5 (APS)
Criação de Escaneamento de Portas com Python.

Descrição: Desenvolvimento de uma aplicação que realize o escaneamento de portas de comunicação de um destino por meio de bibliotecas de desenvolvimento da Linguagem de programação Python.

Você deverá realizar uma pesquisa dos módulos e bibliotecas que permitem o desenvolvimento de uma ferramenta para o escaneamento de portas TCP de acordo com as premissas a seguir:

- Ser em linguagem Python;
- Deverá possuir uma interface amigável e de fácil utilização (user-friendly interface); (1 ponto)
- Permitir o escaneamento de um host ou uma rede; (1 ponto)
- Permitir inserir o range (intervalo) de portas a serem escaneadas; (1 ponto)
- Além da função de escaneamento, espera-se que seu código relacione as portas Well-Known Ports e seus serviços, e apresente em sua saída (imprimir) o número da porta e o nome do serviço associado. (2 pontos)
- Existem diversos projetos e documentações relacionados com esta atividade. Aproveite para analisar os códigos já desenvolvidos para teu projeto.
