import requests

def buscar_endereco_via_cep(cep):
    try:
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        response.raise_for_status()  # Levanta um erro se a requisição não teve sucesso
        dados = response.json()
        if 'erro' in dados:
            return None
        return {
            'rua': dados.get('logradouro', ''),
            'bairro': dados.get('bairro', ''),
            'cidade': dados.get('localidade', ''),
            'estado': dados.get('uf', '')
        }
    except requests.RequestException as e:
        print(f"Erro ao buscar o CEP: {e}")
        return None
