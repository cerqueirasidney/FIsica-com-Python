# Arquitetura editorial de Física com Python

Este documento orienta a construção do livro. Os cinco volumes de *Understanding Physics*, de D. C. Pandey, foram consultados para compreender abrangência, progressão e granularidade típicas de uma coleção preparatória para o JEE. A redação, os exemplos, os problemas, as figuras e os códigos deste projeto serão originais.

## Identidade do livro

**Proposta:** ensinar Física por três linguagens complementares: explicação conceitual, modelagem matemática e investigação computacional.

**Público inicial:** estudantes do ensino médio e início da graduação que conheçam álgebra elementar, mas não necessariamente programação.

**Unidade pedagógica de cada capítulo:**

1. pergunta motivadora;
2. conceitos e hipóteses do modelo;
3. desenvolvimento matemático;
4. exemplos autorais resolvidos;
5. laboratório Python reproduzível;
6. análise de limites e erros do modelo;
7. exercícios conceituais, analíticos e computacionais;
8. síntese e próximos passos.

## Organização planejada

### Parte I — Ferramentas para investigar a Física

1. Física, modelos e algoritmos
2. Medidas, unidades e incertezas
3. Vetores e geometria computacional
4. Experimentos, dados e ajuste de modelos

### Parte II — Mecânica: do movimento às forças

5. Movimento em uma dimensão
6. Movimento no plano e lançamentos
7. Movimento relativo
8. Forças e diagramas de corpo livre
9. Atrito, vínculos e referenciais acelerados
10. Trabalho, energia e potência
11. Movimento circular

### Parte III — Sistemas mecânicos e meios contínuos

12. Centro de massa e momento linear
13. Colisões e sistemas de massa variável
14. Rotação de corpos rígidos
15. Gravitação e órbitas
16. Oscilações
17. Elasticidade
18. Fluidos em repouso e movimento

### Parte IV — Ondas e termodinâmica

19. Propagação de ondas
20. Superposição, interferência e modos normais
21. Som e efeito Doppler
22. Temperatura, expansão e teoria cinética
23. Leis da termodinâmica e máquinas térmicas
24. Calorimetria e transferência de calor

### Parte V — Eletricidade e magnetismo

25. Carga, campo e potencial elétrico
26. Capacitores e energia eletrostática
27. Corrente e circuitos de corrente contínua
28. Campo magnético e forças magnéticas
29. Indução eletromagnética
30. Circuitos de corrente alternada

### Parte VI — Óptica e física moderna

31. Ondas eletromagnéticas
32. Reflexão, refração e instrumentos ópticos
33. Interferência e difração da luz
34. Quanta, fótons e matéria ondulatória
35. Átomos, núcleos e radioatividade
36. Semicondutores, sensores e comunicação

## Trilha computacional

Os laboratórios avançam em paralelo com a Física:

- Python básico, NumPy e Matplotlib;
- propagação de incertezas e análise de dados;
- vetores e gráficos paramétricos;
- derivação e integração numéricas;
- solução de equações diferenciais;
- animações e campos vetoriais;
- ajuste de curvas e comparação com experimentos;
- métodos de Monte Carlo e análise de sensibilidade.

## Regras de originalidade

- Não transcrever explicações, exemplos, exercícios, soluções ou legendas dos livros de referência.
- Não redesenhar figuras conservando composição e valores numéricos do original.
- Criar contextos, parâmetros e perguntas próprios para todos os problemas.
- Citar fontes quando uma formulação histórica, conjunto de dados ou imagem externa for usado.
- Registrar no Git a evolução autoral de texto, código e figuras.
- Usar os volumes apenas para cobertura temática e diagnóstico de pré-requisitos.

