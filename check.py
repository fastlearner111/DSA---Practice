class Counter:
    def __init__(self):
        self.count = 0      # 8 spaces — inside __init__

    def increment(self):
        self.count += 1     # 8 spaces — inside increment

    def get(self):
        return self.count   # 8 spaces — inside get

c = Counter()
c.increment()
c.increment()
c.increment()
print(c.get())