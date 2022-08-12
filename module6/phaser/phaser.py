import  requests

def main():

    url = 'http://potolki46.com/'

    links = []

    filename = 'checks.txt'
    #filename = input('Enter filename:\t')

    extension = ""


    with open(filename, 'rt') as f:
        links = f.readlines()

    #print(links)

    if len(links) == 0:
        print('empty link file')

    for link in links:
        link = link.replace('\n', '')
        full_link = ''.join((url, link, extension))
        print(full_link)

        responce = requests.get(full_link, timeout=5)
        print(responce.status_code)

        if responce.status_code != 404:
            print(f'{full_link} - link exists')



if __name__ == "__main__":
    main()