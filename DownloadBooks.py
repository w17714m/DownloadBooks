import urllib3

from pdf.html_to_pdf import get_pdf_from_html
from util.banner import *
from listData.downloadsList import *

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
urlBook = 'https://learning.oreilly.com/library/view/hands-on-software-engineering/9781838554491/'


def download_pdfs(list_urls, t):
    i = 0
    for elem in list_urls:
        if 'cookies' in elem:
            print('cookies')
        else:
            i = i + 1
            result = get_pdf_from_html(elem['path'], t)
            name = elem['name'].translate({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
            with open('D:/GIT_HUB/DownloadBooks/download/' + str(i) + ' ' + name + '.pdf', 'wb') as file:
                file.write(result)
    pass


if __name__ == '__main__':
    print(banner())
    t = SeleniumDownload()
    temp = get_all_urls(t, urlBook)
    download_pdfs(temp, t)
