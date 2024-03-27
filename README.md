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

Çözüm Yolu (path): 14, 16, 44, 15, 38, 50, 39, 31, 22, 1, 25, 20, 37, 21, 43, 29, 42, 11, 18, 40, 19, 7, 13, 4, 8, 46, 3, 27, 41, 24, 34, 23, 35, 30, 12, 36, 6, 26, 47, 45, 9, 10, 28, 2, 5, 33, 0, 32, 48, 49, 17

![tsp_51](https://github.com/SametKaanKskn/Travelling-salesman-problem-Greedy-Algorithm/assets/111184050/7acb607f-6f6b-40c5-aca5-8be1fa8b42fe)


100 Şehir (Düğüm) Veri Seti Sonucu:

Cost (Maliyet): 24003.04990232166

Çözüm Yolu (path) : 0, 97, 80, 12, 62, 27, 66, 90, 93, 68, 41, 45, 85, 94, 67, 73, 26, 65, 51, 91, 63, 13, 31, 82, 64, 55, 53, 32, 15, 23, 9, 36, 38, 92, 99, 4, 72, 71, 37, 96, 30, 28, 14, 86, 21, 3, 1, 7, 33, 56, 83, 6, 43, 84, 10, 76, 20, 61, 47, 81, 8, 25, 78, 57, 48, 46, 40, 77, 52, 60, 42, 34, 22, 2, 19, 88, 89, 16, 54, 11, 5, 49, 75, 18, 24, 79, 29, 69, 87, 35, 98, 17, 59, 70, 44, 50, 39, 95, 74, 58


![tsp_100](https://github.com/SametKaanKskn/Travelling-salesman-problem-Greedy-Algorithm/assets/111184050/2ab80b44-7aef-492e-be07-b848723c3176)

783 Şehir(Düğüm) Veri Seti Sonucu:

Cost (Maliyet):9861.527268825988

Çözüm yolu (path) : 314, 313, 317, 296, 286, 279, 287, 293, 288, 298, 283, 268, 263, 253, 256, 260, 267, 273, 280, 291, 305, 312, 333, 342, 346, 355, 386, 377, 380, 369, 368, 373, 353, 343, 326, 344, 340, 351, 347, 330, 306, 300, 299, 289, 265, 257, 269, 292, 277, 274, 259, 254, 261, 262, 270, 258, 250, 240, 237, 223, 212, 189, 181, 167, 180, 179, 183, 151, 135, 130, 132, 122, 128, 161, 145, 152, 140, 153, 157, 154, 146, 158, 191, 210, 216, 203, 182, 175, 190, 200, 214, 201, 224, 245, 255, 278, 284, 282, 276, 275, 272, 281, 301, 309, 308, 297, 318, 294, 303, 307, 315, 321, 341, 345, 327, 328, 329, 334, 348, 356, 363, 362, 365, 367, 366, 384, 376, 387, 385, 381, 382, 374, 370, 335, 357, 358, 371, 378, 388, 389, 354, 339, 338, 331, 349, 324, 316, 310, 332, 350, 360, 364, 372, 359, 390, 391, 383, 379, 375, 361, 352, 337, 320, 319, 322, 325, 336, 323, 304, 311, 302, 295, 290, 285, 266, 264, 271, 251, 243, 233, 231, 228, 193, 163, 124, 131, 112, 111, 118, 136, 133, 117, 110, 106, 86, 76, 62, 55, 48, 35, 59, 79, 89, 87, 98, 70, 69, 52, 50, 36, 29, 21, 14, 12, 2, 7, 4, 6, 20, 11, 23, 22, 8, 10, 24, 40, 54, 67, 58, 73, 83, 96, 101, 97, 88, 82, 95, 105, 104, 102, 84, 72, 78, 77, 75, 65, 64, 57, 68, 81, 85, 91, 99, 108, 109, 115, 113, 129, 150, 166, 173, 178, 185, 213, 197, 218, 226, 247, 239, 241, 222, 209, 208, 192, 199, 195, 211, 217, 238, 244, 230, 229, 215, 225, 236, 252, 249, 227, 221, 242, 235, 220, 205, 206, 198, 207, 196, 186, 174, 171, 172, 164, 149, 144, 143, 137, 123, 103, 121, 127, 126, 160, 165, 155, 148, 139, 147, 169, 177, 187, 170, 162, 138, 142, 159, 194, 202, 219, 234, 248, 246, 232, 204, 188, 176, 184, 168, 156, 141, 134, 119, 107, 90, 80, 44, 37, 3, 775, 754, 743, 750, 747, 734, 719, 735, 749, 757, 730, 737, 744, 756, 762, 767, 13, 0, 780, 5, 15, 9, 773, 778, 781, 31, 53, 60, 66, 61, 74, 92, 93, 114, 125, 120, 116, 100, 94, 71, 63, 46, 51, 33, 30, 41, 34, 38, 32, 28, 47, 39, 43, 49, 56, 45, 42, 26, 19, 25, 27, 18, 17, 16, 1, 768, 761, 763, 782, 766, 771, 777, 772, 755, 774, 764, 779, 776, 759, 728, 729, 731, 739, 742, 745, 751, 727, 717, 709, 703, 692, 678, 673, 674, 679, 699, 701, 711, 722, 695, 688, 687, 656, 655, 638, 629, 625, 645, 671, 676, 706, 705, 720, 732, 746, 748, 758, 765, 760, 770, 769, 753, 752, 740, 733, 725, 715, 689, 700, 675, 670, 652, 636, 643, 632, 663, 662, 654, 651, 635, 620, 619, 611, 594, 582, 580, 588, 574, 579, 592, 604, 612, 617, 628, 648, 666, 653, 642, 644, 641, 660, 672, 681, 684, 682, 690, 677, 697, 707, 698, 691, 683, 694, 702, 686, 721, 713, 712, 724, 736, 738, 741, 723, 716, 714, 710, 718, 726, 708, 685, 669, 664, 665, 639, 640, 613, 618, 622, 621, 646, 667, 668, 680, 693, 704, 696, 661, 657, 637, 630, 627, 633, 626, 606, 607, 596, 577, 571, 563, 576, 537, 516, 508, 501, 506, 514, 530, 538, 546, 551, 566, 586, 587, 575, 553, 547, 544, 518, 527, 542, 511, 502, 498, 485, 474, 467, 489, 486, 480, 465, 468, 439, 455, 462, 476, 490, 493, 496, 499, 503, 507, 524, 528, 534, 543, 552, 578, 595, 593, 599, 615, 634, 647, 658, 659, 649, 650, 631, 623, 624, 616, 608, 597, 591, 589, 570, 567, 581, 603, 602, 600, 610, 601, 573, 564, 556, 555, 548, 560, 554, 531, 519, 529, 509, 517, 512, 515, 535, 541, 550, 545, 521, 520, 494, 483, 463, 473, 477, 459, 452, 450, 441, 453, 445, 433, 442, 460, 484, 481, 469, 482, 487, 495, 504, 510, 536, 522, 523, 532, 558, 549, 557, 565, 569, 583, 598, 614, 605, 609, 590, 584, 562, 526, 525, 540, 568, 572, 585, 561, 559, 539, 533, 513, 505, 500, 497, 492, 470, 475, 478, 466, 457, 464, 435, 446, 451, 434, 429, 431, 397, 404, 402, 395, 425, 419, 415, 418, 417, 412, 407, 423, 405, 413, 426, 422, 411, 427, 421, 410, 399, 396, 394, 401, 400, 403, 424, 420, 430, 454, 449, 444, 438, 456, 472, 458, 461, 471, 491, 488, 479, 447, 440, 443, 448, 436, 432, 437, 409, 398, 393, 414, 408, 428, 416, 406, 392


![tsp783_](https://github.com/SametKaanKskn/Travelling-salesman-problem-Greedy-Algorithm/assets/111184050/5e957616-7fca-4735-82d9-31d0d13a17a9)



4461 Şehir(Düğüm) Veri Seti Sonucu:

Cost (Maliyet):195933.11694264726


![Ekran görüntüsü 2024-03-26 231440](https://github.com/SametKaanKskn/Travelling-salesman-problem-Greedy-Algorithm/assets/111184050/92cf426a-1d4b-4ac4-ae73-bf764c0e4145)



Sonuç

Gezgin Satıcı Problemi, verilen şehirler listesi ve her bir şehir çifti arasındaki mesafelerle, bir satıcının tüm şehirleri yalnızca bir kez ziyaret edip başladığı şehre en kısa yoldan geri dönmesini sağlamayı amaçlayan bir optimizasyon problemidir. Bu problem, lojistik ve dağıtım, DNA sıralama ve biyoinformatik, devre tasarımı ve mikroçipler, seyahat planlaması ve turizm gibi çeşitli alanlarda zaman, maliyet ve kaynakları optimize etmek için kullanılmaktadır.


![Ekran görüntüsü 2024-03-26 235322](https://github.com/SametKaanKskn/Travelling-salesman-problem-Greedy-Algorithm/assets/111184050/54d4204a-e0f9-458b-9043-37cbff925364)


Grafikte, problem boyutunun artmasıyla birlikte çalışma zamanının artmıştır. Özellikle, şehir sayısının 10.000'in üzerine çıktığı noktada çalışma zamanında belirgin bir artış vardır. Bu, algoritmanın karmaşıklığının, problem boyutunun büyüklüğüyle üstel ya da polinomsal bir şekilde arttığını göstermektedir, bu da algoritmanın büyük veri setleriyle karşılaştığında ölçeklenebilirlik sınırlarına ulaşabileceğini göstermektedir.
Daha düşük şehir sayılarında (51 ve 100 gibi) çalışma zamanları oldukça düşük (sırasıyla 0.01 ve 0.02 saniye), bu da algoritmanın küçük boyutlu problemlerde çok hızlı çalıştığını göstermektedir




