import os
import requests
urls = ['https://tesla-cdn.thron.com/static/ZBOUYO_TSLA_Q2_2021_Update_DJCVNJ.pdf?xseo=&response-content-disposition=inline%3Bfilename%3D%22q2_2021.pdf%22', 'https://www.annualreports.com/HostedData/AnnualReports/PDF/NASDAQ_AMZN_2021.pdf']
output_dir = '.\output'
for url in urls:
    r  = requests.get(url)
    if r.status_code == 200:
        file_path = os.path.join(output_dir, os.path.basename(urls))
        with open(file_path, 'wb') as f:
            f.write(r.content)