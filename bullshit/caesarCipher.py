# just a tiny code to decode the sasear cipher

def decode():
    sen = raw_input('please input a cipher code:')
    for i in range(1,25):
        list_s = []
        for j in range(len(sen)):
            if sen[j]>='a' and sen[j]<='z':
                ch = ord(sen[j])+i
                if ch > ord('z'):
                    ch = ch - 26
                list_s.append(chr(ch))
            else:
                list_s.append(sen[j])
        newsen = ''.join(list_s)
        print newsen

if __name__== '__main__':
    decode()
