import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.validator import is_valid_cnpj, is_valid_cpf


client = TestClient(app)


def test_rf07_health_check():
    response = client.get("/v1/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.parametrize(
    ("cpf", "expected"),
    [
        ("111.444.777-35", True),
        ("11144477735", True),
        ("123.456.789-00", False),
        ("111.111.111-11", False),
        ("123", False),
        ("111.444.777-3500", False),
    ],
)
def test_rf03_cpf_validation(cpf, expected):
    assert is_valid_cpf(cpf) is expected


@pytest.mark.parametrize(
    ("cnpj", "expected"),
    [
        ("11.222.333/0001-81", True),
        ("11222333000181", True),
        ("11.222.333/0001-00", False),
        ("11.222.333/000", False),
        ("11.111.111/1111-11", False),
    ],
)
def test_rf03_cnpj_validation(cnpj, expected):
    assert is_valid_cnpj(cnpj) is expected


@pytest.mark.parametrize(
    ("text", "entity", "matched_value"),
    [
        ("Meu CPF é 111.444.777-35", "CPF", "111.444.777-35"),
        ("Empresa CNPJ 11.222.333/0001-81", "CNPJ", "11.222.333/0001-81"),
        ("Contato: ana@empresa.com", "EMAIL", "ana@empresa.com"),
        ("Ligue 11 99999-9999", "TELEFONE", "11 99999-9999"),
        ("Envie para 01001-000", "CEP", "01001-000"),
        ("Cartão 4111 1111 1111 1234", "CARTAO_CREDITO", "4111 1111 1111 1234"),
        ("Documento RG 12.345.678-9", "RG", "12.345.678-9"),
        ("Me chamo João Paulo", "NOME", "João Paulo"),
        ("Rua das Flores, 123", "ENDERECO", "Rua das Flores, 123"),
    ],
)
def test_rf01_rf02_detects_configured_entity(text, entity, matched_value):
    response = client.post(
        "/v1/scan", json={"text": text, "config": {"entities": [entity]}}
    )

    assert response.status_code == 200
    findings = response.json()["findings"]
    assert len(findings) == 1
    assert findings[0]["type"] == entity
    assert text[findings[0]["start"] : findings[0]["end"]] == matched_value


@pytest.mark.parametrize(
    ("entity", "sensitivity"),
    [("CPF", "ALTA"), ("EMAIL", "MEDIA"), ("CEP", "BAIXA")],
)
def test_rn03_classifies_sensitivity(entity, sensitivity):
    values = {
        "CPF": "111.444.777-35",
        "EMAIL": "ana@empresa.com",
        "CEP": "01001-000",
    }
    response = client.post(
        "/v1/scan", json={"text": values[entity], "config": {"entities": [entity]}}
    )

    assert response.status_code == 200
    assert response.json()["findings"][0]["sensitivity"] == sensitivity


@pytest.mark.parametrize("strategy", ["MASK", "REDACT", "HASH"])
def test_rf04_applies_configured_strategy(strategy):
    original = "ana@empresa.com"
    response = client.post(
        "/v1/scan",
        json={
            "text": original,
            "config": {"entities": ["EMAIL"], "strategy": strategy},
        },
    )

    assert response.status_code == 200
    result = response.json()
    assert result["findings"][0]["value_masked"] == result["sanitized_text"]
    assert original not in result["sanitized_text"]
    if strategy == "MASK":
        assert result["sanitized_text"] == "***@empresa.com"
    elif strategy == "REDACT":
        assert result["sanitized_text"] == "[REDACTED]"
    else:
        assert result["sanitized_text"].startswith("[HASH:")


@pytest.mark.parametrize(
    ("entity", "original", "expected"),
    [
        ("CPF", "111.444.777-35", "***.***.***-35"),
        ("EMAIL", "ana@empresa.com", "***@empresa.com"),
        ("CARTAO_CREDITO", "4111 1111 1111 1234", "**** **** **** 1234"),
    ],
)
def test_rn05_masking_rules(entity, original, expected):
    response = client.post(
        "/v1/scan", json={"text": original, "config": {"entities": [entity]}}
    )

    assert response.status_code == 200
    assert response.json()["findings"][0]["value_masked"] == expected


@pytest.mark.parametrize("text", ["", "   "])
def test_rf08_empty_text_returns_structured_error(text):
    response = client.post("/v1/scan", json={"text": text})

    assert response.status_code == 400
    assert response.json()["error"]["code"] == "INVALID_PAYLOAD"
    assert response.json()["error"]["message"]


@pytest.mark.parametrize("payload", [{}, {"text": None}])
def test_rf08_missing_or_null_text_returns_client_error(payload):
    response = client.post("/v1/scan", json=payload)

    assert response.status_code == 400
    assert response.json()["error"]["code"] == "INVALID_PAYLOAD"
    assert response.json()["error"]["message"]


def test_rf08_unknown_entity_returns_client_error():
    response = client.post(
        "/v1/scan", json={"text": "Teste", "config": {"entities": ["ENTIDADE_FALSA"]}}
    )

    assert response.status_code == 400
    assert response.json()["error"]["code"] == "INVALID_PAYLOAD"
    assert response.json()["error"]["message"]


def test_section9_text_without_personal_data_returns_empty_findings():
    text = "Um texto comum sem nada sensível."
    response = client.post("/v1/scan", json={"text": text})

    assert response.status_code == 200
    assert response.json()["findings"] == []
    assert response.json()["sanitized_text"] == text


def test_section9_multiple_findings_are_ordered_and_keep_offsets():
    text = "Emails: a@a.com, b@b.com. Número 11144477735."
    response = client.post("/v1/scan", json={"text": text})

    assert response.status_code == 200
    findings = response.json()["findings"]
    assert [finding["type"] for finding in findings] == ["EMAIL", "EMAIL", "CPF"]
    assert [finding["start"] for finding in findings] == sorted(
        finding["start"] for finding in findings
    )
    assert all(
        text[finding["start"] : finding["end"]]
        for finding in findings
    )
    assert "a@a.com" not in response.json()["sanitized_text"]
    assert "b@b.com" not in response.json()["sanitized_text"]


def test_section9_overlapping_phone_and_cpf_keeps_more_sensitive_cpf():
    text = "11144477735"
    response = client.post("/v1/scan", json={"text": text})

    assert response.status_code == 200
    findings = response.json()["findings"]
    assert [finding["type"] for finding in findings] == ["CPF"]


def test_section9_processes_text_with_10000_characters():
    text = "x " * 5000
    response = client.post("/v1/scan", json={"text": text})

    assert response.status_code == 200
    assert response.json()["findings"] == []
    assert response.json()["sanitized_text"] == text


def test_rn06_audit_contains_metadata_without_original_value():
    original = "ana@empresa.com"
    response = client.post("/v1/scan", json={"text": original})

    assert response.status_code == 200
    result = response.json()
    assert result["audit"]["total_findings"] == len(result["findings"])
    assert result["audit"]["strategy_applied"] == "MASK"
    assert original not in str(result["audit"])