import grpc
import random
import lab2_pb2_grpc as pb2_grpc
import lab2_pb2 as pb2

def random_array():
    print('[Client] Generating random array')
    return [
        #random.randint(0,500)
        random.uniform(0.0, 500000.0)
        for _ in range(500000)
    ]

class Lab2_Client(object):
    def __init__(self):
        self.host = '0.0.0.0'
        self.server_port = 5000

        # instanciando o canal
        self.channel = grpc.insecure_channel('{}:{}'.format(self.host, self.server_port))

        # Bind entre client e server
        self.stub = pb2_grpc.Lab2Stub(self.channel)
    
    def get_array(self):
        r_array = random_array()
        num_list = pb2.Array(value=r_array)

        print('[Client] Sending array...')

        return self.stub.LessGreaterNumber(num_list)


if __name__ == '__main__':
    client = Lab2_Client()
    result = client.get_array()
    print(f'{result}')


