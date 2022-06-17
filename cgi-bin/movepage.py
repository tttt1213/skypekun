import cgi
import codecs

def html():
    #html = codecs.open('index.html', 'r', 'utf-8').read()
    #print("")
    #print (html)
    print ("Content-type: text/html;\n\n")
    print ("<meta http-equiv=\"refresh\" content=\"0;URL=http://192.168.20.188:8000/\">")

    
if __name__ == '__main__':#直接yobareru.pyを実行した時だけ、def test()を実行する
    print ("hello world!")
