# Mini Plano de Testes — BiblioTech

## 1. Identificação

**Equipe:** Arthur Marques Diniz

**Integrantes:** Arthur Marques Diniz

**Data:** 07/09/2026

---

## 2. Objetivo

Verificar se o módulo de empréstimos do BiblioTech atende aos requisitos funcionais
RF01 (permissão para empréstimo), RF02 (cálculo de multa) e RF03 (classificação de atraso),
produzindo evidências (casos de teste, testes automatizados e cobertura) para embasar a
recomendação de liberação (ou não) para produção.

Resposta: validar o comportamento das rotinas através de testes de caixa preta (a partir da
especificação) e de caixa branca (análise estrutural e de cobertura), registrando defeitos e
emitindo parecer de QA.

---

## 3. Escopo

### Funcionalidades que serão testadas

- RF01 — Permissão para empréstimo (`pode_emprestar`)
- RF02 — Cálculo de multa (`calcular_multa`)
- RF03 — Classificação de atraso (`classificar_atraso`)

### Fora do escopo

- Interface gráfica, banco de dados, autenticação
- Segurança, desempenho, acessibilidade
- Integração com sistemas externos
- Validação de tipos de dados
- Persistência das operações

---

## 4. Estratégia

### Caixa Preta

Marque as técnicas utilizadas:

- [x] Particionamento de equivalência
- [x] Análise de valores-limite
- [x] Cenários positivos
- [x] Cenários negativos

### Caixa Branca

Preenchido após o checkpoint.

Aspectos estruturais analisados:

- [x] Cobertura de linhas
- [x] Cobertura de branches (decisões e caminhos)
- [x] Valores-limite de cada ramo (bordas `<=`, `>`)
- [x] Caminhos individuais de cada função

Decisões analisadas:

- `pode_emprestar`: 3 decisões (`not usuario_ativo`, `possui_pendencia`, `emprestimos_ativos > LIMITE`)
- `calcular_multa`: 2 decisões (`dias_atraso <= 0`, `dias_atraso <= 7`)
- `classificar_atraso`: 3 decisões (`dias_atraso <= 0`, `<= 7`, `<= 30`)

---

## 5. Ambiente

**Sistema operacional:** Windows 11 PRO

**Versão do Python:** 3.14.4

**Framework de testes:** pytest 9.1.1 + pytest-cov 7.1.0

**Repositório:** https://github.com/SilV1966/bibliotech-testing-lab/template_aluno

---

## 6. Critérios de entrada

Quais condições devem estar atendidas antes da execução dos testes?

- Ambiente Python configurado com pytest e pytest-cov instalados
- Módulo `scr/bibliotech.py` disponível para importação
- Arquivo de configuração `pytest.ini` presente
- Especificação de requisitos (`requisitos.md`) disponível

---

## 7. Critérios de saída

Quando a equipe considerará a atividade de teste concluída?

- Todos os requisitos (RF01, RF02, RF03) cobertos por pelo menos um caso de teste
- Testes automatizados executando sem erros de infraestrutura
- Cobertura de linhas e branches calculada e registrada
- Defeitos (se houver) registrados e associados a requisitos
- Parecer de QA emitido com recomendação fundamentada
- Valor-limite do RF01 (3 empréstimos ativos) validado — revelou o BUG-01

---

## 8. Riscos

| Risco | Impacto | Mitigação |
|---|---|---|
| Especificação de requisitos incompleta/truncada | Definição de valores-limite ambígua | Derivar comportamento esperado do código e documentar premissas |
| Cobertura de 100% dar falsa sensação de segurança | Liberação indevida com defeito oculto | Complementar com análise de caixa branca e revisão dos requisitos |
| Ambiente com versão de Python divergente do CI | Diferença de resultado | Padronizar dependências via requirements-dev.txt |

---

## 9. Entregáveis

- [x] Casos de teste (roteiro_testes.md)
- [x] Testes automatizados (tests/)
- [x] Matriz de rastreabilidade (matriz_rastreabilidade.md)
- [x] Evidência de cobertura (saída do pytest --cov)
- [x] Registro de defeitos (BUG-01 — limite de empréstimos; BUG-02 — infraestrutura)
- [x] Pull Request
- [x] Parecer de QA (docs/parecer_qa.md — NÃO APROVAR)

---

## 10. Observações

- O template fornece o pacote de código em `scr/` (enquanto o enunciado e o smoke test
  original citam `src/`). A equipe **manteve a estrutura original** e adaptou os testes e
  o workflow para importar de `scr.bibliotech` e medir cobertura em `scr/`.
- O teste de valor-limite CP04/CT-03 revelou o defeito proposital do enunciado (BUG-01):
  o sistema permite empréstimo com exatamente 3 empréstimos ativos, contrariando o RF01
  ("menos de 3"). Parecer final: NÃO APROVAR para produção até a correção.
