import os
import logging
import requests
from dotenv import load_dotenv
from typing import Dict, List


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
        #self.timeout = (5, 15)  # (connect timeout, read timeout)

    def get_json_api(self, base_url: str, endpoint: str, timeout: int = 10) -> List[Dict]:
        """
        Busca dados JSON da API e retorna lista de registros.
        """
        url = f"{base_url.rstrip('/')}{endpoint}"
        logger.info("Fetching data from %s", url)
        resp = requests.get(url, timeout=timeout)
        resp.raise_for_status()
        data = resp.json()
        if not isinstance(data, list):
            logger.error("Expected list but got %s", type(data))
            raise ValueError("API não retornou lista de registros")
        return data