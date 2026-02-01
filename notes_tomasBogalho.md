# Notas avaliação relatório

# Major

A motivação carece de um objetivo mais bem-definido. Duas fraquesas são identificadas, mas nenhuma delas parece muito bem substanciada:

- Proteger informação durante a sua computação é. de facto, um ponto forte do Intel SGX. Porém, não é claro no exemplo para que é que isto é necessário. Se os dados são da Universidade de Aveiro, então porque é que o processamento não é feito em máquinas confiáveis na própria Universidade? Não há um motivo claro para  os dados sairem do domínio de confiança. Pode haver interesse em fazer offload dessa mesmo computação, ou de combinar dados de diferentes faculdades, o que justificava SGX, mas isso não é sugerido.
- Limitações de memória são um problema basilar do SGX v1, mas o Intel TDX promete conseguir melhor que isto, criando ambientes virtuais com maior flexibilidade de proteção da memória. Adicionalmente, o Intel SGX foi descontinuado; alguma razão em particular para se abordar esta tecnologia em 2026, ao invés de Intel TDX?

Dado que o Intel TDX é uma evolução natural do Intel SGX (internamente também usa ECALLs e toda a noção de enclaves e mecanimos de atestação), permitindo a utilização de ambientes virtuais, creio que faria sentido apresentar estas duas tecnologias em parelha. I.e. admite-se que se foca na tecnologia Intel SGX; apresenta-se Intel SGX, e depois explica-se como TDX expande o SGX como contexto. Falar de TDX antes e depois de SGX parece contra-intuitivo.

Visto que estamos a falar de processamento de sinais enviados por dispositivos possivelmente pequenos (indoor positioning), não me parece bem justificado porque é que estamos só a olhar para Intel SGX (x86) ao invés de ARM TrustZone (ARM).

## Minor

Gostava de ver mais pormenor no que toca ao caso de uso na introdução. Creio que este UC de "processamento de dados WiFi" está desnecessariamente vago aqui.

Não tem resumo/abstract

Main missing refs on TEES:

- Brossard, Mathias, et al. "Private delegated computations using strong isolation." IEEE Transactions on Emerging Topics in Computing 12.1 (2023): 386-398.
- Paju, Arttu, et al. "Sok: A systematic review of tee usage for developing trusted applications." Proceedings of the 18th International Conference on Availability, Reliability and Security. 2023.

Approaches to privacy (3.3) é muito "leve" para o quão subtil e complexa é a discussão destes temas comparativamente. Talvez reconhecer estas abordagens e dizer que está fora do escopo seja melhor; caso contrário está bastante incompleto.

Data Procecssing in SGX (3.5) também está bastante incompleto nos exemplos. Ver acima o SoK que sugeri, que tem muitos mais casos de uso.

## Nitpicks

- Footnote 1 devia estar ligado ao texto
- Presidente/vogais parece placeholder
- Estranho espaçamento na primeira página do cap. 1, e na página 16