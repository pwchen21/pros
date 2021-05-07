    def __init__(self):
        self.freq = Counter()
        self.stacks = defaultdict(list)
        self.maxfreq = 0

    def push(self, x):
        freq_x = self.freq[x] + 1
        self.freq[x] = freq_x
        self.maxfreq = max(self.maxfreq, freq_x)
        self.stacks[freq_x].append(x)

    def pop(self):
        x = self.stacks[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.stacks[self.maxfreq]: self.maxfreq -= 1
        return x