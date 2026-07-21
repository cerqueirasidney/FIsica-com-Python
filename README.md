# Física com Python

Projeto de livro didático que combina conceitos de Física, modelagem matemática e programação em Python.

## Objetivo

Construir uma introdução prática à Física usando simulações, gráficos e experimentos computacionais reproduzíveis.

## Estrutura inicial

- `index.qmd`: apresentação do livro;
- `prefacio.qmd`: público, proposta e convenções;
- `capitulos/`: texto principal;
- `exercicios/`: listas de problemas;
- `codigo/`: scripts Python reutilizáveis;
- `referencias.bib`: bibliografia;
- `_quarto.yml`: organização e configuração do livro.

## Pré-requisitos locais

1. Instale o [Python](https://www.python.org/) e o [Quarto](https://quarto.org/).
2. Crie um ambiente virtual e instale as dependências:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
```

3. Visualize o livro:

```powershell
quarto preview
```

## Licença

O código-fonte é disponibilizado sob a licença MIT. O texto do livro permanece protegido por direitos autorais do autor, salvo indicação diferente.
