import ipfshttpclient

client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')


def push(client):

    res = client.add('useless_file.pdf')

    print("File Added with CID:", res['Hash'])
    
    file_cid = res['Hash']
    
    return file_cid



def pull(file_cfd):
    
    file = client.cat(file_cfd)
    
    print("Retrieved File is: "+ file)
    
    
def peers():
    
    peers = client.swarm.peers()
    print("Connected Peers:", peers)