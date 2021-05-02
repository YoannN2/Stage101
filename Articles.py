import lorem
import random
import pandas as pd
from datetime import datetime, timedelta

from utils import NOMS, PRENOMS



# utils
def random_datetime():
    date = datetime.now() - timedelta(days=random.randint(0,10), hours=random.randint(0,24), minutes=random.randint(0,60), seconds=random.randint(0,60))
    return date.strftime("%d/%m/%Y %H:%M:%S")

class Article:
    """
    Modele d'article
    """
    id: int
    title: str
    description: str
    full_text: str
    created_date: str
    author: str
    image: str

    columns = ["id", "title", "description", "full_text", "created_date", "author", "image"]

    def to_dict(self):
        return {attr: self.__getattribute__(attr) for attr in self.columns}

class ArticleMaker:
    """
    Factory pour creer des Articles
    """
    def __init__(self, n=100):
        self.make_articles(n)


    def make_articles(self, n: int) -> [dict]:
        """
        Creer une liste de n article et return une liste de dictionnaire
        """
        # Creer une liste vide pour sauvegarder les n Articles
        self.articles = []

        for i in range(n):
            article = Article()

            # id
            article.id = f"{i:0>{len(str(n))}}"

            # title
            article.title = lorem.sentence()

            # description
            article.description = lorem.paragraph()

            # full_text
            article.full_text = lorem.text()

            # created_date
            article.created_date = random_datetime()

            # author
            article.author = f"{random.choice(PRENOMS).title()} {random.choice(NOMS).upper()}"

            # image
            article.image = f"https://picsum.photos/id/{1000 + int(article.id)}/400/200.jpg"

            # Append Article to Articles
            self.articles.append(article.to_dict())

    def to_df(self):
        """
        Converti la liste d'utilisateurs en DataFrame
        """
        return pd.DataFrame(self.articles, columns=Article.columns)

    def to_json(self, fn="articles.json"):
        """
        Enregistre la liste d'utilisateurs en fichier json dans fn
        """
        return self.to_df().to_json(fn)

# Test
if __name__ == '__main__':

    # Make 15 Articles
    AM = ArticleMaker(n=15)
    articles = AM.to_df()

    print("Articles")
    print(articles.head())

    fn = "articles.json"
    AM.to_json(fn)
    print(f"{len(articles)} Articles saved in {fn}")
