import re
import json

class Article:
    def __init__(self, title, link, summary, date, isBreakingNews = False):
        self.title = title
        self.summary = summary
        self.link = link
        self.domainName = self.__extract_domain_name(link)
        self.date = f"{date:%d-%b-%Y}"
        self.isBreakingNews = isBreakingNews
    
    def toJson(self):
        return json.dumps(self.__dict__)

    def __extract_domain_name(self, link):
        # https://www.blahblahblah.com/somedir/somesubdir
        domain = re.search('https?://([A-Za-z_0-9.-]+).*', link)
        if domain:
            return domain.group(1)
        else:
            return link
