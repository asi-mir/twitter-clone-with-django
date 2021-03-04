import datetime
import random,hashlib,uuid
def generate_token():
    token = ''.join(str(random.randint(0,9)) for i in range(6))
    salt = uuid.uuid4().hex
    #send2faTokenToUser(token)
    expiration_date = datetime.datetime.now()+datetime.timedelta(minutes = 1)
    print(token,salt,expiration_date)
    token += salt
    hash_token=hashlib.sha256(token.encode('utf-8')).hexdigest()
    #Save hash_token salt and expiration_date in Database
    return hash_token,salt,expiration_date
