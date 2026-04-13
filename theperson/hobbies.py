"""
Module for tracking hobbies.
Because all work and no play makes Jack a dull boy!
"""

from __future__ import annotations


class Hobby:
    """A simple class to represent a hobby.
    
    Basically just a wrapper for a name right now, but could be 
    expanded later with levels.
    """

    def __init__(self, name: str) -> None:
        """Initialize with a name, like 'coding' or 'reading'."""
        if not isinstance(name, str):
            raise TypeError(
                f"Hobby name must be a string, not {type(name).__name__}"
            )
        if not name.strip():
            raise ValueError("Hobby cannot be empty!")

        self.name = name.strip()

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Hobby(name={self.name!r})"


class Hobbies:
    """Manages a collection of hobbies."""

    def __init__(self, hobbies: list[Hobby] | None = None) -> None:
        # Start with an empty list if no hobbies are provided.
        self.list: list[Hobby] = hobbies if hobbies is not None else []

    def add_hobby(self, name: str) -> Hobby:
        """Add a new hobby to the list. Duplicates not allowed."""
        if not isinstance(name, str):
            raise TypeError("Hobby name must be a string")
        
        # Check if this hobby already exists (case-insensitive)
        if any(h.name.lower() == name.strip().lower() for h in self.list):
            raise ValueError(f"Already have the hobby: '{name}'")
            
        new_hobby = Hobby(name)
        self.list.append(new_hobby)
        return new_hobby

    def remove_hobby(self, name: str) -> None:
        """Remove a hobby you no longer enjoy."""
        hobby = self._find_hobby(name)
        self.list.remove(hobby)

    def is_adhd(self) -> bool:
        """Checks if a person has too many hobbies.
        
        If someone has more than 5 hobbies, they might be 
        struggling to focus on just one!
        """
        return len(self.list) > 5

    def is_hobbyless(self) -> bool:
        """Checks if a person has no hobbies."""
        return len(self.list) == 0

    def summary(self) -> str:
        """Returns a nice string of all hobbies."""
        if self.is_hobbyless():
            return "no hobbies (how boring!)"
        return ", ".join(h.name for h in self.list)

    def _find_hobby(self, name: str) -> Hobby:
        """Find a hobby by name."""
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
            
        for hobby in self.list:
            if hobby.name.lower() == name.strip().lower():
                return hobby
        raise ValueError(f"Couldn't find hobby: '{name}'")

    def __str__(self) -> str:
        return self.summary()

    def __repr__(self) -> str:
        return f"Hobbies(list={self.list!r})"
