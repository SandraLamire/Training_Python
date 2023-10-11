"zre gfseg srt hdr h"
# commentaire en début de page devient la doc de la page

# 1er datetime = module, 2nd = object
from datetime import datetime
# Si import datetime seul, utiliser après datetime.datetime

def day_and_month(date: datetime):
    day = date.day
    month = date.month
    return (day, month)

(day, month) = day_and_month(datetime.now())

res = f"""zmoe gjimoizj egmoijz ergoij zerog ij zeorji zrrg
sze ghezhui ezruih""" , str(day) , """ ezrhui ezrihu ezrg 
ezrg iou rezg oihu ezrhui ezrohui ezrg u u"""
print(res)

#----------------------------------------------------#

a = 25

def add(a, b):
    # commentaire en début de fonction devient la doc de la fonction
    "Returns the sum of a and b"
    res = a
    res += b
    return res

print(a)

if __name__ == "__main__":
    print(add(2, 2))
    