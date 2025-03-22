def filter_by_type(data, data_type):
    """Filtruje dane, zwracając tylko elementy o określonym typie."""
    return [item for item in data if isinstance(item, data_type)]

def normalize_numbers(data):
    """Normalizuje liczby w liście do wartości między 0 a 1."""
    numeric_data = [float(x) for x in data if isinstance(x, (int, float))]
    max_value = max(numeric_data)
    return [x / max_value for x in numeric_data] if max_value > 0 else numeric_data

def remove_duplicates(data):
    """Usuwa duplikaty z listy, zachowując ich oryginalną kolejność."""
    seen = set()
    return [x for x in data if not (x in seen or seen.add(x))]

def split_list(data, n):
    """Dzielenie listy na mniejsze podlisty o długości maksymalnej n."""
    return [data[i:i + n] for i in range(0, len(data), n)]

from my_awesome_lib.data_utils import remove_duplicates
print(remove_duplicates([1, 2, 2, 3, 4, 4]))  # Output: [1, 2, 3, 4]

