"""
Exemplo de teste para o João Paulo usar como ponto de partida no Test Harness.
Cobre a RN01 (validação de CPF) descrita em docs/SPECIFICATION.md.

A suíte completa (cenários principais + casos de borda da seção 9 da spec)
é responsabilidade da frente de Test Harness — este arquivo é só o pontapé inicial.
"""
from app.validator import is_valid_cpf, is_valid_cnpj


def test_cpf_valido_e_aceito():
    assert is_valid_cpf("111.444.777-35") is True


def test_cpf_com_digitos_repetidos_e_invalido():
    # RN01: mesmo que "feche" matematicamente, sequência repetida é inválida
    assert is_valid_cpf("111.111.111-11") is False


def test_cpf_com_tamanho_errado_e_invalido():
    assert is_valid_cpf("123") is False


def test_cnpj_valido_e_aceito():
    assert is_valid_cnpj("11.222.333/0001-81") is True


def test_cnpj_invalido_e_rejeitado():
    assert is_valid_cnpj("11.222.333/0001-00") is False
