# omid_khosusi

import random
kochici="qwertyuiopasdfghjklzxcvbnm"
bozoeg="QWERTYUIOPASDFGHJKLZXCVBNM"
nombar="1234567890"
ghayra="\.!#$%^&*()-_),=-@@@@@.\]+["

all =kochici+bozoeg+nombar+ghayra
tool_pasbord =20
passbord ="".join(random.sample(all,tool_pasbord))

print(passbord)
