# talk2city
## Communicating with City


Creating models:
```
...
```

### V1
Build backend:
```
docker build -f dockerfiles/bot_backend -t fbml/talk2city:0.1 .
```

Run:
```
docker run  -p 8000:8000 fbml/talk2city:0.1
```


### V2
Build backend:
```
docker build -f dockerfiles/twitter_bot_backend_prebuilt -t fbml/talk2city_prebuilt:0.1 .
docker build -f dockerfiles/twitter_bot_backend_from_prebuilt -t fbml/talk2city:0.1 .
```

Run:
```
docker run -t fbml/talk2city:0.1
```

