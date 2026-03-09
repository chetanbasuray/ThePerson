class Person:
    """A class to represent a person."""
    
    def __init__(self,
                 name: str | None = None,
                 age: int | None = None,
                 gender: str | None = None):
        """Initialize the person's attributes."""
        self.name = name
        self.age = age
        self.gender = gender
        
    def greet(self) -> None:
        """Do a simple greeting and introduction."""
        self.say(f"Hello! My name is {self.name}.")

    def say(self,
            *args: object,
            sep: str | None = " ",
            end: str | None = "\n",
            file=None,
            flush: bool = False) -> None:
        """Say a word, phrase, sentence or paragraph."""
        print(*args, sep=sep, end=end, file=file, flush=flush)
    
        print(f'Hello! My name is {self.name}.')

    def introduce(self) -> None:
        """Print a full self-introduction using the person's attributes."""
        intro = f"Hi, my name is {self.name}."
        if self.age is not None:
            intro += f" I am {self.age} years old."
        if self.gender is not None:
            intro += f" I identify as {self.gender}."
        print(intro)
    