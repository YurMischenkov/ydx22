pos = 0
with open("res.bmp", "wb") as bfile:
    with open("input.bmp", "rb") as f:
        while (byte := f.read(1)):
            pos += 1
            if pos>53:
                byte = (255-int.from_bytes(byte, byteorder='big')).to_bytes(1, byteorder='big')
            bfile.write(byte)
