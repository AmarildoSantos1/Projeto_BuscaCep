from consulta_cep.consulta_cep import buscar_endereco, formatar_endereco_completo


# -----------------------------
# Testes da função buscar_endereco
# -----------------------------

def test_buscar_endereco_sucesso(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "cep": "01001-000",
        "logradouro": "Praça da Sé",
        "bairro": "Sé",
        "localidade": "São Paulo",
        "uf": "SP"
    }
    mocker.patch("requests.get", return_value=mock_response)

    endereco = buscar_endereco("01001000")

    assert endereco is not None
    assert endereco["localidade"] == "São Paulo"


def test_buscar_endereco_nao_encontrado(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"erro": True}
    mocker.patch("requests.get", return_value=mock_response)

    assert buscar_endereco("99999999") is None


def test_buscar_endereco_formato_invalido(mocker):
    assert buscar_endereco("12345") is None
    assert buscar_endereco("abc") is None


# -----------------------------
# Testes da função formatar_endereco_completo
# -----------------------------

def test_formatar_endereco_completo_valido(mocker):
    mocker.patch(
        "consulta_cep.consulta_cep.buscar_endereco",
        return_value={
            "logradouro": "Praça da Sé",
            "bairro": "Sé",
            "localidade": "São Paulo",
            "uf": "SP"
        }
    )
    resultado = formatar_endereco_completo("01001000")
    assert resultado == "Praça da Sé, Sé - São Paulo/SP"


def test_formatar_endereco_completo_nao_encontrado(mocker):
    mocker.patch(
        "consulta_cep.consulta_cep.buscar_endereco",
        return_value=None  # Simula CEP não encontrado
    )
    resultado = formatar_endereco_completo("99999999")
    assert resultado is None


def test_formatar_endereco_completo_invalido(mocker):
    mocker.patch(
        "consulta_cep.consulta_cep.buscar_endereco",
        return_value=None  # Simula CEP inválido
    )
    resultado = formatar_endereco_completo("abc")
    assert resultado is None
