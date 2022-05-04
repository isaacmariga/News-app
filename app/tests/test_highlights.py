import unittest
from ..models.highlights import Highlights

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Highlights("cnn","CNN","Kim Kardashian defends Meghan and Harry over press treatment","As the UK's Prince Harry takes on the tabloid media over its treatment of his wife, Meghan, Duchess of Sussex, Kim Kardashian has weighed in on the royal couple's side.","http://www.bbc.co.uk/news/world-us-canada-61311966","https://cdn.cnn.com/cnnnext/dam/assets/191014055104-meghan-markle-prince-harry-kim-kardashian-split-super-tease.jpg","2019-10-14T12:57:42Z","(CNN)As the UK's Prince Harry takes on the tabloid media over its treatment of his wife, Meghan, Duchess of Sussex, Kim Kardashian has weighed in on the royal couple's side. The reality TV star, who has long been a target of intense public scrutiny, has come… [+1678 chars]")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_highlights,Highlights))


if __name__ == '__main__':
    unittest.main()