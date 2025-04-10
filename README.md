# 📦 database_client

Uma biblioteca simples e reutilizável para conectar a um banco de dados MySQL e executar queries SQL com facilidade em projetos Python.

## ✅ Recursos

- Conexão automática e única com o banco de dados.
- Execução de queries SQL (`SELECT`) com retorno em formato de dicionário.
- Fechamento seguro da conexão.
- Pronto para ser usado como biblioteca em outros projetos.

---

## 🔧 Instalação

Você pode instalar diretamente a partir do GitHub:

## 🌐 Variáveis de Ambiente

A conexão depende das seguintes variáveis, que você pode definir em um arquivo .env ou diretamente no seu ambiente:

```bash
DATABASE_HOSTNAME=localhost
DATABASE_USERNAME=root
DATABASE_PASSWORD=sua_senha
DATABASE_BASENAME=nome_do_banco
```

## 🧪 Exemplo de Uso

```python
from database_client.db import Database

# Executar uma query
resultado = Database.query("SELECT * FROM usuarios")

# Imprimir os resultados
for linha in resultado:
    print(linha)

# Fechar a conexão
Database.close()
```

## 🧪 Testes

Para executar os testes:

1. Ative sua virtualenv.

2. Instale o pytest se ainda não tiver:
```bash
pip install pytest
```

3. Execute:
```bash
pytest tests/
```

## 📁 Estrutura do Projeto
```bash
database_client/
├── database_client/
│   ├── __init__.py
│   └── db.py
├── tests/
│   └── test_db.py
├── .env
├── README.md
├── requirements.txt
└── setup.py
```

## 🧙‍♂️ Autor
Desenvolvido por Vinicius Costa – sinta-se à vontade para contribuir, sugerir melhorias ou reportar problemas.

## ⚖️ Licença
Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo LICENSE para mais detalhes.
```go
Se quiser, também posso te ajudar com os arquivos `setup.py`, `requirements.txt` ou testes automatizados (`test_db.py`). Só avisar!
```