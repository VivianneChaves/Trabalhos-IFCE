#!/usr/bin/env python3

import cgitb, cgi
cgitb.enable(display=0, logdir="./")

form = cgi.FieldStorage()

ip = form.getvalue("ip")

print("Content-type:text/html\r\n\r\n")
print("<html><head><title>Teste de IP</title><meta charset=\"UTF-8\"></head>")
#print("<body style=\"background-color:black;\">")
print("<img src=\"imagens/WhatsApp Image 2020-08-03 at 3.14.37 PM.jpeg\" width=\"360\">")
print("<h1 style=\"font-size:300%;color:tomato;\">TESTE DE IP</h1><br>")
            

msg = 'erro'
validade = 'Valido'
classe = "Classe Indefinida"
localoop = ""
i = 0
flag = 0
ip = ip.split(".")
if len(ip) != 4:
    msg = "Erro"
    flag = 1

while i < 4:
    if flag == 0:
        if ip[i] == "":
            msg = "Erro"
            flag = 1
    i = i + 1

if flag != 1:
    ip1 = (int(ip[0]))
    ip2 = (int(ip[1]))
    ip3 = (int(ip[2]))
    ip4 = (int(ip[3]))
    if ip1 > 256 or ip2 > 255 or ip3 > 255 or ip4 > 255 or ip1 < 0 or ip2 < 0 or ip3 < 0 or ip4 < 00:
        validade = "style=\"color:red;\">Invalido<"
    if ip1 == 127:
        validade = "style=\"color:red;\">Invalido<"
    if ip1 == 255:
        validade = "style=\"color:red;\">Invalido<"
    if ip3 == 255 and ip4 == 255:
        validade = "style=\"color:red;\">Invalido<"

    if 127 > ip1 > 0 and 256 > ip2 >= 0 and 256 > ip3 >= 0 and 256 > ip4 >= 0 :
        classe = "style=\"color:red;\">Classe A<"
    if 192 > ip1 > 127 and 226 > ip2 >= 0 and 256 > ip3 >= 0 and 256 > ip4 >= 0:
        classe = "style=\"color:red;\">Classe B<"
    if 224 > ip1 > 191 and 226 > ip2 >= 0 and 226 > ip3 >= 0 and 255 > ip4 >= 0:
        classe = "style=\"color:red;\">Classe C<"

    if ip1 == 127:
        localoop = "style=\"color:red;\">Loopback<"
        classe = "style=\"color:red;\">Classe A<"

    if ip1 == 192 and ip2 == 168:
        localoop = "style=\"color:red;\">Privado<

    if ip1 == 169 and ip2 == 254:
        localoop = ("\<h1 "style=\"color:red;\">Privado</h1>")

msg = "Ip " + validade + " e de "+ classe + localoop
print(validade)
print(classe)
print(localoop)
print("<br>")
print("<a href=../index.html>Voltar</a>")
print("</body>")
print("</html>")
