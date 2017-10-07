# talk2city
## Communicating with City


Creating models:
```
...
```

Build backend:
```
docker build -f dockerfiles/bot_backend -t fbml/talk2city:0.1 .
```

Run:
```
docker run  -p 8000:8000 fbml/talk2city:0.1
```