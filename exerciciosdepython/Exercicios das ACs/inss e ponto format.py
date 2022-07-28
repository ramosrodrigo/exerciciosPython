salario_base = float(input())


if salario_base <= 1751.81:
   print("Desconto do INSS: R$ {:.2f}".format(salario_base * 0.08))
elif salario_base < 2919.73:
   print("Desconto do INSS: R$ {:.2f}".format(salario_base * 0.09))
elif salario_base <=5839.45:
   print("Desconto do INSS: R$ {:.2f}".format(salario_base * 0.11))
else:
   print("Desconto do INSS: R$ {:.2f}".format(5839.45 * 0.11))

   
