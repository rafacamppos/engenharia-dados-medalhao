import boto3
import logging
from botocore.client import Config
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import current_timestamp


# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s"
)
logger = logging.getLogger(__name__)

def get_s3_client(
    endpoint_url: str = "http://localhost:4566",
    aws_access_key_id: str = "test",
    aws_secret_access_key: str = "test",
    region_name: str = "us-east-1",
    signature_version: str = "s3v4"
) -> boto3.client:
    """
    Cria e retorna um cliente S3 configurado.
    """
    session = boto3.session.Session()
    return session.client(
        "s3",
        endpoint_url=endpoint_url,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        config=Config(signature_version=signature_version),
        region_name=region_name
    )

def upload_spark_parquet(
    df: DataFrame,
    bucket: str,
    key_prefix: str
) -> None:
    """
    Escreve DataFrame Spark no S3 como Parquet.
    """
    output_path = f"s3://{bucket}/{key_prefix}"
    logger.info("Escrevendo DataFrame Spark em: %s", output_path)
    # Overwrite by partition for fresh load
    df.write.mode("overwrite").parquet(output_path)

if __name__ == "__main__":
    s3 = get_s3_client()
    # Exemplo de uso
    upload_to_s3(
        client=s3,
        bucket="camada-bronze",
        key="bronze/products/20250706T120000/products.json",
        body=b"[]"
    )