from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Ganti dengan path ke file ChromeDriver di sistem Anda
chrome_driver_path = '/usr/local/bin/chromedriver'

# Inisialisasi ChromeOptions dan tentukan path ke ChromeDriver
chrome_options = Options()
chrome_options.binary_location = '/usr/bin/google-chrome'  # Ganti dengan path ke Chrome executable

# Aktifkan ChromeOptions saat inisialisasi Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

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
