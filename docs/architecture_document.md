# Documento de arquitetura

## Histórico de revisão
 Data   | Versão | Modificação  | Autor  |
| :- | :- | :- | :- |
| 10/09/2019 | 0.1 | Adição do tópico Objetivo |  Durval Carvalho |
| 10/09/2019 | 0.2 | Adição do tópico Escopo e Django REST Framework |  Durval Carvalho |
| 11/09/2019 | 0.3 | Adição do tópico Metas e Restrições arquiteturais |  Durval Carvalho |
| 12/09/2019 | 0.4 | Adição de tópico Casos de Uso | Renato Britto Araújo |
| 12/09/2019 | 0.5 | Adição do tópico MTV |  Durval Carvalho |
| 12/09/2019 | 0.6 | Adição de diagrama de pacotes back-end e informações sobre base de dados | Renato Britto Araujo | 
| 12/09/2019 | 0.7 | Adição de diagrama de pacotes front-end e referências e comentário sobre MTV | Renato Britto Araujo |

## 1. Introdução

### 1.1 Objetivo
Este documento oferece uma visão geral arquitetural do 
sitema que será implementado, permitindo assim que os 
envolvidos no projeto conheça como a aplicação será 
subdivida e quais será a função de cada componente.

Outro objetivo desse documento é elucidar quais foram as 
motivações que levaram a equipe a tomar decisões à respeito
dessa arquitetura.

### 1.2 Escopo

Esse documento aplica-se ao projeto <Nome do Projeto>, um 
sistema que será desenvolvido pelos alunos das disciplinas 
Métodos de Desenvolvimento de Software e Engenharia de 
Produto de Software, da Universidade de Brasília - Campus 
Gama.

### 1.3 Definições, Acrônimos e Abreviações

| **Sigla/Termo/Acrônimo** | **Definição** |
| ------------------------ | ------------- |
| MDS | Métodos de Desenvolvimento de <i>Software</i> | 
| EPS | Engenharia de Produto de <i>Software</i> | 
| FGA | Faculdade do Gama | 
| UnB | Universidade de Brasília | 
| DRF | Django Rest Framework |
| MTV | Model Template View |
| MVC | Model View Controller |

## 2. Representação arquitetural

### 2.1 Django REST Framework

O Django REST Framework é uma biblioteca para o Framework 
Django que disponibiliza funcionalidades para implementar 
APIs Rest de forma rápida e eficiente.

REST é a abreviação do termo <i>Representational State 
Transfer</i>, isto é, um conjunto de princípios e boas 
práticas desenvolvido pelo pesquisador Roy Fielding, que 
quando aplicados permite uma interface concisa que pode 
ser utilizado por diversas outras aplicações.

Como explicado acima o DRF é um framework do framework 
Django. Então primeiro explicaremos o motivo de termos 
escolhido Django para o back-end desse projeto.

#### 2.2.1 Django

O Django é um framework web criado com a linguagem Python, que 
utiliza o padrão model-template-view. Esse modelo MTV é basedo 
no modelo Model-View-Controler, com a diferença que as 
responsabilidades do módulo de Controller está dispersa no 
próprio Framework.

Outro motivo do uso do Django é sua robustez. O framework 
possui diversos módulos embutidos que aumenta a 
produtividade da equipe no decorrer do projeto. Os 2 
principais módulos que pode ser citado é o 
Mapeador objeto-relacional (OMR) que irá facilitar a vida 
dos desenvolvedores que não tiverem afinidade em SQL, e o 
painel administrativo que irá de forma visual criar, 
deletar, editar e visualizar objetos do banco de dados.

#### 2.2.2 Modelo MTV

A **Model** é a camada de acesso dos dados. Nessa camada contém 
as classes que abstraem os dados, as lógicas de validação, de 
filtro e de acesso.

O **View** é a camada da regras de negócios. Nessa camada será 
implementada as restrições, o que um usuário pode ou não pode 
fazer, e quais páginas eles tem acesso. É através dessa camada 
que as requisições do usuário será gerenciada.

Essa camada implementa algumas funções do Controller do padrão 
MVC, porém o MTV se diferencia de MVC por ser mais permissivo
quanto a comunicação entre diferentes partes do software 
[[1]](##referências).

O **Template** é a camada de apresentação. Os templates são 
arquivos de texto, que isola os dados do sistema da forma como 
esses dados serão apresentados. O formato mais comum é o HTML.

#### 2.2.3 Django REST
Assim contextualizado, podemos falar sobre o Django REST.
O Django REST possui diversos módulos embutidos que 
facilita a implementação dos princípios e boas práticas 
da arquitetura REST. 

Um exemplo de facilidade é o fato de por padrão as rotas 
dos recursos selecionados serem codificadas para 
respeitar o padrão da arquitetura REST, assim não sendo 
necessário escrever todas as 7 rotas do REST (index, new, 
create, show, edit, update e destroy).

# TODO: Pesquisar sobre o funcionamento do Vue
### 2.2 Vue.js

## 3. Metas e Restrições arquiteturais

3.1 **Suportabilidade**

A aplicação poderá ser utilizada sem grandes problemas 
pelos principais navegadores modernos da atualizada, no 
entanto o enfoque será para o Google Chrome, tanto sua 
versão desktop quanto sua versão mobile, e o Safari, 
navegador padrão dos sistemas da Apple.

3.2 **Usabilidade**

O sistema deverá ser intuitivo e de simples uso, de forma 
que a curva de aprendizado para utilizar a aplicação não 
seja um impedimento para usar o sistema.

3.3 **Ferramentas de Desenvolvimento**

O projeto será desenvolvido em Python (versão 3.7), 
utilizando o framework Django (versão 2.2), em conjunto 
com o framework Vue, um framework JavaScript para criação 
de interfaces e aplicativos. 

Para facilitar a portabilidade do projeto, tanto para o 
ambiente de deploy quanto para os ambientes de 
desenvolvimento, será utilizado o <i>Docker</i> para 
realizar o empacotamento da aplicação.

A tecnologia para o banco de dados está para ser determinada. 
As informações e relações cujos os bancos de dados tem por 
responsabilidade persistir são objetos grandes, em sua 
grande maioria com um intervalo de uso extenso e várias 
relações com outros objetos.

3.4 **Confiabilidade**

O sistema terá uma cobertura mínima de testes de 90%, 
buscando garantir que suas funcionalidades foram 
suficientemente testadas.

## 4. Visão de Casos de Uso

Segue a lista de casos de uso:

- Criar colheita
- Comunicar com time de colheita
- Registrar árvores
- Registrar conta
- Registrar propriedade
- Selecionar voluntários
- Ver dados de todas as colheitas
- Ver lista de colheitas
- Voluntariar para colheita

### 4.1 Casos de Uso significantes para a arquitetura

![](https://user-images.githubusercontent.com/45462822/64752921-bf1efb00-d4f7-11e9-9aa4-01672e9ddee8.png)

Esse diagrama expõe os seguintes requisitos: 

- RF01: Permitir que o usuário faça cadastro e autenticação.
- RF03: Permitir cadastro de árvores, propriedades e colheitas.
- RF04: Permitir usuários se candidatar a colheita.
- RF05: Habilitar comunicação entre envolvidos em colheita (voluntários, líderes e proprietários). 
- RF08: Prover à líderes a possiblidade de escolher voluntários cadastrados em colheita.
- RF09 Mostrar dados à respeito de colheitas realizadas de forma transparente.

## 5. Visão Lógica
[Descrever uma visão lógica da arquitetura. Descrever as classes mais importantes, sua organização em pacotes de serviços e subsistemas. Diagramas de classes e sequência devem ser incluídos para ilustrar os relacionamentos entre as classes significativas na arquitetura, subsistemas, pacotes e camadas. Descrever também a relação de Vue.js com Django Rest no contexto do projeto e descrição breve dos pacotes.]

### 5.1 Diagrama de relações
[Relação macro dos componentes.]

### 5.2 Diagrama de pacotes
#### 5.2.1 _Back-end_

![](https://i.imgur.com/t93zw5t.png)

#### 5.2.2 _Front-end_

![](https://i.imgur.com/XtD2gKR.png)

## 6. Visão de implementação

### 6.1 Diagrama de classes e serviços

### 6.2 Diagrama do banco de dados


## Referências

Departamento de Informática do SUS. Documento de Arquitetura de Software. Disponível em: <datasus.saude.gov.br/images/MDSF/MDSoftware/Artefatos/Arquitetura/MDS_DAS_Documento_Arquitetura_Software2.docx>. Acesso em: 10 de setembro de 2019.

[1] - Andrew Pinkham. Livro. Disponível em: <https://django-unleashed.com>. Acesso em: 12 de setembro de 2019.
