# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 16:26:03 2021

@author: Ace
"""
'''
4.	已知網頁API回應內容如下
{ 
"total": 5,
"data": [
    {"id": "001", "name": "productA", "price": 25, "category": "AAA", "stock": 7},
    {"id": "002", "name": "productB", "price": 30, "category": "AAA", "stock": 17},
    {"id": "003", "name": "productC", "price": 60, "category": "BBB", "stock": 2},
    {"id": "004", "name": "productD", "price": 10, "category": "CCC", "stock": 26},
    {"id": "005", "name": "productE", "price": 15, "category": "BBB", "stock": 16},
]
}
# 請按照category欄位進行整理，算出每個category的stock加總：
{
    "AAA": {"products": ["ProductA", "ProductB"], "stock": 24},
    "BBB": {"products": ["ProductC", "ProductE"], "stock": 18},
    "CCC": {"products": ["ProductD"], "stock": 26}
}
'''
# 題目
API_Response = {"total": 5,
              "data": [
                {"id": "001", "name": "productA", "price": 25, "category": "AAA", "stock": 7},
                {"id": "002", "name": "productB", "price": 30, "category": "AAA", "stock": 17},
                {"id": "003", "name": "productC", "price": 60, "category": "BBB", "stock": 2},
                {"id": "004", "name": "productD", "price": 10, "category": "CCC", "stock": 26},
                {"id": "005", "name": "productE", "price": 15, "category": "BBB", "stock": 16},]}
# Solution
Result = {}
for each_id in API_Response["data"]:
    # print(each_id["category"])
    if each_id["category"] not in Result:
        Sub_Result = {}
        Sub_Result.setdefault("products", [each_id["name"].replace('product','Product')]) # P要大寫
        Sub_Result.setdefault("stock", each_id["stock"])
        Result[each_id["category"]] = Sub_Result
    else:
        Result[each_id["category"]]["products"].append(each_id["name"].replace('product','Product')) # P要大寫
        Result[each_id["category"]]["stock"] += each_id["stock"]
print(Result)
        