# Python_Excel_Lectura_y_guardado_bd
Se utiliza python y base de datos MySql
El proyecto lee un archivo excel y usando la libreria pandas se hacen registros masivos en la base de datos MySql.

Recomendaciones:
INSTALAR LIBRERIA
pip install pandas sqlalchemy pymysql openpyxl

# Para docker
-- llena el file requirements.txt con las dependencias y versiones del proyecto
pip freeze > "requirements.txt"

-- el que descarga el proyecto debe correr
pip install -r ".\requirements.txt"

-- para ver las dependencias instaladas
pip list


--
docker build -t dockerpy3 .
docker run -d -p 3307:3306 dockerpy3

-- listar imagenes
docker ps -a

-- para ver los logs
docker logs <container_id>
