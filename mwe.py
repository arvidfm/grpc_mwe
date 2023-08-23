import asyncio

import grpc.aio
import sys

from proto import transfer_pb2_grpc, transfer_pb2


async def run_server():
    class TransferService(transfer_pb2_grpc.FileTransferServicer):
        async def Transfer(self, request_iterator, context):
            yield transfer_pb2.TransferResp()

    server = grpc.aio.server()
    server.add_insecure_port("[::]:5555")
    transfer_pb2_grpc.add_FileTransferServicer_to_server(TransferService(), server)
    await server.start()
    await server.wait_for_termination()


async def run_client():
    async def streamer():
        yield transfer_pb2.TransferReq()

    async with grpc.aio.insecure_channel("localhost:5555") as channel:
        stub = transfer_pb2_grpc.FileTransferStub(channel)
        async for _ in stub.Transfer(streamer()):
            break
    sys.exit(0)


async def main():
    match sys.argv:
        case [_, "server"]:
            await run_server()
        case [_, "client"]:
            await run_client()
        case _:
            print("please specify either 'server' or 'client'")


if __name__ == "__main__":
    asyncio.run(main())
