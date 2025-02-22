print("Dobrodošli u Lov na Blago!")

put = int(input("Nalaziš se na pustom ostrvu, a pred tobom su dva puta. Unesi bilo koji cijeli broj. "))
print(put)

if put % 2:

    print("Tvoj broj je paran. Ideš prvim putem")

else:
    print("Tvoj broj je neparan. Ideš putem preko neobične plaže.")

vrata = int(input("Ispred tebe su tri vrata: 1, 2 i 3. Koja biraš? "))
print(vrata)

if vrata != 3:
    print("Pogrešan broj! GAME OVER!")
else:
    print("Sreća te poslužila! Broj ti je djeliv sa 3, pronašao si tajnu prečicu i spasio se!")