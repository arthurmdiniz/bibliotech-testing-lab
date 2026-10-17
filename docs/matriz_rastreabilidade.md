# Matriz de Rastreabilidade — BiblioTech

## Objetivo

Relacionar requisitos aos casos de teste e verificar se todos os requisitos possuem evidências de validação.

---

| Requisito | Casos de Caixa Preta | Casos de Caixa Branca | Coberto? |
|---|---|---|---|
| RF01 | CT-01, CT-02, CT-03, CT-04, CT-05, CT-06, CT-07 | `test_caixa_branca.py`: limite (3), inativo, pendência, limite excedido | Sim (defeito BUG-01) |
| RF02 | CT-08, CT-09, CT-10, CT-11, CT-12 | `test_caixa_branca.py`: multa sem atraso, até 7 dias, acima de 7 dias | Sim |
| RF03 | CT-13, CT-14, CT-15, CT-16, CT-17, CT-18, CT-19, CT-20 | `test_caixa_branca.py`: sem atraso, leve, moderado, grave | Sim |

---

# Análise

## Existe requisito sem teste?

Resposta: Não. Todos os requisitos (RF01, RF02 e RF03) possuem casos de teste de
caixa preta e de caixa branca associados.

---

## Existe caso de teste sem requisito claramente associado?

Resposta: Não. Cada caso de teste está vinculado a um dos requisitos (RF01, RF02 ou RF03).

---

## Qual requisito apresentou maior risco durante a atividade?

Resposta: RF01 — Permissão para empréstimo. Apresenta duas condições booleanas e uma
fronteira crítica (menos de 3 empréstimos), e é justamente nessa fronteira que foi
encontrado o defeito BUG-01.

---

## Justificativa

Resposta: RF01 contém o defeito proposital da atividade: a condição
`emprestimos_ativos > 3` permite empréstimo com exatamente 3 empréstimos ativos,
enquanto o requisito exige **menos de 3** (`>=`). Isso só foi revelado pelo teste de
valor-limite (CP04/CT-03), comprovando a importância da análise de borda. RF02 e RF03
apresentaram forte risco nas fronteiras (7/8 e 30/31 dias), mas foram validados sem
divergências.

---

# Cobertura

## Cobertura de linhas

Resultado:

100 %

## Cobertura de branches

Resultado:

100 %

---

# Observações

- A cobertura de 100% de linhas e branches foi atingida, inclusive com o teste BUG-01
  executando o caminho do limite (a falha de asserção não reduz a cobertura).
- Isso reforça o princípio didático da missão: **100% de cobertura não significa
  ausência de defeitos** — o BUG-01 é funcional e foi detectado pela análise de
  valor-limite, não pela cobertura.
- Como a especificação `requisitos.md` estava truncada neste template, o comportamento
  esperado foi derivado do enunciado da atividade (PDF) e do código (`scr/bibliotech.py`).
