import requests

def buscar_endereco(cep: str) -> dict | None:
    """
    Busca um endereço a partir de um CEP na API ViaCEP.
    Retorna um dicionário com os dados do endereço ou None se não for encontrado.
    """
    if not isinstance(cep, str) or not cep.isdigit() or len(cep) != 8:
        return None 

    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status() 
        
        dados = response.json()
        
        # A API ViaCEP retorna {"erro": true} para CEPs que não existem
        if dados.get("erro"):
            return None
            
        return dados
    except requests.RequestException:
        # Captura erros de conexão, timeout, etc.
        return None


def formatar_endereco_completo(cep: str) -> str | None:
    """
    Retorna o endereço completo formatado no padrão:
    Logradouro, Bairro - Cidade/UF.
    
    Exemplo: "Praça da Sé, Sé - São Paulo/SP"
    """
    dados = buscar_endereco(cep)
    
    if not dados:
        return None
    
    logradouro = dados.get("logradouro", "").strip()
    bairro = dados.get("bairro", "").strip()
    cidade = dados.get("localidade", "").strip()
    uf = dados.get("uf", "").strip()
    
    # Monta a string formatada
    return f"{logradouro}, {bairro} - {cidade}/{uf}"


