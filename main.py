from icrawler.builtin import GoogleImageCrawler

def google_img_downloader():
    crawler = GoogleImageCrawler(storage={'root_dir' : './img'})
    filter = dict(
        type = "photo",
        # color = "blackandwhite",
        size = "large",
        # license = "noncommercial"
        # date = "pastweek"

    )
    # crawler.crawl(keyword='mr.robot', max_num=5)
    # crawler.crawl(keyword='spongebob', max_num=5, min_size=(1000,1000), overwrite=True)
    crawler.crawl(keyword='city',
                  max_num=5,
                  min_size=(1000,1000),
                  overwrite=True,
                  filters=filter,
                  file_idx_offset='auto')
def main():
    google_img_downloader()

if __name__ == '__main__':
    main()

