# bugsworld-asm

Custom assembly-ish language compiler for the bytecode used by the OSU CSE BugsWorld project.

The project description can be found [here](http://web.cse.ohio-state.edu/software/2231/web-sw2/readings/bugs-world.html).

## Background

BugsWorld is a project in the OSU CSE curriculum. Part of it includes building a compiler in java for a simple programming language. The compiler outputs bytecode to be interpreted by an interpreter that we also build. By compiling several test programs, I reverse-engineered the bytecode structure without looking at any future assignment descriptions.

`bugsworld-asm` is a compiler for my own custom assembly-like language that targets the same bytecode format used in BugsWorld. Compiler-time optimization is out of scope for this project.

## Bytecode reference

I determined each bytecode's meaning by sending various test programs to the original BugsWorld compiler and comparing them with the resulting opcode output.

| bytecode | meaning        |
|----------|----------------|
| 0        | move           |
| 1        | turnleft       |
| 2        | turnright      |
| 3        | infect         |
| 4        | skip           |
| 5        | end program    |
| 6        | jump           |
| 7        | next-is-empty  |
| 8        |                |
| 9        | next-is-wall   |
| 10       |                |
| 11       | next-is-friend |
| 12       |                |
| 13       | next-is-enemy  |
| 14       |                |
| 15       | random         |
| 16       | true           |

Jump operations use the numeric value of the next bytecode as the target address.
Conditions like `next-is-empty` and `random` function like a jump, but will only perform the jump if the condition is false.

## Language reference

1. Programs are a sequence of lines. Each line can contain up to 4 fields: a label, an operation, an operand, and a comment.
2. Comments begin with a semicolon. Anything after the first `;` in a line will be discarded.
3. Empty lines are discarded.
4. If a line begins with whitespace, it is assumed that there is no label.
5. Some operations expect an operand, some don't.

| operation         | corresponding function                                 |
|-------------------|--------------------------------------------------------|
| `mov`             | move                                                   |
| `tnl`             | turn left                                              |
| `tnr`             | turn right                                             |
| `inf`             | infect                                                 |
| `skp`             | skip turn                                              |
| `jmp`             | jump to label specified by operand                     |
| `cempty <label>`  | jump to label if not facing an empty square            |
| `cwall <label>`   | jump to label if not facing a wall                     |
| `cfriend <label>` | jump to label if not facing an allied unit             |
| `cenemy <label>`  | jump to label if not facing an enemy                   |
| `crand <label>`   | jump to label if some (unknown) random condition fails |
| `ctrue <label>`   | does nothing                                           |
