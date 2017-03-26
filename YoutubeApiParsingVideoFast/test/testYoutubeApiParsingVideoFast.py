from YoutubeApiParsingVideoFast import youtubeApiParsingVideoFast
import unittest
import asyncio
from pprint import pprint
class FlightTicketInfoFromSkyscannerTest(unittest.TestCase):

    def setUp(self):
        self.mainClass = youtubeApiParsingVideoFast.parsingYoutubeChannelVideo()
        self.loop = asyncio.get_event_loop()

    def tearDown(self):
        pass

    def test_parsingVideoList(self):
        result = self.loop.run_until_complete(self.mainClass.parsingVideoList({'id':'UC-lHJZR3Gqxm24_Vd_AJ5Yw', 'name':'PewDiePie'}))
        pprint(result)
        self.assertGreaterEqual(len(result), 1)

    def test_parsingDetailVideoList(self):
        result = self.loop.run_until_complete(self.mainClass.parsingDetailVideoList('zk4foqmpMHg,WHWRHUso5Rs,QyCv5bmvivU,FiW6nq55Tx8,-GFPpQGDF4g,E5qK9w8tDOI,qLDZF7V3_q4,ONUZSrVVKXk,sDKPtObKlcw,BFhkQqo4BSk'))
        pprint(result)
        self.assertGreaterEqual(len(result), 1)


if __name__ == '__main__':
    unittest.main()

