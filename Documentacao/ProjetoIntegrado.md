Documentação do Sistema de Gerenciamento de Estoque
Introdução
Este projeto foi desenvolvido com o objetivo de criar um sistema de gerenciamento de estoque voltado para empresas de e-commerce. A necessidade surgiu diante do crescimento acelerado das operações, que trouxe desafios como controle de estoque, excesso ou falta de produtos e dificuldade em organizar movimentações logísticas. Para solucionar esses problemas, este sistema oferece funcionalidades robustas de cadastro, consulta, movimentação e geração de relatórios.

Metodologia
A metodologia ágil Scrum foi adotada para garantir uma abordagem eficiente e iterativa ao desenvolvimento do projeto. O Trello desempenhou um papel essencial na organização do trabalho, permitindo dividir as tarefas em sprints bem definidas. Com listas como "Backlog", "Em Progresso" e "Concluído", a equipe conseguiu gerenciar prioridades e acompanhar o progresso das atividades. Capturas de tela do Trello foram incluídas como anexo para ilustrar o gerenciamento.

Tabela Verdade
Uma tabela verdade foi criada para validar as combinações possíveis entre os principais requisitos booleanos do sistema:

P (Cadastro de Produtos)

E (Atualização de Estoque)

L (Rastreamento de Localização)

R (Relatórios)

A solução completa é alcançada quando todos os requisitos são atendidos. A tabela também ajuda a entender os cenários nos quais certos requisitos podem não ser necessários.

Estruturas e Algoritmos
O sistema foi implementado utilizando Python, com base em uma estrutura clara e organizada:

Classes:

Categoria: Representa as categorias dos produtos.

Produto: Contém as informações detalhadas de cada produto.

Movimentacao: Registra todas as movimentações de estoque.

Principais Funções:

Cadastro de novos produtos.

Movimentação de estoque (entrada e saída).

Geração de relatórios, como produtos com estoque baixo e histórico de movimentações.

O código completo está disponível na pasta CódigoFonte/.

Diagrama de Casos de Uso
O diagrama de casos de uso foi elaborado para representar as interações entre os usuários do sistema:

Estoquista: Responsável por registrar entradas de produtos e validar notas fiscais.

Usuário: Solicita relatórios e acompanha o estoque.

Gerente de Setor: Autoriza compras e supervisiona o estoque.

Conclusão
O desenvolvimento deste projeto resultou em um sistema funcional e flexível para a gestão de estoque em empresas de e-commerce. A aplicação das práticas de Scrum, aliada à modelagem lógica com diagramas e tabelas, contribuiu para a eficiência do trabalho e para uma solução final robusta.