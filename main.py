import enum



def is_label(token: str) -> bool:
    if len(token) <= 0:
        return False
    if token[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        return True
    return False

opcodes: dict[str, int] = {
    'mov':      0,
    'tnl':      1,
    'tnr':      2,
    'inf':      3,
    'skp':      4,
    'end':      5,
    'jmp':      6,
    'cempty':   7,
    'cwall':    9,
    'cfriend':  11,
    'cenemy':   13,
    'crand':    15,
    'ctrue':    16,
}

def print_source(lines: list[str], description=''):
    print(description)
    for line in lines:
        print(f'\t> {line}')

def print_jump_table(jump_table: dict[str, int], description=''):
    print(description)
    for label in jump_table:
        print(f'\t| {label}\t{jump_table[label]}')

def print_program(opcodes: list[int], description=''):
    print(description)
    width: int = 0
    for opcode in opcodes:
        if width == 0:
            print('\t', end='')
        
        print(f'{opcode:0>2} ', end='')

        width += 1
        if width >= 4:
            width = 0
            print('')
    print('')

def compile(source_code: str) -> list[int]:
    program: list[int] = []

    lines: list[str] = source_code.splitlines()

    jump_table: dict[str, int] = {}
    
    print_source(lines, 'Original source code:')

    # Remove comments:
    temp: list[str] = []
    for line in lines:
        idx_comment: int = line.find(';')
        if idx_comment != -1:
            temp.append(line[:idx_comment])
        else:
            temp.append(line)
    lines = temp
    print_source(lines, 'Comments removed:')

    # Remove empty lines:
    temp: list[str] = []
    for line in lines:
        if line.strip() != '':
            temp.append(line)
    lines = temp
    print_source(lines, 'Empty lines removed:')

    # Remove label definitions and build jump table:
    temp: list[str] = []
    jump_pos: int = 0
    for line in lines:
        if line[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            label: str = line.split()[0]
            assert label not in jump_table
            jump_table[label] = jump_pos
            line = line.removeprefix(label)
        jump_pos += len(line.split())
        line = line.lstrip()
        if line != '':
            temp.append(line)
    lines = temp
    print_source(lines, 'Label definitions removed:')
    print_jump_table(jump_table, 'Jump table:')

    # Parse tokens:
    for line in lines:
        tokens: list[str] = line.split()
        operation: str = tokens[0]
        program.append(opcodes[operation])
        
        if operation in ['jmp', 'cempty', 'cwall', 'cfriend', 'cenemy', 'crand', 'ctrue']:
            operand: str = tokens[1]
            program.append(jump_table[operand])

    program.append(opcodes['end'])
    program.insert(0, len(program))

    print_program(program, 'Final program:')

    return program

def main():

    source_filepath = 'test/sample.bsm'
    destination_filepath = 'test/sample.bo'

    # Load source file:
    with open(source_filepath) as f:
        text = f.read()

    program = compile(text)

    with open(destination_filepath, 'w') as f:
        while len(program) > 0:
            opcode = program.pop(0)
            f.write(f'{opcode}')

            if len(program) > 0:
                f.write('\n')

if __name__ == '__main__':
    main()