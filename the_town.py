"""Add yourself as a Person instance here!"""

from theperson.person import Person

if __name__ == "__main__":
    
    morpheus = Person(
        name="Morpheus",
        gender="male",
        occupation="developer on GitHub"
    )
    morpheus.introduce()
