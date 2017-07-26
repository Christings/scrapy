# 扇贝面试小作业

> 作业要求如下：
>
> 1. 使用 scrapy / pyspider 抓取 [亚马逊-文学图书](https://www.amazon.cn/%E6%96%87%E5%AD%A6%E5%9B%BE%E4%B9%A6/b/ref=sa_menu_books_l2_b658394051?ie=UTF8&node=658394051) 上尽可能多的书籍名称、价格及评论数
> 2. 从京东爬取相应的书籍信息（价格及评论数）
> 3. 实现书籍的去重，并考虑如果抓取价格更新的问题
> 4. 将爬取到的信息存入 mysql 中
>
>
>
> 请考虑尽可能优化爬虫性能，实现分布式爬取是加分项

## 爬虫

### AmazonSpider
爬取amazon图书, 以不同分类为起点，分页爬取


亚马逊图书id为unique, 确保图书不重复

### JdSpider

根据图书名, 在JD图书搜索, 获取京东图书id, 价格信息

### AmazonSyncSpider

同步价格数据, 使用Linux crontab命令每个一天开启一次。

### JdSyncSpider

根据JD图书id, JD图书获取价格的ajax, 更新价格数据