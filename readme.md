## Tumblr Personal TimeLine(Feed) Video Crawler

### Require

- Python 2.7.12
- Scrapy 1.3.3
- Requests 2.11.1

### For Mac or Linux

```shell
pip install requests
pip install scrapy
```

### How It Works

This crawler working principle is to simulate the browser request , not the tumblr's official open api.

So you need to login the tumblr first , find your cookies and setup the config.json.

### How to Work

- edit config.json , fill cookies field on your account login cookies
- Then start crawler by start.py or ``` scrapy crawl index ``` on shell;
- your feed video download link will in ./data.json
- you can execute handle_result.py to analysis data and init download command.

### configs

cookies : your account login cookies

maxPage : the crawler's working max page

```json
{
  "cookies": "your login cookies",
  "maxPage": 20
}
```

#### Notice:Cookie Require Field

If the crawler not work , check your cookies' field.

Recommend field : 

```
tmgioct
rxx 
anon_id
language
logged_in
pfp
pfs
pfe
pfu
capture
nts
devicePixelRatio
documentWidth
yx
__utma
__utmb
__utmz
_ga
_gid
```

### Feature

- [ ]  Proxy List

- [ ]  Auto Download

- [ ]  Offical API Crawler 

      ​

 