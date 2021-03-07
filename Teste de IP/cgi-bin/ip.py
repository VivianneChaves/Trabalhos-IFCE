#!/usr/bin/env python3

import cgitb, cgi
cgitb.enable(display=0, logdir="./")

form = cgi.FieldStorage()

ip = form.getvalue("ip")

print("Content-type:text/html\r\n\r\n")
print("<html><head><title>Teste de IP</title><meta charset=\"UTF-8\"></head>")
print("<body style=\"background-color:LightGray;\">")

print("<h1 style=\"font-size:300%;color:ForestGreen;text-aling: center;\">TESTE DE IP</h1><br>")

            

msg = "<h1 style=\"font-size:140%;color:red;text-aling: center; font-family:courier;\">Formato invalido</h1><br>"
validade = "<h1 style=\"font-size:140%;color:green;text-aling: center; font-family:courier;\">Valido</h1><br>"
classe ="<h1 style=\"font-size:140%;color:MidnightBlue;text-aling: center; font-family:courier;\">Classe Indefinida</h1><br>"
localoop = ""
i = 0
flag = 0
ip = ip.split(".")
if len(ip) != 4:
    msg = "<h1 style=\"font-size:140%;color:red;text-aling: center; font-family:courier;\">Formato invalido</h1><br>"
    flag = 1

while i < 4:
    if flag == 0:
        if ip[i] == " ":
            msg = "<h1 style=\"font-size:140%;color:tomato;text-aling: center; font-family:courier;\">Formato invalido</h1><br>"
            flag = 1
    i = i + 1

if flag != 1:
    ip1 = (int(ip[0]))
    ip2 = (int(ip[1]))
    ip3 = (int(ip[2]))
    ip4 = (int(ip[3]))
    if ip1 == 0:
        validade = "<h1 style=\"font-size:140%;color:red;text-aling: center; font-family:courier;\">Invalido</h1><br>"
    if ip1 > 256 or ip2 > 255 or ip3 > 255 or ip4 > 255 or ip1 < 0 or ip2 < 0 or ip3 < 0 or ip4 < 00:
        validade = "<h1 style=\"font-size:140%;color:red;text-aling: center; font-family:courier;\">Invalido</h1><br>"
    if ip1 == 127:
        validade = "<h1 style=\"font-size:140%;color:red;text-aling: center; font-family:courier;\">Invalido</h1><br>"
    if ip1 == 255:
        validade = "<h1 style=\"font-size:140%;color:red;text-aling: center; font-family:courier;\">Invalido</h1><br>"
    if ip3 == 255 and ip4 == 255:
        validade = "<h1 style=\"font-size:140%;color:red;text-aling: center; font-family:courier;\">Invalido</h1><br>"

    if 127 > ip1 > 0 and 256 > ip2 >= 0 and 256 > ip3 >= 0 and 256 > ip4 >= 0 :
        classe = "<h1 style=\"font-size:140%;color:MidnightBlue;text-aling: center; font-family:courier;\">Classe A</h1><br>"
    if 192 > ip1 > 127 and 226 > ip2 >= 0 and 256 > ip3 >= 0 and 256 > ip4 >= 0:
        classe = "<h1 style=\"font-size:140%;color:MidnightBlue;text-aling: center; font-family:courier;\">Classe B</h1><br>"
    if 224 > ip1 > 191 and 226 > ip2 >= 0 and 226 > ip3 >= 0 and 255 > ip4 >= 0:
        classe = "<h1 style=\"font-size:140%;color:MidnightBlue;text-aling: center; font-family:courier;\">Classe C</h1><br>"

    if ip1 == 127:
        localoop = "<h1 style=\"font-size:140%;color:orange;text-aling: center; font-family:courier;\">de Loopback</h1><br>"
        classe = "<h1 style=\"font-size:170%;color:MidnightBlue;text-aling: center; font-family:courier;\">Classe A</h1><br>"

    if ip1 == 192 and ip2 == 168:
        localoop = "<h1 style=\"font-size:140%;color:orange;text-aling: center; font-family:courier;\">Privado</h1><br>"

    if ip1 == 169 and ip2 == 254:
        localoop = "<h1 style=\"font-size:140%;color:orange;text-aling: center; font-family:courier;\">Privado</h1><br>"

erro =  "<h1 style=\"font-size:140%;color:tomato;text-aling: center; font-family:courier;\">Formato invalido</h1><br>"


if flag != 1:
    print("<h1 style=\"font-size:170%;color:tomato;text-aling: center;\">O IP analisado e:</h1>")
    print(ip)
    print("<br>") 
    print("<br>")
    print("<br>")
    print("<h1 style=\"font-size:170%;color:tomato;text-aling: center;\">Classificacao do IP:</h1>")
    print(validade,classe,localoop)
else:
    print( "<h1 style=\"font-size:140%;color:tomato;text-aling: center; font-family:courier;\">Formato invalido</h1><br>")
    print("<h1 style=\"font-size:140%;color:tomato;text-aling: center; font-family:courier;\">Coloque um IP no formato: num.num.num.num </h1><br>")
    


print("<br>")
print("<br>")
print("<a href=../index.html>Voltar</a>")
print("</body>")
print("</html>")
