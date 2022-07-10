import grpc
import random
import lab2_pb2_grpc as pb2_grpc
import lab2_pb2 as pb2

def random_array():
    return [
        random.randint(0,500)
        for _ in range(10)
    ]

class Lab2_Client(object):
    def __init__(self):
        self.host = '0.0.0.0'
        self.server_port = 50050

        # instanciando o canal
        self.channel = grpc.insecure_channel('{}:{}'.format(self.host, self.server_port))

        # Bind entre client e server
        self.stub = pb2_grpc.Lab2Stub(self.channel)
    
    def get_array(self):
        r_array = random_array()

        print("------------------------------------------------------")
        print(r_array)
        print("------------------------------------------------------")

        num_list = pb2.Array(value=r_array)

        print('[Client] Sending array...')

        return self.stub.LessGreaterNumber(num_list)


if __name__ == '__main__':
    client = Lab2_Client()
    result = client.get_array()
    print(f'{result}')
