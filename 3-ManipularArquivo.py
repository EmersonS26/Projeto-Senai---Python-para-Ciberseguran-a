arquivotxt = "arquivotxt.txt"

with open(arquivotxt, "w") as f:
    f.write("Arquivo criado\n")

f=open(arquivotxt, "r")
conteudo = f.read()
print(conteudo)

with open(arquivotxt, "w") as f:
    f.write("Sobre\n")

print(open(arquivotxt,"r").read())

with open(arquivotxt, "w") as f:
    f.write("Python Modulo 1 - Python para ciberseguranca\n")
    f.write("Python Modulo 2 - Ethical Hacking\n")
    f.write("Python Modulo 3 - Blue Team\n")
    f.write("Python Modulo 4 - Red Team\n")
    f.write("Python Modulo 5 - Purple Team\n")

lines = []
with open(arquivotxt) as f:
    lines = f.readline()

count = 0
for line in lines:
    count = count+1
    print(f"linha {count}: {line}")

lines

with open(arquivotxt) as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line)

with open(arquivotxt) as f:
    for line in f:
        print(line)

f = open(arquivotxt, "r")
conteudo = f.read()
f.close()
