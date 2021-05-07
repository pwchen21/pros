class Codec:
    urlD={}

    def encode(self, longUrl: str) -> str:
        sht=''
        for x in longUrl[-1::-2]:
           #print(x)
            if x not in ['.', '//', '/']:
                sht+=x
            if (len(sht) >= 5) and (sht not in self.urlD):
                break


        self.urlD[sht]=longUrl
        print('http://tinyurl.com/'+sht)
        print(self.urlD)
        return 'http://tinyurl.com/'+sht
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        tmp=shortUrl.split('om/')
        print(self.urlD[tmp[1]])


A=Codec()
print('----sample')
A.encode("http://testa.jiwoji.com.tw")
A.encode("http://testa.jiwoji.com.tw.aa")
A.decode("http://tinyurl.com/wojwj")
A.decode("http://tinyurl.com/atmci")
print('---Failed')
A.encode("https://www.example.com/amount")
A.decode("http://tinyurl.com/tumol")
