#En reprenant l’exercice de pool de threads, créer le téléchargement en
#parallèle des photos sur 3 codes différents:
    #• Utilisation du mécanisme de threading.Thread
    #• Utilisation du pool de threads
    #• Utilisation du multiprocessing
    #• A l’aide du suivi de processus, donnez la différence entre les threads et les processus
import time
import concurrent.futures
import requests
import multiprocessing

img_url_1 = 'https://img.freepik.com/photos-premium/astronaute-dans-espace-exterieur-ouvert-planete-terre-etoiles-fournissent-arriere-plan-formant-espace-au-dessus-planete-terre-lever-du-soleil-coucher-du-soleil-notre-maison-iss-elements-image-fournie-par-nasa_150455-16829.jpg'
img_url_2 = 'https://www.akamai.com/site/im-demo/perceptual-standard.jpg'

img_urls = [
    'https://helpx.adobe.com/content/dam/help/en/photoshop/using/convert-color-image-black-white/jcr_content/main-pars/before_and_after/image-before/Landscape-Color.jpg'
    'http://cdn.eso.org/images/screen/eso1907a.jpg'
            ]

####################################################################
def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[-1]
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")


start = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)

end = time.perf_counter()
print(f"Tasks ended in {round(end - start, 2)} second(s)")

##############################################################################


def task1():
    print(f"Task starts for 1 second")
    time.sleep(1)
    print(f"Task ends")


def task2():
    print(f"Task starts for 1 second")
    time.sleep(1)
    print(f"Task ends")

if __name__ == '__main__':
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=task1)
    p2 = multiprocessing.Process(target=task2)
    p1.start()
    p2.start()
    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")
