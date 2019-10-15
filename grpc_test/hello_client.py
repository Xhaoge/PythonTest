#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import logging
import grpc
from grpc_test.rpc_package.helloworld_pb2  import HelloRequest,HelloReply
from grpc_test.rpc_package.helloworld_pb2_grpc import HelloWoeldServiceStub


def run():
    # 使用with 语法保证chanel 自动close
    with grpc.insecure_channel("localhost:50000") as channel:
        # 客户端通过stub 来实现rpc通信
        stub = HelloWoeldServiceStub(channel)

        # 客户端必须使用定义好的类型，这里是HelloRequest类型；
        response = stub.SayHello(HelloRequest(name="eric"))
    print("hello client received: "+response.message)


if __name__ == "__main__":
    logging.basicConfig()
    run()


    