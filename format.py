from typing import List


def canvas(width: int, height: int) -> str:
    return '\n'.join(height * [width * ' '])

def border(text: str) -> str :
    return 

def pad_block(text: str, left: int, top: int, right: int, bottom: int) :
    return top * '\n' + '\n'.join([left * " " + line + right * " " for line in text.split('\n')]) + bottom * '\n'

def as_table(size: List[int], data: List[List[any]]) -> str:
    output = ''
    for row in data :
        for width in size :
            output += '+' + width * '-'
        output += '+\n'

        for (width, element) in zip(size, row) :
            output += '|'
            output += (element + width * ' ')[0:width]
        output += '|\n'

    for width in size :
        output += '+' + width * '-'
    output += '+'
    return output
