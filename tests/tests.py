from pymarket.api import Market
from unittest2 import TestCase

class MarketTest(TestCase):

    def setUp(self):
        self.market = Market('192.168.1.100', 3000)

    def test_get_rates(self):
        rates = self.market.get_rates()
        self.assertIn(u'PZU', rates)

    def test_login(self):
        julek = self.market.login('julek', 'abc')
        self.assertEquals(julek, {
            u'money':1000, 
            u'name':'julek', 
            u'secret':'abc', 
            u'wallet': {u'items': {}}
        })

    def test_buy_not_logged_in(self):
        with self.assertRaises(AttributeError):
            self.market.buy('TPE', 1, 0, 9999)

    def test_buy(self):
        julek = self.market.login('julek', 'abc')
        julek_2 = self.market.buy('TPE', 1, 0, 9999)
        self.assertEquals(julek_2, {
            u'money':995.06, 
            u'name':u'julek', 
            u'secret':u'abc', 
            u'wallet': {u'items': {
                u'TPE': {
                    u'amount': u'01',
                    u'name': 'TPE',
                    u'price': 4.94
                }
            }}
        }) 

