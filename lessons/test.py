my_fave_frats: dict[int,str] = {1:"pika", 2:"aepi"}
my_fave_frats[2] = "dsig"
my_fave_frats[3] = "lit"
my_fave_frats.pop(1) 

tay: dict[str,int] = {"lover":1,"midnights":2}
tay.pop("lover")
tay["speaknow"] = 3
tay["midnights"] += 1

girls: dict[str,int] = {"julia":1,"aarya":2,"bella":3,"kate":4}

for drunk in girls:
    print(drunk)
    print(girls[drunk])

print(dict(my_fave_frats))
print(dict(tay))
ok: bool ="yay" in tay
print(len(my_fave_frats))
print(ok) 