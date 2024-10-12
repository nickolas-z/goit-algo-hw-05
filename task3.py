import timeit
import random
from typing import List, Tuple

def boyer_moore_search(text: str, pattern: str) -> List[int]:
    """ Boyer-Moore search algorithm """
    def bad_char_heuristic(pattern: str) -> List[int]:
        """ Bad character heuristic """
        bad_char = [-1] * 65536
        for i in range(len(pattern)):
            bad_char[ord(pattern[i])] = i
        return bad_char

    def good_suffix_heuristic(pattern: str) -> List[int]:
        """ Good suffix heuristic """
        m = len(pattern)
        good_suffix = [0] * (m + 1)
        border_pos = [-1] * (m + 1)
        i, j = m, m + 1
        border_pos[i] = j
        while i > 0:
            while j <= m and pattern[i - 1] != pattern[j - 1]:
                if good_suffix[j] == 0:
                    good_suffix[j] = j - i
                j = border_pos[j]
            i -= 1
            j -= 1
            border_pos[i] = j
        j = border_pos[0]
        for i in range(m + 1):
            if good_suffix[i] == 0:
                good_suffix[i] = j
            if i == j:
                j = border_pos[j]
        return good_suffix

    m, n = len(pattern), len(text)
    bad_char = bad_char_heuristic(pattern)
    good_suffix = good_suffix_heuristic(pattern)
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            yield s
            s += good_suffix[0]
        else:
            s += max(1, j - bad_char[ord(text[s + j])], good_suffix[j + 1])

def kmp_search(text: str, pattern: str) -> List[int]:
    """ Knuth-Morris-Pratt search algorithm """
    def compute_lps(pattern: str) -> List[int]:
        lps = [0] * len(pattern)
        length, i = 0, 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = compute_lps(pattern)
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            yield i - j
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

def rabin_karp_search(text: str, pattern: str) -> List[int]:
    """ Rabin-Karp search algorithm """
    prime, base = 101, 256
    
    def calculate_hash(s: str) -> int:
        return sum(ord(s[i]) * pow(base, len(s)-1-i, prime) for i in range(len(s))) % prime

    m, n = len(pattern), len(text)
    pattern_hash = calculate_hash(pattern)
    text_hash = calculate_hash(text[:m])
    
    for i in range(n - m + 1):
        if pattern_hash == text_hash and text[i:i+m] == pattern:
            yield i
        if i < n - m:
            text_hash = (text_hash - ord(text[i]) * pow(base, m-1, prime)) % prime
            text_hash = (text_hash * base + ord(text[i+m])) % prime

def read_file(file_path: str) -> str:
    """ Read file with utf-8 encoding """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def read_file_latin1(file_path: str) -> str:
    """ Read file with latin1 encoding """
    with open(file_path, 'r', encoding='latin1') as file:
        return file.read()
    
def measure_time(func, *args) -> float:
    """ Measure the execution time of a function """
    return timeit.timeit(lambda: list(func(*args)), number=1)

def run_tests(text: str, patterns: List[str]) -> List[Tuple[str, float, float]]:
    """ Run tests for all algorithms """
    algorithms = [
        ("Boyer-Moore", boyer_moore_search),
        ("KMP", kmp_search),
        ("Rabin-Karp", rabin_karp_search)
    ]
    
    results = []
    for name, func in algorithms:
        time_existing = measure_time(func, text, patterns[0])
        time_non_existing = measure_time(func, text, patterns[1])
        results.append((name, time_existing, time_non_existing))
    
    return results

def main():
    """ Main function """

    file_paths = ['data/article_1.txt', 'data/article_2.txt']
    
    for file_path in file_paths:
        text = read_file(file_path)
        
        # Selecting substrings for search
        existing_pattern = "Література"
        non_existing_pattern = "Квадробери"
        
        patterns = [existing_pattern, non_existing_pattern]
        
        print(f"\nРезультати для файлу: {file_path}")
        print(f"Довжина тексту: {len(text)} символів")
        print(f"Підрядок, що існує: '{existing_pattern}'")
        print(f"Підрядок, що не існує: '{non_existing_pattern}'")
        print("\nАлгоритм     | Час (існуючий)  | Час (неіснуючий)")
        print("—" * 50)
        
        results = run_tests(text, patterns)
        
        for name, time_existing, time_non_existing in results:
            print(f"{name:<12} | {time_existing:.6f} s      | {time_non_existing:.6f} s")
        
        fastest = min(results, key=lambda x: x[1] + x[2])
        print(f"\nНайшвидший алгоритм для цього тексту: {fastest[0]}")

if __name__ == "__main__":
    main()