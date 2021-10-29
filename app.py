import streamlit as st
import yake


def yake_keyword(doc):
    text = doc
    language = "id"
    max_ngram_size = 3
    deduplication_thresold = 0.2
    deduplication_algo = 'seqm'
    windowSize = 1
    numOfKeywords = 20

    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_thresold, dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords, features=None)
    keywords = custom_kw_extractor.extract_keywords(text)
    list_keyword = []
    list_keyword_clean = []
    for kw in keywords:
        list_keyword.append(kw[0].lower())
    return list_keyword[:15]

def main():
    st.title('Tag Recommendations')
    text = st.text_input("Text", "Type Here")

    # clean text
    text = text.replace('Terima kasih atas pertanyaan Anda.', '')
    text = text.replace('Artikel di bawah ini adalah pemutakhiran dari artikel dengan judul','')
    text = text.replace('Bingung menentukan keterkaitan pasal dan kewajiban bisnis Anda, serta keberlakuan peraturannya? Ketahui kewajiban dan sanksi hukum perusahaan Anda dalam satu platform integratif dengan Regulatory Compliance System dari Hukumonline, klik di sini untuk mempelajari lebih lanjut','')
    text = text.replace('Seluruh informasi hukum yang ada di Klinik hukumonline.com disiapkan semata – mata untuk tujuan pendidikan dan bersifat umum (lihat Pernyataan Penyangkalan selengkapnya). Untuk mendapatkan nasihat hukum spesifik terhadap kasus Anda, konsultasikan langsung dengan Konsultan Mitra Justika.','')
    tag_result = ''
    final_result = []
    stopwords = ['pasal', 'nomor', 'ayat', 'undang', 'angka',
                 'undang nomor', 'pemerintah nomor', 'hukum',
                 'tahun', 'bangsa', 'negara', 'republik',
                 'indonesia', 'nasional', 'adalah', 'huruf',
                 'undang-undang nomor', 'untuk']
    if st.button("Give Recommendations"):
        tag_result = yake_keyword(text)
        for i in tag_result:
            if i not in stopwords:
                final_result.append(i)
    st.success("Tag recommendations: {}".format(final_result))


if __name__ == '__main__':
    main()