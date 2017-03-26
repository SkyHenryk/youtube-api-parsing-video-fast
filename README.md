Documentation

https://skyhenryk.github.io/python/youtube-api-parsing-video-fast/


# How to set up?

Update the values in the repository.

serviceYoutubeClient.py - CLIENT_SECRETS_FILE

youtubeApiParsingVideoFast.py - apiKey

# compare the speed

```python
python3 compareYoutubeApiParsingSpeed.py
```

# Performance result

Condition : Parsing 100 channel's recent 10 videos and update the detail information of videos

```text
fast method spend time :  2.376873016357422
slow method spend time :  60.857258558273315
```