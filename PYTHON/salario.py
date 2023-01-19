#salario



salario=float(input("informe o valor do salário: "))
print(f"{salario}")
desconto_inss=(salario*0.085)
desconto_ir=(salario*0.05)
salario_fim=(salario-desconto_inss-desconto_ir)
print(f"o salário final será: {salario_fim} ")
