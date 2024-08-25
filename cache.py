from collections import defaultdict

class Cache:
    def __init__(self):
        self.cache = defaultdict(lambda: None)

    def is_cached(self, title, price):
        return self.cache[title] == price

    def update_cache(self, title, price):
        self.cache[title] = price

