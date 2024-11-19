lexer grammar ExprLexer;

CAN_CONTROL: 'can control';
CAN_ORDER: 'can order';
INCLUDE: 'include';
NEXT_TO: 'next to';
COMMA: ',';
SEMI: ';';

INT: [0-9]+;
ID: [a-zA-Z_][a-zA-Z_0-9]*;
NEWLINE: '\r'? '\n';

WS: [ \t]+ -> skip;
