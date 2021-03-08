import unittest
from ..models import quotes
Quotes = quotes.Quotes

class QuotesTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the quotes class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''

        self.new_quotes = Quotes('Jamie Zawinski','4','Some people, when confronted with a problem, think “I know, I’ll use regular expressions.” Now they have two problems','http://quotes.stormconsultancy.co.uk/quotes/4')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quotes,Quotes))


if __name__ == '__main__':
    unittest.main()