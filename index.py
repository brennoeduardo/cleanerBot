import os
import subprocess

pasta_temp = 'C:\\Windows\\Temp'

for item in os.listdir(pasta_temp):
    file_path = os.path.join(pasta_temp, item)
    try:
        if os.path.isdir(file_path) and not os.listdir(file_path):
            os.rmdir(file_path)
            print(f'Diretório removido: {item}')
        else:
            os.remove(file_path)
            print(f'Arquivo removido: {item}')
    except PermissionError:
        print(f'Acesso negado para remover {item}. Tentando mudar permissões...')
        subprocess.run(['takeown', '/F', file_path])
        subprocess.run(['icacls', file_path, '/grant', f'{os.getlogin()}:F'])
        try:
            os.remove(file_path)
            print(f'Arquivo removido após alteração de permissões: {item}')
        except Exception as e:
            print(f'Não foi possível remover {item} após alteração de permissões: {e}')
            try:
                subprocess.run(['yarn', 'cache', 'clean'], check=True)
                print('Cache do Yarn limpo com sucesso.')
            except Exception as e:
                print(f'Erro ao executar o comando yarn cache clean: {e}')
    except Exception as e:
        print(f'Não foi possível remover {item}: {e}')
