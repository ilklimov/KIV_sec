# (public_key ^ a)^b mod private_key = (public_key ^ b)^a mod private_key = (public_key ^ ab) mod private_key

class DH_protocol():
   def __init__(self, public_key1, public_key2, private_key):
       self.public_key1 = public_key1
       self.public_key2 = public_key2
       self.private_key = private_key
       self.full_key = None
      
   def generate_partial_key(self):
       part_key = self.public_key1 ** self.private_key
       part_key = part_key % self.public_key2
       return part_key
  
   def generate_full_key(self, part_key_r):             
       full_key = part_key_r ** self.private_key
       full_key = full_key % self.public_key2
       self.full_key = full_key
       return full_key
  
   def encrypt_message(self, message):
       encrypted_message = ""
       key = self.full_key
       for c in message:
           encrypted_message += chr(ord(c) + key)
       return encrypted_message
  
   def decrypt_message(self, encrypted_message):
       decrypted_message = ""
       key = self.full_key
       for c in encrypted_message:
           decrypted_message += chr(ord(c) - key)
       return decrypted_message

message = "Hello world!"
a_public = 619
a_private = 631
m_public = 173
m_private = 179
print ('Пусть открытый ключ Алисы равен:', a_public, '\nА закрытый:', a_private)
print ('Пусть открытый ключ Майка равен:', m_public, '\nА закрытый:', m_private)
Alice = DH_protocol(a_public, m_public, a_private)
Michael = DH_protocol(a_public, m_public, m_private)

a_partial = Alice.generate_partial_key()
print("Сгенерированный частичный ключ Алисы:", a_partial) 
m_partial = Michael.generate_partial_key()
print("Сгенерированный частичный ключ Майка:", m_partial) 

a_full = Alice.generate_full_key(m_partial)
print("Сгенерированный полный ключ Алисы:", a_full) 
m_full=Michael.generate_full_key(a_partial)
print("Сгенерированный полный ключ Майка:", m_full) 


m_encrypted = Michael.encrypt_message(message)
print("Зашифрованное сообщение:", m_encrypted) 
message = Alice.decrypt_message(m_encrypted)
print("Расшифрованное сообщение:", message)