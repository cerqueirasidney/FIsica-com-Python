$ErrorActionPreference = "Stop"

$pythonDoProjeto = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"

if (-not (Test-Path -LiteralPath $pythonDoProjeto)) {
    Write-Host "O ambiente virtual ainda nao existe. Criando .venv..."
    py -m venv (Join-Path $PSScriptRoot ".venv")
}

Write-Host ""
Write-Host "Fisica com Python - escolha uma aula"
Write-Host "0 - Primeiros passos"
Write-Host "1 - Primeiro grafico"
Write-Host "2 - Vetores"
Write-Host "3 - Movimento"
Write-Host "J - Abrir Jupyter Lab"
Write-Host ""

$escolha = (Read-Host "Digite sua escolha").Trim()

$aulas = @{
    "0" = "aulas\00_primeiros_passos.py"
    "1" = "aulas\01_primeiro_grafico.py"
    "2" = "aulas\02_vetores.py"
    "3" = "aulas\03_movimento.py"
}

if ($aulas.ContainsKey($escolha)) {
    & $pythonDoProjeto (Join-Path $PSScriptRoot $aulas[$escolha])
}
elseif ($escolha.ToUpper() -eq "J") {
    & $pythonDoProjeto -m jupyter lab --notebook-dir $PSScriptRoot
}
else {
    Write-Host "Escolha invalida. Execute o script novamente."
}
