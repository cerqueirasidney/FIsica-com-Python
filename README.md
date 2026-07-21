# Física com Python

Projeto de livro didático que combina conceitos de Física, modelagem matemática e programação em Python.

## Objetivo

Construir uma introdução prática à Física usando simulações, gráficos e experimentos computacionais reproduzíveis.

O projeto cobre a progressão de uma coleção ampla de Física preparatória, mas possui texto, exemplos, exercícios e códigos próprios. A [arquitetura editorial](planejamento/arquitetura.md) registra o plano dos 36 capítulos e as regras de originalidade.

## Estrutura inicial

- `index.qmd`: apresentação do livro;
- `prefacio.qmd`: público, proposta e convenções;
- `capitulos/`: texto principal;
- `exercicios/`: listas de problemas;
- `codigo/`: scripts Python reutilizáveis;
- `testes/`: verificações automáticas dos modelos;
- `planejamento/`: arquitetura e critérios editoriais;
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

Para verificar os módulos Python sem instalar bibliotecas adicionais:

```powershell
py -m unittest discover -s testes
```

## Licença

O código-fonte é disponibilizado sob a licença MIT. O texto do livro permanece protegido por direitos autorais do autor, salvo indicação diferente.
