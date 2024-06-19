import bz2
import os

from dotenv import load_dotenv

load_dotenv()


class NumbersStatistic:

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.numbers = []
        self._load_numbers()

    def _load_numbers(self) -> None:
        with bz2.open(self.filename, "rt") as file:
            for line in file:
                num = float(line.strip())
                self.numbers.append(num)

    def _get_min_value(self) -> float:
        return min(self.numbers)

    def _get_max_value(self) -> float:
        return max(self.numbers)

    def _get_median_value(self) -> float:
        sorted_numbers = sorted(self.numbers)
        numbers_length = len(sorted_numbers)
        middle = numbers_length // 2

        if numbers_length % 2 == 0:
            median = (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2.0
        else:
            median = sorted_numbers[middle]

        return median

    def _get_mean_value(self) -> float:
        return sum(self.numbers) / len(self.numbers)

    def _get_longest_increasing_sequence(self) -> list[float]:
        longest_increasing_sequence = []
        current_sequence = []

        for num in self.numbers:
            if not current_sequence or num > current_sequence[-1]:
                current_sequence.append(num)
            else:
                if len(current_sequence) > len(longest_increasing_sequence):
                    longest_increasing_sequence = current_sequence
                current_sequence = [num]

        if len(current_sequence) > len(longest_increasing_sequence):
            longest_increasing_sequence = current_sequence

        return longest_increasing_sequence

    def _get_longest_decreasing_sequence(self) -> list[float]:
        longest_decreasing_sequence = []
        current_sequence = []

        for num in self.numbers:
            if not current_sequence or num < current_sequence[-1]:
                current_sequence.append(num)
            else:
                if len(current_sequence) > len(longest_decreasing_sequence):
                    longest_decreasing_sequence = current_sequence
                current_sequence = [num]

        if len(current_sequence) > len(longest_decreasing_sequence):
            longest_decreasing_sequence = current_sequence

        return longest_decreasing_sequence

    def show_statistics(self) -> None:
        print(f"Min value:{self._get_min_value()}")
        print(f"Max value: {self._get_max_value()}")
        print(f"Median value: {self._get_median_value()}")
        print(f"Mean value: {self._get_mean_value()}")
        print(f"Longest increasing sequence: {self._get_longest_increasing_sequence()}")
        print(f"Longest decreasing sequence: {self._get_longest_decreasing_sequence()}")


if __name__ == "__main__":
    num_stats = NumbersStatistic(os.getenv("FILENAME"))
    num_stats.show_statistics()
