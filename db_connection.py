#we import the neccessary library to be able to connect to our database 
import pyodbc



User = 'Cowculator'
Password = '123'


conection_string = 'DRIVER={ODBC Driver 17 for SQL Server}; SERVER=DAZUR; DATABASE=Prueba; UID={'+User+'}; PWD={'+Password+'}'

def db_connection():
    try:
        conexion = pyodbc.connect(conection_string)
        print("Conexion Exitosa")
        return conexion

    except Exception as e:
        
        print(f"Error al conectarse: {e}")


#Este cambio fue hecho desde la pcerda xdddd