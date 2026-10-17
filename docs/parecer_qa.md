# Parecer Técnico de QA — BiblioTech

## Equipe

**Equipe:** Arthur Marques Diniz

**Integrantes:** Arthur Marques Diniz

**Data:** 07/09/2026

---

# Requisitos verificados

- [x] RF01
- [x] RF02
- [x] RF03

---

# Caixa Preta

## Quantidade de casos

Resposta: 21 casos de caixa preta (executados nos arquivos `test_caixa_preta_*.py`);
20 estão documentados no `roteiro_testes.md` (CT-01 a CT-20).

## Técnicas utilizadas

- [x] Particionamento de equivalência
- [x] Valores-limite
- [x] Cenários positivos
- [x] Cenários negativos

## Principal descoberta

Resposta: O teste de valor-limite CP04/CT-03 revelou o defeito proposital da atividade:
`pode_emprestar(True, False, 3)` retorna `True`, mas o requisito RF01 determina que só
quem possui **menos de 3** empréstimos ativos pode realizar novo empréstimo (esperado
`False`). Defeito registrado como BUG-01.

---

# Caixa Branca

## Decisões analisadas

Resposta:
- `pode_emprestar`: 3 decisões — `not usuario_ativo`, `possui_pendencia`,
  `emprestimos_ativos > LIMITE_EMPRESTIMOS`.
- `calcular_multa`: 2 decisões — `dias_atraso <= 0`, `dias_atraso <= 7`.
- `classificar_atraso`: 3 decisões — `dias_atraso <= 0`, `<= 7`, `<= 30`.

## Novos testes criados após analisar o código

Resposta: `tests/test_caixa_branca.py` — 11 testes que cobrem explicitamente cada ramo
e cada condição de fronteira das três funções (incluindo o limite padrão
`LIMITE_EMPRESTIMOS == 3`). A análise estrutural confirmou que a condição de fronteira
do RF01 usa `>` em vez de `>=`, confirmando o BUG-01.

---

# Cobertura

## Cobertura de linhas

100 %

## Cobertura de branches

100 %

## Observação sobre cobertura

A cobertura continua em 100% mesmo com o teste BUG-01 falhando, porque o teste executa
todas as linhas/branches do trecho antes da asserção. Isso demonstra que cobertura
elevada não equivale a ausência de defeitos.

---

# Execução

**Total de testes:** 33

**Testes aprovados:** 32

**Testes reprovados:** 1 (teste que revela o BUG-01)

---

# Defeitos encontrados

## BUG-01 — Limite de empréstimos permite 3 empréstimos ativos

**Requisito associado:** RF01

**Caso de teste:** CT-03 (CP04)

**Entrada utilizada:** `pode_emprestar(True, False, 3)`

**Resultado esperado:** `False` (requisito: menos de 3 empréstimos ativos)

**Resultado obtido:** `True`

**Prioridade:** Alta

**Justificativa:** A condição `emprestimos_ativos > LIMITE_EMPRESTIMOS` (limite 3) permite
o empréstimo com exatamente 3 empréstimos ativos; o requisito exige **menos de 3**
(deveria ser `>=`). Erro de fronteira que libera empréstimo em desacordo com a regra de
negócio.

## OBS-01 — Estrutura do pacote de código adaptada (infraestrutura)

**Requisito associado:** não se aplica (infraestrutura do repositório)

**Caso de teste:** execução da suíte/pipeline

**Entrada utilizada:** comando `python -m pytest --cov=scr` e `import scr.bibliotech`

**Resultado esperado:** testes executando mantendo a estrutura original do template

**Resultado obtido:** o template fornece o código em `scr/` (enunciado e smoke test
original citam `src/`); para não alterar o diretório de produção, testes e workflow
foram adaptados para `scr.bibliotech` e `--cov=scr`

**Prioridade:** Baixa

**Justificativa:** não afeta a lógica de negócio; mantém o repositório fiel ao fornecido,
adaptando apenas imports de teste e configuração de CI.

---

# GitHub Actions

## Resultado da pipeline (execução local equivalente)

- [ ] Sucesso
- [x] Falha

## Interpretação

Resposta: O comando executado pela action de CI falha por causa do teste
`test_emprestimo_usuario_no_limite_deve_ser_recusado`, que corretamente revela o
BUG-01. Uma pipeline vermelha aqui é o resultado **correto**: o teste que protege o
requisito RF01 falha porque o código não atende ao requisito. A pipeline deve, portanto,
**bloquear a entrega** até a correção do BUG-01 (em `scr/`, pela equipe de desenvolvedores).

---

# Parecer de QA

A equipe recomenda:

- [ ] APROVAR PARA PRODUÇÃO
- [x] NÃO APROVAR PARA PRODUÇÃO

## Justificativa

Resposta: O requisito RF01 não é atendido para o valor-limite de 3 empréstimos ativos:
o sistema libera um novo empréstimo quando o usuário já possui 3, contrariando a
especificação ("possuir menos de 3 empréstimos ativos"). O defeito (BUG-01) tem
prioridade alta e impacto direto na regra de negócio, com evidência reproduzível no
teste automatizado. RF02 e RF03 foram validados sem divergências (100% de cobertura de
linhas e branches), mas a liberação em produção depende da correção do BUG-01 pela
equipe de desenvolvimento.

---

# Reflexão

## Um teste criado exclusivamente a partir dos requisitos

Resposta: CT-03/CP04 (empréstimo com exatamente 3 empréstimos ativos deve ser negado) —
derivado da leitura literal do requisito RF01 ("menos de 3 empréstimos ativos"), sem
consultar o código.

## Um teste cuja importância ficou mais clara depois da análise do código

Resposta: O teste da fronteira de 7→8 dias na multa (CT-10 e CT-11) — somente a leitura do
código revelou a mudança de fórmula em `14.0 + (dias - 7) * 3.0`. Além dele, a análise
de caixa branca confirmou visualmente a causa raiz do BUG-01 (`>` em vez de `>=`).

## Cobertura elevada significa necessariamente ausência de defeitos?

Resposta: Não. Este laboratório é a prova concreta: com 100% de cobertura de linhas e
branches, um defeito de lógica de fronteira (BUG-01) permaneceu ativo e foi encontrado
pelo teste de valor-limite. A cobertura (100%) mede o que foi executado, e o defeito
continua existindo dentro do código executado.
