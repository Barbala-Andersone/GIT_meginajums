"""
d=open("puce1.txt", "r", encoding="utf8")
print(d.read())

# Faila tekstam pievienot "vasara būs!"
d=open("puce1.txt","a", encoding="utf8")
d.write("\nvasara būs!")         # \n 
d.close()
"""

# Atvērt failu, ierakstot tajā četrrindi.
"""
a=open("puce13.txt", "w", encoding="utf8")
a.write("mana \nlaipa \nir \nšeit!")
a.close()
"""
#vai

ziema=open("puce.txt", "w", encoding="utf8")
lin1="mana \n"
lin2="laipa \n"
lin3="ir \n"
lin4="šeit! \n"

ziema.write(lin1+lin2+lin3+lin4)
ziema.close()