# Testes Automatizados com Pytest

[![Testes Automatizados](https://github.com/gabrielpe7/testes-pytest/actions/workflows/testes.yml/badge.svg)](https://github.com/gabrielpe7/testes-pytest/actions/workflows/testes.yml)

Conjunto de funções de lógica de negócio (cálculo de desconto, frete e validação de pedidos) com testes automatizados usando Pytest, cobertura de código e um pipeline de CI/CD com GitHub Actions, desenvolvido como projeto de estudo.

## Funcionalidades

- Cálculo de desconto percentual sobre um valor
- Cálculo de frete baseado em peso
- Validação de percentual de desconto, recusando valores fora do intervalo permitido
- Composição de funções para cálculo de pedido final (desconto + frete)
- Suíte de testes automatizados cobrindo casos normais, casos-limite e casos de erro
- Relatório de cobertura de código
- Pipeline de integração contínua: testes executados automaticamente a cada push e pull request

## Tecnologias utilizadas

- **Python 3**
- **Pytest** (framework de testes)
- **pytest-cov** (relatório de cobertura de testes)
- **GitHub Actions** (integração contínua / CI)

## Estrutura do projeto

```
testes-pytest/
├── calculos.py                    # funções de lógica de negócio
├── test_calculos.py               # testes automatizados
└── .github/
    └── workflows/
        └── testes.yml             # pipeline de CI
```

## Sobre o projeto

Este projeto foi construído em etapas, introduzindo testes automatizados e integração contínua:

1. **Fundamentos de teste** — uso de `assert` para verificar resultados esperados
2. **Testes parametrizados** — cobertura de múltiplos cenários com `@pytest.mark.parametrize`
3. **Testes de exceção** — verificação de que funções recusam corretamente valores inválidos, usando `pytest.raises`
4. **Cobertura de código** — medição de quanto do código-fonte está de fato coberto pelos testes
5. **Integração contínua (CI)** — pipeline no GitHub Actions que instala dependências e roda os testes automaticamente a cada alteração, incluindo pull requests

## Como executar

Pré-requisito: ter o [Python 3](https://www.python.org/) instalado.

```bash
# Clone o repositório
git clone https://github.com/gabrielpe7/testes-pytest.git

# Entre na pasta do projeto
cd testes-pytest

# Instale as dependências
python -m pip install -r requirements.txt

# Rode os testes
python -m pytest

# Rode os testes com relatório de cobertura
python -m pytest --cov=calculos
```

## Pipeline de CI

Toda vez que há um `push` ou `pull request` neste repositório, um workflow do GitHub Actions:

1. Baixa o código
2. Instala o Python e as dependências
3. Roda a suíte de testes automaticamente

O badge no topo deste README reflete o status mais recente dessa verificação.

## Possíveis melhorias futuras

- Cobertura completa de 100%, incluindo a função de cálculo de juros compostos
- Adicionar etapa de deploy automático (CD) ao pipeline
- Testes de integração com um banco de dados real

## Autor

Desenvolvido por Gabriel Pereira de Oliveira — estudante de Análise e Desenvolvimento de Sistemas.

[LinkedIn](#) · [GitHub](https://github.com/gabrielpe7)
