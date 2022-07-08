clients = 'pablo,ricardo,'


def create_client(client_name):
    global clients

    clients += client_name
    _add_comma()


def list_clients():
    global clients
    print(clients)

def _add_comma():
    global clients
    clients += ','

def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50) 
    print('What would like to do today?')
    print('[C]reate client')
    print('[D]elete client')

if __name__ == '__main__':
    list_clients()

    create_client('David')

    print(clients)

    list_clients