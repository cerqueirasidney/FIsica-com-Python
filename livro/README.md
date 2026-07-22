# Fonte LaTeX do livro

O arquivo principal é `main.tex`. O preâmbulo compartilhado está em `configuracao/preambulo.tex`, e cada capítulo possui seu próprio arquivo em `capitulos/`.

## Organização

```text
livro/
├── main.tex
├── configuracao/
│   └── preambulo.tex
├── capitulos/
│   ├── cap00-python.tex
│   └── cap01-ferramentas-matematicas.tex
├── codigos/
│   └── cap01/
├── figuras/
└── solucoes/
    └── solucoes.tex
```

O arquivo principal usa `\include` para os capítulos. Isso permite usar `\includeonly` durante a revisão e mantém cada capítulo começando em uma nova página. O preâmbulo usa `\input`, pois não constitui uma unidade textual independente.

A família tipográfica principal é **Nunito**, incluída em `fontes/` sob a SIL Open Font License. O projeto deve ser compilado com um mecanismo compatível com `fontspec`, como XeLaTeX, LuaLaTeX ou Tectonic; `pdflatex` não é compatível com esta configuração.

## Processo editorial

1. escrever e revisar o texto do capítulo;
2. propor os códigos separadamente;
3. executar e validar os códigos no VS Code;
4. gerar e inspecionar as figuras;
5. inserir códigos e figuras aprovados no capítulo;
6. compilar e revisar o PDF;
7. somente então criar commit e enviar ao GitHub.

Todas as atividades propostas serão resolvidas em `solucoes/solucoes.tex`, ao final do livro. As resoluções serão adicionadas somente depois que os enunciados do respectivo capítulo forem aprovados.
