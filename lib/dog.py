#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Dog", breed="Beagle"):
        self.name = name
        self.breed = breed

        @property
        def name(self):
            return self._name
        
        @name.setter
        def name(self, value):
            if isinstance(value, str) and 1 <= len(value) <= 20:
                raise TypeError("Name must be a string")
            self._name = value
    pass
