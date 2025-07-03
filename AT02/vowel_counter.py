def count_vowels(s: str) -> int:
    """
    Считает количество гласных букв в строке (русские и английские, регистр не важен).
    """
    vowels = set('aeiouyаеёиоуыэюяAEIOUYАЕЁИОУЫЭЮЯ')
    return sum(1 for char in s if char in vowels) 