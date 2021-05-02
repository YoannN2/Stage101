import random
import pandas as pd

from utils import NOMS, PRENOMS, EMAILS

class User:
    """
    Modele d'utilisateur
    """
    id: int
    profile: str
    nom: str
    prenom: str
    email: str
    tel: str

    columns = ["id", "nom", "prenom", "email", "tel"]

    def to_dict(self):
        return {attr: self.__getattribute__(attr) for attr in self.columns}

class UserMaker:
    """
    Factory pour creer des Users
    """
    def __init__(self, n=100):
        self.make_users(n)

    def make_users(self, n):
        """
        Creer une liste de n user et return une liste de dictionnaire
        """
        # Creer une liste vide pour sauvegarder les n Users
        self.users = []

        for i in range(n):
            user = User()
            user.id = f"{i:0>{len(str(n))}}"

            # profile
            user.profile = f"./user/{user.id}"

            # nom
            user.nom = random.choice(NOMS)

            # prenom
            user.prenom = random.choice(PRENOMS)

            # email
            user.email = f"{user.prenom[0].lower()}.{user.nom.lower()}@{random.choice(EMAILS)}"

            # tel
            user.tel = f"{random.randint(20,99)}.{random.randint(0,99):0>2}.{random.randint(0,99):0>2}"

            #
            self.users.append(user.to_dict())

    def to_df(self):
        """
        Converti la liste d'utilisateurs en DataFrame
        """
        return pd.DataFrame(self.users, columns=User.columns)

    def to_json(self, fn="users.json"):
        """
        Enregistre la liste d'utilisateurs en fichier json dans fn
        """
        self.to_df().to_json(fn)

# Test
if __name__ == '__main__':
    # Make 15 Users
    UM = UserMaker(n=15)

    # transform users
    users = UM.to_df()
    print("Users")
    print(users.head())

    fn = "users.json"
    UM.to_json(fn)
    print(f"{len(users)} Users saved in {fn}")
