Dados Brutos de Input do STIC (fase de dev):
1. Registo do Catalyst Semanal (bruto, toda a UA)
2. Constituição das Turmas (AC2) lista de ficheiros
3. Horários, cada sigla de turma é o horário em que está
4. Alunos que aceitaram o consentimento
5. Adicionar um ficheiro de conf (inputs para o Argon2)

- Neste momento o ficheiro de horários sou eu que faço, o a sério é para o futuro.
  - Json - Cada disciplina (identificado pelo código da disciplina) possui várias turmas, salas e intervalo de tempo da aula e em que dia da semana há aula

Passos do STICK:
1. Filtram do catalyst os alunos que **não** aceitaran o consentimento
2. Extraio apenas em relação aos dias que estes têm aulas
3. Anonimizar os resultados
4. Opcionalmente comprimir


Isto vai gerar o ficheiro de input do Catalyst


### 2026/02/25
#### Fase Dev
1. Cálculos 
   1. Ficheiro com turma anonimizado, para cada turma medir a quantidade de alunos que esteve presente na presente semana (mapa de carga de uma semana)
      1. Output deve ser um ficheiro e guardar
   2. Gráfico de frequência, existe X alunos que foram a Y aulas (consome várias semanas)
   
#### Fase Deploy
1. Gerar canal seguro entre o ambiente seguro e inseguro 
   1. Diffie Hellman no guião
2. Como vou obter dados?
   1. Quem vai dar os dados?
3. Como dar os dados ao SGX?


### 2026/03/19
- O script de python deve também descartar linhas não relevantes
  - Analisar mais que linhas são estas
  - Cifrar o conteudo do ficheiro com a chave pública do SGX
- Mais um ficheiro de input público que são os APs que cada sala apanha


## Notas para o Dev de SGX

## Flow de Dados
- 1ª Fase - Carregar os dados estáticos como as turmas e os horários (assumindo que são ficheiros pequenos)
  - Untrusted App para o SGX
- 2ª Fase - Carregar os dados do catalyst(p.e linha a linha ou 1000 linhas de cada vez)
  - Untrusted App para o SGX
- 3ª Fase - Extrair os Logs do SGX
  - SGX para a Untrusted App

## Input de Ficheiros e Cifras
- Ver a biblioteca do projeto sgx_tprotected_fs para lidar com operações com ficheiros.


