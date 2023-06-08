from classes.MenuGerenciadorS3 import MenuGerenciadorS3


#controla_s3 = GerenciarS3('aulanoitekawan02')

#controla_s3.lista_arquivos()

#controla_s3.delete_arquivo('index.html')

#controla_s3.upload_arquivo('/home/ec2-user/environment/POO-31-05/arquivos/Capturar.PNG', 'Capturar.PNG')

#diretorio_destino = '/home/ec2-user/environment/POO-31-05/arquivos/'
#nome_arquivo = 'Capturar.PNG'
#controla_s3.download_arquivo(nome_arquivo, diretorio_destino)

nome_bucket = 'aulanoitekawan02'
menu = MenuGerenciadorS3(nome_bucket)
menu.executar()