import hashlib

def hash(boxID, coin_name, public_key, private_key, webdev_key, amount,
         period, amountUSD, userID, language, iframeID, orderID,
         width, height):
    user_format = 'MANUAL' 
    string = ''
    string = (str(boxID) + coin_name + public_key + private_key +webdev_key +
              str(amount) + period + str(amountUSD)+ language + str(amount) +
              iframeID + str(amountUSD) + userID + user_format + orderID +
              str(width) + str(height))
    m = hashlib.md5(string.encode('utf-8'))
    return m.hexdigest()
