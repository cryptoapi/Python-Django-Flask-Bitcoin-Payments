import hashlib

def hash(boxID, coin_name, public_key, private_key, webdev_key, amount,
         period, amountUSD, userID, language, iframeID, orderID,
         width, height):
    user_format = 'MANUAL' 
    values_to_combine = [
              str(boxID), coin_name, public_key, private_key, webdev_key,
              str(amount), str(amountUSD), period, language,
              orderID, userID, user_format, iframeID,
              str(width), str(height),
            ]
    string = '|'.join(values_to_combine)
    m = hashlib.md5(string.encode('utf-8'))
    return m.hexdigest()
