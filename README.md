# Testes Automatizados com Pytest

# [![Testes Automatizados](https://github.com/gabrielpe7/testes-pytest/actions/workflows/testes.yml/badge.svg)](https://github.com/gabrielpe7/testes-pytest/actions/workflows/testes.yml)

Conjunto de funções de lógica de negócio (cálculo de desconto, frete e validação de pedidos) com testes automatizados usando Pytest, incluindo relatório de cobertura de código, desenvolvido como projeto de estudo.

## Funcionalidades

- Cálculo de desconto percentual sobre um valor
- Cálculo de frete baseado em peso
- Validação de percentual de desconto, recusando valores fora do intervalo permitido
- Composição de funções para cálculo de pedido final (desconto + frete)
- Suíte de testes automatizados cobrindo casos normais, casos-limite e casos de erro
- Relatório de cobertura de código

## Tecnologias utilizadas

- **Python 3**
- **Pytest** (framework de testes)
- **pytest-cov** (relatório de cobertura de testes)

## Estrutura do projeto

```
testes-pytest/
├── calculos.py         # funções de lógica de negócio
└── test_calculos.py    # testes automatizados
```

## Sobre o projeto

Este projeto foi construído em etapas, introduzindo a prática de testes automatizados:

1. **Fundamentos de teste** — uso de `assert` para verificar resultados esperados
2. **Testes parametrizados** — cobertura de múltiplos cenários com `@pytest.mark.parametrize`, evitando repetição de código
3. **Testes de exceção** — verificação de que funções recusam corretamente valores inválidos, usando `pytest.raises`
4. **Cobertura de código** — medição de quanto do código-fonte está de fato coberto pelos testes

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

## Possíveis melhorias futuras

- Cobertura completa de 100%, incluindo a função de cálculo de juros compostos
- Testes de integração com um banco de dados real
- Integração contínua (rodar os testes automaticamente a cada envio ao GitHub)

## Autor

Desenvolvido por Gabriel Pereira de Oliveira — estudante de Análise e Desenvolvimento de Sistemas.

[LinkedIn](#) · [GitHub](https://github.com/gabrielpe7)
