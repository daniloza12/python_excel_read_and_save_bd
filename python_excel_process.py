import pandas as pd
import logging, sys

from datetime import datetime
from sqlalchemy import create_engine

h = [
    logging.FileHandler('./logs/log.log'), 
    logging.StreamHandler(stream=sys.stdout),
]

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=h,
)

logger = logging.getLogger(__name__)

# Credenciales de la BD
DATABASE_TYPE = 'mysql'
DBAPI = 'pymysql'
USER = 'root2'
PASSWORD = '123456'
# HOST = 'localhost'
HOST = 'host.docker.internal'
PORT = '3306'
DATABASE = 'db_pam_cliente'
DB_TABLE = 'tbl_cliente'

# Crear la cadena de conexión
logger.info("Conectando a BD")
connection_string = f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
engine = create_engine(connection_string)

logger.info("Conexion a BD success")

#excel_file  = '.\\resources\\clientes_excel_2.xlsx'
excel_file = './resources/clientes_excel_2.xlsx'

# columnas de la tabla de la bd
# dni	cliente_id	telefono	correo	estado	password	rol	apellidos	nombre	direccion

# Obtener hora actual
def obtener_hora_actual():
    return datetime.now()

# Función para calcular la diferencia de tiempo
def calcular_diferencia(inicio, fin):
    diferencia = fin - inicio
    horas, resto = divmod(diferencia.total_seconds(), 3600)
    minutos, segundos = divmod(resto, 60)
    logger.info(f"Diferencia: {int(horas)} horas, {int(minutos)} minutos, {int(segundos)} segundos")
  
try:
    hora_inicial = obtener_hora_actual()

    # Lectura del excel
    data = pd.read_excel(excel_file, engine='openpyxl')
    logger.info(f"Archivo cargado con éxito. Total de registros: {len(data)}")

    # Tamaño de fragmentos para cada inserción
    chunk_size = 5

    # Divide en fragmentos (chunks)
    for i in range(0, data.shape[0], chunk_size):
        chunk = data.iloc[i:i+chunk_size]
        
        # Guarda el fragmento en la base de datos
        chunk.to_sql(DB_TABLE, con=engine, if_exists='append', index=False)
        logger.info(f'{len(chunk)} Registros insertados correctamente.')
    
    logger.info("Datos guardados exitosamente.")
    
    # Calcular tiempo de ejecución
    hora_final = obtener_hora_actual()    
    calcular_diferencia(hora_inicial, hora_final)

    logger.info("Proceso completado exitosamente.")
    
except Exception as e:
    logger.error(f"Error al procesar el archivo o insertar datos: {e}")






