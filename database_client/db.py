from .logger import get_logger
from typing import Dict
import mysql.connector

logger = get_logger("database_service")


class Database:
    """Classe de conexão e utilização de banco de dados"""
    _conn = None
    _cursor = None

    @classmethod
    def connect(cls, database_config: Dict):
        """Conecta ao banco de dados"""
        if cls._conn is None or not cls._conn.is_connected():
            try:
                cls._conn = mysql.connector.connect(
                    host=database_config['host'],
                    user=database_config['user'],
                    password=database_config['password'],
                    database=database_config['database']
                )
                cls._cursor = cls._conn.cursor(dictionary=True, buffered=True)
                logger.info("Conexão com o banco estabelecida.")
            except mysql.connector.Error as err:
                logger.error(f"Erro ao conectar ao banco: {err}")
                cls._conn = None
                cls._cursor = None

    @classmethod
    def select(cls, query: str, one: bool = False):
        """Executa um select no banco de dados au receber uma query"""
        cls.connect()
        if cls._conn is None:
            logger.error("Não foi possível executar a query: conexão não disponível.")  # noqa: E501
            return None

        try:
            logger.debug(f"Executando query: {query}")
            cls._cursor.execute(query)
            return cls._cursor.fetchone() if one else cls._cursor.fetchall()
        except mysql.connector.Error as err:
            logger.error(f"Erro na query: {err}")
            return None

    @classmethod
    def delete(cls, query: str):
        """Executa um delete no banco de dados"""
        cls.connect()
        if cls._conn is None:
            logger.error("Não foi possível executar a query: conexão não disponível.")  # noqa: E501
            return None

        try:
            logger.debug(f"Executando query: {query}")
            cls._cursor.execute(query)
            cls._conn.commit()
            return cls._cursor.rowcount
        except mysql.connector.Error as err:
            logger.error(f"Erro na query: {err}")
            return None

    @classmethod
    def update(cls, query: str):
        """Executa um update no banco de dados"""
        cls.connect()
        if cls._conn is None:
            logger.error("Não foi possível executar a query: conexão não disponível.")  # noqa: E501
            return None
        try:
            logger.debug(f"Executando query: {query}")
            cls._cursor.execute(query)
            cls._conn.commit()
            return cls._cursor.rowcount
        except mysql.connector.Error as err:
            logger.error(f"Erro na query: {err}")
            return None

    @classmethod
    def insert(cls, query: str, values):
        """Executa um insert no banco de dados.
        Suporta múltiplos inserts com executemany."""
        cls.connect()
        if cls._conn is None:
            logger.error("Não foi possível executar a query: conexão não disponível.")  # noqa: E501
            return None

        try:
            logger.debug(f"Executando insert: {query} | Valores: {values}")
            if isinstance(values, list) and all(isinstance(v, (tuple, list)) for v in values):  # noqa: E501
                cls._cursor.executemany(query, values)
            else:
                cls._cursor.execute(query, values)
            cls._conn.commit()
            return cls._cursor.rowcount
        except mysql.connector.Error as err:
            logger.error(f"Erro no insert: {err}")
            return None

    @classmethod
    def close(cls):
        """Fecha a conexão com o banco de dados"""
        if cls._conn and cls._conn.is_connected():
            cls._cursor.close()
            cls._conn.close()
            logger.info("Conexão com o banco fechada.")
            cls._conn = None
            cls._cursor = None
