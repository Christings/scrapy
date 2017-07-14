# import scrapy
# import scrapy
#
# class MyfilesPipeline(FilesPipeline):
#     def get_media_requests(self, item, info):
#         for url in item["file_urls"]:
#             yield scrapy.Request(url)
#
#     def item_completed(self, results, item, info):
#         """下载完成之后，重命名文件之类的处理，文件路径在results 里，具体results数据结构用pdb看一下就可以了"""
#         file_paths = [x["path"] for ok, x in results if ok]
#         if not file_paths:
#             raise DropItem("Item contains no images")
