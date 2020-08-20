hour=float(input())
min=float(input())
sec=int(input())
if sec >=3600:
    hour=hour+(sec//3600)
    sec%=3600
if sec<3600:
    min=min+(sec//60)
    sec%=60
if min>=60:
    hour=hour+(min//60)
    min%=60
if min<60:
    sec=min*60
    if sec >=3600:
        hour=hour+(sec//3600)
        sec%=3600
    if sec<3600:
        min=(sec//60)
        sec%=60
# print(hour,min,sec)
print('{:02}'.format(int(hour)),'{:02}'.format(int(min)),'{:02}'.format(int(sec)))