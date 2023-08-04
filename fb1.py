from selenium import webdriver

# Inisialisasi browser
driver = webdriver.Chrome(executable_path='/home/argadwiihsanulridha/.local/lib/python3.9/site-packages/selenium/webdriver/')  # Ganti dengan browser yang sesuai (misalnya, Firefox atau Edge)

# Buka halaman web dengan video
video_url = "https://web.facebook.com/watch/?v=1327787108138374"  # Ganti dengan URL video yang ingin ditonton
driver.get(video_url)

# Cari elemen video dan putar video (jika diperlukan)
# Contoh untuk YouTube menggunakan class "video-stream html5-main-video"
video_element = driver.find_element_by_css_selector("video.video-stream.html5-main-video")
video_element.click()

# Tambahkan kode lain jika Anda ingin mengontrol video (berhenti, pause, geser waktu, dll.)
# ...

# Tunggu beberapa waktu untuk menonton video (misalnya, 30 detik)
import time
time.sleep(910)

# Tutup browser
driver.quit()
