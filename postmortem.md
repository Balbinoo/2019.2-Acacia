# Post Mortem

## Histórico de revisão

| Data   | Versão | Modificação  | Autor  |
| :- | :- | :- | :- |
| 08/11/2019 | 0.1 | Criação da estrutura do documento |  Fabíola |
| 14/11/2019 | 0.2 | Adição do tópico de capacitação do time | Shayane |
| 15/11/2019 | 0.3 | Adição dos sentimentos | Shayane e Renato |
| 15/11/2019 | 0.4 | Adição dos sentimentos e revisão | Hugo |
| 15/11/2019 | 0.5 | Adição do tópico Arquitetura | Flavio e Durval |
| 15/11/2019 | 0.6 | Adição dos sentimentos | Durval |


# Introdução

Este documento é uma reflexão do time, realizada na fase de finalização do projeto, para concretizar as lições aprendidas e permitir que projetos futuros similares possam ser facilitados.

# Metodologia e Processo

# Tecnologias utilizadas

# Arquitetura

    No início do projeto, foi feito uma verificação da viabilidade para iniciar
o projeto utilizando uma arquitetura de microsserviços, porém após alguns
estudos foi visto que escopo, tamanho e complexidade do nosso projeto não
justificava se iniciar utilizando arquitetura orientada a microsserviços. Com
isso, produziria uma otimização prematura e ainda teríamos muitos mais pontos
negativos do que positivos.
Iniciar a aplicação utilizando microsserviços, apesar de ter a sua concepção
de simplicidade, teríamos alguns desafios que poderia colocar o projeto em risco.
Como a o time de desenvolvedor tinha pouca experiencia e ainda não tinha a
cultura de devops , seria adicionado uma maior complexidade no projeto como um
todo e a curva de aprendizado seria muito maior.
Então ficou decidido iniciar o projeto com uma arquitetura monolítica e fazer a
aplicação funcionar e se mostrar viável para depois considerar mudar para
microsserviços.
Apesar de não ter iniciado com a arquitetura de microsserviços toda as
tecnologias foram pensadas para termos API como o mínimo acoplamento possível,
com comunicação padronizada utilizando chamadas (HTTP) usando uma API REST e
estamos utilizando a melhores práticas na área de desenvolvimento como:
integração continua, contêineres e devops.

# Capacitação do Time

Todas as issues de treinamento aqui sintetizadas, foram registradas no repositório, podendo ser filtradas pelas labels: ["training"](https://github.com/fga-eps-mds/2019.2-Acacia/issues?q=is%3Aissue+label%3Atraining+is%3Aclosed) e/ou "meetings".

#### Planejamento

No início do semestre, percebemos a importância de planejar treinamentos com as tecnologias que previamente já tínhamos em mente: Git, Github, Metodologia ágil, HTML, CSS, Docker e Javascript ou algum framework específico. Em agosto iniciou-se os treinamentos planejados para auxiliar no andamento do projeto. Como não tínhamos um projeto definido, realizávamos nossas reuniões juntamente com os treinamentos aos sábados.

#### Git, Github e Scrum

O primeiro treinamento foi o de Git, Github e metodologia ágil: Scrum, todos ministrados pelos membros de EPS. Sobre o treinamento de Git, alguns membros de MDS já possuiam conhecimento prévio, portanto não foi uma tecnologia muito nova. Apesar disso, foi uma dinâmica completamente nova para outros e por isso, pode haver o compartilhamento do conhecimento desde antes do início do desenvolvimento.

O treinamento de Scrum, adaptado ao XP era essencial porque era com ele que iríamos trabalhar durante todo o projeto, então foram explicados todos os métodos necessários para o bom funcionamento da metodologia. A forma que a Scrum Master ministrou o treinamento, em que havia uma simulação entre os membros com seus respectivos papéis, possibilitou uma grande absorção do processo.

#### Docker

Houve também o treinamento de Docker, que mostrou-se necessário para os membros de MDS e EPS saberem o que estavam usando, visto que nem todos sabiam os termos e práticas. O treinamento foi ministrado por um membro de EPS com a estratégia de um tutorial prático de um pequeno ambiente com as principais funcionalidades. Isso contribuiu para que, no decorrer do semestre, os membros propunham mudanças nos arquivos de configuração.

#### HTML, CSS e Vue.js

O treinamento de HTML e CSS foi realizado np período de agosto porque até então a equipe não possuía os temas definidos, ou seja, aproveitamos o tempo para permitir um maior vivenciamento com os elementos de estilização que provavelmente iríamos utilizar.

Após as escolhas de tecnologia, Vue.js para o frontend e o Django Rest para o backend, procuramos um voluntário para ministrar o treinamento de Vue, já que ninguém da equipe tinha conhecimentos suficientes. O treinamento, realizado no horário do almoço, permitiu que os membros pudessem ter uma noção básica das funcionalidades do framework. Por questões de disponibilidade dos membros e da grande quantidade de conteúdo, optamos por realizar o treinamento apenas de Vue.js.

#### Django Rest

Já o treinamento de Django Rest não foi realizado por falta de disponibilidade dos membros e pelo acúmulo de tarefas em diversas matérias. Além disso, os membros mostravam no começo uma maior confiança com python, o que deu uma pseudo sensação de que a equipe teria mais dificuldades no front. No decorrer do tempo, percebemos que essa primeira impressão não condizia com a realidade dos membros, pela constante dificuldade nas issues ou pelo próprio depoimento nas retrospectivas em relação ao django. No fim, a maioria dos membros possuiam mais crescimento no frontend.

#### Pontos de melhoria

Após discussões com os membros de MDS, foi notória a necessidade de treinamentos referente a testes unitários no frontend. Isso refletiu na deficiência dos testes em Vue e na delimitação dos critérios de aceitação do projeto.


# Entrega da R1

# Escopo do projeto


# Sentimentos da Equipe

### Renato

Aprendi muito sobre desenvolvimento de software, muito além do código. O trabalho em equipe é o que faz o conhecimento e determinação de cada um se destacar. Durante uma parte significativa do projeto, reconheço que faltei com trabalho em equipe porque não enxergava seu valor, o que mudou durante o decorrer e tomei conta do quanto é relevante, acima de tudo, um time com moral alta que trabalha junto e se apoia à cada dificuldade. O valor do pareamento, cujo o qual fui aprender apenas após tempo significativo, se tornou claro e quando pude vê-lo, entendi sua importância. A integração de um time ressalta as habilidades somadas dos membros: um grupo de pessoas vai bem mais longe e bem mais alto que um programador lone wolf.

Sobre um aspecto mais técnico, o projeto também me ensinou a ter uma postura de engenheiro: em pensar nas decisões, levando em conta as alternativas e pesos, balanceando tempo, viabilidade técnica, qualidade de código, mantenabilidade entre outros fatores. Também aumentei minha proficiência em Git e Github, aprendendo o workflow usado para se fazer softwares modernos, e a utilizar Docker. Aprendi a fazer testes embora ainda sinta que falta muito mais, foi um ótimo começo.

No geral, já via MDS como uma matéria essencial para quem quer ser um engenheiro de software de verdade, mas pelos motivos errados. Hoje, por causa dela, enxergo que software vai além de projetos e envolve muito mais do que antes imaginei.

### Shayane

O começo da disciplina foi um desafio para todos os membros, principalmente na aplicação da metodologia alvo. Foi complicado para o time de MDS reconhecer as utilidades da correta adoção das métricas e isso acabou causando um estresse. No entanto, com o passar do tempo e com discussões construtivas, o grupo todo amadureceu bastante essas questões e pode se preocupar com outras questões mais importantes. Notamos desde o começo alguns membros que não se sentiam muito confortáveis em trabalhar com pareamento ou que se sentiam inseguros em relação aos outros membros, em questões de conhecimento. Percebemos que isso seria um problema se não tratado rápido e não deixamos de tentar resolver isso, seja na escolha do pareamento, supervisão do repositório e discussões nas dailies e retrospectivas.

Sobre o matéria em si, foram imensas as oportunidades de aprendizado. Houve uma alta alternância/rotatividade dos papéis de arquiteto e devops, permitindo que ambos pudessem aprender termos e práticas antes não desenvolvidas por eles mesmo. Além disso, os membros de MDS tiveram bastante crescimento, indicado no quadro de conhecimento e no andamento das sprints.

O que chamou bastante atenção também foi o trabalho em equipe e a contribuição de alguns membros para ajudar outros em suas issues. Em relação à metodologia, houveram algumas dívidas técnicas em algumas sprints e senti que o grupo de EPS tinha dúvidas em relação a como agir para contornar e planejar melhor as sprints. Além disso, com a release 2, foi notória a maior participação dos membros de MDS nas discussões e questionamentos de certas demandas, apesar do estresse em relação ao curto tempo para entregar um escopo. Foi notória também a necessidade de acompanhar a saúde mental dos membros, que com muitas demandas da faculdade se sentiam sobrecarregados por todos os lados.

A matéria por si só já vem com uma pressão grande em todos e é difícil controlar esse medo ao longo do semestre, eu mesma tinha medo de não me adaptar ao grupo ou não conseguir fazer as demandas, mas eu não poderia ter uma equipe melhor, com todo o suporte que recebi, apesar de todos os altos e baixos. :rosette:

### Hugo

Minhas primeiras impressões sobre a matéria de MDS foram as mais esperançosas possíveis. Eu tinha uma grande curiosidade sobre como funcionavam as metodologias e cargas de trabalho que rondeavam a matéria, que é conhecida dentro da faculdade como "divisora de águas" para o curso de engenharia de software, e não demorou muito para essa curiosidade ser sanada, já que a demanda por tarefas foi grande desde o começo do semestre e vem se mantendo constante desde então.

Poder trabalhar como um time, alinhado por uma causa e propósito, tem sido maravilhoso. Entretanto, esta nem sempre foi a situação da equipe da Acácia, o começo do projeto foi uma fase dura e confusa (às vezes até mesmo desmotivadora), em que alguns dos membros se encontravam perdidos em meio ao andamento do projeto e dos porquês de estarmos trabalhando da forma como estávamos (e ainda estamos) trabalhando.
Ainda assim, com o passar do tempo a equipe foi se unindo cada vez mais, e cada vez mais eu consegui me sentir pertencente a um time de trabalho.

Além disso, o contato com um projeto grande me possibilitou o aprendizado sobre metodologias de desenvolvimento e a especialização em algumas das tecnologias que estamos usando para a construção da Acácia. Pude também aprender bastante sobre como funciona o andamento de um projeto e como trabalhar com um time ágil. A Ácácia me possibilitou ter contato também com contribuições em repositórios no GitHub, o que me motivou a conhecer mais sobre o mundo de Software Livre.

Em relação às entregas, restam alguns traços de preocupação em volta do tempo restante de trabalho, já que a matéria de MDS/EPS possui um ritmo acelerado quando comparado à quantidade de trabalho necessária.

Por fim, me sinto grato de todas as formas possíveis por ter trabalhado com o time da Acácia, pude criar e reforçar laços de proximidade com pessoas incríveis dentro do projeto, além de receber, sempre que preciso, suporte dos membros da equipe. :heart:

### Durval

A matéria de MDS sempre foi um monstro na minha cabeça.
Era frequente eu ouvir de amigos que essa matéria iria
exigir a alma e que iria definir se você pertence ou
não ao curso.

Isso me fez postergar o máximo possível a matéria até
que eu me sentisse preparado para enfrentar esse monstro.
Eu lembro que nas férias anterior ao semestre que iria
me inscrever eu fui atrás de todos os frameworks e
tecnologias que os projetos dos anos anteriores tinham
usado, fui atrás das metodologias ágeis que tanto eram
faladas, eu realmente estava desesperado...

Eu estava encarando a matéria como se fosse uma maratona,
em que eu precisava me preparar com meses de antecedência.

Outro fato que me preocupava bastante era o fato de
trabalhar em equipe. A única referência de trabalho em
equipe que tinha foi o 3° projeto da matéria de
Orientação à Objetos e que foi um completo desastre.
Eu morria de medo de o grupo olhar para mim e não poder
contar comigo…

Então quando finalmente chegou no primeiro dia de aula,
eu encontrei com o meu grupo, que ainda não tinha tanta
intimidade e abracei a causa. Eu queria mostrar trabalho
de todas as maneiras possíveis, sempre que surgia qualquer
coisa pra fazer eu queria ser o primeiro a começar, para
justamente não parecer que eu não sabia fazer as coisas.

Com o tempo e com as diversas conversas que tivemos em
grupo, essa sentimento de se provar para o grupo foi
diminuindo até o ponto de eu não me sentir mal de está
estudando para outra matéria invés de está fazendo as
coisas de MDS.

Hoje eu vejo que foi uma besteira encarar a disciplina
com a visão que eu tinha. Por mais que eu não me arrependa
de ter me preparado para a disciplina, eu vejo que poderia
tranquilamente ter me inscrito na matéria ainda calouro que
o meu grupo estava preparado e disposto a guiar alguém assim.

# Conclusão
