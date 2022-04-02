import streamlit as st
import tensorflow as tf
import numpy as np
import requests
from PIL import Image
from io import BytesIO

descriptions = {
    "Bacterial Spot": {
        "Gejala": "Bakteri ini menyerang daun, batang, dan buah tomat. Gejala pertamanya berupa luka kecil berwarna kuning kehijauan pada daun muda, yang biasanya tampak cacat dan menggulung. Pada daun-daun yang lebih tua, luka dibatasi oleh vena, menjadi kaku seiring waktu. Pada awalnya luka berwarna hijau tua, nampak berminyak, dan dikelilingi oleh lingkaran cahaya kuning. Luka-luka ini biasanya lebih banyak pada tepian atau ujung daun. Dalam kondisi yang nyaman, luka membesar dengan cepat hingga merah kecoklatan. Pada akhirnya, bercak-bercak terlihat seperti lubang bekas tembakan karena bagian tengahnya mengering dan hancur. Bercak-bercak buah (hingga 0,5 cm) diawali dengan warna hijau pucat, area berair dan dikelilingi lingkaran cahaya kuning yang pada akhirnya berwujud kasar, menjadi kecoklatan dan berkeropeng",
        "Penyebab": "Bercak bakteri disebabkan oleh beberapa spesies bakteri dari genus Xanthomonas. Ini terjadi di seluruh dunia dan merupakan salah satu penyakit paling merusak pada tomat yang tumbuh di lingkungan yang hangat dan lembab. Patogen dapat bertahan hidup di dalam atau pada biji, pada puing-puing tanaman dan pada gulma tertentu. Bakteri ini memiliki masa bertahan hidup yang sangat terbatas dari hari ke minggu di tanah. Ketika kondisinya nyaman, bakteri menyebar melalui percikan air hujan atau irigasi pancur ke tanaman yang sehat. Memasuki jaringan tanaman melalui pori-pori dan luka pada daun. Kisaran suhu optimal untuk penyebarannya adalah 25 hingga 30 derajat celsius. Setelah tanaman terinfeksi, penyakit ini sangat sulit dikendalikan dan dapat menyebabkan kerugian total pada hasil panen.",
        "Pengendalian hayati": "Bakteri sangat sulit dan mahal untuk diobati. Jika penyakit terjadi pada awal musim, pertimbangkan untuk menghancurkan saja seluruh tanaman. Bakterisida yang mengandung tembaga memberikan lapisan pelindung pada daun dan buah. Ada virus bakteri (bakteriofag) yang secara spesifik bisa membunuh bakteri. Merendam benih selama satu menit dalam 1,3% natrium hipoklorit atau dalam air panas (50 derajat celsius) selama 25 menit dapat mengurangi timbulnya penyakit.",
        "Pengendalian kimiawi": "Selalu pertimbangkan pendekatan terpadu dengan tindakan pencegahan bersama dengan perlakuan hayati jika tersedia. Bakterisida yang mengandung tembaga dapat digunakan sebagai pelindung dan memberikan kontrol terhadap sebagian penyakit. Pemberiannya dilakukan pada tanda-tanda awal penyakit dan selanjutnya pada selang 10 hingga 14 hari ketika kondisi hangat dan lembab. Oleh karena perkembangan resistensi terhadap tembaga sering terjadi, kombinasi bakterisida yang mengandung tembaga dengan mancozeb juga direkomendasikan",
        "Pencegahan": [
            "Jika memungkinkan, tanam benih yang bebas penyakit dari pemasok yang bersertifikat.",
            "Gunakan varietas yang tahan penyakit jika tersedia di lokasi setempat.",
            "Periksa lahan secara teratur, terutama saat cuaca mendung.",
            "Buang dan bakar setiap bibit atau bagian tanaman yang mengalami bercak daun.",
            "Bersihkan gulma di dalam dan di sekitar lahan",
            "Pasang mulsa tanah untuk menghindari kontaminasi tanah ke tanaman.",
            "Bersihkan peralatan-peralatan kerja.",
            "Hindari irigasi pancur dan bekerja di lahan saat daun-daun basah.",
            "Bajak dalam-dalam sisa-sisa tanaman setelah panen.",
            "Sebagai alternatif, singkirkan puing-puing tanaman dan biarkan tanah menganggur selama beberapa minggu atau bulan (lakukan solarisasi).",
            "Rencanakan rotasi tanaman 2-3 tahun dengan tanaman yang tidak rentan.",
        ],
    },
    "Early Blight": {
        "Gejala": "Gejala penyakit bercak kering terjadi pada daun, batang, dan buah yang lebih tua. Bercak abu-abu hingga coklat muncul di daun dan perlahan-lahan tumbuh secara konsentris di sekitar bagian tengah yang bersih - ciri khasnya berbentuk mata banteng. Luka ini dikelilingi oleh lingkaran cahaya kuning cerah. Ketika penyakit ini berkembang, seluruh daun dapat mengalami klorosis dan gugur, yang mengarah ke perontokan daun yang parah. Saat daun mati dan gugur, buah menjadi lebih rentan terhadap luka bakar matahari. Jenis bercak yang sama dengan bagian tengah yang bersih muncul pada batang dan buah. Buah-buah membusuk dan kadang-kadang berjatuhan.",
        "Penyebab": "Gejala-gejalanya disebabkan oleh Alternaria solani, jamur yang melewati musim dingin pada puing-puing tanaman yang terinfeksi di tanah atau pada inang alternatif. Bibit atau benih yang dibeli mungkin juga sudah terkontaminasi. Daun bagian bawah sering terinfeksi ketika kontak dengan tanah yang terkontaminasi. Suhu hangat (24-29 derajat celsius) dan kelembaban tinggi (90%) mendukung pengembangan penyakit ini. Periode basah yang panjang (atau cuaca basah/kering bergantian) meningkatkan produksi spora, yang dapat menyebar melalui angin, percikan air hujan atau irigasi pancur. Umbi yang dipanen masih hijau atau dalam kondisi basah sangat rentan terhadap infeksi. Jamur ini sering menyerang setelah periode curah hujan tinggi dan sangat merusak  di daerah tropis dan subtropis.",
        "Pengendalian hayati": "Para petani kecil dapat menggunakan batu kapur alga, campuran susu bebas lemak dan air (1:1) atau tepung batu untuk mengobati tanaman yang terinfeksi. larutan 3 sendok teh soda bikarbonat + emulsi ikan dalam 4 liter air juga membantu. Pemberian produk berbahan dasar Bacillus subtilis atau fungisida berbahan dasar tembaga yang terdaftar sebagai bahan organik juga bisa berfungsi baik.",
        "Pengendalian kimiawi": "Jika memungkinkan, selalu pertimbangkan pendekatan terpadu dengan langkah-langkah pencegahan bersamaan dengan perlakuan hayati. Ada banyak fungisida di pasaran untuk mengendalikan penyakit bercak kering. Fungisida berbahan dasar atau kombinasi azoxystrobin, pyraclostrobin, difenoconazole, boscalid, chlorothalonil, fenamidone, maneb, mancozeb, trifloxystrobin dan ziram dapat digunakan. Melakukan rotasi senyawa kimia yang berbeda juga dianjurkan. Lakukan perawatan tepat waktu, dengan mempertimbangkan kondisi cuaca. Perhatikan betul-betul selang waktu sebelum panen di mana Anda dapat memanen dengan aman setelah pemberian produk-produk fungisida ini.",
        "Pencegahan": [
            "Gunakan benih atau transplantasi bebas patogen yang bersertifikat.",
            "Cari varietas yang tahan terhadap penyakit.",
            "Tanam atau transplantasi pada bedengan untuk memperbaiki drainase.",
            "Arahkan susunan baris tanaman ke arah angin utama dan hindari area yang teduh.",
            "Ciptakan ruang tanam yang memungkinkan kanopi mengering dengan cepat setalah hujan atau irigasi.",
            "Letakkan mulsa di tanah agar tanaman tidak menyentuh tanah.",
            "Pantau tanda-tanda penyakit, khususnya selama cuaca basah.",
            "Buang daun-daun bagian bawah yang terlalu dekat dengan tanah.",
            "Buang daun-daun yang menunjukkan gejala penyakit dan musnahkan.",
            "Jaga tanaman agar kuat dan tegak dengan nutrisi yang memadai.",
            "Gunakan cagak untuk menjaga tanaman tetap tegak.",
            "Gunakan sistem irigasi tetes untuk meminimalkan kebasahan daun.",
            "Sirami tanaman pada pagi hari agar tanaman bisa kering pada siang hari.",
            "Kendalikan gulma yang rentan di dalam dan di sekitar lahan.",
            "Hindari bekerja di lahan saat tanaman basah.",
            "Setelah panen, bersihkan dan bakar sisa-sisa tanaman (jangan dijadikan kompos).",
            "Atau, bajak sisa-sisa tanaman jauh ke dalam tanah (lebih dari 45 cm).",
            "Rencanakan rotasi panen 2 atau 3 tahun dengan tanaman yang tidak rentan.",
        ],
    },
    "Late Blight": {
        "Gejala": "Bintik-bintik hijau kecoklatan muncul di tepi daun dan bagian atas daun. Selanjutnya, area besar pada daun berubah menjadi coklat seluruhnya. Selama cuacah basah, luka di sisi bawah daun mungkin ditutupi dengan pertumbuhan lapisan jamur abu-abu, sehingga lebih mudah untuk membedakan jaringan daun sehat dengan jaringan daun mati. Saat penyakit berkembang, daun menjadi coklat, keriting dan kering. Dalam beberapa kasus, bintik-bintik coklat yang mencolok dan lapisan putih juga muncul pada batang, cabang dan tangkai daun. Warna hijau keabu-abuan hingga coklat kotor dan keriput muncul pada buah. Pada titik-titik ini, daging buah mengeras.",
        "Penyebab": "Risiko infeksi paling tinggi terjadi pada pertengahan musim panas. Jamur memasuki tanaman melalui luka dan sobekan di kulit. Suhu dan kelembaban adalah faktor lingkungan terpenting yang mempengaruhi perkembangan penyakit. Jamur busuk daun tumbuh paling baik pada kelembaban relatif tinggi (sekitar 90%) dan dalam kisaran suhu 18 hingga 26 derajat celsius. Cuaca musim panas yang hangat dan kering dapat menghentikan penyebaran penyakit ini.",
        "Pengendalian hayati": "Tidak ada pengendalian hayati berkhasiat yang diketahui bisa mengatasipenyakit busuk daun. Untuk menghindari penyebaran, segera singkirkan dan mushankan tanaman di sekitar lokasi yang terinfeksi dan jangan membuat kompos dari bahan tanaman yang terinfeksi.",
        "Pengendalian kimiawi": "Selalu pertimbangkan pendekatan terintegrasi dengan tindakan pencegahan bersama dengan perlakuan hayati jika tersedia. Gunakan semprotan fungisida berbahan dasar mandipropamid, klorotalonil, fluazinam, atau mankozeb untuk melawan penyakit busuk daun. Fungisida umumnya diperlukan hanya jika penyakit muncul dalam periode setahun ketika kemungkinan terjadi hujan atau penerapan irigasi pancur.",
        "Pencegahan": [
            "Pilih benih yang sehat dari pengecer terpercaya.",
            "Tanam varietas yang lebih kebal terhadap penyakit",
            "Tomat dan kentang jangan dibudidayakan bersama-sama.",
            "Usahakan tanaman tetap kering dengan drainase dan ventilasi kultur yang baik",
            "Pemasangan naungan sederhana transparan dengan bahan terpal dan tiang kayu mungkin bisa membantu.",
            "Pupuk yang mengandung silikat dapat meningkatkan daya tahan terhadap jamur, terutama pada tahap semai.",
            "Hindari irigasi pada sore hari dan irigasi siram di permukaan tanah.",
        ],
    },
    "Leaf Mold": {
        "Gejala": "Pada umunya gejala terjadi di kedua sisi daun dan kadang-kadang pada buah. Daun yang lebih tuan terinfeksi lebih dahulu dan selanjutnya penyakit perlahan menyebar ke arah daun muda. Pada permukaan sisi atas daun, muncul bercak-bercak kecil yang menyebar, berwarna hijau pucat atau kekuningan dengan tepian yang bisa meluas. Di sisi bagian bawah, bercak hijau zaitun hingga abu-abu dan potongan beludru berkembang di bawah bercak-bercak daun. Bercak ini terdiri dari struktur penghasil spora dan massa spora (konidia). Seiring waktu, ketika bercak-bercak membesar, warna daun yang terinfeksi berubah dari kekuningan (klorosis) menjadi coklat (nekrosis) dan daun mulai menggulung dan mengering. Daunnya akan rontok seblum waktunya, menyebabkan pengguguran daun yang parah. Kadang-kadang, patogen ini menyebabkan penyakit pada bunga atau buah dengan berbagai gejala. Bunga bisa berubah menjadi hitam dan akan mati sebelum buah terbentuk. Buah hijau dan matang akan mengembangkan area hitam halus yang tidak beraturan di ujung batang. Seiring perkembangan penyakit, area yang terinfeksi menjadi cekung, kering, dan kasar.",
        "Penyebab": "Gejala-gejalanya disebabkan oleh jamur Mycovellosiella fulva, yang sporanya dapat bertahan hidup tanpa inang selama 6 bulan hingga satu tahun pada suhu kamar (tidak harus). Kelembaban udara dan kelembaban daun yang berkepanjangan di atas 85% mendukung perkecambian spora. Suhu antara 4 hingga 34 derajat celsius mendukung perkecambahan spora, dengan suhu optimalnya pada 24-26 derajat celsius. Kondisi kering dan ketiadaan air pada daun bisa merusak daya kecambah. Gejala biasanya mulai muncul 10 hari setelah inokulasi dengan perkembangan flek di kedua sisi daun. Di bagian bawah, sejumlah besar struktur penghasil spora terbentuk dan spora ini mudah menyebar dari tanaman ke tanaman dengan bantuan percikan air dan angin, peralatan dan pakaian pekerja, dan serangga. Patogen biasanya menginfeksi daun dengan menembus stomata pada tingkat kelembaban tinggi.",
        "Pengendalian hayati": "Disarankan melakukan perawatan benih dengan air panas(25 menit pada 122 derajat farhenheit atau 50 derajat celsius) untuk menghindari patogen pada biji. Jamur Acremonium strictrum, Dicyma pulvinata, Trichoderma harzianum atau T. viride dan Trichothecium roseum bersifat antagonis terhadap M. fulva dan dapat digunakan untuk mengurangi penyebarannya. dalam percobaan di dalam rumah kaca, pertumbuhan M. fulva pada tomat dihambat oleh A. strictum, Trichoderma viride strain3 dan T. roseum masing-masing sebesar 53, 66 dan 84%. Dalam kadar yang ringan, sari apel, semprotan bawang putih atau susu dan campuran cuka dapat digunakan untuk mengobati jamur.",
        "Pengendalian kimiawi": "Selalu pertimbangkan pendekatan terpadu dengan tindakan pencegahan bersama dengan perlakuan hayati jika tersedia. Tindakan pencegahan harus dilakukan sebelum infeksi ketika kondisi lingkungan optimal untuk pengembangan penyakit. Senyawa yang direkomendasikan untuk penggunaan di lahan adalah formulasi chlorothalonil, maneb, mancozeb dan tembaga. Untuk di rumah kaca, direkomendasikan menggunakan difenoconazole, mandipropamid, cymoxanil, famoxadone dan cyprodinil.",
        "Pencegahan": [
            "Gunakan benih bersertifikat, bebas penyakit, dan varietas yang tahan penyakit jika tersedia di daerah Anda.",
            "Lakukan penanaman lebih awal untuk mengurangi keparahan penyakit.",
            "Sesuaikan jarak tanam untuk meningkatkan sirkulasi udara dan mengurangi kelembaban di kanopi",
            "Pantau kehadiran penyakit dan tanaman perusak yang terinfeksi segera setelah terdeteksi.",
            "Hindari pemupukan nitrogen yang berlebihan.",
            "Sediakan sirkulasi udara di dalam rumah kaca.",
            "Jaga kelembaban relatifnya agar di bawah 85% dan suhu malam hari lebih tinggi daripada suhu di luar (cocok untuk rumah kaca).",
            "Gunakan irigasi tetes dan hindari penyiraman daun.",
            "Gunakan tonggak, tali, atau pangkas tanaman untuk menjaganya tetap tegak dan meningkatkan aliran udara di dalam dan di sekitarnya.",
            "Buang dan musnahkan (bakar) seluruh puing tanaman setelah panen.",
            "Bersihkan rumah kaca di titik-titik antar tanaman dan pertahankan standar kebersihan yang tinggi pada para pekerja dan peralatan kerja.",
        ],
    },
    "Septoria Leaf Spot": {
        "Gejala": "Gejala menyebar ke atas dari pertumbuhan di daun tertua ke daun termuda. Bintik-bintik kecil kelabu berair dengan tepian berwarna coklat tua muncul di bagian bawah daun yang lebih tua. Pada tahap selanjutnya dari penyakit ini, bintik-bintik membesar dan menyatu, dan titik-titik hitam muncul di pusat-pusatnya. Pola yang sama juga dapat diamati pada batang dan bunga, tetapi jarang pada buah. Daun yang terinfeksi berat akan menjadi agak kuning, layu, dan rontok. Perontokan daun-daun menyebabkan buah terpapar dan terbakar matahari.",
        "Penyebab": "Bercak daun Septoria terjadi di seluruh dunia disebabkan oleh jamur Septoria lycopersici. Jamur hanya menginfeksi tanaman dari famili kentang dan tomat. Kisaran suhu untuk pengembangan jamur bervariasi antara 15 derajat dan 27 derajat celsius, dengan pertumbuhan optimal pada 25 derajat celsius. Spora mungkin disebarkan oleh air dari irigasi curah, percikan air hujan, tangan dan pakaian pemetik, serangga seperti kumbang, dan peralatan budidaya. Jamur ini melewati musim dingin pada gulma solanaceous dan di tanah atau puing-puing tanah selama periode yang singkat.",
        "Pengendalian hayati": "Fungisida berbahan dasar tembaga, seperti campuran Bordeaux, tembaga hidroksida, tembaga sulfat, atau tembaga oksiklorida sulfat dapat membantu mengendalikan patogen. Terapkan pada selang waktu 7 hingga 10 hari sepanjang akhir musim. Patuhi batasan penggunaannya selama masa panen yang tercantum pada label pestisida.",
        "Pengendalian kimiawi": "Selalu pertimbangkan pendekatan terpadu dengan tindakan pencegahan bersama dengan perlakuan hayati jika tersedia. Fungisida yang mengandung maneb, mankozeb, klorothalonil secara efektif dapat mengendalikan bercak daun Septoria. Semprotkan pada selang waktu 7 hingga 10 hari sepanjang musim, terutama selama tahap pembungaan dan pembentukan buah. Patuhi batasan penggunaannya selama masa panen yang tercantum pada pestisida.",
        "Pencegahan": [
            "Dapatkan benih bersertifikat yang bebas penyakit.",
            "Jika tersedia, pilij varietas yang tahan penyakit.",
            "Gunakan mulsa organik atau plastik untuk menghindari penularan dari tanah.",
            "Buang dan musnahkan daun yang terinfeksi.",
            "Tingkatkan sirkulasi udara dan jauhkan tanaman dari tanah dengan tonggak.",
            "Pastikan lahan produksi bebas dari gulma yang rentan.",
            "Jangan menggunakan penyemprot air (sprinkler) atau irigasi curah lainnya.",
            "Bersihkan peralatan kerja Anda setelah bekerja di lahan.",
            "Pendam atau buang dan musnahkan sisa-sisa tanaman jauh di dalam tanah setelah panen.",
            "Rencanakan rotasi tanaman selama beberapa tahun dengan tanaman yang tidak rentan.",
        ],
    },
    "Spider Mites": {
        "Gejala": "Tungau laba-laba yang memamah biak menyebabkan terbentuknya bintik-bintik putih hingga kuning di permukaan atas daun. Telurnya menempel di bagian bawah daun. Tungau laba-laba sendiri berada di situ, bersarang di dalam kepompong yang berupa anyaman. Ketika serangan bertambah hebat, daun nampak berwarna perunggu atau keperakan pada awalnya dan selanjutnya menjadi rapuh, sobek di antara pembuluh daun, dan akhirnya gugur. Tungau memutar jaring-jaringnya sehingga dapat menutupi permukaan tanaman. Pucuk tunas bisa menjadi gundul dan tunas tumbuh menyamping. Dalam kasus kerusakan yang berat, kuantitas dan kualitas buah menurun.",
        "Penyebab": "Kerusakan disebabkan oleh tungau laba-laba dari genus Tetranychus, terutama T. urticae dan T. cinnabarinus. Betina dewasa memiliki panjang 0,6 mm, berwarna hijau pucat dengan dua bercak lebih gelap di tubuhnya yang oval dan rambutnya panjang di belakang. Pada musim dingin, betinanya berwarna kemerahan. Pada musim semi, betina bertelur bulat-bulat dan transparan di bagian bawah daun. Nimfa berwarna hijau pucat dengan tanda lebih gelap di sisi punggungnya. Tungau melindungi diri dalam kepompong di bagian bawah bilah daun. Tungau laba-laba tumbuh subur pada iklim kering dan panas dan akan berkembang biak hingga 7 generasi dalam satu tahun dalam kondisi ini. Ada berbagai macam inang alternatif, termasuk gulma.",
        "Pengendalian hayati": "Dalam kasus serangan yang ringan, cukup bersihkan tungau dan buang daun yang terserang. Siapkan bahan olahan yang terdiri dari biji rapa, selasih, kedelai dan minyak nimba untuk menyemprot daun secara menyeluruh dan mengurangi populasi T. urticae. Coba juga teh bawang putih, bubur jelatang atau larutan sabun insektisida untuk mengendalikan populasinya. Di ladang, manfaatkan pengendali biologis inang tertentu dengan tungau pemangsanya (misalnya Phytoseiulus persimilis) atau perstisida biologis Bacillus thuringiensis. Perawatan berupa penyemprotan kedua perlu dilakukan 2 hingga 3 hari setela perawatan awal.",
        "Pengendalian kimiawi": "Jika memungkinkan, selalu pertimbangkan pendekatan terpadu berupa langkah-langkah pencegahan bersamaan dengan perlakuan hayati. Tungau laba-laba sangat sulit dikendalikan dengan akarisisda karena sebagian besar populasinya mengembangkan kekebalan terhadap bahan-bahan kimia yang berbeda setelah beberapa tahun digunakan. Hati-hati dalam memilih agensia pengendalian kimiawi agar tidak mengganggu populasi pemangsanya. Fungisida berbasis belerang/sulfur yang dapat dilarutkan (3 g/l), spiromesifen (1 ml/l), dicofol (5 ml/l) atau abamektin dapat digunakan sebagai contoh (diencerkan dengan air). Perawatan berupa penyemprotan kedua perlu dilakukan 2 hingga 3 hari setelah perawatan awal.",
        "Pencegahan": [
            "Siapkan varietas tanaman yang tahan.",
            "Pantau lahan Anda secara rutin dan periksa bagian bawah daun.",
            "Cara lain, kibaskan beberapa serangga dari permukaan daun ke atas selembar kertas putih.",
            "Buang daun atau tanaman yang terserang.",
            "Singkirkan jelatang dan gulma-gulma lain dari lahan.",
            "Pasoklah air ke jalur-jalur lintas dan area berdebu lainnya secara rutin untuk menghindari kondisi berdebu pada lahan.",
            "Sirami tanaman Anda secara teratur karena pohon dan tanaman yang stres kurang toleran terhadap kerusakan karena tungau laba-laba.",
            "Kendalikan penggunaan insektisida agar memungkinkan serangga yang menguntungkan bisa berkembang.",
        ],
    },
    "Target Spot": {
        "Gejala": "-",
        "Penyebab": "-",
        "Pengendalian hayati": "-",
        "Pengendalian kimiawi": "-",
        "Pencegahan": [
            "-",
            "-",
            "-",
            "-",
        ],
    },
    "Yellow Leaf Curl Virus": {
        "Gejala": "Ketika menginfeksi tanaman pada tahap pembibitan, Virus Kuning Keriting Daun Tomat (Tomato Yellow Leaf Curl Virus, TYLCV) menyebabkan pengerdilan parah pada daun pucuk muda, menghasilkan pertumbuhan tanaman yang agak lebat. Pada tanaman yang lebih tua, infeksi mengakibatkan percabangan yang berlebihan, daun lebih tebal dan keriput, dan klorosis kekuningan di antara tulang daun (interveinal) terlihat jelas pada bilah daun. Pada penyakit tahap selanjutnya, muncul tekstur kasar dan tepian klorosis kekuningan yang menggulung ke atas dan ke dalam. Jika infeksi terjadi sebelum tahap berbungan, jumlah buah sangat berkurang, meskipun tidak ada gejala yang terlihat di permukaanya.",
        "Penyebab": "Virus Kuning Keriting Daun Tomat bukan berasal dari benih dan tidak ditularkan secara mekanis. Penyakit ini disebarkan oleh lalat putih dari spesies Bemisia tabaci. Lalat putih ini memakan permukaan daun bagian bawah dari sejumlah tanaman dan terpikat oleh tanaman muda yang lembut. Seluruh siklus infeksi dapat terjadi dalam waktu sekitar 24 jam dan didukung oleh cuaca kering dengan suhu tinggi.",
        "Pengendalian hayati": "Mohon maaf, kami tidak mengetahui pengobatan alternatif apa pun terhadap Virus Daun Tomat Kuning Keriting.",
        "Pengendalian kimiawi": "Selalu pertimbangkan pendekatan terpadu berupa tindakan pencegahan bersama dengan perlakuan hayati jika tersedia. Insektisida dari keluarga piretroid yang diterapkan pada tanah basah atau penyemprotas selama tahap pembibitan dapat mengurangi populasi lalat putih. Namun, penggunaanya yang luas dapat mendorong perkembangan resistensi pada populasi kutu kebul.",
        "Pencegahan": [
            "Gunakan varietas yang tahan atau toleran.",
            "Lakukan penanaman lebih awal untuk menghindari populasi puncak kutu kebul.",
            "Terapkan tumpang sari dengan tanaman-tanaman yang tidak rentan seperti labu dan mentimun.",
            "Gunakan jaring untuk menutupi persemaian dan mencegah lalat putih menghinggapi tanaman Anda.",
            "Hindari menanam tanaman inang alternatif yang dekat dengan tanaman anda",
            "Pasang mulsa pada persemaian atau lahan untuk memutus siklus hidup kutu kebul",
            "Gunakan perangkap plastik kuning lengket untuk menangkap serangga secara massal",
            "Pantau lahan, petik tanaman yang sakit dan kuburlah jauh dari lahan.",
            "Musnahkan gulma di dalam dan di sekitar lahan.",
            "Bajak atau bakar seluruh sisa tanaman setelah panen.",
            "Lakukan rotasi dengan tanaman yang tidak rentan.",
        ],
    },
    "Mosaic Virus": {
        "Gejala": "Semua bagian tanaman dapat terpengaruh selama tahap pertumbuhan apa pun. Gejala-gejalanya tergantung pada kondisi lingkungan (cahaya, durasi waktu siang hari, suhu). Daun yang terinfeksi menunjukan bercak hijau dan kuning atau pola mosaik. Daun muda sedikit mengalami perubahan bentuk (terdistorsi). Daun yang lebih tua menunjukan area hijau tua. Dalam beberapa kasus, garis nekrotik (sel mati) yang gelap muncul di batang dan tangkai daun. Pertumbuhan tanaman terhambat ke berbagai tingkatan dan pembentukan buah bisa sangat berkurang. Buah yang matang secara tidak merata membentuk bintik-bintik coklat di permukaanya, dan terdapat noda kecoklatan di dinding bagian dalam buah. Hasil panen bisa berkurang secara drastis.",
        "Penyebab": "Virus ini dapat bertahan di sisa-sisa tanaman atau akar di tanah kering selama periode lebih dari 2 tahun (1 bulan di sebagian besar tanah). Tanaman bisa terkontaminasi melalui luka kecil di akar. Virus ini dapat menyebar melalui benih yang terinfeksi, bibit, gulma dan bagian tanaman yang terkontaminasi. Angin, hujan, belalang, mamalia kecil dan burung juga dapat membawa virus antar lahan. Praktik budidaya yang buruk selama penanganan tanaman juga mendukung penularan virus. Durasi waktu siang hari, suhu, dan intensitas cahaya serta varietas dan uur tanaman menentukan tingkat keparahan infeksi.",
        "Pengendalian hayati": "Pemanasan kering terhadap biji pada suhu 70 derajat celsius selama 4 hari atau pada suhu 82-85 derajat celsius selama 24 jam akan membantu membersihkannya dari virus. Atau, biji dapat direndam selama 15 menit dalam larutan 100 g/l trisodium fosfat, dibilas dengan air kemudian dikeringkan.",
        "Pengendalian kimiawi": "Selalu pertimbangkan pendekatan terpadu dengan tindakan pencegahan bersama dengan perlakuan hayati jika tersedia. Tidak ada pengobatan kimia yang efektif terhadap Virus Mosaik Tomat.",
        "Pencegahan": [
            "Gunakan benih dari tanaman sehat atau dari sumber bersertifikat.",
            "Gunakan varietas yang tahan penyakit atau toleran.",
            "Gunakan uap-pasteurisasi untuk membersihkan tanah dari virus.",
            "Jangan menanam di lahan yang sebelumnya terinfeksi oleh virus.",
            "Optimalkan penanganan tanaman dengan mencuci tangan, memakai sarung tangan dan mendesinfeksi peralatan kerja Anda.",
            "Jangan menkonsumsi produk tembakau (seperti rokok) di sekitar tanaman tomat.",
            "Pantau tempat persemaian dan lahan produksi, singkirkan dan bakar tanaman yang sakit.",
            "Bersihkan gulma di dalam dan di sekitar lahan.",
            "Bajak dan abakr sisa-sisa tanaman setelah panen.",
            "Hindari menanam tanaman inang alternatif yang dekat dengan tomat.",
            "Terapkan rotasi tanaman dengan tanaman non-inang setidaknya selama dua tahun.",
        ],
    },
}


def app():
    st.markdown(
        "<h1 style='text-align: center;'>🍅 Tomato 🍅</h1>",
        unsafe_allow_html=True,
    )

    img = None

    def load_prep(image):
        img = np.array(image)
        img = tf.image.resize(img, (224, 224)) / 255.0
        pred = tomato_model.predict(np.expand_dims(img, axis=0))
        return pred

    tomato_model = tf.keras.models.load_model("tomato_model.h5")
    class_name = [
        "Bacterial Spot",
        "Early Blight",
        "Late Blight",
        "Leaf Mold",
        "Septoria Leaf Spot",
        "Spider Mites",
        "Target Spot",
        "Yellow Leaf Curl Virus",
        "Tomato Mosaic Virus",
        "Healthy",
    ]

    options = st.selectbox("Upload an image", ("Upload", "URL"))

    if options == "Upload":
        file = st.file_uploader("Upload an image...", type=["jpg"])
        if file is not None:
            img = Image.open(file)
    else:
        url = st.text_input("Paste the URL here:")
        if url:
            try:
                response = requests.get(url)
                img = Image.open(BytesIO(response.content))
            except:
                st.error("Invalid URL, please use a different URL.")

    if img is not None:
        button = st.button("Predict")
        pred = load_prep(img)
        if button:
            st.markdown(
                "<h1 style='text-align: center;'>The predicted result is:</h1>",
                unsafe_allow_html=True,
            )
            result = f"<h3 style='text-align: center;'>{class_name[np.argmax(pred)]} ({np.max(pred)*100:.2f}% Confidence)</h3>"
            st.markdown(result, unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                st.image(img, use_column_width=True)
            with col2:
                if class_name[np.argmax(pred)] != "Healthy":
                    with st.expander("Gejala"):
                        st.write(descriptions[class_name[np.argmax(pred)]]["Gejala"])
                    with st.expander("Penyebab"):
                        st.write(descriptions[class_name[np.argmax(pred)]]["Penyebab"])
                    with st.expander("Pengendalian hayati"):
                        st.write(
                            descriptions[class_name[np.argmax(pred)]][
                                "Pengendalian hayati"
                            ]
                        )
                    with st.expander("Pengendalian kimiawi"):
                        st.write(
                            descriptions[class_name[np.argmax(pred)]][
                                "Pengendalian kimiawi"
                            ]
                        )
                    with st.expander("Pencegahan"):
                        for i in descriptions[class_name[np.argmax(pred)]][
                            "Pencegahan"
                        ]:
                            st.write("• ", i)
