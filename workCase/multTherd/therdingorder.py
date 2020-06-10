#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
模拟iwofly在生单成功以后，立即调ticketing接口'''

import requests
import json
import time

search_url = "http://test-api.gloryholiday.com/standard/search"
verify_url = "http://test-api.gloryholiday.com/standard/verify"
order_url = "http://test-api.gloryholiday.com/standard/order"
ticketing_url = "http://test-api.gloryholiday.com/standard/ticketing"


class Iwofly():
    def search(self):
        searchd = {
                    "Cid": "iwoflyCOM",
                    "TripType": "1",
                    "FromCity": "HKG",
                    "ToCity": "ICN",
                    "FromDate": "20201017",
                    "RetDate": "20201015",
                    "Currency": "CNY",
                    "AdultNumber": 1,
                    "ChildNumber": 0,
                    "InfantNumber": 0,
                    "CabinGrade": "Y",
                    "IsPriceComparison":False
                }
        res = requests.post(url=search_url,data=json.dumps(searchd))
        print("================================================")
        print(type(res))
        print(type(res.json()))
        print("search: ",res.json())
        print(type(res.text))
        self.search_response = res.json()
    
    def verify(self):
        verifyd = {
                    "cid": "iwoflyCOM",
                    "tripType": "1",
                    "adultNumber": 1,
                    "childNumber": 0,
                    "infantNumber": 0,
                    "data": "451fe026-5255-4b2f-8367-b4878f7dc28d#b361c187-307f-4835-b19b-3133c5e14257#PG215_E#0",
                    "referredTraceId": "7521a333cdc911e9833909314abdef05",
                    "traceId": "bdaec9d9cdc911e9acbb8700893cb1e3",
                    "upstreamInfo": {
                        "clickId": "efec9d7e7bf9f2b4-ap-southeast-1:iwofly.com:0",
                        "extraAttributes": {},
                        "languageCode": "en",
                        "name": "wego",
                        "subSite": "CN"
                    },
                    "routing": self.search_response["routings"][0]
                }
        
        res =  requests.post(url=verify_url, data=json.dumps(verifyd))
        print("================================================")
        print("verify: ",res.json())
        self.verify_response = res.json()
    
    def order(self):
        orderd = {
                    "cid": "iwoflyCOM",
                    "traceId": "",
                    "sessionId": "867A7237E035EAC7B3",
                    "currency": "TWD",
                    "contact": {
                        "email": "xhaoge@hotmail.com",
                        "mobile": "60122540349",
                        "name": "xhaoge"
                    },
                    "passengers": [],
                    "routing":self.verify_response["routing"]
                }
        iwofly_order_info = {
                    "ageType": 0,
                    "birthday": "19950123",
                    "cardExpired": "20250911",
                    "cardIssuePlace": "MY",
                    "cardNum": "G21035998",
                    "cardType": "PP",
                    "gender": "M",
                    "name": "DUO/XIANG",
                    "nationality": "MY",
                    "ticketNumbers": [],
                    "ticketNumbersAsText": ""
                }
        orderd["passengers"].append(iwofly_order_info)
        
        res = requests.post(url=order_url, data=json.dumps(orderd))
        self.order_response = res.json()
        print("================================================")
        print("order response: ",self.order_response)

    def ticketing(self):
        ticketingd = {
                    "cid": "iwoflyCOM",
                    "orderNo": self.order_response["pnrCode"],
                    "payCurrency": "TWD",
                    "payPrice": 3333,
                    "referenceOrderNo": "WF201421HKWOU",
                    "referredTraceId": "955d34fe355411eaab20b37b4820dccd",
                    "traceId": "a20f5453355411eaab20b37b4820dccd",
                    "upstreamInfo": {
                        "cid": "iwoflyCOM",
                        "extraAttributes": {},
                        "name": "iwoflyCOM"}
                    }
        res = requests.post(url=ticketing_url, data=json.dumps(ticketingd))
        self.ticketing_response = res.json()
        print("================================================")
        print("self.ticketing_response :",self.ticketing_response)

    def run(self):
        self.search()
        self.verify()
        # time.sleep(5)
        self.order()
        self.ticketing()
    
if __name__ == "__main__":
    xx = Iwofly()
    xx.run()
    # xx.search()
    # xx.verify()
    # time.sleep(5)
    # xx.order()