from typing import List
from numpy import number
from math import ceil

def format_bytes(bytes: float) -> str :
    KB = float(1024)
    MB = float(KB ** 2)
    GB = float(KB ** 3)
    TB = float(KB ** 4)

    if bytes < KB:
        return '{0} B'.format(bytes)
    elif KB <= bytes < MB :
        return '{0:.2f} KB'.format(bytes / KB)
    elif MB <= bytes < GB :
        return '{0:.2f} MB'.format(bytes / MB)
    elif GB <= bytes < TB :
        return '{0:.2f} GB'.format(bytes / GB)
    elif TB <= bytes :
        return '{0:.2f} TB'.format(bytes / TB)

def canvas(width: int, height: int) -> str :
    return '\n'.join(height * [width * ' '])

def border(text: str) -> str :
    return 

def pad_block(text: str, left: int, top: int, right: int, bottom: int) -> str :
    return top * '\n' + '\n'.join([left * " " + line + right * " " for line in text.split('\n')]) + bottom * '\n'

def as_table(size: List[int], data: List[List[any]]) -> str:
    output = ''
    for i, row in enumerate(data) :
        for (width, element) in zip(size, row) :
            output += (' ' + element + width * ' ')[0:width]
        output += ' \n'
        if (i == 0) :
            output += ' '.join([(width - 1) * '-' for width in size])
        output += '\n'

    return output

def progress_bar(width: int, portion: number) -> str :
    progress = ceil((width - 2) * portion)
    blank = width - progress - 2
    return '[' + progress * 'O' + blank * '-' + ']'