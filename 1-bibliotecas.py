# Documentação: https://docs.python.org/pt-br/3/library/os.html

# Bibliotecas
import os
import shutil
import glob

# Declaração das variáveis
directory = "Senai"
parent_dir = "C:/NewPasty"
path = os.path.join(parent_dir, directory)
 
# Criação do diretório
os.mkdir(path)
print("Diretório '% s' foi criado" % directory)

# Tratamento de erro 1
try:
    os.makedirs(path, exist_ok = True)
    print("Diretório '%s' criado com successo" % directory)
except OSError as error:
    print("Diretório '%s' não foi criado" % directory)

# Tratamento de erro 2
caminho = 'C:/Users/Aluno/Downloads/Senavas'

if os.path.exists(caminho):
    print('O diretório existe')
else:
    print('O diretório não existe')

# Renomear caminho do diretório
caminho_antigo = 'C:/Users/Aluno/Downloads/Senavas'
caminho_novo = 'C:/Users/Aluno/Documents/novoP#'
os.rename('O diretorio antigo {} mudou para a pasta {}'.format (str(caminho_antigo),str(caminho_novo)))

# Criar pasta se não existe
nome_pasta = "nova_pasta"

if not os.path.exists(nome_pasta):
    os.mkdir(nome_pasta)

# Procurar arquivo
arquivos_txt = glob.glob("*.txt")
print(f"Arquivos txt: {arquivos_txt}")

# Mover arquivo
diretorio_origem = "C:/NewPasta/Senai"
diretorio_destino = "C:/Users/Aluno/Documents/novoP#"

for nome_arquivo in os.listdir(diretorio_origem):
    caminho_origem = os.path.join(diretorio_origem, nome_arquivo)
    caminho_destino = os.path.join(diretorio_destino, nome_arquivo)
    shutil.move(caminho_origem, caminho_destino)

# Copiar arquivo
for nome_arquivo in os.listdir(diretorio_origem):
    caminho_origem = os.path.join(diretorio_origem, nome_arquivo)
    caminho_destino = os.path.join(diretorio_destino, nome_arquivo)
    shutil.copy(caminho_origem, caminho_destino)
 
# Renomear arquivo
diretorio = "C:/NewPasta/Senai"
prefixo = "novo_Sesc.log"

for nome_arquivo in os.listdir(diretorio):
    novo_nome = prefixo + nome_arquivo
    os.rename(os.path.join(diretorio, nome_arquivo), os.path.join(diretorio, novo_nome))

# Excluir arquivo
diretorio = "C:/Users/Aluno/Documents/novoP#"
extensao = "novo_Sesc.log"

for nome_arquivo in os.listdir(diretorio):
    if nome_arquivo.endswith(extensao):
        os.remove(os.path.join(diretorio, nome_arquivo))


txt_files = glob.glob('*.txt')
csv_files = glob.glob('data_*.csv')
xyz_files = glob.glob('?xyz')
all_txt_files = glob.glob('**.txt', recursive=True)
csv_files_in_subdir = glob.glob('C:/Users/Aluno/Documents/novoP#/**/*.csv', recursive=True)