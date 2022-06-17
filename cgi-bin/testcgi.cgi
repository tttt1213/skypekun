import cgi
f = cgi.FieldStorage()
if f.getfirst('btn1'):
    btn = '1'
elif f.getfirst('btn2'):
    btn = '2'
elif f.getfirst('btn3'):
    btn = '3'
else:
    btn = ''
print (html % btn)