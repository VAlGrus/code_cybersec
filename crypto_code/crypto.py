from hashlib import sha256                                      # import hashlib, a python library for cryptography / import sha256 (typology of hash algorithm)

insecure_file = input('select file to encrypt : ')              
final_file_name = input('encrypted file name : ')
key = input('key : ')
keys = sha256(key.encode('utf-8')).digest()                     # encode the key and return sha256 hash (function digest)

with open(insecure_file,'rb') as f_insecure_file:               # open the file to encrypt, read and binary (rb) 
    with open(final_file_name,'wb') as f_final_file_name:       # open the final file, write and binary (wb)
        i = 0 
        while f_insecure_file.peek():                           # while octet in the file, we read the file and encrypt 
            c = ord(f_insecure_file.read(1))                    # read one octet and transform to binary with fucntion ord  
            j = i % len(keys)                                   # when the key is not fix, this function return to 0 i when the hash algorithm is arrived to the end  
            b = bytes([c^keys[j]])                              # XOR of the result (c) and the indexation of the key
            f_final_file_name.write(b)
            i = i + i 

            