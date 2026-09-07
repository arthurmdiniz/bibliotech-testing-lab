# Missão QA — BiblioTech

## Testes de Caixa Preta e Caixa Branca com Python e GitHub

**Disciplina:** Garantia da Qualidade do Software  
**Duração:** 90 minutos  
**Tecnologias:** Python, pytest, pytest-cov, GitHub e GitHub Actions  
**Organização:** duplas ou trios  

---

# 1. Situação-problema

Você integra temporariamente a equipe de Quality Assurance (QA) do BiblioTech, uma biblioteca digital.

Uma nova versão do módulo de empréstimos está sendo preparada para produção.

A equipe de desenvolvimento afirma que o sistema está pronto para liberação.

Sua equipe recebeu a missão de verificar se a versão realmente atende aos requisitos e produzir evidências suficientes para recomendar ou não sua liberação.

Ao longo da atividade serão utilizadas duas estratégias:

1. Teste de Caixa Preta.
2. Teste de Caixa Branca.

Ao final da missão, sua equipe deverá responder:

> A versão atual do BiblioTech pode ser liberada para produção?

A decisão deverá ser sustentada pelas evidências produzidas durante os testes.

---

# 2. Objetivos

Ao finalizar o laboratório, sua equipe deverá ser capaz de:

- elaborar casos de teste a partir de requisitos;
- identificar classes de equivalência;
- identificar valores-limite;
- criar cenários positivos e negativos;
- automatizar testes utilizando pytest;
- analisar decisões e caminhos internos do programa;
- interpretar cobertura de código;
- relacionar requisitos e casos de teste;
- registrar evidências no GitHub;
- utilizar Pull Requests;
- interpretar a execução da integração contínua;
- emitir um parecer técnico de QA.

---

# 3. Regras da missão

## Regra 1 — Caixa Preta

Durante a primeira etapa:

**NÃO abra o arquivo:**

`src/bibliotech.py`

Sua principal fonte de informação será:

`requisitos.md`

Construa os testes a partir da especificação do comportamento esperado.

---

## Regra 2 — Código de produção

Durante toda a atividade:

**NÃO modifique arquivos da pasta `src/`.**

Sua equipe atua como equipe de QA.

Caso encontre um defeito:

- registre o comportamento;
- reproduza o problema;
- associe-o a um requisito;
- registre evidências;
- emita um parecer.

Não corrija o código durante a missão.

Arquivos que podem ser modificados:

- `tests/`
- `docs/`

---

## Regra 3 — Teste vermelho

Um teste que falha não significa necessariamente que o teste está errado.

Caso um teste fique vermelho:

1. confira o requisito;
2. confira a entrada utilizada;
3. confira o resultado esperado;
4. confira o resultado obtido;
5. investigue a divergência.

Não altere um teste correto apenas para fazê-lo passar.

---

# 4. Preparação do ambiente

## 4.1 Clone o repositório

```bash
git clone URL_FORNECIDA_PELO_PROFESSOR
cd bibliotech-testing-lab
