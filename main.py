import Functions
from multiprocessing.pool import ThreadPool as Pool
proxys = []
WorksFile = open("ProxyWorks.txt", "r").read().split("\n")
NewFile = open("proxies.txt", "r").read().split("\n")
proxys = WorksFile + NewFile
proxys = list(set(proxys))

pool_size = 10
pool = Pool(pool_size)


if __name__ == '__main__':
    url = 'https://google.com' 
    Timeout = 5
    for proxy in proxys:
        pool.apply_async(Functions.test_proxy, (proxy, url, Timeout))

    pool.close()
    pool.join()

    with open('ProxyWorks.txt', 'w') as f:
        for line in Functions.ProxyWorks:
            f.write(f"{line}\n")
    open('proxies.txt', 'w').close()