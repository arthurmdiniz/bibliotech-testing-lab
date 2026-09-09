# Roteiro de Testes — BiblioTech

Casos de teste elaborados na etapa de caixa preta a partir dos requisitos
(`requisitos.md`), no formato enxuto definido na missão.

---

# Caso de Teste

ID: CT-01

Requisito:

RF01

Título:

Usuário ativo, sem pendências e sem empréstimos pode realizar empréstimo.

Tipo:

Caixa preta

Prioridade:

Alta

Pré-condição:

Sistema disponível e usuário ativo.

Dados de teste:

usuario_ativo = True

possui_pendencia = False

emprestimos_ativos = 0

Passos:

1. Executar pode_emprestar(True, False, 0).

Resultado esperado:

True

Resultado obtido:

True

Status:

[x] Passou

[ ] Falhou

---

# Caso de Teste

ID: CT-02

Requisito:

RF01

Título:

Usuário inativo não pode realizar empréstimo.

Tipo:

Caixa preta

Prioridade:

Alta

Pré-condição:

Sistema disponível e usuário inativo.

Dados de teste:

usuario_ativo = False

possui_pendencia = False

emprestimos_ativos = 0

Passos:

1. Executar pode_emprestar(False, False, 0).

Resultado esperado:

False

Resultado obtido:

False

Status:

[x] Passou

[ ] Falhou

---

# Caso de Teste

ID: CT-03

Requisito:

RF01

Título:

Usuário com três empréstimos não pode realizar outro empréstimo.

Tipo:

Caixa preta

Prioridade:

Alta

Pré-condição:

Sistema disponível e usuário ativo.

Dados de teste:

usuario_ativo = True

possui_pendencia = False

emprestimos_ativos = 3

Passos:

1. Executar pode_emprestar(True, False, 3).

Resultado esperado:

False

Resultado obtido:

True

Status:

[ ] Passou

[x] Falhou

Observações:

Defeito revelado. O código permite empréstimo com 3 empréstimos ativos, mas o requisito
determina que é preciso possuir menos de 3. Registrado como BUG-01.

---

# Caso de Teste

ID: CT-04

Requisito:

RF01

Título:

Usuário com empréstimos acima do limite não pode realizar empréstimo.

Tipo:

Caixa preta

Prioridade:

Alta

Pré-condição:

Sistema disponível e usuário ativo.

Dados de teste:

usuario_ativo = True

possui_pendencia = False

emprestimos_ativos = 4

Passos:

1. Executar pode_emprestar(True, False, 4).

Resultado esperado:

False

Resultado obtido:

False

Status:

[x] Passou

[ ] Falhou

---

# Caso de Teste

ID: CT-05

Requisito:

RF01

Título:

Usuário com pendência não pode realizar empréstimo.

Tipo:

Caixa preta

Prioridade:

Alta

Pré-condição:

Sistema disponível e usuário ativo com pendência.

Dados de teste:

usuario_ativo = True

possui_pendencia = True

emprestimos_ativos = 0

Passos:

1. Executar pode_emprestar(True, True, 0).

Resultado esperado:

False

Resultado obtido:

False

Status:

[x] Passou

[ ] Falhou

---

# Caso de Teste

ID: CT-06

Requisito:

RF01

Título:

Usuário com dois empréstimos (menos de 3) pode realizar empréstimo.

Tipo:

Caixa preta

Prioridade:

Alta

Pré-condição:

Sistema disponível e usuário ativo.

Dados de teste:

usuario_ativo = True

possui_pendencia = False

emprestimos_ativos = 2

Passos:

1. Executar pode_emprestar(True, False, 2).

Resultado esperado:

True

Resultado obtido:

True

Status:

[x] Passou

[ ] Falhou

---

# Caso de Teste

ID: CT-07

Requisito:

RF01

Título:

Usuário inativo com pendência não pode realizar empréstimo.

Tipo:

Caixa preta

Prioridade:

Média

Pré-condição:

Sistema disponível e usuário inativo com pendência.

Dados de teste:

usuario_ativo = False

possui_pendencia = True

emprestimos_ativos = 0

Passos:

1. Executar pode_emprestar(False, True, 0).

Resultado esperado:

False

Resultado obtido:

False

Status:

[x] Passou

[ ] Falhou

---

# Caso de Teste

ID: CT-08

Requisito:

RF02

Título:

Sem atraso não gera multa.

Tipo:

Caixa preta

Prioridade:

Alta

Pré-condição:

Sistema disponível.

Dados de teste:

dias_atraso = 0

Passos:

1. Executar calcular_multa(0).

Resultado esperado:

0.0

Resultado obtido:

0.0

Status:

[x] Passou

[ ] Falhou

---

# Caso de Teste

ID: CT-09

Requisito:

RF02

Título:

Multa de R$ 2,00 por dia para atraso de 3 dias.

Tipo:

Caixa preta

Prioridade:

Alta

Pré-condição:

Sistema disponível.

Dados de teste:

dias_atraso = 3

Passos:

1. Executar calcular_multa(3).

Resultado esperado:

6.0

Resultado obtido:

6.0

Status:

[x] Passou

[ ] Falhou

---

# Caso de Teste

ID: CT-10

Requisito:

RF02

Título:

Multa de R$ 2,00 por dia no limite de 7 dias.

Tipo:

Caixa preta

Prioridade:

Alta

Pré-condição:

Sistema disponível.

Dados de teste:

dias_atraso = 7

Passos:

1. Executar calcular_multa(7).

Resultado esperado:

14.0

Resultado obtido:

14.0

Status:

[x] Passou

[ ] Falhou

---

# Caso de Teste

ID: CT-11

Requisito:

RF02

Título:

Multa de R$ 14,00 + R$ 3,00 por dia excedente no primeiro dia da faixa (8 dias).

Tipo:

Caixa preta

Prioridade:

Alta

Pré-condição:

Sistema disponível.

Dados de teste:

dias_atraso = 8

Passos:

1. Executar calcular_multa(8).

Resultado esperado:

17.0

Resultado obtido:

17.0

Status:

[x] Passou

[ ] Falhou

---

# Caso de Teste

ID: CT-12

Requisito:

RF02

Título:

Multa de R$ 14,00 + R$ 3,00 por dia excedente para 10 dias.

Tipo:

Caixa preta

Prioridade:

Média

Pré-condição:

Sistema disponível.

Dados de teste:

dias_atraso = 10

Passos:

1. Executar calcular_multa(10).

Resultado esperado:

23.0

Resultado obtido:

23.0

Status:

[x] Passou

[ ] Falhou

---

# Caso de Teste

ID: CT-13

Requisito:

RF03

Título:

Sem atraso é classificado como "sem atraso".

Tipo:

Caixa preta

Prioridade:

Alta

Pré-condição:

Sistema disponível.

Dados de teste:

dias_atraso = 0

Passos:

1. Executar classificar_atraso(0).

Resultado esperado:

"sem atraso"

Resultado obtido:

"sem atraso"

Status:

[x] Passou

[ ] Falhou

---

# Caso de Teste

ID: CT-14

Requisito:

RF03

Título:

Atraso de 1 dia é classificado como "atraso leve".

Tipo:

Caixa preta

Prioridade:

Alta

Pré-condição:

Sistema disponível.

Dados de teste:

dias_atraso = 1

Passos:

1. Executar classificar_atraso(1).

Resultado esperado:

"atraso leve"

Resultado obtido:

"atraso leve"

Status:

[x] Passou

[ ] Falhou

---

# Caso de Teste

ID: CT-15

Requisito:

RF03

Título:

Atraso de 7 dias (limite da faixa) é classificado como "atraso leve".

Tipo:

Caixa preta

Prioridade:

Alta

Pré-condição:

Sistema disponível.

Dados de teste:

dias_atraso = 7

Passos:

1. Executar classificar_atraso(7).

Resultado esperado:

"atraso leve"

Resultado obtido:

"atraso leve"

Status:

[x] Passou

[ ] Falhou

---

# Caso de Teste

ID: CT-16

Requisito:

RF03

Título:

Atraso de 8 dias é classificado como "atraso moderado".

Tipo:

Caixa preta

Prioridade:

Alta

Pré-condição:

Sistema disponível.

Dados de teste:

dias_atraso = 8

Passos:

1. Executar classificar_atraso(8).

Resultado esperado:

"atraso moderado"

Resultado obtido:

"atraso moderado"

Status:

[x] Passou

[ ] Falhou

---

# Caso de Teste

ID: CT-17

Requisito:

RF03

Título:

Atraso de 30 dias (limite da faixa) é classificado como "atraso moderado".

Tipo:

Caixa preta

Prioridade:

Alta

Pré-condição:

Sistema disponível.

Dados de teste:

dias_atraso = 30

Passos:

1. Executar classificar_atraso(30).

Resultado esperado:

"atraso moderado"

Resultado obtido:

"atraso moderado"

Status:

[x] Passou

[ ] Falhou

---

# Caso de Teste

ID: CT-18

Requisito:

RF03

Título:

Atraso de 31 dias é classificado como "atraso grave".

Tipo:

Caixa preta

Prioridade:

Alta

Pré-condição:

Sistema disponível.

Dados de teste:

dias_atraso = 31

Passos:

1. Executar classificar_atraso(31).

Resultado esperado:

"atraso grave"

Resultado obtido:

"atraso grave"

Status:

[x] Passou

[ ] Falhou

---

# Caso de Teste

ID: CT-19

Requisito:

RF03

Título:

Dias de atraso negativos são tratados como "sem atraso".

Tipo:

Caixa preta

Prioridade:

Média

Pré-condição:

Sistema disponível.

Dados de teste:

dias_atraso = -1

Passos:

1. Executar classificar_atraso(-1).

Resultado esperado:

"sem atraso"

Resultado obtido:

"sem atraso"

Status:

[x] Passou

[ ] Falhou

---

# Caso de Teste

ID: CT-20

Requisito:

RF03

Título:

Atraso de 90 dias é classificado como "atraso grave".

Tipo:

Caixa preta

Prioridade:

Baixa

Pré-condição:

Sistema disponível.

Dados de teste:

dias_atraso = 90

Passos:

1. Executar classificar_atraso(90).

Resultado esperado:

"atraso grave"

Resultado obtido:

"atraso grave"

Status:

[x] Passou

[ ] Falhou

---

# Registro de Defeito

## BUG-01 — Limite de empréstimos permite 3 empréstimos ativos

### Requisito associado

RF01

### Caso de teste

CT-03

### Entrada utilizada

pode_emprestar(True, False, 3)

### Resultado esperado

False

### Resultado obtido

True

### Prioridade sugerida

- [x] Alta
- [ ] Média
- [ ] Baixa

### Evidência

```
tests/test_caixa_preta_emprestimo.py::test_emprestimo_usuario_no_limite_deve_ser_recusado FAILED
E       assert True is False
E        +  where True = pode_emprestar(True, False, 3)
```

### Justificativa

A condição implementada (`emprestimos_ativos > LIMITE_EMPRESTIMOS`, limite 3) permite o
empréstimo quando o usuário possui exatamente 3 empréstimos ativos. O requisito RF01 é
explícito: o usuário poderá emprestar apenas se possuir **menos de 3** empréstimos ativos.
Erro de fronteira: o operador deveria ser `>=`.

### Observações

Defeito proposital da atividade. A equipe de QA não deve corrigir o código (`scr/`);
apenas registrar e reportar.