# omid_khosusi
import hashlib
matn_omid=input("What do you want to hashh!")

hash_kardan=hashlib.sha256(matn_omid.encode("ascii")).hexdigest()
print(hash_kardan)
o=input("pot!")
hash_o=hashlib.sha256(o.encode("ascii")).hexdigest()
print(hash_o)
