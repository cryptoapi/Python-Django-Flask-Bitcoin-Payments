from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import hashlib
from . import md5hash


def cryptobox_rendering(request):
    boxID = 1234    # Your gourl cryptobox ID, https://gourl.io/editrecord/coin_boxes/0
    coin_name = 'bitcoin'
    public_key = 'your-gourl_public-key'
    private_key = 'your-gourl_private-key'
    webdev_key  = 'optional your-web-developer-key'
    amount = 0  # amount in bitcoins (Or another crybtocurrency
    period = '1 MINUTE'
    amountUSD = 5
    userID = request.user.username
    language = 'en'
    iframeID = 'iframeID'
    orderID = 'product-1'
    width = 530
    height = 230
    md5 = md5hash.hash(boxID, coin_name, public_key, private_key, webdev_key, amount,
                        period, amountUSD, userID, language, iframeID, orderID,
                        width, height)
    variables = {'boxID': boxID, 'coin_name': coin_name, 'public_key': public_key, 'webdev_key': webdev_key,
                 'amount': amount, 'period': period, 'amountUSD': amountUSD, 'userID': userID, 'language': language,
                 'iframeID': iframeID, 'orderID': orderID, 'width': width, 'height': height, 'hash': md5}
    return render(request, 'cryptobox_template.html', variables)

    
@csrf_exempt     # Very important! You need to allow a Foreign site (Gourl server) communicate with your server
def callback(request, *args, **kwargs):
    html = ""
    if request.method == 'POST':
        private_key = "Your-cryptobox-private-key"
        h = hashlib.sha512(private_key.encode(encoding='utf-8'))    # The incoming 'private_key' data from Gourl is sha512 encrypted
        private_key_hash = h.hexdigest()    # Hence, you need to hash your private key too for make security check
        if (request.POST.get('confirmed') == '0' and request.POST.get('box') == 'box-number' and
                request.POST.get('status') == 'payment_received' and
                request.POST.get('private_key_hash') == private_key_hash):     # Make the checks you need (Don't forget to check the 'private_key_hash')
            """
               Your code here for getting a unconfirmed payment    
            """
            html = "cryptobox_newrecord"     # Don't change this text. It's used by gourl server
        elif request.POST.get('confirmed') == '1':
        """
           Your code here for a payment confirmation
        """
            html = "cryptobox_updated"        # Don't change it
        else:
        """
           Your code here
        """
            html = "cryptobox_nochanges"    # Don't change it

    else:
        html = "Only POST Data Allowed"     # Don't change it

    return HttpResponse(html)
