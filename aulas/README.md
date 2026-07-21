# Aulas executáveis — começando do zero

Esta pasta é a entrada prática do livro. As aulas são numeradas e devem ser executadas em ordem.

O modo mais simples no Windows é dar duplo clique em `iniciar_estudos.cmd`, na pasta principal do projeto, e escolher uma aula no menu.

## Como executar

Abra o PowerShell na pasta do projeto e ative o ambiente virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

Execute a primeira aula:

```powershell
python aulas\00_primeiros_passos.py
```

Depois continue:

```powershell
python aulas\01_primeiro_grafico.py
python aulas\02_vetores.py
python aulas\03_movimento.py
```

Cada arquivo possui três tipos de comentário:

- `FÍSICA`: interpretação do fenômeno;
- `PYTHON`: recurso de programação utilizado;
- `EXPERIMENTE`: alteração sugerida para o estudante.

Não tenha receio de modificar os valores. Se algo quebrar, leia a última linha da mensagem de erro: ela geralmente informa o tipo e a localização do problema.

Quando um gráfico for aberto, feche a janela para o programa terminar e o terminal voltar a aceitar comandos.

## Jupyter Lab

Para estudar em células interativas, execute:

```powershell
jupyter lab
```

O navegador abrirá a pasta do projeto. Os capítulos `.qmd` também contêm células Python, mas as aulas desta pasta foram preparadas para execução direta.
