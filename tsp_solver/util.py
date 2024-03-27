
if "xrange" in globals():
    # Eğer Python 2 kullanılıyorsa, 'range' yerine 'xrange' kullan
    range = xrange
    # Python 2'deki 'next' fonksiyonunu tanımla
    def next(x): return x.next()

def path_cost(distance_matrix, path):
    """
    Verilen bir yolun toplam uzunluğunu, sağlanan mesafe matrisi kullanarak hesaplar.
    
    Parametreler:
    - distance_matrix: NxN boyutunda 2 boyutlu dizi (numpy veya liste içeren liste),
                       düğümler arası mesafeyi içerir, sadece sol alt üçgen kısmı kullanılır.
    - path: Düğümlerin grafiğindeki yol, değerler düğüm indeksleridir, 0'dan N-1'e kadar.

    Dönüşler:
    - int: Yolun uzunluğu. Eğer yol boşsa veya sadece 1 düğüm içeriyorsa, 0 döner.
    """
    
    # Yolu bir yineleyici (iterator) olarak al
    ipath = iter(path)
    try:
        # İlk düğümü al, eğer yol boşsa StopIteration hatası al ve 0 dön
        j = next(ipath)
    except StopIteration:
        # Boş yol durumu
        return 0
    
    # Toplam mesafeyi hesaplama
    dist = 0
    for i in ipath:
        # Eğer i'nin indeksi j'den büyükse veya eşitse, mesafe matrisindeki uygun değeri ekleyin
        # Bu, mesafe matrisinin sadece bir yarısının kullanıldığını varsayar
        if i >= j:
            dist += distance_matrix[i][j]
        else:
            dist += distance_matrix[j][i]
        j = i  # Geçerli düğümü sonraki adım için güncelle
    return dist
