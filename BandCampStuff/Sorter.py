import requests
r =  requests.get("https://aarongrooves.bandcamp.com/album/avm-16-note-block-battle-ost-animation-vs-minecraft-shorts-ep-16", stream=True)

sc = 0
def scan(url):
    global sc
    for i in url.iter_lines(decode_unicode=True):
                    ha = []
                    if r"https://t4.bcbits" in i:
                        ha = str(i).split(";")
                    else:
                        pass
                    for k,j in enumerate(ha):
                        if r"https://t4.bcbits" in j:
                            sc+=1
                            l=requests.get(f"{ha[k]};{ha[k+1]};{ha[k+2]};{ha[k+3]}")
                            if l.ok:
                                #print(f"{sc} :",l.url)
                                open(f'dl/{sc}.mp3', 'wb').write(l.content)
                            else:
                                print(f"Error {l.status_code}")


if "sitemap" not in r.url:
    scan(r)
else:
    for link in r.iter_lines(decode_unicode=True):
        if "loc" in link:
            print("op1")
            cont = str(link).replace("<",";").replace(">",";").split(";")
            for en in cont:
                if r"https" in en:
                    sitemap = requests.get(en, stream=True)
                    scan(sitemap)
                    