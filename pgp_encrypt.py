import gnupg

gpg = gnupg.GPG(gnupghome='/root/ctf/script/gpg_decrypt')

#to encrypt a small message
#data = "My name is gr3g"
#result = str(gpg.encrypt(data, recipients='None', symmetric='AES256', passphrase='ensibs', output='data.txt.gpg'))


#I use AES256 which is a symetric encryption mechanism
with open('PFE.docx','rb') as f:
        encryption = gpg.encrypt_file(f, recipients='None', symmetric='AES256', passphrase='ensibs', output='PFE.docx.gpg')
f.close()

print(encryption.status)
