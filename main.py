import funcLOF as lof


def menu():
    menuAwal = (
        '\nLocal Outlier Factor\n'
        '________________________________\n'
        '\nPilih dengan input angka\n'
        '  [1] Input Data Lewat Console\n'
        '  [2] Input Data Random\n'
        '  [3] Input Data Template Soal\n'
        '  [4] Keluar'
        '\n\nPilihan : '
    )
    pilihan = input(menuAwal)
    return int(pilihan)


def calcLOF():
    print('\n#  Data Awal\n')
    print(dataAwal)

    print('\n\n#1 Proximity Matrix\n')
    proxMatrix = lof.proximity_matrix(dataAwal, dataAwal)
    lof.np.set_printoptions(precision=2, suppress=True)
    print(proxMatrix)

    print('\n\n#2 Nearest Matrix sejauh K\n')
    K = input('Ukuran K: ')
    idxM = lof.idx_matrix(proxMatrix.shape[0])
    lof.nearest_matrix(proxMatrix, idxM)

    print('\n\n#2.1 Index dari Nilai Terdekat\n')
    print(idxM[:, 1:K+1])

    print('\n\n#2.2 Nilai Terdekat\n')
    print(proxMatrix[:, 1:K+1])

    print('\n\n#3 Average Density\n')
    avgDens = lof.average_density(K, proxMatrix[:, 1:K+1])
    print(avgDens)

    print('\n\n#4 Average Relative Density\n')
    avgRel = lof.average_rel_dens(idxM[:, 1:K+1], avgDens, K)
    print(avgRel)

    print('\n\n#5 Nilai Outlier\n')
    batas = input('Nilai threshold: ')
    print('')
    outlier = avgRel[avgRel > batas]
    totalOutlier = outlier.shape[0]
    print(outlier.reshape(totalOutlier, 1))
    print('\n________________________________\n')


while True:
    dataAwal = []
    pil = menu()
    if pil == 1:
        row = input('\nUkuran baris: ')
        col = input('Ukuran kolom: ')
        print('')
        dataAwal = lof.manual_list(row, col)
        dataAwal = lof.np.reshape(dataAwal, (row, col))
        calcLOF()
    elif pil == 2:
        row = input('\nUkuran baris: ')
        col = input('Ukuran kolom: ')
        print('')
        dataAwal = lof.populate_list(row, col, 200)
        lof.np.set_printoptions(precision=2, suppress=True)
        calcLOF()
    elif pil == 3:
        dataAwal = lof.template_list()
        calcLOF()
    elif pil == 4:
        print('\n\nAnda keluar dari program\n\n')
        break
    else:
        print('\n\nInput tidak sesuai ketentuan\n\n')
