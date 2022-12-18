"""
    Se está importando la biblioteca os y se está definiendo una constante MYSQL_URL que 
    se inicializa con una cadena de texto que representa la URL de una base de datos MySQL.

    La biblioteca os se utiliza para acceder a las variables de entorno del sistema operativo 
    en el que se está ejecutando el código. El método os.getenv() se utiliza para obtener el valor 
    de una variable de entorno específica. Si la variable de entorno no existe, os.getenv() devuelve None.
"""
import os

MYSQL_URL: str = os.getenv("MYSQL_URL") if os.getenv("MYSQL_URL") != None  else "mysql://admin_db:admin_db@0.0.0.0:3306/fastapi"