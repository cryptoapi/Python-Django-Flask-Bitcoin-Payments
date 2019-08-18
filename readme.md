
GoUrl.io Python's Django v1 & v2 Bitcoin Payment Gateway - 
------------------------------------------------------


**This example explains how you can use GoUrl Bitcoin Payment Gateway on Python's Django. It's easily adapted to other frameworks (such as Flask).**

The views.py file has two functions:

* cryptobox_rendering: The view for rendering the template, which contains the cryptobox
* callback: This is the view which receives and processes the POST data sent within the IPN callback

To render the cryptobox in your template, you will need to send all the requeried parameters to it. (the  value of the hash parameter is returned by the hash function of the provided md5hash.py file). Then, pass all these parameters to the cryptobox_show function of the [cryptobox.js](https://github.com/cryptoapi/Payment-Gateway/blob/master/cryptobox.js) file. 


Steps for the Gourl API-integration IPN feature:
------------------------------------------------------

* Add the callback URL into the urlpatterns list of your urls.py file.
* Add the callback view to views.py


More Info: [https://gourl.io/python\_django\_flask\_bitcoin\_payment\_gateway.html](https://gourl.io/python\_django\_flask\_bitcoin\_payment\_gateway.html)

