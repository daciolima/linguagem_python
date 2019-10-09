"""
 Escrevendo em arquivos

 OBS:
    1 - AO abrir um arquivo em modo leitura não podemosrealizar escrita nele. Apenas ler.
    Ao abrir arquivos em modo escrita, não podemos lê-lo, somente escrever nele.

 OBS2:
  1- -Ao abrir um arquivo para escrita,, o arquivo é criado no sistema operacional.


  Para escrevermos dados em um arquivo, após abrir o arquivo a função write(), está
  Esta funcão recebe uma string como parâmetro, caso contrário teremos um TypeError

  Abrindo um arquivo para escrita(w), se existir já um arquivo com o mesmo nome ocorrerá a sobrescrita
  do conteúdo, caso contrário será criado um arquivo novo com o nome dado.

"""

with open('file2.txt', 'w', encoding="utf-8") as arquivo:
    arquivo.write('Estou aprendendo Python!!')
    arquivo.write('Linguagem é muito bacana')
    arquivo.write('Está é a última linha')


with open('numeros.txt', 'w', encoding="utf-8") as numeros:
    numeros.write('Dacio lima ' * 1000)

with open('frutas.txt', 'w', encoding="utf-8") as frutas:
    while True:
        fruta = input('Informe o nome de uma fruta: ')
        if fruta != 'sair':
            frutas.write(fruta)
            frutas.write('\n')
        else:
            break

