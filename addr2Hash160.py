import codecs
import sys
import base58

def a2H160(filein, fileout):
    with open(filein) as inf, open(fileout, 'wb') as outf:
        count = 0
        skip = 0
        for address in inf.readlines():
            address = address.strip()
            try:
                hash160 = base58.b58decode_check(address)  #
                hash160 = codecs.encode(hash160, 'hex').decode()[2:]
                outf.write(bytes.fromhex(hash160))
                count += 1
            except:
                skip += 1
                print("Skipped address: ", address)

        print('Count: ', count, ' - ', '\n Skipped: ', skip,)


argc = len(sys.argv)
argv = sys.argv

if argc == 1 or argc != 3:
    print('Usage:')
    print('\tpython3 ' + argv[0].replace('\\', '/').split('/')[-1] + ' addrIn.txt hashOut.bin')
elif argc == 3:
    a2H160(argv[1], argv[2])
