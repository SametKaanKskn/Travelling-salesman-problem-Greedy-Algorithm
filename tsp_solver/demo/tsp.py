from __future__ import print_function
import numpy as np
import time  
from tsp_solver.greedy_numpy import solve_tsp

def read_dataset(file_path):
    # Verilen dosya yolundan dataseti okur ve koordinatlar numpy dizisi olarak döndürülür.
    with open(file_path, 'r') as f:
        lines = f.readlines()
    # İlk satırı atlandı çünkü ilk satırda düğüm (şehir)  sayısı ve koordinatlar belirtildi  
    coordinates = np.array([list(map(int, line.strip().split())) for line in lines[1:]])
    return coordinates

def make_dist_matrix(x, y):
    # Belirtilen koordinat vektörleri için mesafe matrisi hesaplandı
    N = len(x)
    xx = np.vstack((x,)*N)
    yy = np.vstack((y,)*N)
    return np.sqrt((xx - xx.T)**2 + (yy - yy.T)**2)

def main():
    
    file_path = file_path = r'your path'


    # Dataseti oku
    coordinates = read_dataset(file_path)

    # x ve y koordinatları ayrıldı
    x = coordinates[:, 0]
    y = coordinates[:, 1]

    distances = make_dist_matrix(x, y)

    # Ne kadar sürede çalıştığını gözlemlemek için çözüm öncesi zaman kaydedildi
    start_time = time.time()

    
    path = solve_tsp(distances)

    # Çözüm sonrası zamanı kaydedildi ve süre hesaplandı
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Çözüm süresi: {:.2f} saniye".format(elapsed_time))

    # Solution path  ve cost
    print("Çözüm Yolu:", path)
    total_distance = sum(distances[path[i], path[(i + 1) % len(path)]] for i in range(len(path)))
    print("Toplam Mesafe:", total_distance)

    
    try:
        import matplotlib.pyplot as plt
        plt.plot(coordinates[path, 0], coordinates[path, 1], 'o-')
        plt.show()
    except ImportError as err:
        print("Matplotlib modülü yüklü değil, görselleştirme yapılamıyor.", err)

if __name__ == '__main__':
    main()
