import os
import pytest
from database_client.db import Database

# Certifique-se de que as variáveis de ambiente estão setadas para o teste
os.environ["DATABASE_HOSTNAME"] = "localhost"
os.environ["DATABASE_USERNAME"] = "root"
os.environ["DATABASE_PASSWORD"] = ""
os.environ["DATABASE_BASENAME"] = ""


def test_connection():
    """Testa se a conexão é estabelecida corretamente"""
    Database.connect()
    assert Database._conn is not None
    assert Database._conn.is_connected()
    Database.close()


def test_query_select():
    """Testa se uma query SELECT simples retorna um resultado (ajuste para sua base)"""
    resultado = Database.select("SELECT 1 as test_col", one=True)
    assert resultado is not None
    assert "test_col" in resultado
    assert resultado["test_col"] == 1
    Database.close()


def test_query_fail():
    """Testa se uma query inválida é tratada corretamente"""
    resultado = Database.select("SELECT * FROM tabela_inexistente")
    assert resultado is None
    Database.close()
