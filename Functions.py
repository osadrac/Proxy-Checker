import urllib.request
import ssl
import json
ProxyWorks = []
def test_proxy(proxy, url, Timeout):

    proxy_handler = urllib.request.ProxyHandler({'http': proxy, 'https': proxy})
    opener = urllib.request.build_opener(proxy_handler, urllib.request.HTTPSHandler(context=ssl._create_unverified_context()))
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]

    try:
        response = opener.open(url, timeout=Timeout)
        if response.getcode() == 200:
            print(f"Proxy {proxy} está funcionando corretamente")
            ProxyWorks.append(proxy)
        else:
            print(f"Proxy {proxy} retornou uma resposta inválida")
    except urllib.error.URLError as e:
        print(f"Erro ao conectar-se ao proxy {proxy}: {e.reason}")

def GetListUrlJson():
    opener = urllib.request.build_opener(urllib.request.HTTPSHandler(context=ssl.create_default_context()))
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    ProxyJson = []
    ReturnProxy = []
    try:
        TotalPages = 2
        Loop = 1
        while( Loop < TotalPages):
            response = opener.open(f"https://proxylist.geonode.com/api/proxy-list?limit=500&page={Loop}&sort_by=lastChecked&sort_type=desc", timeout=10)
            ProxyJson = json.loads(response.read())
            TotalPages = int(ProxyJson['total'] / ProxyJson['limit'])
            for x in ProxyJson['data']:
                ReturnProxy.append(x['ip'] + ":" + x['port'])
            Loop += 1
        return ReturnProxy
    except urllib.error.URLError as e:
        return ReturnProxy
    
def GetListUrlList():
    ReturnProxy = []
    with urllib.request.urlopen('https://api.proxyscrape.com/v3/free-proxy-list/get?request=getproxies&proxy_format=ipport&format=json') as f:
        html = f.read().decode('utf-8')
    TmpJson = json.loads(html)
    for x in TmpJson['proxies']:
        ReturnProxy.append(x['proxy'])
    return ReturnProxy