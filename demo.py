# coding:utf-8
import requests
import time
import execjs

def get_time():
    now = int(time.time())*1000
    now = now + (16798545 + -72936737 + 156138192)
    print(now)
    return now

def js_md5(timestamp):
    js_txt = open('yuanrenxue1.js','r',encoding='utf-8').read()
    js_complie = execjs.compile(js_txt)
    hex_md5 =  js_complie.call('hex_md5',str(timestamp))
    print(hex_md5)
    return hex_md5

def yuanrenxue_sprider(md5,timestamp,page):
    url = 'https://match.yuanrenxue.com/api/match/1?page={page}&m={m}'.format(page=page,m=md5+'丨'+str(int(timestamp / 1000)))
    print(url)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.10 Safari/537.36',
        'cookie': 'Hm_lvt_0362c7a08a9a04ccf3a8463c590e1e2f=1632991231; vaptchaNetway=cn; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1632991226,1633063557; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1632991248,1633063559; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1633063559; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1633063623'
    }

    if page == 4 or page == 5:
        headers['user-agent'] = 'yuanrenxue.project'
    response = requests.get(url,headers=headers)
    res = response.json()
    for i in res['data']:
        data = i['value']
        ticket_lists.append(data)

if __name__ == '__main__':
    ticket_lists = []
    timestamp = get_time()
    md5 = js_md5(timestamp)
    for i in range(1,6):
        yuanrenxue_sprider(md5,timestamp,i) 
    #计算飞机票总数 和平均值 
    average = sum(ticket_lists) / len(ticket_lists)
    print('飞机票的平均值为：',average)
