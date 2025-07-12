import os
from typing import List
import pyarrow.parquet as pq
from azure.cosmos import CosmosClient


def read_parquet(path: str) -> List[dict]:
    """Read a parquet file and return a list of dictionaries."""
    table = pq.read_table(path)
    return table.to_pylist()


def get_cosmos_client() -> CosmosClient:
    """Create a Cosmos DB client from environment variables."""
    endpoint = os.environ.get("COSMOS_ENDPOINT")
    key = os.environ.get("COSMOS_KEY")
    if not endpoint or not key:
        raise EnvironmentError("COSMOS_ENDPOINT and COSMOS_KEY must be set")
    return CosmosClient(endpoint, credential=key)


def upsert_items(
    client: CosmosClient,
    database: str,
    container: str,
    items: List[dict],
) -> None:
    """Insert or update items in the specified Cosmos container."""
    db = client.get_database_client(database)
    cont = db.get_container_client(container)
    for item in items:
        cont.upsert_item(item)


if __name__ == "__main__":
    parquet_path = os.environ.get("PARQUET_PATH")
    database = os.environ.get("COSMOS_DATABASE")
    container = os.environ.get("COSMOS_CONTAINER")

    if not parquet_path or not database or not container:
        raise EnvironmentError(
            "PARQUET_PATH, COSMOS_DATABASE and COSMOS_CONTAINER must be defined"
        )

    records = read_parquet(parquet_path)
    cosmos_client = get_cosmos_client()
    upsert_items(cosmos_client, database, container, records)
    print(f"Inserted {len(records)} records into Cosmos DB")
