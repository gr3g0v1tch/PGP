import gnupg

def file_lengthy(fname):
        i=0
        with open(fname,'rb') as f:
                for l in f:
                        i=i+1
        return i

wordfile = "zeropass1.txt"
wdLines = file_lengthy(wordfile)
print("Dictionnaire",wordfile,"has",wdLines,"entries.")

wd = open(wordfile)

gpg = gnupg.GPG(gnupghome='/root/ctf/script/gpg_decrypt')

i=0

for word in wd: 
        with open('flag.txt.gpg', 'rb') as f:
                #real passphrase is "password"
                word = word.rstrip("\n")
                #print('test passwrd ',word)
                status = gpg.decrypt_file(f, passphrase=word, output='my-decrypted.txt')
                if status.ok:
                        print('passphrase is: ',word)
        f.close()

        i = i+1
        if i%10000==0:
                progress = round(((i / wdLines)*100),1)
                print(progress,'per cent of the dic browsed')

wd.close()
