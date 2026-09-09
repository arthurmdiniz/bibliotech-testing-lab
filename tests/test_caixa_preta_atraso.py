from scr.bibliotech import classificar_atraso


def test_atraso_sem_atraso_zero():
    assert classificar_atraso(0) == "sem atraso"


def test_atraso_sem_atraso_negativo():
    assert classificar_atraso(-1) == "sem atraso"


def test_atraso_leve_minimo():
    assert classificar_atraso(1) == "atraso leve"


def test_atraso_leve_maximo():
    assert classificar_atraso(7) == "atraso leve"


def test_atraso_moderado_minimo():
    assert classificar_atraso(8) == "atraso moderado"


def test_atraso_moderado_maximo():
    assert classificar_atraso(30) == "atraso moderado"


def test_atraso_grave_minimo():
    assert classificar_atraso(31) == "atraso grave"


def test_atraso_grave_muitos_dias():
    assert classificar_atraso(90) == "atraso grave"
