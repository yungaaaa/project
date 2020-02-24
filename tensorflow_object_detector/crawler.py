from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()  


arguments = {"keywords":"寶礦力","limit":500,"print_urls":True,"chromedriver":".\chromedriver.exe"}    
#keywords 搜尋的關鍵字;limit 設定最多抓幾張;print_urls 要不要記錄圖檔路徑

paths = response.download(arguments)  
print(paths)   #printing absolute paths
