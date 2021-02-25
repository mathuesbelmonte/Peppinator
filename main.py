personagens = ["Peppa Pig", "Danny Dog", "Suzy Sheep", "Pedro Pony", "Freddy Fox", "Emily Elfante", "George Pig", "Mommy Pig", "Candy Cat", "Rebecca Rabbit"]

print("Seja bem-vindo ao Peppanator. Aqui vamos adivinhar em qual personagem do mundo Peppa você está pensando. Estes são os persoagens disponíveis: \n\n* Peppa Pig\n* Danny Dog\n* Suzy Sheep\n* Pedro Pony\n* Freddy Fox\n* Emily Elephant\n* George Pig\n* Mommy Pig\n* Candy Cat\n* Rebecca Rabbit")


#meninas: Peppa, Suzy, Rebecca, Emily, Mommy, Candy
#meninos: Pedro, Danny, Freddy, George

resposta = 0
iniciar = input("\nIniciar: ")
if iniciar == "true":
  resposta = 1

while resposta == 1:

  boy = input("\n\nO personagem é um menino? " )

  if boy == "true":
  
    dog = input("Seu personagem é um cachorro? " )

    if dog == "true":
      print("Seu personagem é o Danny Dog! ")

    if dog == "false":
      pony = input("Seu personagem é um pônei? ")
      if pony == "true":
        print("Seu personagem é o Pedro Pony!" )
      else:
        pig=input("Seu personagem é um porco? ")
        if pig == "true":
          print("Seu personagem é o George Pig! " )
        else: 
          print("Seu personagem é o Freddy Fox! " )


  else:
  
    pig = input("O seu personagem é um porco? " )

    if pig == "true":
      adult=input("Seu personagem tem mais de 18 anos? ")
      if adult == "true":
        print("O seu personagem é a Mommy Pig! " )
      else:
        print("O seu personagem é a Peppa Pig! " )

    

    if pig == "false":
      sheep=input("Sua personagem é uma ovelha? ")
      if sheep == "true":
        print("Sua personagem é a Suzy Sheep! " )
      else:
        rabbit=input("Sua personagem é um coelho? ")
        if rabbit == "true":
          print("Sua personagem é a Rebecca Rabbit! " )
        else:
          elephant=input("Sua personagem é um elefante? ")
          if elephant == "true":
            print("Sua personagem é a Emily Elephant! " )
          else:
            print("Sua personagem é a Candy Cat! " )
      
    


  resposta = int(input('\nDeseja jogar novamente ou fechar o sistema?\nDigite "1" para reiniciar e "2" para fechar: '))
  if resposta == 2:
    print('\nVocê optou por fechar o sistema. Obrigado por usar o programa! Adeus.')
