import pyodbc

# Connection parameters
server = '192.168.1.245'
database = 'A1A'
username = 'your username'
password = 'your password'

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 18 for SQL Server};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password};'
    'TrustServerCertificate=yes'
)

cursor = conn.cursor()
