ime_grada = input("Unesi ime jednog grada. ")
ime_životinje = input("Unesi ime jedne životinje. ")
ime_prijatelja = input("Unesi ime jednog prijatelja. ")

najduže_ime = max([ime_grada, ime_životinje, ime_prijatelja], key=len)
print(f" Najduže ime ima {len(najduže_ime)} karaktera, {najduže_ime}")

najkraće_ime = min([ime_grada, ime_životinje, ime_prijatelja], key=len)
print(f"Najkraće ime ima {len(najkraće_ime)} karatera, {najkraće_ime}")
















#if len(ime_grada) > len(ime_prijatelja and len(ime_grada) > len(ime_životinje)):
    #print(len(ime_grada))

#if len(ime_grada) > len(ime_prijatelja) > len(ime_životinje) and len(ime_prijatelja) > len(ime_životinje) > len(ime_grada):
    #print(f"Najduže ime ima 6 karaktera: {ime_grada}")

#else:
    #print(f"Najkraće ime ima 4 karaktera: {ime_životinje}")


