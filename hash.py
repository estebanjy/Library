import hashlib
import os

class Hash:
    @staticmethod
    def hash_password(password):
        # Genera una sal aleatoria
        salt = os.urandom(16)
        # Prepara la contraseña para ser hasheada
        pwdhash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        # Almacena la sal junto con el hash para poder verificar la contraseña luego
        pwdhash = salt + pwdhash
        return pwdhash

    @staticmethod
    def check_password(stored_password_hash, user_password):
        # Extrae la sal del hash almacenado
        salt = stored_password_hash[:16]
        stored_password_hash = stored_password_hash[16:]
        # Hashea la contraseña proporcionada con la misma sal
        pwdhash = hashlib.pbkdf2_hmac('sha256', user_password.encode('utf-8'), salt, 100000)
        # Compara los hashes
        return pwdhash == stored_password_hash

"""
my_password = 'esteban42'
hashed = Hash.hash_password(my_password)
print(f'Hashed Password: {hashed.hex()}')

password_to_check = 'esteban42'
if Hash.check_password(hashed, password_to_check):
    print('El acceso es permitido. La contraseña es correcta.')
else:
    print('El acceso es denegado. La contraseña es incorrecta.')
"""