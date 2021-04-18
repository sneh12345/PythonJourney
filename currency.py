import requests
# https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=72eb9fb8e3ec49128b7b
currency_1 = input('What currency you would like to convert from? e.g CAD\n')
currency_2 = input('What currency you would like to convert to? e.g USD\n')
api_key = "72eb9fb8e3ec49128b7b"
url = "http://free.currconv.com/api/v7/convert?q="+currency_1+"_"+currency_2+"&compact=ultra&apiKey="+api_key

