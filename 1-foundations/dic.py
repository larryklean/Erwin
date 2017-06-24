# info = {
#     "A001": "小明",
#     "A002": "小红",
#     "A003": "小刚"
# }
#
# # query
# print(info)
# print(info.get("A001"))
# print(info.get("A004"))
# print(info["A002"])
#
# # update
# info["A003"] = "jack"
# print(info)
#
# # delete
# info.popitem()
# print(info)
#
# info.pop("A001")
# print(info)
#
# del info["A002"]

catalog = {
    "欧美": {
        "www.youporn.com": ["很多免费的,世界最大的", "质量一般"],
        "www.pornhub.com": ["很多免费的,也很大", "质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多", "资源不多,更新慢"],
        "x-art.com": ["质量很高,真的很高", "全部收费,屌比请绕过"]
    },
    "日韩": {
        "tokyo-hot": ["质量怎样不清楚,个人已经不喜欢日韩范了", "听说是收费的"]
    },
    "大陆": {
        "1024": ["全部免费,真好,好人一生平安", "服务器在国外,慢"]
    }
}

# catalog.setdefault("大陆", {"1024": ["1", "2"]})
# print(catalog)

# print(catalog.items())

for key in catalog:
    print(key, catalog[key])

# for k, v in catalog.items():
#     print(k, v)

# print(catalog.keys())
# print(catalog.values())
