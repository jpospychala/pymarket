from pymarket.api import Market
from unittest2 import TestCase

class MarketTest(TestCase):

    def setUp(self):
        self.login = u'julek'
        self.secret = u'abc'
        self.market = Market('192.168.1.100', 3000)

    def test_get_rates(self):
        rates = self.market.get_rates()
        self.assertIn(u'CONS', rates)

    def test_login(self):
        user = self.market.login(self.login, self.secret)
        self.assertEquals(user, {
            u'money':1000, 
            u'name':self.login, 
            u'secret':self.secret, 
            u'wallet': {u'items': {}}
        })

    def test_buy_not_logged_in(self):
        with self.assertRaises(AttributeError):
            self.market.buy('CONS', 1, 0, 9999)

    def test_buy(self):
        self.market.login(self.login, self.secret)
        user = self.market.buy('CONS', 1, 0, 9999)
        self.assertEquals(user, {
            u'money':999, 
            u'name':self.login, 
            u'secret':self.secret, 
            u'wallet': {u'items': {
                u'CONS': {
                    u'amount': 1,
                    u'name': 'CONS',
                    u'price': 1
                }
            }}
        }) 

    def test_sell(self):
        self.market.login(self.login, self.secret)
        # TODO buy here
        user = self.market.buy
        self.assertEquals(user, {
            u'money':999, 
            u'name':self.login, 
            u'secret':self.secret, 
            u'wallet': {u'items': {
                u'CONS': {
                    u'amount': 1,
                    u'name': u'CONS',
                    u'price': 1
                }
            }}
        })
        
        # TODO sell here 
        user = self.market.sell
        self.assertEquals(user, {
            u'money':1000, 
            u'name':self.login, 
            u'secret':self.secret, 
            u'wallet': {u'items': {}}
        })