import binance_f

from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *

def ReadFile(inFile):
    inFile += ""#".txt"
    with open(inFile, "r") as f:
        content = f.readlines()    
    content = [x.strip() for x in content]
    return (content)

#request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
g_api_key = ReadFile("D:\Eslam Hosney\Software\Python\Binance\\new.txt")[0]
g_secret_key = ReadFile("D:\Eslam Hosney\Software\Python\Binance\\new.txt")[1]

print (g_api_key,g_secret_key)


print ("Authentication Key Fetched EL7!!!")

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

print ("Authentication Completed EL7!!!")

result = request_client.get_mark_price(symbol="BTCUSDT")

print ("Reading Completed EL7!!!")


print("======= Mark Price =======")
PrintBasic.print_obj(result)
print("==========================")