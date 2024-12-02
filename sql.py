import sqlite3

banco = sqlite3.connect('banco_questoes.db')
cursor = banco.cursor()

# excluindo tabelas para ajustes
# cursor.execute("DROP TABLE IF EXISTS QuestoesBasicas")
# cursor.execute("DROP TABLE IF EXISTS QuestoesIntermediarias")
# cursor.execute("DROP TABLE IF EXISTS QuestoesAvancadas")


# Criando tabela de questões básicas
cursor.execute("""
CREATE TABLE IF NOT EXISTS QuestoesBasicas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pergunta TEXT, 
    A TEXT, 
    B TEXT, 
    C TEXT, 
    D TEXT, 
    Gabatito TEXT, 
    Dica_estat TEXT, 
    Dica_vida TEXT
)""")

# Inserindo questões básicas
cursor.execute("""
INSERT INTO QuestoesBasicas (pergunta, A, B, C, D, Gabatito, Dica_estat, Dica_vida) VALUES (
    'Considerando seis alunos, Enzo, Valentina, Miguel, Sofia, Gael e Virgínia que tiraram as seguintes notas, respectivamente: 6, 5, 6, 5, 3 e 8. Responda: Qual a média de nota entre eles?', 
    '7,2', 
    '6,5', 
    '5,5', 
    '5', 
    'C', 
    'Dica de estatística: Média é o valor que está no “meio” entre os valores observados, para calcular isso somamos todos os valores e dividimos pela quantidade.', 
    'Dica da vida: Encontre equilíbrio na sua rotina, assim como calculamos a média para equilibrar os dados.'
)
""")

cursor.execute("""
INSERT INTO QuestoesBasicas (pergunta, A, B, C, D, Gabatito, Dica_estat, Dica_vida) VALUES (
    'Considerando seis alunos, Enzo, Valentina, Miguel, Sofia, Gael e Virgínia que tiraram as seguintes notas, respectivamente: 6, 5, 6, 5, 3 e 8. Responda: Se a média para passar é 6. Quantos alunos passaram e quantos reprovaram, respectivamente?', 
    '2 e 4', 
    '1 e 4', 
    '3 e 3', 
    '4 e 2', 
    'C', 
    'Dica de estatística: Conte quantos alunos tiveram uma nota maior ou igual a 6 e quantos tiveram uma nota menor.', 
    'Dica da vida: Estude matemática, pois é muito importante para a vida.'
)
""")

cursor.execute("""
INSERT INTO QuestoesBasicas (pergunta, A, B, C, D, Gabatito, Dica_estat, Dica_vida) VALUES (
    'Considerando seis alunos, Enzo, Valentina, Miguel, Sofia, Gael e Virgínia que tiraram as seguintes notas, respectivamente: 6, 5, 6, 5, 3 e 8. Responda: Qual a mediana das notas?', 
    '5,5', 
    '5', 
    '6', 
    '6,5', 
    'A', 
    'Dica de estatística: Liste os valores em ordem crescente e ache o valor que está no meio, se a sequência tiver um número par de valores faça a média dos 2 valores centrais.', 
    'Dica da vida: Não seja uma pessoa mediana, busque novos desafios para evoluir na vida.'
)
""")

cursor.execute("""
INSERT INTO QuestoesBasicas (pergunta, A, B, C, D, Gabatito, Dica_estat, Dica_vida) VALUES (
    'Considerando seis alunos, Enzo, Valentina, Miguel, Sofia, Gael e Virgínia que tiraram as seguintes notas, respectivamente: 6, 5, 6, 5, 3 e 8. Responda: Qual é a Moda das notas?', 
    '6', 
    '8', 
    '5', 
    '5 e 6', 
    'D', 
    'Dica de estatística: Conte qual ou quais valores mais aparecem na sequência.', 
    'Dica de vida: Identifique o que mais se destaca em você, como a moda faz com os números.'
)
""")

cursor.execute("""
INSERT INTO QuestoesBasicas (pergunta, A, B, C, D, Gabatito, Dica_estat, Dica_vida) VALUES (
    'Considerando seis alunos, Enzo, Valentina, Miguel, Sofia, Gael e Virgínia que tiraram as seguintes notas, respectivamente: 6, 5, 6, 5, 3 e 8. Responda: Escolhido um aluno aleatoriamente, qual a probabilidade que ele tenha tirado uma nota maior que a mediana?',
    '0,35', 
    '0,5', 
    '0,99', 
    '1,44', 
    'B', 
    'Dica de estatística: Conte quantos alunos tiraram uma nota maior que a mediana e divida pelo total de alunos.',
    'Dica da vida: Na faculdade descobrimos que o importante é passar.'
)
""")

cursor.execute("""
INSERT INTO QuestoesBasicas (pergunta, A, B, C, D, Gabatito, Dica_estat, Dica_vida) VALUES (
    'O que é Estatística?', 
    'Uma pessoa que morre', 
    'Um ramo da matemática que trata da coleta, da análise, da interpretação e da apresentação de massas de dados.', 
    'Dados de IBGE', 
    'Nenhuma das alternativas anteriores', 
    'B', 
    'Dica de estatística: Se trata de uma ciência que, entre outras coisas, utiliza métodos matemáticos para analisar dados.',
    'Dica da vida: Na vida é importante não virar estatística, nunca representa coisa boa.'
)
""")

cursor.execute("""
INSERT INTO QuestoesBasicas (pergunta, A, B, C, D, Gabatito, Dica_estat, Dica_vida) VALUES (
    'Para quê a Estatística Serve?', 
    'Analisar Dados', 
    'Auxiliar na tomada de decisão', 
    'Resumir informações sobre um grande conjunto de dados', 
    'Todas as alternativas anteriores', 
    'D', 
    'Dica de estatística: Tem várias utilidades…', 
    'Dica da vida: Para fazer a gente sofrer fazendo muita conta.'
)
""")

# Criando tabela de questões intermediárias
cursor.execute("""
CREATE TABLE IF NOT EXISTS QuestoesIntermediarias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pergunta TEXT, 
    A TEXT, 
    B TEXT, 
    C TEXT, 
    D TEXT, 
    Gabatito TEXT, 
    Dica_estat TEXT, 
    Dica_vida TEXT
)""")

# Inserindo questões intermediárias
cursor.execute("""
INSERT INTO QuestoesIntermediarias (
    pergunta, A, B, C, D, Gabatito, Dica_estat, Dica_vida
) VALUES (
    'Quantas chances tenho de sentar ao lado do meu chefe na mesa em uma reunião com 10 pessoas??', 
    '2*8!', 
    '10!', 
    '8!', 
    '2*9!', 
    'A', 
    'Dica de estatística: Permutações e combinações estão sempre presentes em questões, estude sobre elas.', 
    'Dica de vida: O seu círculo não tem só Enzo e Valentina, se cerque de boas companhias. Não necessariamente seu chefe.'
)
""")

cursor.execute("""
INSERT INTO QuestoesIntermediarias (
    pergunta, A, B, C, D, Gabatito, Dica_estat, Dica_vida
) VALUES (
    'Qual é a correlação esperada entre a prática de exercícios e a saúde cardiovascular?', 
    'Positiva', 
    'Negativa', 
    'Nula', 
    'Inversa', 
    'A', 
    'Dica de estatística: Correlacione as variáveis para ver como uma mudança em uma afeta a outra.', 
    'Dica de vida: Cuide do seu corpo, pois a prática de hábitos saudáveis pode melhorar sua saúde.'
)
""")

cursor.execute("""
INSERT INTO QuestoesIntermediarias (
    pergunta, A, B, C, D, Gabatito, Dica_estat, Dica_vida
) VALUES (
    'Qual é a diferença entre um teste de hipótese unilateral e bilateral?', 
    'Unilateral testa duas direções; bilateral, uma.', 
    'Bilateral testa duas direções; unilateral, uma.', 
    'Ambos testam uma direção.', 
    'Ambos testam duas direções.', 
    'B', 
    'Dica de estatística: A escolha entre um teste unilateral e bilateral depende da pergunta de pesquisa e da hipótese alternativa que se deseja testar.', 
    'Dica de vida: Avalie se a opção mais conservadora é válida!'
)
""")

cursor.execute("""
INSERT INTO QuestoesIntermediarias (
    pergunta, A, B, C, D, Gabatito, Dica_estat, Dica_vida
) VALUES (
    'Se o coeficiente de correlação entre duas variáveis é 0, qual das afirmações é verdadeira?', 
    'Elas são independentemente relacionadas.', 
    'Elas são linearmente relacionadas.', 
    'Uma é causa da outra.', 
    'Não há relação linear entre elas.', 
    'D', 
    'Dica de estatística: Uma correlação de 0 significa simplesmente que não há relação linear e, portanto, não apoia uma ligação causal, mas não exclui outras formas de dependência.', 
    'Dica de vida: Nem sempre as relações são evidentes; procure além do óbvio.'
)
""")

cursor.execute("""
INSERT INTO QuestoesIntermediarias (
    pergunta, A, B, C, D, Gabatito, Dica_estat, Dica_vida
) VALUES (
    'Qual é a probabilidade de tirar um Ás em um baralho de 52 cartas?', 
    '1/13', 
    '1/4', 
    '1/26', 
    '1/52', 
    'A', 
    'Dica de estatística: Considere o número total de áses sobre o número total de cartas.', 
    'Dica de vida: Compreender as chances pode ajudar na tomada de decisões.'
)
""")

cursor.execute("""
INSERT INTO QuestoesIntermediarias (
    pergunta, A, B, C, D, Gabatito, Dica_estat, Dica_vida
) VALUES (
    'Qual é a principal função de um gráfico de barras?', 
    'Comparar diferentes categorias de dados', 
    'Mostrar a frequência de dados numéricos', 
    'Apresentar dados qualitativos em ordem cronológica', 
    'Calcular a média de um conjunto de dados', 
    'A', 
    'Dica de estatística: Para melhorar a utilização de gráficos de barras, considere a utilização de ferramentas de visualização de dados que permitam a personalização e interatividade.', 
    'Dica de vida: Visualizar informações pode facilitar a tomada de decisões.'
)
""")

cursor.execute("""
INSERT INTO QuestoesIntermediarias (
    pergunta, A, B, C, D, Gabatito, Dica_estat, Dica_vida
) VALUES (
    'Qual é a diferença entre dados qualitativos e quantitativos?', 
    'Dados qualitativos são sempre numéricos', 
    'Dados qualitativos descrevem características, enquanto quantitativos medem quantidades', 
    'Dados quantitativos são sempre descritivos', 
    'Dados qualitativos são usados apenas em estatísticas descritivas', 
    'B', 
    'Dica de estatística: Dados qualitativos são descritivos; quantitativos são numéricos.', 
    'Dica de vida: Entender a natureza das coisas é essencial para uma análise clara.'
)
""")


# Criando tabela de questões avançadas
cursor.execute("""
CREATE TABLE IF NOT EXISTS QuestoesAvancadas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pergunta TEXT, 
    A TEXT, 
    B TEXT, 
    C TEXT, 
    D TEXT, 
    Gabatito TEXT, 
    Dica_estat TEXT, 
    Dica_vida TEXT
)""")

# Inserindo questões avançadas
cursor.execute("""
INSERT INTO QuestoesAvancadas (
    pergunta, A, B, C, D, Gabatito, Dica_estat, Dica_vida
) VALUES (
    'Calcule o coeficiente de variação para o conjunto: 10, 15, 20.', 
    '27.2', 
    '34', 
    '50.5', 
    '66', 
    'A', 
    'Dica de estatística: Divida o desvio padrão pela média e multiplique por 100%.', 
    'Dica de vida: Escolha seu conjunto de pessoas, mas não seja como a média.'
)
""")

cursor.execute("""
INSERT INTO QuestoesAvancadas (
    pergunta, A, B, C, D, Gabatito, Dica_estat, Dica_vida
) VALUES (
    'Qual é a interpretação correta de um intervalo de confiança de 95%?', 
    'Há 95% de chance de conter a média populacional.', 
    '95% dos dados estão dentro do intervalo.', 
    'O intervalo cobre 95% do tempo.', 
    'O intervalo cobre 95% dos dados amostrais.', 
    'A', 
    'Dica de estatística: Para melhorar a compreensão do intervalo de confiança, considere estudar a diferença entre erro padrão e desvio padrão da média.', 
    'Dica de vida: A confiança vem da repetição e da consistência nas ações.'
)
""")

cursor.execute("""
INSERT INTO QuestoesAvancadas (
    pergunta, A, B, C, D, Gabatito, Dica_estat, Dica_vida
) VALUES (
    'Qual é a probabilidade de obter cara ao lançar uma moeda duas vezes?', 
    '1/4',
    '1/3', 
    '1/2', 
    '3/4', 
    'D', 
    'Dica de estatística: Considere os possíveis resultados (cara-cara, cara-coroa, coroa-cara, coroa-coroa).', 
    'Dica de vida: Simplifique o complexo observando todas as possibilidades.'
)
""")

cursor.execute("""
INSERT INTO QuestoesAvancadas (
    pergunta, A, B, C, D, Gabatito, Dica_estat, Dica_vida
) VALUES (
    'Qual é a definição de um outlier em um conjunto de dados?', 
    'Um valor que ocorre com mais frequência', 
    'Um valor que está no meio do conjunto de dados', 
    'Um valor que está significativamente distante dos outros valores', 
    'Um valor que representa a média', 
    'C', 
    'Dica de estatística: Outliers podem indicar variabilidade inesperada ou erros nos dados.', 
    'Dica de vida: Às vezes, estar fora da curva pode ser uma vantagem.'
)
""")

cursor.execute("""
INSERT INTO QuestoesAvancadas (
    pergunta, A, B, C, D, Gabatito, Dica_estat, Dica_vida
) VALUES (
    'Se um experimento tem uma distribuição binomial com n=10 e p=0.5, qual é a probabilidade de obter exatamente 5 sucessos?', 
    '0.024', 
    '0.246', 
    '0.5', 
    '0.75', 
    'B', 
    'Dica de estatística: A fórmula da distribuição binomial pode ser utilizada para calcular essa probabilidade.', 
    'Dica de vida: Prepare-se para o inesperado, mas também valorize o que é consistente.'
)
""")

cursor.execute("""
INSERT INTO QuestoesAvancadas (
    pergunta, A, B, C, D, Gabatito, Dica_estat, Dica_vida
) VALUES (
    'Qual é a distribuição de probabilidade mais apropriada para modelar o tempo até que um equipamento falhe?', 
    'Normal', 
    'Exponencial', 
    'Binomial', 
    'Poisson', 
    'B', 
    'Dica de estatística: A distribuição exponencial é usada para modelar o tempo entre eventos.', 
    'Dica de vida: Planeje sua vida para o longo prazo, mas esteja pronto para lidar com falhas inesperadas.'
)
""")

cursor.execute("""
INSERT INTO QuestoesAvancadas (
    pergunta, A, B, C, D, Gabatito, Dica_estat, Dica_vida
) VALUES (
    'Qual é a interpretação correta de um p-valor de 0.03 em um teste de hipótese?', 
    'Há 3% de chance de rejeitar a hipótese nula incorretamente.', 
    'Em geral, rejeitamos a hipótese nula em favor da hipótese alternativa.', 
    'O resultado é estatisticamente insignificante.', 
    'O teste não tem erro.', 
    'B', 
    'Dica de estatística: Um p-valor baixo indica que o resultado é improvável sob a hipótese nula.', 
    'Dica de vida: Confie em suas análises, mas sempre questione os resultados que parecem improváveis.'
)
""")

banco.commit()

banco.close()
