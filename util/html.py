import dominate
from dominate.tags import *
import os
from operator import itemgetter


class HTML:
    def __init__(self, web_dir, title, reflesh=0):
        self.title = title
        self.web_dir = web_dir
        self.img_dir = os.path.join(self.web_dir, 'images')
        if not os.path.exists(self.web_dir):
            os.makedirs(self.web_dir)
        if not os.path.exists(self.img_dir):
            os.makedirs(self.img_dir)
        # print(self.img_dir)

        self.doc = dominate.document(title=title)
        if reflesh > 0:
            with self.doc.head:
                meta(http_equiv="reflesh", content=str(reflesh))

    def get_image_dir(self):
        return self.img_dir

    def add_header(self, str):
        with self.doc:
            h3(str)

    def add_table(self, border=1):
        self.t = table(border=border, style="table-layout: fixed;")
        self.doc.add(self.t)

    def add_images(self, ims, txts, links, width=400):
        self.add_table()
        with self.t:
            with tr():
                ### HACKY
                txts = list(txts)
                for i in range(len(txts)):
                    txt = txts[i]
                    if len(txts) == 6:  # If cyclegan. This is hacky. Just want to display relevant images.
                        if txt in ['fake_B', 'rec_A', 'rec_B']:
                            continue
                        if txt == 'real_A':
                            txt = 'Ground truth material segmentation'
                        if txt == 'real_B':
                            txt = 'Input rendering'
                        if txt == 'fake_A':
                            txt = 'Output material segmentation'
                    if len(txts) == 3:  # If pix2pix. This is hacky. Just want to display relevant images.
                        if txt == 'real_A':
                            txt = 'Input rendering'
                        if txt == 'fake_B':
                            txt = 'Output material segmentation'
                        if txt == 'real_B':
                            txt = 'Ground truth material segmentation'
                    txts[i] = txt
                l = zip(ims, txts, links)
                # This is too hacky
                print txts
                if 'idt_A' not in txts:
                    l.sort(key=itemgetter(1))
                ###
                #for im, txt, link in zip(ims, txts, links):
                for im, txt, link in l:
                    ### HACKY
                    if len(txts) == 6:  # If cyclegan. This is hacky. Just want to display relevant images.
                        if txt in ['fake_B', 'rec_A', 'rec_B']:
                            continue
                    with td(style="word-wrap: break-word;", halign="center", valign="top"):
                        with p():
                            with a(href=os.path.join('images', link)):
                                img(style="width:%dpx" % width, src=os.path.join('images', im))
                            br()
                            p(txt)

    def save(self):
        html_file = '%s/index.html' % self.web_dir
        f = open(html_file, 'wt')
        f.write(self.doc.render())
        f.close()


if __name__ == '__main__':
    html = HTML('web/', 'test_html')
    html.add_header('hello world')

    ims = []
    txts = []
    links = []
    for n in range(4):
        ims.append('image_%d.png' % n)
        txts.append('text_%d' % n)
        links.append('image_%d.png' % n)
    html.add_images(ims, txts, links)
    html.save()
