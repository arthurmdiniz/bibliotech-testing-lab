from scr.bibliotech import (
    LIMITE_EMPRESTIMOS,
    pode_emprestar,
    calcular_multa,
    classificar_atraso,
)


def test_limite_emprestimos_e_tres():
    assert LIMITE_EMPRESTIMOS == 3


def test_branch_emprestimo_usuario_inativo_retorna_falso_antes_da_pendencia():
    assert pode_emprestar(False, False, 0) is False


def test_branch_emprestimo_pendencia_retorna_falso_antes_do_limite():
    assert pode_emprestar(True, True, LIMITE_EMPRESTIMOS + 5) is False


def test_branch_emprestimo_limite_excedido_retorna_falso():
    assert pode_emprestar(True, False, LIMITE_EMPRESTIMOS + 1) is False


def test_branch_multa_sem_atraso_retorna_zero():
    assert calcular_multa(0) == 0.0


def test_branch_multa_ate_sete_dias():
    assert calcular_multa(7) == 7 * 2.0


def test_branch_multa_acima_de_sete_dias():
    assert calcular_multa(8) == 14.0 + (1 * 3.0)


def test_branch_classificacao_sem_atraso():
    assert classificar_atraso(0) == "sem atraso"


def test_branch_classificacao_atraso_leve():
    assert classificar_atraso(7) == "atraso leve"


def test_branch_classificacao_atraso_moderado():
    assert classificar_atraso(30) == "atraso moderado"


def test_branch_classificacao_atraso_grave():
    assert classificar_atraso(31) == "atraso grave"
