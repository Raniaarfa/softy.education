Kdrama ={"revenat","goblin","18 again","snowdrop"}
Kdrama.add('penthouse')
Kdrama.discard('18 again')
Kdrama.update({"humming bird", "connected "})

other_kdrama = {"move to heaven","taxi driver"}

print("\nnames before update :")
print (Kdrama)

Kdrama.update(other_kdrama)
print("\nnames after update :")
print(Kdrama,"\n")