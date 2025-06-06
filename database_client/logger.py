import logging
import sys
from pathlib import Path


def get_logger(name: str = "app", level: int = logging.INFO) -> logging.Logger:
    """Cria ou obtém um logger configurado com handlers para console e arquivo."""  # noqa: E501
    logger = logging.getLogger(name)

    if not logger.handlers:
        # Evita múltiplos handlers ao reutilizar o logger
        logger.setLevel(level)

        formatter = logging.Formatter(
            fmt='[%(asctime)s] [%(levelname)s] %(name)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)

        # File handler
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        file_handler = logging.FileHandler(log_dir / f"{name}.log")
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

        logger.propagate = False  # Evita log duplicado

    return logger
