hp_ryu = int(input())
hp_ken = int(input())
g_ryu = 0
g_ken = 0

while hp_ken > 0 and hp_ryu > 0:
  golpe = int(input())
  if golpe > 0: 
    hp_ken = hp_ken - golpe
    g_ryu += 1
    print("RYU APLICOU UM GOLPE:", golpe)
    print("HP RYU =", hp_ryu)
    if hp_ken > 0:
      print("HP KEN =", hp_ken)
    else:
      print("HP KEN = 0")

  elif golpe < 0:
    hp_ryu = hp_ryu + golpe
    g_ken += 1
    print("KEN APLICOU UM GOLPE:", abs(golpe))
    if hp_ryu > 0:
        print("HP RYU =", hp_ryu)
    else:
        print("HP RYU = 0")
    print("HP KEN =", hp_ken)
  

else:
  if hp_ken <= 0:
    print("LUTADOR VENCEDOR: RYU")
    print("GOLPES RYU =", g_ryu)
    print("GOLPES KEN =", g_ken)
  if hp_ryu <= 0:
    print("LUTADOR VENCEDOR: KEN")
    print("GOLPES RYU =", g_ryu)
    print("GOLPES KEN =", g_ken)