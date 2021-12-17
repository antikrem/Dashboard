from typing import List


def canvas(width: int, height: int) -> str:
    return '\n'.join(height * [width * ' '])

def border(text: str) -> str :
    return 

def pad_block(text: str, left: int, top: int, right: int, bottom: int) :
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
