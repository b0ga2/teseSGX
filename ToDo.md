## Tasks
### First Task (2025-07-25 by André Zuquete)
Podes começar por fazer um programa que corra num portátil e que detete todos os APs eduroam nas redondezas.
O objetivo depois é levantar todos os APs que consegues apanhar em cada sala do DETI.
Deverás entrar na sala, deixar a porta aberta, e depois colocares o teu portátil em cada lugar sentado.
Em cada lugar deves correr um procedimento de scan de todos os canais.
Não sei se o mesmo tem algum controlo fino, mas deveras percorrer todos os canais de 5GHz e 2.4GHz e ficar algum tempo em cada canal à espera de beacons, ou então enviar um probe request e esperar por um probe response.
Uma vez feito o estudo das salas, é possível depois verificar se um dado aluno estava numa dada hora numa dada sala.

**Done**

#### Notas
- Após alguma pesquisa encontrei as seguintes refs:
  - https://techcommunity.microsoft.com/discussions/windowspowershell/retrieving-information-from-multiple-access-points-via-powershell/1163088
  - https://superuser.com/questions/267170/see-available-wireless-access-points-in-the-terminal
  - https://askubuntu.com/questions/75625/how-do-i-scan-for-wireless-access-points
  - https://github.com/kootenpv/access_points 


### Second Task (2025-07-25 by André Zuquete)
No Google Scholar começar a reunir artigos para o estado da arte
Os encontrados estão no ficheiro listSOA.txt juntamente com as queries no google Scholar

**Done**

### Third Task and a Note (2025-11-12 by Liliana Paulo (DPO da UA))
Redigir um documento para recolher o consentimento dos alunos para o tratamento dos dados
A DPO falou de um documento de Tratamento de Dados Interno (que nos irá fazer chegar) que eu tenho de preencher e apenas eu

**Done** mas pelo professor André Zuquete 

#### Notes
- Os dados recolhidos vão ser de turmas que não tenham alunos em comum para não ser possivel realizar cruzamento de dados
- Inicialmente terei os dados de mim e dos orientadores para treinar
- Adicionar telemovel

#### Fourth Task (2025-11-16 by André Zuquete no Documento AIPD)
- O aluno irá fornecer aos STIC pequenas aplicações que podem ser usadas para pseudonimizar os dados do PACO e do Catalyst.
OS STIC devem usá-las após validação.

#### Notes
- O prof recomenda utilização de Python para ser mais simples
- Utilizar Argon2 (porque tem menos parametros e é mais fácil)
  - Preciso de confirmar que parametros o prof quer que eu passe
  - Discutir que campos é que vou realmente utilizar
- Return base64 ou hex


#### Fifth Task (2025-11-17 by Tomás Bogalho)
- Perguntar aos profs, boas teses para verificar como fizeram o SOA (Duarte Mortagua e Fábio Santos)
- Começar a escrever o SOA, normalmente este ocupa 4 a 5 páginas
  - (2025-11-30)Escolhi fazer um Related Work porque não há nada igual por isso não é um SOA, mas se calhar a divisão deveria ser Indoor Location e depois falar das várias uti-idades e colocar referências (dava mais jeito para escrever mais)
  - (2025-12-08) - Devia usar \noident?
  - (2025-12-08) - Ler melhor o artigo do IPS, duvidas principais:
    - O que é APP-CAT
    - Se o meu cenário está incluido no scene analysis
    - Ler os artigos a partir do 21 para a frente
    - Escrever Wifi sempre da mesma forma, qual a mais correta?
    - Mencionar que a figura 3.1 também é do autor, o Carlos disse para refazer e dizer que é com base em X
  - Fazer documentação básica, e adicionar memoria em cache com a lista de alunos

##### Tasks SGX
- Recebe ficheiro texto ou csv para binário protegido pelo cifra
- Tentar perceber como vou relacionar os logs com as aulas
- Pensar quais são os dados de input de output, comparar desempenho uma turma de cada vez ou todas em brutas, pensar em Diffie Helman


- Fazer um use case para o cenário final, turmas e horário fixos (obtidos no inicio), e que os alunos podem mudar semanalmente (extração semanal)
  - Valores a obter quantidade de alunos por sala e nº de aulas que um aluno foi num semestre
  - Visibilidade intermédia, variação ao longo do ano/semestre 
  - Ver opções de compressão
  - Usar formato cache, em que a cada entrada nova é atualizado

##### Sixth
- Pesquisar para SOA algo como "SGX Anonimity"

#### Seventh 
1- Os dados ficam sempre cifrados e a computação pode ser feita mesmo perdendo as chaves, o processamento pode ser feito fora do campus (p.e num servidor externo), proteção extra sobre o processamento mesmo no caso de um atacante entrar na rede

2- É a infrastrutura que existe disponivel de momento