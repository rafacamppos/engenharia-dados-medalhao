from src.request.http_client import HttpClient, API_BASE_URL, PRODUCTS_ENDPOINT, USERS_ENDPOINT

class BronzeIngestionService:
    def __init__(self):
        self.client = HttpClient(API_BASE_URL)

    def fetch_products(self):
        """
        Busca todos os produtos da FakeStore API e retorna a lista de dicionários.
        """
        return self.client.get(PRODUCTS_ENDPOINT)
    
    def fetch_users(self):
        """
        Busca todos os usuários da FakeStore API e retorna a lista de dicionários.
        """
        return self.client.get(USERS_ENDPOINT)

if __name__ == '__main__':
    service = BronzeIngestionService()
    products = service.fetch_products()
    users = service.fetch_users()
    print(f"Total de produtos obtidos: {len(products)}")
    print(f"Total de usuarios obtidos: {len(users)}")
    # exibe apenas os 3 primeiros para exemplo
    for p in products[:3]:
        print(f"- {p['id']}: {p['title']} (R${p['price']})")

    for p in users[:3]:
        print(f"- {p['id']}: {p['username']} {p['email']}")