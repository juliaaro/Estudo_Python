bruto = float(input())

# Desconto do INSS
if bruto <= 1045.00:
  inss = bruto * 0.075
elif 1045.01 <= bruto <= 2089.60:
  inss = bruto * 0.09
elif 2089.61 <= bruto <= 3134.40:
  inss = bruto * 0.12
elif 3134.41 <= bruto:
  inss = bruto * 0.14

s_inss = bruto - inss

# Desconto do IR
if s_inss <= 1903.98:
  ir = 0
  s_liq = s_inss
elif 1903.99 <= s_inss <= 2826.65:
  ir = s_inss * 0.075 - 142.80
elif 2826.66 <= s_inss <= 3751.05:
  ir = s_inss * 0.15 - 354.80
elif 3751.06 <= s_inss <= 4664.68:
  ir = s_inss * 0.225 - 636.13
elif 4664.69 <= s_inss:
  ir = s_inss * 0.275 - 869.36

s_liq = s_inss - ir

print("Bruto: R$", format(bruto, ".2f").replace(".", ","))
print("INSS: R$", format(inss, ".2f").replace(".", ","))
print("IR: R$", format(ir, ".2f").replace(".", ","))
print("Liquido: R$", format(s_liq, ".2f").replace(".", ","))