import newspaper
from datetime import datetime
from Articles import Article
from NewsBuffer import NEWS_BUFFER
# import nltk
# nltk.download("punkt")

class Sourcer:

    def __init__(self):
        pass

    def __importSources(self):
        with open("newspapers.txt", "r") as f:
            return [line.strip() for line in f.read().splitlines()]

    def start(self):
        # dispatch fetch function
        self.__scrape_main_sources()

    def __fetch(self):
        # result = self.__scrapePage(link)
        # self.__push_to_buffer(result)
        pass

    def stop(self):
        # stop dispatched fetch function
        pass

    def __scrape_main_sources(self):
        # predefined news sources
        mainSources = self.__importSources()
        for link in mainSources:
            # print(f"\tFound {len(NEWS_BUFFER)} articles so far...", end='\r')
            self.__scrapePage(link)

    def __push_to_buffer(self, news):
        NEWS_BUFFER.append(news)

    def __scrapePage(self, link):
        curr_month = datetime.now().month
        paper = newspaper.build(link, memoize_article= False)
        for article in paper.articles:
            artcl = newspaper.Article(article.url)
            try:
                artcl.download()
                artcl.parse()
                artcl.nlp()
                if artcl.publish_date and artcl.publish_date.month == curr_month:
                    self.__push_to_buffer(Article(artcl.title, artcl.url, artcl.summary, artcl.publish_date))
            except:
                return
