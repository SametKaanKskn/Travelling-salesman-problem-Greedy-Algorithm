import numpy
from tsp_solver.greedy import solve_tsp as base_solve_tsp

# Python 2 ve Python 3 arasında uyumluluk sağlamak için xrange kontrolü yapıldı
if "xrange" not in globals():
    xrange = range  # Python 3'te, xrange yerine range kullanılır

def pairs_by_dist_np(N, distances):
    """
    Mesafelere göre şehir çiftlerini sıralayan ve Numpy kullanarak optimize edilmiş bir fonksiyon.
    
    Parametreler:
    - N (int): Şehir sayısı.
    - distances (array): İki şehir arasındaki mesafeleri içeren N x N mesafe matrisi.
    
    Dönüş:
    - array: Mesafeye göre sıralanmış şehir çiftlerinin indeksleri (i, j).
    """
    # Şehir çiftlerini ve mesafelerini tutacak numpy dizisini oluşturma
    pairs = numpy.zeros((N*(N-1)//2,), dtype=('f4, i2, i2'))

    idx = 0
    for i in xrange(N):
        for j in xrange(i):
            # İlgili şehir çifti ve mesafeyi diziye ekleme
            pairs[idx] = (distances[i][j], i, j)
            idx += 1
    # Mesafeye göre dizi sıralama
    pairs.sort(order=["f0"])
    # Sıralanmış şehir çiftlerinin indekslerini döndürme
    return pairs[["f1", "f2"]]

def solve_tsp(distances, optim_steps=3, pairs_by_dist=pairs_by_dist_np, endpoints=None):
    """
    Verilen bir mesafe matrisi kullanarak Gezgin Satıcı Problemi (TSP) için bir çözüm bulur.
    Numpy kullanarak daha az bellek tüketir ve daha hızlı çalışır.
    
    Parametreler:
    - distances (array): İki şehir arasındaki mesafeleri içeren N x N mesafe matrisi.
    - optim_steps (int): Çözümün optimizasyonu için yapılacak ekstra adım sayısı.
    - pairs_by_dist (function): Şehir çiftlerini mesafeye göre sıralayan fonksiyon.
    - endpoints (tuple): Yolculuğun başlangıç ve bitiş noktaları (opsiyonel).
    
    Dönüş:
    - list: Ziyaret edilecek şehirlerin sıralı indeks listesi.
    """
    # Base çözüm fonksiyonunu çağırarak TSP çözümünü al
    return base_solve_tsp(distances, optim_steps=optim_steps, pairs_by_dist=pairs_by_dist, endpoints=endpoints)
