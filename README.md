Um testador de proxys usando ThreadPool para testar varios proxys ao mesmo tempo.
Os proxys sao adicionados ao arquivo proxies.txt com os seguintes formatos

ip:port

user:pass@ip:port

Apos testar os proxys que estiverem funcionando sao adicionados ao arquivo ProxyWorks.txt e o arquivo proxies.txt é limpo, para a segunda verificação ele aproveita os proxys checados anteriormente do arquivo ProxyWorks.txt e testa novamente junto com os novos proxys.


