"""
Configuración del logging
"""
import logging
import os

if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(
    filename="logs/general.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# LOG TRANSACCIONES
log_transacciones = logging.getLogger("transacciones")
handler_transacciones = logging.FileHandler("logs/transacciones.log")
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler_transacciones.setFormatter(formatter)
log_transacciones.addHandler(handler_transacciones)
log_transacciones.setLevel(logging.INFO)

# LOG ERRORES
log_errores = logging.getLogger("errores")
handler_errores = logging.FileHandler("logs/errores.log")
handler_errores.setFormatter(formatter)
log_errores.addHandler(handler_errores)
log_errores.setLevel(logging.ERROR)
