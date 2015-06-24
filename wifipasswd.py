import subprocess, sys


perfis = []
senhas = open('senhas.txt', 'w')


rawoutput = subprocess.getoutput('chcp 1250 > nul && netsh wlan show profiles | find "Todos os Perfis de Usuários:" ').split('\n')
for x in rawoutput: perfis.append(x.replace('Todos os Perfis de Usuários: ', ''))
if not perfis[0]:
        print('[-]Nenhum perfil para ser exportado')
        sys.exit(1)
else:
        for perfil in perfis:
                try:
                        print('[+] Exportado o perfil: {perfil}' .format(perfil = perfil))
                        senhas.writelines(subprocess.getoutput('chcp 1250 > nul && netsh wlan show profiles name="{perfil}" key=clear'.format(perfil $
                except:
                        print('[-] Falha ao exportar o perfil: {perfil}'.format(perfil = perfil))


print('\nFinalizado!\n[+] Perfis exportados para o arquivo senhas.txt')
senhas.close()
