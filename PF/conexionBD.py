import os, binascii, hashlib
import mysql.connector

DB = {
    "host": "127.0.0.1",
    "port": 3307,
    "user": "asistencias",
    "password": "Asis#123",
    "database": "asistenciasV2"
}

def conectar(sin_db=False):
    try:
        if sin_db:
            return mysql.connector.connect(
                host=DB["host"], port=DB["port"], user=DB["user"], password=DB["password"]
            )
        return mysql.connector.connect(
            host=DB["host"], port=DB["port"], user=DB["user"],
            password=DB["password"], database=DB["database"]
        )
    except mysql.connector.Error as e:
        print("\n[Error] No es posible conectarse a la base de datos.")
        print("Detalle:", e)
        return None

def hash_password(password, iterations=150000):
    salt = os.urandom(16)
    dk = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, iterations)
    return f"pbkdf2${iterations}${binascii.hexlify(salt).decode()}${binascii.hexlify(dk).decode()}"

def verificar_password(password, almacenado):
    try:
        metodo, iters_s, salt_hex, hash_hex = almacenado.split("$")
        if metodo != "pbkdf2": return False
        iters = int(iters_s)
        salt = binascii.unhexlify(salt_hex)
        esperado = binascii.unhexlify(hash_hex)
        dk = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, iters)
        return hashlib.compare_digest(dk, esperado)
    except:
        return False
