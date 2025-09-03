# Monitor de Pesquisa

## Descrição
Painel para monitorar menções sobre "Inteligência Artificial no Piauí" em notícias públicas, com análise de sentimento e identificação de temas recorrentes.

## Estrutura do Projeto

Projeto organizado com foco em clareza e facilidade de manutenção.

- `app.py` - Ponto de entrada do dashboard (Streamlit).
- `src/` - Código fonte do pacote:
   - `src/coleta/` - coleta de dados (RSS). Contém `coleta.py`.
   - `src/processamento/` - limpeza e classificação de texto. Contém `processamento.py`.
   - `src/lexicons/` - listas de palavras (positivo/negativo).
   - `src/utils/` - utilitários de normalização.
   - `src/viz/` - funções de visualização reutilizáveis.
   - `src/cli.py` - script para coleta em lote que salva `data/latest.csv`.
- `data/` - saída dos dados processados (`latest.csv`).
- `tests/` - testes unitários (ex: `test_processamento.py`).
- `DECISIONS.md` - justificativas técnicas e decisões do projeto.

## Como rodar (rápido)

1. Criar e ativar ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Instalar dependências:

```bash
pip install -r requirements.txt
```

3. Coletar dados e gerar `data/latest.csv` (opcional):

```bash
make collect
```

4. Rodar o dashboard:

```bash
make run
```

5. Rodar testes:

```bash
make test
```

## Layout de código e boas práticas

- Organização em pacotes (`src.*`) para facilitar import e empacotamento.
- Arquivos `__init__.py` expõem API pública mínima para cada submódulo.
- `pyproject.toml` e `Makefile` incluídos para apresentar boas práticas e facilitar execução.

## Próximos passos sugeridos (diferenciais)

- Adicionar CI (GitHub Actions) para rodar testes e lint automaticamente.
- Incluir linters/formatters (`flake8`, `black`) no fluxo de desenvolvimento.
- Subir o projeto para um repositório público com um `README.md` completo e bem formatado.


## Como rodar
1. Crie e ative o ambiente virtual:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute a coleta/processamento dos dados (exemplo):
   ```bash
   # Implemente um script para rodar coleta e processamento, salvando em data/latest.csv
   ```
4. Inicie o dashboard:
   ```bash
   streamlit run app.py
   ```

## Testes
```bash
python -m unittest tests/test_processamento.py
```

## Diferenciais
- Filtros e visualização interativa
- Exportação de dados
- Estrutura modular e testável
# projeto-sia
# projeto-sia
