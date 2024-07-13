site_url = input("Enter the website name: ")
if "https://" in site_url:
    site_url = site_url.replace("https://","").replace("/","").replace("\\","")
with open(r"C:\Windows\System32\drivers\etc\hosts",'a+') as file:
    c = ''
    file.write("{}127.0.0.1                    {}".format(c,site_url))
print("Website blocked")
