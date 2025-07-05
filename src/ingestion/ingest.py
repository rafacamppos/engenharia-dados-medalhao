"""Exemplo de script de ingestão.

Este módulo fornece uma função simples de ingestão que copia arquivos para a
camada Bronze.
"""

from pathlib import Path

BRONZE_PATH = Path(__file__).resolve().parents[2] / "data" / "bronze"


def ingest(file_path: str) -> Path:
    """Copia um arquivo para a camada Bronze.

    Parameters
    ----------
    file_path: str
        Caminho do arquivo de origem.

    Returns
    -------
    Path
        Caminho do arquivo copiado dentro da camada Bronze.
    """
    src = Path(file_path)
    dest = BRONZE_PATH / src.name
    dest.write_bytes(src.read_bytes())
    return dest


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Uso: python ingest.py <arquivo>")
        sys.exit(1)
    arquivo = sys.argv[1]
    destino = ingest(arquivo)
    print(f"Arquivo copiado para {destino}")
