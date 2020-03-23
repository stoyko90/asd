b = "abcdefghijklmnopqrstuvwxyz"
symbols = "?!,.;:' "
def decoder(message,keyword):
  deciph = ""
  count=0
  for i in range(len(message)):
        c = b.find(message[i])
        if c==-1:
            deciph += message[i]
            count-=1
        else:
            d = b.find(keyword[((i+count) % len(keyword))])
            f = c - d
            deciph += b[f]
        print(i,c,d,f,count)
  return deciph

def coder(message,keyword):
  deciph = ""
  count=0
  for i in range(len(message)):
        c = b.find(message[i])
        if c==-1:
            deciph += message[i]
            count-=1
        else:
            d = b.find(keyword[((i+count) % len(keyword))])
            f = (c + d)%26
            deciph += b[f]
        print(i,c,d,f,count)
  return deciph
print(decoder("kco oids utpq hi viocxw xtwm? fmos qgvw! mim eds vwgaacfk cicli fvy wbbsll ef qlqxaulsttm!","mouse"))
print(coder("you were able to decode this? nice work! you are becoming quite the expert at crytography!","mouse"))