import os
import logging
import requests
from dotenv import load_dotenv


# Determina a raiz do projeto dinamicamente
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dotenv_path = os.path.join(BASE_DIR, 'configs/.env')

# Carrega o .env da raiz
load_dotenv(dotenv_path=dotenv_path)

API_BASE_URL = os.getenv('API_BASE_URL')
PRODUCTS_ENDPOINT = os.getenv('PRODUCTS_ENDPOINT')
USERS_ENDPOINT = os.getenv('USERS_ENDPOINT')

# configurar logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s: %(message)s'
)
logger = logging.getLogger('HttpClient')

class HttpClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        # Timeout padrão para todas as requisições
        self.timeout = (5, 15)  # (connect timeout, read timeout)

    def get(self, path: str, params: dict = None) -> dict:
        url = f"{self.base_url}{path}"
        try:
            logger.info(f"GET {url} params={params}")
            resp = self.session.get(url, params=params, timeout=self.timeout)
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as e:
            logger.error(f"Erro ao chamar {url}: {e}")
            raise