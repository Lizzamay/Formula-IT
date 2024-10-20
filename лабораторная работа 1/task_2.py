volume=1.44
stranic=100
strok=50
simvol=25
khranenie=4
ss=khranenie*simvol
stranica=ss*strok
kniga=stranica*stranic
mb=kniga/1024/1024
number=volume//mb
print("Количество книг, помещающихся на дискету:", int(number))


