from scr.bibliotech import calcular_multa


def test_multa_sem_atraso():
    assert calcular_multa(0) == 0.0


def test_multa_um_dia():
    assert calcular_multa(1) == 2.0


def test_multa_sete_dias():
    assert calcular_multa(7) == 14.0


def test_multa_oito_dias():
    assert calcular_multa(8) == 17.0


def test_multa_dez_dias():
    assert calcular_multa(10) == 23.0


def test_multa_muitos_dias():
    assert calcular_multa(100) == 14.0 + (93 * 3.0)
