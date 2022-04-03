import streamlit as st
import tensorflow as tf
import numpy as np
import requests
from PIL import Image
from io import BytesIO

descriptions = {
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
        "Gejala": "Bercak cokelat tua terbentuk pada daun mulai dari ujung atau tepi daun. Pada iklim lembab, bercak-bercak ini menjadi lesi yang basah. Lapisan jamur putih dapat dilihat pada bagian bawah daun. Seiring perkembangan penyakit, seluruh daun menjadi nekrotik, berubah kecokelatan, dan mati. Lesi serupa terjadi pada batang dan tangkai daun. Umbi kentang memiliki bintik-bintik biru keabu-abuan di kulitnya dan dagingnya juga berubah warna menjadi cokelat, membuatnya tidak bisa dimakan. Pembusukan lahan yang terinfeksi memberi aroma yang khas.",
        "Penyebab": "Jamur ini adalah parasit obligat. Ini berarti bahwa jamur ini harus melewati musim dingin di sisa-sisa tanaman dan umbi-umbian serta pada inang alternatif untuk bertahan hidup. Jamur ini memasuki tanaman melalui luka dan robekan di kulit. Spora jamur berkecambah pada suhu yang lebih tinggi selama musim semi dan menyebar melalui angin atau air. Penyakit ini lebih parah pada periode malam yang dingin (di bawah 18 ° C), hari-hari hangat (antara 18 dan 22 ° C), dan kondisi basah yang panjang seperti hujan dan kabut (kelembaban relatif 90%). Dalam kondisi ini, epidemi hawar daun dapat terjadi.",
        "Pengendalian hayati": "Aplikasikan fungisida berbasis tembaga sebelum cuaca kering. Semprotan daun dengan agen pelapis organik juga dapat mencegah infeksi.",
        "Pengendalian kimiawi": "Selalu pertimbangkan pendekatan terpadu berupa tindakan pencegahan bersama dengan perlakuan hayati jika tersedia. Aplikasi fungisida penting untuk mengendalikan penyakit hawar daun, terutama di daerah lembab. Fungisida kontak yang melapisi daun dapat efektif sebelum infeksi dan tidak memicu kekebalan pada jamur. Fungisida yang mengandung mandipropamid, chlorothalonil, fluazinam, atau mancozeb juga dapat digunakan sebagai perlakuan pencegahan. Perlakuan benih sebelum disemai dengan fungisida seperti mancozeb juga berhasil.",
        "Pencegahan": [
            "Gunakan benih yang sehat atau tanaman yang lebih toleran.",
            "Pastikan lahan memiliki ventilasi udara yang baik dan tanah yang dikeringkan dengan baik.",
            "Pantau lahan dan singkirkan tanaman yang terinfeksi dan sekitarnya.",
            "Gunakan rotasi tanaman selama dua hingga tiga tahun dengan tanaman yang bukan inang.",
            "Hancurkan tanaman inang yang tumbuh dengan sendirinya di dalam dan sekitar lahan.",
            "Hindari pemupukan berlebihan dengan nitrogen.",
            "Gunakan pembatas tanaman.",
            "Simpan umbi pada suhu rendah dan dengan ventilasi yang baik.",
            "Hancurkan umbi-umbian dan sisa-sisa tanaman setelah panen dengan menguburnya sedalam dua kaki (sekitar 60 cm) atau memberikannya pada binatang.",
        ],
    },
}


def app():
    st.markdown(
        "<h1 style='text-align: center;'>🥔 Kentang 🥔</h1>",
        unsafe_allow_html=True,
    )

    img = None

    def load_prep(image):
        img = np.array(image)
        img = tf.image.resize(img, (150, 150)) / 255.0
        pred = potato_model.predict(np.expand_dims(img, axis=0))
        return pred

    potato_model = tf.keras.models.load_model("potato_model.h5")
    class_name = ["Early Blight", "Late Blight", "Healthy"]

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
            result = f"<h2 style='text-align: center;'>{class_name[np.argmax(pred)]}<br><span style='font-size: 1.5rem'>{np.max(pred)*100:.2f}% Confidence</span></h2>"
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
                    with st.expander("Pengendalian Hayati"):
                        st.write(
                            descriptions[class_name[np.argmax(pred)]][
                                "Pengendalian hayati"
                            ]
                        )
                    with st.expander("Pengendalian Kimiawi"):
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
