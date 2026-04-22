"""Add yourself as a Person instance here!"""

from theperson.hobbies import Hobbies
from theperson.person import Person, Personal, Profile, Professional


if __name__ == "__main__":
    morpheus = Person(
        profile=Profile(name="Morpheus", gender="male"),
        professional=Professional(occupation="developer on GitHub"),
    )

    morpheus.introduce()

    syed = Person(
        profile=Profile(name="Syed Abdul Aman", gender="male"),
        professional=Professional(occupation="Generative AI Developer"),
    )

    syed.introduce()
    
    gloria = Person(
        profile=Profile(name="Gloria", gender="female"),
        professional=Professional(occupation="Data Scientist"),
    )       
    
    gloria.introduce()

    joe = Person(
        profile=Profile(
            name="Joe", 
            gender="male",
        ),
        personal=Personal(
            hobbies=Hobbies()
        ),
        professional=Professional(
            occupation="Product Owner", 
            skills=["product design", "prototyping"]
        )
    )
    joe.hobbies.add_hobby("coding")
    joe.hobbies.add_hobby("chess")
    joe.hobbies.add_hobby("hiking")

    joe.introduce()
    joe.mood.set_mood("calm", 0.9)
    joe.goals.add_goal("master git")
    joe.greet(morpheus)
    
    morpheus.greet(joe)
    morpheus.compliment(joe)

    chetan = Person(
        profile=Profile(
            name="Chetan",
            gender="Male",
        ),
        personal=Personal(
            hobbies=Hobbies()
        ),
        professional=Professional(
            occupation="Software Engineer",
            skills=["Software Architecture", "Web Development"]
        )
    )
    chetan.hobbies.add_hobby("Music")
    chetan.hobbies.add_hobby("Reading")
    chetan.hobbies.add_hobby("Movies")

    chetan.introduce()
    chetan.say("Hello everyone! I'm excited to be part of TheTown. 🚀")
    chetan.mood.set_mood("excited", 0.8)
    chetan.goals.add_goal("Contribute to open-source")
