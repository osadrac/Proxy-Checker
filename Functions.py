import urllib.request
import ssl

ProxyWorks = []
def test_proxy(proxy, url, Timeout):

    proxy_handler = urllib.request.ProxyHandler({'http': proxy, 'https': proxy})
    opener = urllib.request.build_opener(proxy_handler, urllib.request.HTTPSHandler(context=ssl.create_default_context()))
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
