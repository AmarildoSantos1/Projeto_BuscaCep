from consulta_cep.consulta_cep import buscar_endereco


def test_buscar_endereco_sucesso(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "cep": "01001-000",
        "logradouro": "Praça da Sé",
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
