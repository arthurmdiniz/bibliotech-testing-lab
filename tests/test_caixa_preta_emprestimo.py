from scr.bibliotech import pode_emprestar

LIMITE = 3


def test_emprestimo_usuario_ativo_sem_pendencia_dentro_do_limite():
    assert pode_emprestar(True, False, 0) is True


def test_emprestimo_usuario_ativo_sem_pendencia_com_dois_emprestimos():
    assert pode_emprestar(True, False, LIMITE - 1) is True


def test_emprestimo_usuario_no_limite_deve_ser_recusado():
    assert pode_emprestar(True, False, LIMITE) is False


def test_emprestimo_usuario_inativo():
    assert pode_emprestar(False, False, 0) is False


def test_emprestimo_usuario_com_pendencia():
    assert pode_emprestar(True, True, 0) is False


def test_emprestimo_com_limite_excedido():
    assert pode_emprestar(True, False, LIMITE + 1) is False


def test_emprestimo_usuario_inativo_com_pendencia():
    assert pode_emprestar(False, True, 0) is False
