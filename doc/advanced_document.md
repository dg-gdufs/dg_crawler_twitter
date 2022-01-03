<!--
 * @Description: file description
 * @Version: 1.0
 * @Autor: Renhetian
 * @Date: 2022-01-03 20:35:40
 * @LastEditors: Renhetian
 * @LastEditTime: 2022-01-03 22:00:46
-->

# Advanced

advanced爬虫使用配置文件生成高级搜索字符串并搜索，输出为json文件。

## 使用方式

proxy: 使用哪个梯子，在host_config.py设置。 (-a proxy=01)

config: 爬虫启动配置文件名，从路径config/下寻找。 (-a config=advanced_config.json)

例: scrapy crawl advanced -a config=advanced_config.json -a proxy=01 -o out.json

## 配置文件

words: 搜索词，二维列表类型，一维列表为与，二维列表为或

none_words: 屏蔽词，列表类型

hashtags: 标签，列表类型

language: 语言(此参数无法使用)

from: tweet发布者，列表类型

to: tweet接受者或被回复者，列表类型

mention: tweet提及的人，就是内容里被@的，列表类型

filter_links: 过滤(回复)，取值为None,True,False。None为不做处理

filter_replies: 过滤(链接)，取值为None,True,False。None为不做处理

min_reply: 最小评论数，int类型

min_like: 最小点赞数，int类型

min_retweet: 最小转推数，lint类型

until: 此时间之前的推文，时间类型，不填为无限制。 yyyy-mm-dd

since: 此时间之后的推文，时间类型，不填为无限制。 yyyy-mm-dd

step: 循环步数，取值有day,month,year，如果推文多就用day，如果推文少就用month或year
