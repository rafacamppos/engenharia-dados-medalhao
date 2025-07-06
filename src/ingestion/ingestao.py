from src.request.http_client import HttpClient, API_BASE_URL, PRODUCTS_ENDPOINT, USERS_ENDPOINT
from pyspark.sql import SparkSession, DataFrame
from typing import Dict, List
from pyspark.sql import SparkSession

class BronzeIngestionService:
    def __init__(self):
        self.client = HttpClient(API_BASE_URL)

    def get_products(self):
        """
        Busca todos os produtos da FakeStore API e retorna a lista de dicionários.
        """
        return self.client.get_json_api(API_BASE_URL, PRODUCTS_ENDPOINT)
        #return self.client.get(PRODUCTS_ENDPOINT)
    
    def get_users(self):
        """
        Busca todos os usuários da FakeStore API e retorna a lista de dicionários.
        """
        return self.client.get_json_api(API_BASE_URL, USERS_ENDPOINT)
    
    def api_records_to_spark_df(
        spark: SparkSession,
        records: List[Dict]
    ) -> DataFrame:
        """
        Converte lista de dicts em Spark DataFrame.
        Serializa cada registro em JSON e usa spark.read.json.
        """
        json_strs = [json.dumps(rec) for rec in records]
        rdd = spark.sparkContext.parallelize(json_strs)
        df = spark.read.json(rdd)
        # Marca timestamp de ingestão
        df = df.withColumn("ingest_ts", current_timestamp())
        return df

if __name__ == '__main__':
    service = BronzeIngestionService()
    products = service.get_products()
    users = service.get_users()
    print(f"Total de produtos obtidos: {len(products)}")
    print(f"Total de usuarios obtidos: {len(users)}")
    # exibe apenas os 3 primeiros para exemplo
    for p in products[:3]:
        print(f"- {p['id']}: {p['title']} (R${p['price']})")

    for p in users[:3]:
        print(f"- {p['id']}: {p['username']} {p['email']}")

    # Cria SparkSession
    spark = (
    SparkSession.builder
        .appName("TesteLocal")
        .master("local[*]")              
        .config("spark.ui.showConsoleProgress", "false")
        .getOrCreate()
    )

    print("Spark version:", spark.version)
    # Converte produtos e usuários para DataFrame Spark
    products_df = BronzeIngestionService.api_records_to_spark_df(spark, products)
    users_df = BronzeIngestionService.api_records_to_spark_df(spark, users)