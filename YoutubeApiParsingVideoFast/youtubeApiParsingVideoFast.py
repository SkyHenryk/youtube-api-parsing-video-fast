import ujson
import asyncio
import aiohttp
import traceback
import time
from pprint import pprint

class parsingYoutubeChannelVideo():

    def __init__(self):
        self.loop = asyncio.get_event_loop()
        self.quotas = 0
        self.quotasLimit = 1000000
        self.taskSize = 500
        self.resultFileName = "./result.txt"
        self.apiKey = 'apikey'
        self.channelList = [{'id': 'UC-lHJZR3Gqxm24_Vd_AJ5Yw', 'name': 'PewDiePie'},
                             {'id': 'UCZJ7m7EnCNodqnu5SAtg8eQ', 'name': 'HolaSoyGerman.'},
                             {'id': 'UCHkj014U2CQ2Nv0UZeYpE_A', 'name': 'JustinBieberVEVO'},
                             {'id': 'UCBR8-60-B28hp2BmDPdntcQ', 'name': 'YouTube Spotlight'},
                             {'id': 'UC2xskkQVFEpLcGFnNSLQY0A', 'name': 'RihannaVEVO'},
                             {'id': 'UCXazgXDIYyWH-yXLAkcrFxw', 'name': 'elrubiusOMG'},
                             {'id': 'UCY30JRSgfhYXA6i6xX1erWg', 'name': 'Smosh'},
                             {'id': 'UCbW18JZRgko_mOGm5er8Yzg', 'name': 'OneDirectionVEVO'},
                             {'id': 'UCANLZYMidaCbLQFWXBC95Jg', 'name': 'TaylorSwiftVEVO'},
                             {'id': 'UC20vb-R_px4CguHzzBPhoyQ', 'name': 'EminemVEVO'},
                             {'id': 'UC-8Q-hLdECwQmaWNwXitYDw', 'name': 'KatyPerryVEVO'},
                             {'id': 'UCKqH_9mk1waLgBiL2vT5b9g', 'name': 'VanossGaming'},
                             {'id': 'UCV4xOVpbcV8SdueDCOxLXtQ', 'name': 'Fernanfloo'},
                             {'id': 'UCSAUGyc_xA8uYzaIVG6MESQ', 'name': 'nigahiga'},
                             {'id': 'UCp0hYYBW6IMayGgR-WeoCvQ', 'name': 'TheEllenShow'},
                             {'id': 'UCYiGq8XF7YQD00x7wAd62Zg', 'name': 'JuegaGerman'},
                             {'id': 'UCBNs31xysxpAGMheg8OrngA', 'name': 'Yuya'},
                             {'id': 'UC3KQ5GWANYF8lChqjZpXsQw', 'name': 'whinderssonnunes'},
                             {'id': 'UCam8T03EOFBsNdR0thrFHdQ', 'name': 'VEGETTA777'},
                             {'id': 'UC9gFih9rw0zNCK3ZtoKQQyA', 'name': 'JennaMarbles'},
                             {'id': 'UC7_YxT-KID8kRbqZo7MyscQ', 'name': 'Markiplier'},
                             {'id': 'UCpDJl2EmP7Oh90Vylx0dZtA', 'name': "Spinnin' Records"},
                             {'id': 'UCRijo3ddMTht_IHyNSNXpNQ', 'name': 'Dude Perfect'},
                             {'id': 'UCq-Fj5jknLsUf-MWSy4_brA', 'name': 'T-Series'},
                             {'id': 'UCVtFOytbRpEvzLjvqGG5gxQ', 'name': 'KSI'},
                             {'id': 'UC0VOyT2OCBKdQhF3BAbZ-1g', 'name': 'ArianaGrandeVevo'},
                             {'id': 'UC_TVqp_SyG6j5hG-xVRy95A', 'name': 'Skrillex'},
                             {'id': 'UC0v-tlzsn0QZwJnkiaUSJVQ', 'name': 'FBE'},
                             {'id': 'UCYzPXprvl5Y-Sf0g4vX-m6g', 'name': 'jacksepticeye'},
                             {'id': 'UCJ5v_MCY6GNUBTO8-D3XoAg', 'name': 'WWE'},
                             {'id': 'UCS5Oz6CHmeoF7vSad0qqXfw', 'name': 'DanTDM'},
                             {'id': 'UCMu5gPmKp5av0QCAajKTMhw', 'name': 'ERB'},
                             {'id': 'UComP_epzeKzvBX156r6pm1Q', 'name': 'AdeleVEVO'},
                             {'id': 'UCaWd5_7JhbQBe4dknZhsHJg', 'name': 'WatchMojo.com'},
                             {'id': 'UC2pmfLm7iq6Ov1UwYrWYkZA', 'name': 'Vevo'},
                             {'id': 'UCoGDh1Xa3kUCpok24JN5DKA', 'name': 'enchufetv'},
                             {'id': 'UC8-Th83bH_thdKZDJCrn88g',
                              'name': 'The Tonight Show Starring Jimmy Fallon'},
                             {'id': 'UC1l7wYrva1qCH-wgqcHaaRg', 'name': 'David Guetta'},
                             {'id': 'UCEWHPFNilsT0IfQfutVzsag', 'name': 'Porta dos Fundos'},
                             {'id': 'UCoUM-UJ7rirJYP8CQ0EIaHA', 'name': 'Bruno Mars'},
                             {'id': 'UCzVIrPfZBE-XkBISBybMBLA', 'name': 'Werevertumorro'},
                             {'id': 'UCmv1CLT6ZcFdTJMHxaR9XeA', 'name': 'PTXofficial'},
                             {'id': 'UCcMTZY1rFXO3Rj44D5VMyiw', 'name': 'Machinima'},
                             {'id': 'UCN1hnUccO4FD5WfM7ithXaw', 'name': 'Maroon5VEVO'},
                             {'id': 'UCGnjeahCJW1AF34HBmQTJ-Q', 'name': 'shakiraVEVO'},
                             {'id': 'UCa10nxShhzNrCE1o2ZOPztg', 'name': 'Trap Nation'},
                             {'id': 'UCPDis9pjXuqyI7RYLJ-TTSA', 'name': 'FailArmy'},
                             {'id': 'UC0C-w0YjGpqDXGB8IHb662A', 'name': 'Ed Sheeran'},
                             {'id': 'UCKlhpmbHGxBE6uw9B_uLeqQ', 'name': 'Sky Does Minecraft'},
                             {'id': 'UC4PooiX37Pld1T8J5SYT-SQ', 'name': 'Good Mythical Morning'},
                             {'id': 'UCq-Fj5jknLsUf-MWSy4_brA', 'name': 'T-Series'},
                             {'id': 'UC-lHJZR3Gqxm24_Vd_AJ5Yw', 'name': 'PewDiePie'},
                             {'id': 'UCHkj014U2CQ2Nv0UZeYpE_A', 'name': 'JustinBieberVEVO'},
                             {'id': 'UCJ5v_MCY6GNUBTO8-D3XoAg', 'name': 'WWE'},
                             {'id': 'UCqdGW_m8Rim4FeMM29keDEg',
                              'name': 'Fun Toys Collector Disney Toys Review'},
                             {'id': 'UCR5wZcXtOUka8jTA57flzMg', 'name': 'netd müzik'},
                             {'id': 'UCKAqou7V9FAWXpZd9xtOg3Q', 'name': 'LittleBabyBum ®'},
                             {'id': 'UClZkHt2kNIgyrTTPnSQV3SA', 'name': 'Get Movies'},
                             {'id': 'UC-8Q-hLdECwQmaWNwXitYDw', 'name': 'KatyPerryVEVO'},
                             {'id': 'UC2xskkQVFEpLcGFnNSLQY0A', 'name': 'RihannaVEVO'},
                             {'id': 'UCRv76wLBC73jiP7LX4C3l8Q', 'name': 'Маша и Медведь'},
                             {'id': 'UCANLZYMidaCbLQFWXBC95Jg', 'name': 'TaylorSwiftVEVO'},
                             {'id': 'UCpDJl2EmP7Oh90Vylx0dZtA', 'name': "Spinnin' Records"},
                             {'id': 'UCS5Oz6CHmeoF7vSad0qqXfw', 'name': 'DanTDM'},
                             {'id': 'UCpko_-a4wgz2u_DgDgd9fqA', 'name': 'BuzzFeedVideo'},
                             {'id': 'UCG9gfnA5UDoLvz-tC9B-HKw', 'name': 'GMM GRAMMY OFFICIAL'},
                             {'id': 'UCvthuVsurPaVz2a7_4LepGg', 'name': 'Family Fun Pack'},
                             {'id': 'UCGnjeahCJW1AF34HBmQTJ-Q', 'name': 'shakiraVEVO'},
                             {'id': 'UCp0hYYBW6IMayGgR-WeoCvQ', 'name': 'TheEllenShow'},
                             {'id': 'UC20vb-R_px4CguHzzBPhoyQ', 'name': 'EminemVEVO'},
                             {'id': 'UCi8e0iOVk1fEOogdfu4YgfA', 'name': 'Movieclips Trailers'},
                             {'id': 'UCpGdL9Sn3Q5YWUH2DVUW1Ug', 'name': 'PopularMMOs'},
                             {'id': 'UC1l7wYrva1qCH-wgqcHaaRg', 'name': 'David Guetta'},
                             {'id': 'UCaWd5_7JhbQBe4dknZhsHJg', 'name': 'WatchMojo.com'},
                             {'id': 'UCWr4vlkj5xXQ4bSXNeTT2AA', 'name': 'Baby Big Mouth'},
                             {'id': 'UCBnZ16ahKA2DZ_T5W0FPUXg',
                              'name': 'ChuChu TV Nursery Rhymes & Kids Songs'},
                             {'id': 'UCVttQE6tS_agDSAU61Q65aA', 'name': 'EnriqueIglesiasVEVO'},
                             {'id': 'UC7nGdI1YVbdj0lBqEeg8KxQ', 'name': 'Blu Toys Club Surprise'},
                             {'id': 'UCppHT7SZKKvar4Oc9J4oljQ', 'name': 'zeetv'},
                             {'id': 'UCbW18JZRgko_mOGm5er8Yzg', 'name': 'OneDirectionVEVO'},
                             {'id': 'UCK1i2UviaXLUNrZlAFpw_jA', 'name': 'El Reino Infantil'},
                             {'id': 'UClVrJwcIy7saPcGc1nct80A', 'name': 'Fueled By Ramen'},
                             {'id': 'UCj2HtBTppiQLVrZfEjcFxig', 'name': 'SevenSuperGirls'},
                             {'id': 'UCay_OLhWtf9iklq8zg_or0g', 'name': 'BuzzFeedYellow'},
                             {'id': 'UCKqH_9mk1waLgBiL2vT5b9g', 'name': 'VanossGaming'},
                             {'id': 'UCN1hnUccO4FD5WfM7ithXaw', 'name': 'Maroon5VEVO'},
                             {'id': 'UC7_YxT-KID8kRbqZo7MyscQ', 'name': 'Markiplier'},
                             {'id': 'UC8-Th83bH_thdKZDJCrn88g',
                              'name': 'The Tonight Show Starring Jimmy Fallon'},
                             {'id': 'UCKjjmMqvuxNYw8c6knceexQ', 'name': 'DisneyCarToys'},
                             {'id': 'UCYzPXprvl5Y-Sf0g4vX-m6g', 'name': 'jacksepticeye'},
                             {'id': 'UC9zX2xZIJ4cnwRsgBpHGvMg', 'name': 'beyonceVEVO'},
                             {'id': 'UCaHNFIob5Ixv74f5on3lvIw', 'name': 'CalvinHarrisVEVO'},
                             {'id': 'UC0VOyT2OCBKdQhF3BAbZ-1g', 'name': 'ArianaGrandeVevo'},
                             {'id': 'UCam8T03EOFBsNdR0thrFHdQ', 'name': 'VEGETTA777'},
                             {'id': 'UCY30JRSgfhYXA6i6xX1erWg', 'name': 'Smosh'},
                             {'id': 'UCVWA4btXTFru9qM06FceSag', 'name': 'PitbullVEVO'},
                             {'id': 'UCstEtN0pgOmCf02EdXsGChw', 'name': 'ABS-CBN Entertainment'},
                             {'id': 'UCsU-ktDYPSvRyRqcFV4uXPw', 'name': 'DCTC Toy Channel'},
                             {'id': 'UCKy1dAqELo0zrOtPkf0eTMw', 'name': 'IGN'},
                             {'id': 'UCpEhnqL0y41EpW2TvWAHD7Q', 'name': 'SET India'}]

    def start(self):
        tasks = []
        for channel in self.channelList:
            tasks.append(asyncio.ensure_future(self.parsingYoutubeVideo(channel)) )
            if len(tasks) > self.taskSize:
                self.loop.run_until_complete(asyncio.gather(*tasks))
                tasks = []
                time.sleep(60) # for quatos

        if len(tasks) > 0:
            self.loop.run_until_complete(asyncio.gather(*tasks))

    async def parsingYoutubeVideo(self,channel):
        try:
            self.AddQuotasForYoutubeApi()
            videoList = await self.parsingVideoList(channel)
            videoDetailList = await self.parsingDetailVideoList(videoList)
            self.saveVideoDetail(videoDetailList)
            self.checkQuotasLimit()
        except:
            pprint(traceback.format_exc())

    def AddQuotasForYoutubeApi(self):
        self.quotas += 111

    async def parsingVideoList(self,channel):
        channelId = channel.get('id')
        parsingChannelUrl = "https://www.googleapis.com/youtube/v3/search"
        parsingChannelHeader = {'cache-control': "no-cache"}
        parsingChannelQueryString = {"part": "Snippet", "channelId": channelId, "maxResults": "10",
                                     "key": self.apiKey, "order": "date", "type": "video"}
        parsingChannel = None
        async with aiohttp.ClientSession() as session:
            async with session.get(parsingChannelUrl,headers=parsingChannelHeader,params=parsingChannelQueryString) as resp:
                parsingChannel = await resp.read()

        parsingChannelItems = ujson.loads(parsingChannel).get("items")
        if parsingChannelItems is None:
            return
        VideoIds = ",".join(str(x.get("id").get("videoId")) for x in parsingChannelItems)
        return VideoIds

    async def parsingDetailVideoList(self, videoList):

        parsingVideoUrl = "https://www.googleapis.com/youtube/v3/videos"
        parsingVideoHeader = {'cache-control': "no-cache"}
        parsingVideoQueryString = {"part": "Snippet,contentDetails,status,statistics",
                                                 "id": videoList,
                                                 "key": self.apiKey}
        parsingVideo = None
        async with aiohttp.ClientSession() as session:
            async with session.get(parsingVideoUrl,headers=parsingVideoHeader,params=parsingVideoQueryString) as resp:
                parsingVideo = await resp.read()
        parsingVideoItems = ujson.loads(parsingVideo).get("items")
        legalVideoItems = list(filter(lambda x: x.get("status").get("embeddable"), parsingVideoItems))
        return legalVideoItems

    def saveVideoDetail(self,videoDetailList):
        with open(self.resultFileName, "a") as resultFile:
            resultFile.write(str(videoDetailList) + "\n")

    def checkQuotasLimit(self):
        if self.quotas > self.quotasLimit:
            quit()

if __name__ == '__main__':
    startTime = time.time()
    parsingYoutubeChannelVideo().start()
    endTime = time.time()
    print("spend time : " , endTime - startTime)

