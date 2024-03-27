Gezgin Satıcı Problemi Çözümü (TSP Solver)
Giriş
Bu proje, lisans sürecinde ders olarak aldığım  "Algoritma Analizi ve Tasarımı" derside Gezgin Satıcı Problemi (TSP) için en verimli ve en performanslı algoritmayı bulma, implemente etme ve test etme amacını taşımaktadır. TSP, başlangıç ve bitiş şehirlerinin aynı olduğu, her şehrin yalnızca bir kez ziyaret edildiği minimum mesafeli turu bulma problemidir. Projede, hocalarımız tarafından sağlanan 5 farklı nokta veri seti kullanılmıştır. Bu veri setleri, düğümlerin sınırsız bir uzayda X ve Y koordinatlarına göre konumlandığı 51, 100, 783, 4461 ve 85900 düğümlü şehirler içermektedir.

Geliştirme ve Çalıştırma Ortamları
Algoritmayı geliştirmek için Visual Studio Code IDE ve Python programlama dili kullanılmıştır. TSP için birçok çözüm algoritması mevcut olup, 85,900 şehirlik örnek 2006 yılında Cook ve diğerleri tarafından bir mikroçip düzeni problemi olarak çözülmüştür ve bu, TSPLIB örnekleri arasında çözülen en büyük problem olma özelliğini taşımaktadır. Bu projede, Greedy algoritması tercih edilmiş ve  5 farklı veri setinde test edilmiştir.

Algoritma Akışı
Greedy Algoritması Pseudo Code
![image](https://github.com/SametKaanKskn/Travelling-salesman-problem-Greedy-Algorithm/assets/111184050/73275700-2fe0-4781-a0c4-27d0083706bb)
Algoritma, belirlenen bir başlangıç noktasından başlayarak, 'C' kümesindeki tüm elemanları içeren bir 'V' kümesi oluşturmayı amaçlar. Her adımda, mevcut konumdan 'C' kümesindeki elemanlara olan mesafeye göre en yakın eleman seçilir ve 'V'ye eklenir. Her seçim sonrası, mevcut konum en son eklenen elemana güncellenir. Bu işlem, 'V' kümesi 'C'nin boyutuna ulaşana kadar devam eder.

51 Şehir (Düğüm) Veri Seti Sonucu:
Cost (Maliyet): 474.64391534902643
Çözüm Yolu: 14, 16, 44, 15, 38, 50, 39, 31, 22, 1, 25, 20, 37, 21, 43, 29, 42, 11, 18, 40, 19, 7, 13, 4, 8, 46, 3, 27, 41, 24, 34, 23, 35, 30, 12, 36, 6, 26, 47, 45, 9, 10, 28, 2, 5, 33, 0, 32, 48, 49, 17
![tsp_51](https://github.com/SametKaanKskn/Travelling-salesman-problem-Greedy-Algorithm/assets/111184050/7acb607f-6f6b-40c5-aca5-8be1fa8b42fe)


Sonuç
Gezgin Satıcı Problemi, verilen şehirler listesi ve her bir şehir çifti arasındaki mesafelerle, bir satıcının tüm şehirleri yalnızca bir kez ziyaret edip başladığı şehre en kısa yoldan geri dönmesini sağlamayı amaçlayan bir optimizasyon problemidir. Bu problem, lojistik ve dağıtım, DNA sıralama ve biyoinformatik, devre tasarımı ve mikroçipler, seyahat planlaması ve turizm gibi çeşitli alanlarda zaman, maliyet ve kaynakları optimize etmek için kullanılmaktadır.
