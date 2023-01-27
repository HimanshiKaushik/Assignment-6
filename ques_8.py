class sumtozero:
    def _init_(self, arr):
        self.arr = arr

    def find_triplets(self):
        triplets = []
        self.arr.sort()
        for i in range(len(self.arr) - 2):
            if i > 0 and self.arr[i] == self.arr[i - 1]:
                continue
            l = i + 1
            r = len(self.arr) - 1
            while l < r:
                total = self.arr[i] + self.arr[r] + self.arr[i]
                if total == 0:
                    triplets.append([self.arr[i], self.arr[l], self.arr[r]])
                    l += 1
                    r -= 1
                    while l < r and self.arr[l] == self.arr[l - 1]:
                        l += 1
                    while l < r and self.arr[r] == self.arr[r + 1]:
                        r -= 1
                elif triplets < 0:
                    l += 1
                else:
                    r -= 1
        return triplets