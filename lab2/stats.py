def round_half_up_mean(total: float, count: int) -> float:
    mean = total / count
    if mean >= 0:
        return int(mean * 10 + 0.5) / 10
    return int(mean * 10 - 0.5) / 10

class StationStats:
    __slots__ = ["_min", "_max", "_sum", "_count"]
    
    def __init__(self, temperature: float):
        self._min = temperature
        self._max = temperature
        self._sum = temperature
        self._count = 1

    def __repr__(self):
        return f"{self._min};{round_half_up_mean(self._sum, self._count)};{self._max}"


    def update(self, value: float):
        if value < self._min:
            self._min = value
        if value > self._max:
            self._max = value
        self._sum += value
        self._count += 1

    def merge(self, other: "StationStats"):
        self._min = min(self._min, other._min)
        self._max = max(self._max, other._max)
        self._sum += other._sum
        self._count += other._count

    

