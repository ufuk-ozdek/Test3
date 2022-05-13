
"""
jump kullanmamın sebebi write ile read arasındaki açılan mesafeyi kapatmak
dosyanın her 7 baytını okurken 6 sını write ediyorum fakat okumaya kaldığım yerden
devam edebilmek için write ile read arasındaki mesafeyi jump kullanarak atlıyorum benzer şekilde
okuduktan sonra en son yazdığım yere dönebilmek için yine jump kullanıyorum.

"""
with open("data.bin", "rb+") as f:
    jump = 0
    while len(f.read(1)):
        f.seek(-1, 1)
        chars = f.read(7)
        if len(chars) < 7:
            if len(chars) > 0:
                f.seek(-1 * len(chars) - jump, 1)
                f.write(chars)
                f.seek(jump, 1)
            break
        f.seek(-1 * len(chars) - jump, 1)
        f.write(chars[:-1])
        jump += 1
        f.seek(jump, 1)
    f.seek(-1 * jump, 1)
    f.truncate()