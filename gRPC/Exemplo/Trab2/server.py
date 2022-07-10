import grpc
from concurrent import futures
import lab2_pb2_grpc as pb2_grpc
import lab2_pb2 as pb2

class Lab2_Service(pb2_grpc.Lab2Servicer):

    def __init__(self, *args, **kwargs):
        pass

    def LessGreaterNumber(self, request, context):
        print("ENTROU SERVER")
        print(request.value)
        array = request.value

        maior = max(array)
        menor = min(array)
        result = f"[Server] Maior = {maior} e Menor = {menor}";

        return pb2.Response(reponse=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_Lab2Servicer_to_server(Lab2_Service(), server)
    server.add_insecure_port('[::]:50050')
    server.start()
    print('[Server] Waiting messages...')
    server.wait_for_termination()


if __name__=='__main__':
    serve()

