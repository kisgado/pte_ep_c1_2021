szavak = ["almaszár","Misina","kerékgyártó","Égervölgyi tó","Flóra-pihenő","Tenkes","Malomvölgy","Zsolnay-kút"]

for szo in szavak:
    if(len(szo)>10):
        hosszabb=" -  10 karakternél hosszabb"
    else:
        hosszabb=""
    print(szo,len(szo),hosszabb)