peso=float(input("insira o peso:"))
altura=float(input("insira a altura:"))

IMC= peso/(altura**2)

if (2.5>altura>0.6)and(peso>15 and peso<250):
      
    
      if IMC<18.5:
           print("está abaixo do peso")
      elif IMC>18.5 and IMC<24.9:
           print("peso normal")
      elif IMC>25 and IMC<29.9:
           print("soprebeso")
      elif IMC>30 and IMC<34.9:
           print("obesidade grau 1")
      elif IMC>35 and IMC<39.9:
           print("obesidade grau 2")
      elif IMC>40:
           print("obesidade grau 3")

if(2.5>altura>0.6)and(peso>15 and peso<250):     
    
      print(f"o seu IMC é:{IMC}")
      
if (altura<0.6 or altura>2.5)and(250>peso>15):      
      
  print ("digite a altura novamente!")
if (2.5>altura>0.6)and(peso<15 or peso>250):
  print ("digite o peso novamente!")
  
if (altura<0.6 or altura>2.5)and(peso<15 or peso>250):

  print ("digite a altura e o peso novamente")