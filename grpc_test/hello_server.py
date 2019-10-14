#!/usr/bin/env python
# -*-coding: utf-8 -*-

from concurrent import futures
import grpc
import logging
import time 

from grpc_test.rpc_package.helloworld_pb2_grpc import add_HelloWoeldServiceServicer_to_server,HelloWoeldServiceServicer
from grpc_test.rpc_package.helloworld_pb2 import HelloRequest,HelloReply

class Hello(HelloWoeldServiceServicer):

    #这个实现我们定义的接口；
    def SayHello(self,request,context):
        return HelloReply(message='Hello,%s'%request.name)

    
def serve():
    # 这里通过thread pool 来并发server的任务；
    server = grpc.server(futures.ThreadPoolExecutor(max_works=10))

    # 将对应的任务处理函数添加到rpc server中；
    add_HelloWoeldServiceServicer_to_server(Hello(),server)

    # 这里使用的非安全接口，世界grpc支持TLS/SSL 安全连接，以及各种鉴权机制；
    server.add_insecure_port('[::]:50000')
    server.start()

    try:
        while True:
            time.sleep(60*60*24)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    logging.basicConfig()
    serve()