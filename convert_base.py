import string
from itertools import chain

char2ord: dict[str, int] = {
    char: digit for digit, char in enumerate(chain(string.digits, string.ascii_letters))
}
ord2char: dict[int, str] = {digit: char for char, digit in char2ord.items()}


def to_decimal(number: str, src_base: int) -> int:
    dec_num, power = 0, 1

    for digit in reversed(number):
        if char2ord[digit] >= src_base:
            raise ValueError(f"{digit} larger than the base")
        dec_num += char2ord[digit] * power
        power *= src_base

    return dec_num


def from_decimal(dec_num: int, base: int) -> str:
    result = ""

    while dec_num > 0:
        dec_num, remainder = divmod(dec_num, base)
        result += ord2char[remainder]

    return result[::-1]


def convert_base(num: str, src_base: int, dest_base: int) -> str:
    return from_decimal(to_decimal(num, src_base), dest_base)

