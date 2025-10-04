import csv
import streamlit as st

# --- Fungsi untuk load data ---
def load_news(filename):
    """Baca file news_data.csv ke list of dict"""
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def load_comments(filename):
    """Baca file comment_news.csv ke list of dict"""
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)
# --- Fungsi untuk memproses data ---
def process_data(news_list, comments_list):
    """
    Gabungkan berita dan komentar,
    hitung jumlah komentar & rata-rata rating.
    Hasilnya list of dict.
    """
    # TODO: Buat dictionary untuk kumpulkan komentar per idBerita
    comments_per_news = {}

    for c in comments_list:
        idb = c['idBerita']
        rating = float(c.get('Rating', 0))  # asumsi kolom Rating ada dan angka
        if idb not in comments_per_news:
            comments_per_news[idb] = {
                'ratings': [],
                'count': 0
            }
        comments_per_news[idb]['ratings'].append(rating)
        comments_per_news[idb]['count'] += 1

    # TODO: Buat list hasil gabungan
    result = []
    for n in news_list:
        idb = n['idBerita']
        headline = n['Headline']
        if idb in comments_per_news:
            jumlah = comments_per_news[idb]['count']
            rata = sum(comments_per_news[idb]['ratings']) / jumlah if jumlah > 0 else 0
        else:
            rata = 0
            jumlah = 0
        rata = 0  # ganti dengan hitungan
        jumlah = 0  # ganti dengan hitungan
        result.append({
            'ID Berita': idb,
            'Headline': headline,
            'Rata-rata Rating': round(rata, 2),
            'Jumlah Komentar': jumlah
        })

    # --- Urutkan berdasarkan rating pakai fungsi biasa ---
    def ambil_rating(item):
        return item['Rata-rata Rating']

    result.sort(key=ambil_rating, reverse=True) 
    return result

# --- Fungsi untuk tampilkan di Streamlit ---
def main():
    st.title("Analisis Sentimen & Popularitas Berita")
    st.write("Menampilkan ID, Headline, Rata-rata Rating, dan Jumlah Komentar, diurutkan dari rating tertinggi.")

    # TODO: baca data CSV
    news_data =   load_news('news_data.csv')
    comment_data = load_comments('comment_news.csv')

    # TODO: proses data
    hasil =  process_data(news_data, comment_data)

    st.table(hasil)

    pass

if __name__ == '__main__':
    main()
