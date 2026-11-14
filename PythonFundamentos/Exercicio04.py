#receba nome , peso e altura. Calcule IMC.

#entrada
nome = input ("Digite seu nome:")
peso = float (input("digite o seu peso"))
altura = float (input("digite sua altura"))

#processamento

#IMC = peso (Kg) / [altura] (m)
IMC = peso / (altura*altura)

#saida
print(f"o é {nome}, seu IMC é: {IMC: .2f}")