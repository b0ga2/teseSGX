Dados Brutos de Input do STIC (fase de dev):
1. Registo do Catalyst Semanal (bruto, toda a UA)
2. Constituição das Turmas (AC2) lista de ficheiros
3. Horários, cada sigla de turma é o horário em que está
4. Alunos que aceitaram o consentimento
5. Adicionar um ficheiro de conf (inputs para o Argon2)

- Neste momento o ficheiro de horários sou eu que faço, o a sério é para o futuro.
  - Json - Cada disciplina (identificado pelo código da disciplina) possui várias turmas, salas e intervalo de tempo da aula e em que dia da semana há aula

Passos:
1. Filtram do catalyst os alunos que **não** aceitaran o consentimento
2. Extraio apenas em relação aos dias que estes têm aulas
3. Anonimizar os resultados
4. Opcionalmente comprimir


Isto vai gerar o ficheiro de input do Catalyst