from consulta_cep.consulta_cep import buscar_endereco, formatar_endereco_completo


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



# Testes para formatar_endereco_completo


def test_formatar_endereco_completo_sucesso(mocker):
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

    resultado = formatar_endereco_completo("01001000")
    assert resultado == "Praça da Sé, Sé - São Paulo/SP"


def test_formatar_endereco_completo_nao_encontrado(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"erro": True}
    mocker.patch("requests.get", return_value=mock_response)

    resultado = formatar_endereco_completo("99999999")
    assert resultado is None


def test_formatar_endereco_completo_formato_invalido():
    assert formatar_endereco_completo("12345") is None
    assert formatar_endereco_completo("abcdefg") is None

