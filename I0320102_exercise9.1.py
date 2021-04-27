import sys

# mendefinisikan array konstan
hari = ('Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu')

def main() :
    #meminta user input nomor hari
    nomor_hari = int(input('Masukkan nomor hari [1..7] : '))

    if (nomor_hari < 1) or (nomor_hari > 7) :
        print('Tidak ada hari ke- %s' % nomor_hari)
        sys.exit(1)

    print('Hari ke-%d adalah %s' %(nomor_hari, hari[nomor_hari-1]))

if __name__ == '__main__' :
    main()
