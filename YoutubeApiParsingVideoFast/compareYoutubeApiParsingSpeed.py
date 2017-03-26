import time
from YoutubeApiParsingVideoFast import youtubeApiParsingVideoFast
from YoutubeApiParsingVideoFast import youtubeApiParsingVideoSlow

startTime = time.time()
youtubeApiParsingVideoFast.parsingYoutubeChannelVideo().start()
endTime = time.time()
print("fast method spend time : ", endTime - startTime)

startTime = time.time()
youtubeApiParsingVideoSlow.parsingYoutubeChannelVideo().start()
endTime = time.time()
print("slow method spend time : ", endTime - startTime)