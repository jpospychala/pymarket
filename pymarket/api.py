import requests

class Market(object):

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def get_rates(self):
        r = requests.get('http://%s:%s/rates' %(self.host, self.port))
        return r.json()

    def login(self, name, secret):
        self.name = name
        self.secret = secret
        data = {'name': self.name, 'secret': self.secret}
        r = requests.post('http://%s:%s/broker' %(self.host, self.port), data=data)
        return r.json()

    def buy(self, product_name, amount, unit_price_min, unit_price_max):
        data = {'product_name': product_name, 'amount':amount, 'unit_price_min':unit_price_min, 'unit_price_max':unit_price_max}
        headers = {'broker_name':self.name,'broker_secret':self.secret}
        r = requests.post('http://%s:%s/buy' %(self.host, self.port), data=data, headers=headers)
        return r.json()

    def sell(self, product_name, amount, unit_price_min, unit_price_max):
        data = {'product_name': product_name, 'amount':amount, 'unit_price_min':unit_price_min, 'unit_price_max':unit_price_max}
        headers = {'broker_name':self.name,'broker_secret':self.secret}
        r = requests.post('http://%s:%s/sell' %(self.host, self.port), data=data, headers=headers)
        return r.json()

