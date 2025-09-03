# Documentação das Decisões e Estrutura do Projeto

## Visão Geral

Este projeto foi desenvolvido para monitorar menções sobre "Inteligência Artificial no Piauí" em fontes de notícias públicas, com foco em análise de sentimento e identificação de temas recorrentes. O objetivo foi criar um painel simples, funcional e transparente, seguindo as etapas obrigatórias do case.

---

## Estrutura das Pastas e Funções

- **src/coleta.py**  
	Responsável por coletar notícias usando RSS do Google News.  
	- Faz requisições HTTP e processa o XML retornado.
	- Extrai título, link e descrição das notícias.
	- Inclui tratamento de erros para garantir robustez.

- **src/processamento.py**  
	Realiza o processamento dos textos coletados.  
	- Limpa o texto (remove HTML, pontuação, acentos).
	- Classifica o sentimento usando uma abordagem baseada em regras (lexicons).
	- Busca por palavras, variações e substrings para melhorar a detecção de sentimentos negativos/positivos.
	- Retorna "positivo", "negativo" ou "neutro" para cada notícia.

- **src/lexicons.py**  
	Contém listas de palavras positivas e negativas.  
	- Lexicons foram ampliados com variações, termos compostos e contextos comuns em notícias.
	- Atualizações constantes para melhorar a sensibilidade do sistema.

- **src/utils.py**  
	Funções auxiliares para normalização de texto.  
	- Garante que as comparações sejam feitas de forma consistente.

- **app.py**  
	Dashboard principal em Streamlit.  
	- Interface interativa para busca, filtro por sentimento e visualização dos dados.
	- Gráfico de pizza para distribuição de sentimentos (cores intuitivas).
	- Nuvem de palavras para temas recorrentes.
	- Tabela de notícias com links clicáveis e exportação para CSV.
	- Mensagens claras para o usuário em caso de erro ou ausência de dados.
	- Rodapé explicando limitações da análise de sentimento.

- **data/**  
	Armazena os dados coletados e processados (ex: latest.csv).

- **tests/**  
	Testes automatizados para garantir o funcionamento dos principais módulos.

- **README.md**  
	Guia de uso, estrutura do projeto e instruções de execução.

- **DECISIONS.md**  
	Documentação das decisões técnicas, limitações e justificativas.

---

## Decisões Técnicas

- **Abordagem de Sentimento**  
	Optei por regras simples (lexicons) para garantir transparência, facilidade de explicação e evitar dependência de dados rotulados ou modelos complexos.

- **Tratamento de Erros**  
	O sistema informa o usuário sobre problemas de conexão, ausência de notícias ou falhas no processamento, sempre de forma clara.

- **Limitações**  
	A análise de sentimento não captura sarcasmo, ironia ou contextos complexos. Isso está destacado no dashboard.

- **Diferenciais**  
	- Filtros dinâmicos e exportação de dados.
	- Visualização intuitiva e design agradável.
	- Estrutura modular e testável.
	- Documentação clara e alinhada ao case.

---

## Entregáveis

- Código-fonte completo e organizado.
- Dashboard funcional.
- Arquivos README.md, DECISIONS.md e requirements.txt completos.
- CSV exportável com dados coletados e processados.

---

