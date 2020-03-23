a = "jga ocvg, jqy'u kv iqkpi? cnn iqqf?"
z = "hey mate, how's it going? all good?"
b = "abcdefghijklmnopqrstuvwxyz"
symbols = "?!,.;:' "


def decoder(message,offset):
  deciph = ""
  for i in range(len(message)):
    c = b.find(message[i])

    if message[i] in symbols:
        deciph += message[i]
    else:
        d=(abs(c+offset))%26
        deciph+=b[d]

  return deciph

def coder(message,offset):
  deciph = ""
  for i in range(len(message)):
    c = b.find(message[i])

    if message[i] in symbols:
      deciph += message[i]

    else:
        d = ((c - offset) % 26)
        deciph += b[d]


  return deciph


print(decoder(a,50))
print(coder(z,50))

def decoder2(message):
    for offset in range(50):
        deciph = ""
        for i in range(len(message)):
            c = b.find(message[i])

            if message[i] in symbols:
              deciph += message[i]

            else:
                d = ((c - offset) % 26)
                deciph += b[d]
        print(deciph)

