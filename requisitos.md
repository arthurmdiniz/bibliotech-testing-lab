# BiblioTech — Especificação de Requisitos

Versão: 2.0

---

# 1. Objetivo do documento

Este documento apresenta os requisitos funcionais que deverão ser utilizados pela equipe de QA durante a primeira etapa da atividade.

Durante a fase de Teste de Caixa Preta, este documento deverá ser a principal fonte de informação para elaboração dos casos de teste.

IMPORTANTE:

Durante a etapa de Caixa Preta, não consulte o código-fonte localizado em:

`src/bibliotech.py`

---

# 2. Escopo da atividade

Serão avaliadas três funcionalidades do módulo de empréstimos do sistema BiblioTech:

- RF01 — Permissão para empréstimo;
- RF02 — Cálculo de multa;
- RF03 — Classificação de atraso.

---

# 3. Fora do escopo

Nesta atividade não serão avaliados:

- interface gráfica;
- banco de dados;
- autenticação;
- segurança;
- desempenho;
- acessibilidade;
- integração com sistemas externos;
- validação de tipos de dados;
- persistência das operações.

---

# 4. Premissas dos dados de entrada

Para esta atividade, considere as seguintes premissas.

## usuario_ativo

Tipo:

`bool`

Valores possíveis:

```text
True
False
