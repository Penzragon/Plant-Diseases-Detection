import streamlit as st
import tensorflow as tf
import numpy as np
import requests
from PIL import Image
from io import BytesIO

descriptions = {
    "Gray Leaf Spot": {
        "Gejala": "Nekrotik kecil (coklat atau sawo matang) yang bisa dikelilingi lingkaran kuning klorosis muncul di daun bagian bawah, biasanya sebelum berbunga. Secara bertahap luka ini akan berubah keabu-abuan dan muncul pada daun yang lebih muda juga. Ketika penyakit ini berkembang, luka ini membesar menjadi memanjang, bersegi empat yang sejajar dengan urat daun. Dalam kondisi optimal (suhu hangat, kelembaban tinggi dan daun basah), luka-luka dapat menyatu dan menutupi seluruh daun. Jika ini terjadi sebelum pembentukan biji, maka bisa terjadi kerugian panen yang cukup besar. Hawar daun dapat melemahkan tanaman dan kadang-kadang melunakkan batang, sehingga dapat membuatnya rubuh.",
        "Penyebab": "Penyakit bercak daun abu-abu disebabkan oleh jamur Cercospora zeae-maydis. Jamur ini bertahan dalam sisa-sisa tanaman di tanah dalam waktu yang lama. Selama musim semi, spora dibawa ke daun bagian bawah oleh percikan air hujan dan angin. Siklus hidupnya didukung oleh suhu tinggi (25 hingga 30 °C), kelembaban tinggi (embun, kabut) dan basahnya daun untuk jangka waktu yang lama. Cuaca panas dan kering menghambat perkembangannya. Gejalanya sedikit berbeda antar varietas tanaman yang berbeda. Jamur menyelesaikan siklus hidupnya (dari infeksi ke produksi spora baru) dalam 14-21 hari pada varietas yang rentan dan dalam 21-28 hari dalam varietas yang tahan.",
        "Pengendalian hayati": "Tidak ada kontrol alami yang tersedia untuk mengendalikan penyakit ini.",
        "Pengendalian kimiawi": "Selalu pertimbangkan pendekatan terpadu berupa tindakan pencegahan dan perlakuan hayati jika tersedia. Perlakuan fungisida daun adalah cara untuk mengelola penyakit ini jika terjadi pada tahap awal tetapi harus mempertimbangkan kondisi cuaca, potensi kerugian panen dan kerentanan tanaman. Fungisida yang mengandung piraklostrobin dan strobilurin, atau kombinasi azoksistrobin dan propikonazol, protiokonazol dan trifloksistrobin bekerja dengan baik untuk mengendalikan jamur.",
        "Pencegahan": [
            "Tanam varietas yang tahan jika tersedia di daerah Anda.",
            "Lakukan penanaman lebih akhir untuk menghindari kondisi buruk bagi tanaman.",
            "Jaga peredaran udara yang baik dengan memperluas ruang di antara tanaman.",
            "Bajak lahan dalam-dalam dan kubur semua sisa tanaman setelah panen.",
            "Rencanakan rotasi tanaman jangka panjang dengan tanaman bukan inang.",
        ],
    },
    "Common Rust": {
        "Gejala": "Flek-flek kecil muncul di kedua sisi daun dan perlahan berkembang menjadi bercak-bercak kecil berwarna kecoklatan. Bercak-bercak yang memanjang ini kemudian berubah menjadi bintil-bintil seperti tepung, berwarna coklat keemasan yang tersebar dalam jarak yang renggang di sisi atas dan bawah. Warnanya bisa berubah menjadi hitam saat tanaman matang. Berlawanan dengan penyakit karat lainnya, gejala biasanya tidak muncul pada bagian-bagian lain tanaman, seperti tangkai, daun pelindung atau kulit ari. Namun, tangkai cenderung tumbuh lemah dan lunak, dan rentan rubuh. Jaringan daun yang lebih muda lebih rentan terhadap infeksi jamur daripada daun tua. Tanaman yang terinfeksi pada tahap awal dapat menunjukkan klorosis daun dan kematian, yang menyebabkan kerugian hasil yang besar jika daun di bagian atas tanaman terpengaruh.",
        "Penyebab": "Penyakit ini disebabkan oleh jamur Puccinia sorghi. Jamur melewati musim dingin di inang alternatif (spesies dari Oxalis) dan melepaskan spora selama musim semi. Spora dapat dipindahkan dalam jarak yang sangat jauh oleh angin dan hujan. Spora memulai proses infeksi ketika menghinggapi daun. Infeksi sekunder dari tanaman ke tanaman juga dapat terjadi karena angin dan hujan. Perkembangan penyakit ini didukung oleh kelembaban yang relatif tinggi (hampir 100%), embun, hujan, dan suhu dingin antara 15 dan 20 °C (dapat bervariasi tergantung daerah). Cuaca panas dan kering pada gilirannya akan memperlambat atau menghambat perkembangan jamur dan timbulnya penyakit. Ini lebih merupakan masalah pada tanaman yang digunakan untuk produksi benih dan jagung manis. Tanaman yang dibudidayakan sebagai pakan ternak, untuk produk industri, atau untuk membuat makanan olahan tidak perlu dikhawatirkan. Hasil panen berkurang karena produktivitas tanaman menjadi lebih rendah dan tanaman rubuh.",
        "Pengendalian hayati": "Hingga saat ini kami belum mengetahui perlakuan alternatif terhadap Puccinia sorghi. Jika Anda mengetahui metode apa pun yang berhasil mengurangi kemunculan atau tingkat gejala tersebut, mohon hubungi kami.",
        "Pengendalian kimiawi": "Selalu pertimbangkan pendekatan terpadu dengan tindakan pencegahan bersama dengan perlakuan hayati jika tersedia. Penyemprotan fungisida dapat bermanfaat jika digunakan pada varietas yang rentan. Berikan fungisida daun pada awal musim jika karat menyebar dengan cepat karena kondisi cuaca. Banyak jenis fungisida yang tersedia untuk pengendalian karat. Produk-produk yang mengandung mankozeb, piraklostrobin, piraklostrobin + metkonazol, piraklostrobin + fluksapiroksad, azoksistrobin + propikonazol, trifloksistrobin + protiokonazol dapat digunakan untuk mengendalikan penyakit ini. Contoh perlakuannya dapat berupa penyemprotan mankozeb @ 2,5 g/l segera setelah bintil-bintil muncul dan ulangi dalam selang 10 hari hingga tahap berbunga.",
        "Pencegahan": [
            "Tanam varietas tahan penyakit yang tersedia di wilayah Anda.",
            "Lakukan penanaman lebih awal untuk menghindari kondisi infeksi yang optimal.",
            "Gunakan varietas pendek musim yang matang lebih awal.",
            "Pantau tanaman Anda secara teratur untuk melihat tanda-tanda penyakit, terlebih saat cuaca mendung.",
            "Lakukan pemupukan seimbang dengan pemberian nitrogen yang terpisah.",
            "Rencanakan rotasi tanaman dengan tanaman yang tidak rentan.",
        ],
    },
    "Northern Leaf Blight": {
        "Gejala": "Gejala berupa bercak-bercak kecil, lonjong, basah, pada daun di bagian bawah terlebih dahulu. Ketika penyakit berlanjut, bercak mulai muncul di bagian atas tanaman. Bercak-bercak yang lebih tua perlahan-lahan tumbuh menjadi lesi cokelat nekrotik berbentuk cerutu panjang dengan bercak-bercak gelap yang jelas dan tepian hijau pucat yang basah. Lesi-lesi ini kemudian menyatu dan melingkupi sebagian besar daun dan tangkai, kadang-kadang menyebabkan kematian dan robohnya tanaman. Jika infeksi menyebar ke bagian atas tanaman selama perkembangan tongkol, kerugian hasil panen yang sangat besar dapat terjadi (hingga 70%).",
        "Penyebab": "Jamur melewati musim dingin di tanah atau di sisa-sisa tanaman. Curah hujan, embun malam, kelembapan tinggi dan suhu sedang mendukung penyebaran jamur. Jamur dibawa oleh angin atau cipratan air hujan dan pertama kali menyebar dari tanah ke daun tanaman jagung muda yang lebih rendah. Kondisi hujan dan kebiasaan yang buruk di lahan mendukung penyebarannya ke tanaman lain dan di dalam lahan. Suhu optimal untuk infeksi berada pada kisaran 18 hingga 27 ° C selama musim tanam. Waktu basah daun 6 hingga 18 jam sehari yang berkepanjangan juga mendukung penyebaran. Sorgum adalah inang favorit lain dari jamur ini.",
        "Pengendalian hayati": "Fungisida hayati berdasarkan Trichoderma harzianum, atau Bacillus subtilis dapat diberikan pada berbagai tahap untuk mengurangi risiko infeksi. Pemberian larutan sulfur juga efektif.",
        "Pengendalian kimiawi": "Pendekatan terpadu berupa tindakan pencegahan bersama dengan kebiasaan budaya yang hati-hati disarankan. Pemberian fungisida sebagai pencegahan dini dapat menjadi cara yang efektif untuk mengendalikan penyakit. Jika tidak, fungisida dapat diberikan ketika gejala terlihat di kanopi bawah untuk melindungi daun bagian atas dan tongkol. Terapkan semprotan berdasarkan azoksistrobin, pikoksistrobin, mankozeb, piraklostrobin, propikonazol, tetrakonazol. Berikan produk berbasis pikoksistrobin + siprokonazol, piraklostrobin + metkonazol, propikonazol + azoksistrobin, protiokonazol + trifloksistrobin. Perlakuan benih tidak dianjurkan.",
        "Pencegahan": [
            "Tamam varietas yang tahan atau toleran.",
            "Pastikan pasokan unsur hara seimbang dan hindari pemupukan nitrogen yang berlebihan.",
            "Singkirkan gulma secara teratur di dalam dan sekitar lahan.",
            "Rotasikan dengan kacang kedelai, kacang, atau bunga matahari untuk menghindari penyebaran yang luas.",
            "Bajak dalam-dalam untuk mengubur sisa-sisa tanaman dan mengurangi jumlah inokulum di tanah.",
        ],
    },
}


def app():
    st.markdown(
        "<h1 style='text-align: center;'>🌽 Jagung 🌽</h1>",
        unsafe_allow_html=True,
    )

    img = None

    def load_prep(image):
        img = np.array(image)
        img = tf.image.resize(img, (150, 150)) / 255.0
        pred = corn_model.predict(np.expand_dims(img, axis=0))
        return pred

    corn_model = tf.keras.models.load_model("corn_model.h5")
    class_name = ["Gray Leaf Spot", "Common Rust", "Northern Leaf Blight", "Healthy"]

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
                    st.markdown(
                        "<h4 style='text-align: center;'>Keterangan Penyakit</h4>",
                        unsafe_allow_html=True,
                    )
                    with st.expander("Gejala 🔬"):
                        st.write(descriptions[class_name[np.argmax(pred)]]["Gejala"])
                    with st.expander("Penyebab 🦠"):
                        st.write(descriptions[class_name[np.argmax(pred)]]["Penyebab"])

                    st.markdown(
                        "<h4 style='text-align: center;'>Penanganan</h4>",
                        unsafe_allow_html=True,
                    )
                    with st.expander("Pengendalian Hayati 🌿"):
                        st.write(
                            descriptions[class_name[np.argmax(pred)]][
                                "Pengendalian hayati"
                            ]
                        )
                    with st.expander("Pengendalian Kimiawi 🧪"):
                        st.write(
                            descriptions[class_name[np.argmax(pred)]][
                                "Pengendalian kimiawi"
                            ]
                        )
                    with st.expander("Pencegahan ⚠️"):
                        for i in descriptions[class_name[np.argmax(pred)]][
                            "Pencegahan"
                        ]:
                            st.write("• ", i)
                else:
                    st.success("Jagung tidak terinfeksi")
                    st.markdown(
                        "<h4 style='text-align: center;'>Saran</h4>",
                        unsafe_allow_html=True,
                    )
                    with st.expander("Perawatan 🩺"):
                        st.write(
                            "Renggangkan tanaman Anda saat tingginya sekitar 8 hingga 10 cm, sehingga jaraknya antara 20 hingga 30 cm. Berhati-hatilah agar tidak merusak akar saat menyiangi. Pastikan drainase tanahnya baik sehingga mampu menjaga tingkat kelembaban yang konsisten. Dalam kondisi kering, Anda perlu menyirami tanaman untuk memastikan akarnya yang dangkal tetap lembab."
                        )
                    with st.expander("Tanah 🪴"):
                        st.write(
                            "Zea mays (jagung) tumbuh paling baik di tanah lempung atau aluvial yang subur dan berdrainase baik. Namun, jagung dapat ditanam di berbagai jenis tanah, dari pasir hingga tanah liat. Tanaman ini toleran terhadap keasaman tanah. Menetralkan keasaman tanah dengan pengapuran dapat meningkatkan hasil panen."
                        )
                    with st.expander("Iklim ☁️"):
                        st.write(
                            "Salah satu alasan mengapa jagung ditanam di seluruh dunia adalah kemampuannya untuk tumbuh di berbagai kondisi agroklimat. Namun, wilayah bersuhu dan bercurah hujan sedang paling cocok bagi tanaman ini."
                        )
