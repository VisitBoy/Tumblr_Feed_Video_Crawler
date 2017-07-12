# encoding:utf-8
import json

import scrapy
from lxml import etree
from scrapy.http.request import Request

stream_cursor = "eyJGb2xsb3dlZFNlYXJjaFBvc3QiOltdLCJiZWZvcmVfaWQiOiIxNjI2ODY4NDM3NDMifQ%3D%3D"

with open("config.json", "r") as f:
    configData = json.loads(f.read(-1))
    default_cookie = configData["cookies"]
    maxPage = configData["maxPage"]

cookieObj = {}
cookieList = default_cookie.split(";")
for pair in cookieList:
    cookieObj[pair.split("=")[0]] = pair.split("=")[1]

video_url_list = set()
start_url_list = []


class Index(scrapy.spiders.Spider):
    name = "index"
    allowed_domains = ["tumblr.com", "taobao.com", "tmall.com"]
    start_urls = [
        "https://www.tumblr.com/dashboard"
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, cookies=cookieObj)

    def parse(self, response):
        if len(response.url.split("svc")) == 1:
            body = response.body
            html = etree.HTML(body)
            video_list = html.xpath("//source")
            for video in video_list:
                video_name = video.xpath("@src")[0].split("tumblr_")[1].split("/")[0]
                video_url = "https://vtt.tumblr.com/tumblr_" + video_name + ".mp4"
                video_url_list.add(video_url)
            next_index = "2"
            next_timestamp = response.body.split("/dashboard/2")[1].split("\"")[0][1:]
            url = "https://www.tumblr.com/svc/dashboard/" + next_index + "/" + next_timestamp + \
                  "?nextAdPos=8&stream_cursor=" + stream_cursor
            yield Request(url, callback=self.parse, cookies=cookieObj)
        else:
            body = json.loads(response.body)['response']['DashboardPosts']['body']
            html = etree.HTML(body)
            video_list = html.xpath("//source")
            for video in video_list:
                video_name = video.xpath("@src")[0].split("tumblr_")[1].split("/")[0]
                video_url = "https://vtt.tumblr.com/tumblr_" + video_name + ".mp4"
                video_url_list.add(video_url)
            with open("data.json", 'wb') as f:
                try:
                    f.write(json.dumps(list(video_url_list)))
                except Exception, e:
                    print("error in result", e)
            try:
                next_index = json.loads(response.body)['meta']['tumblr_next_page'].split('/')[3]
                if int(next_index) > int(maxPage):
                    return
                next_timestamp = json.loads(response.body)['meta']['tumblr_next_page'].split('/')[4]
                url = "https://www.tumblr.com/svc/dashboard/" + next_index + "/" + next_timestamp + \
                      "?nextAdPos=8&stream_cursor=" + stream_cursor
                yield Request(url, callback=self.parse, cookies=cookieObj)
            except Exception, e:
                print("error in result", e)
