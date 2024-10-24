parser grammar ExprParser;
options { tokenVocab=ExprLexer; }

program: rules EOF;

rules: statement*;

statement: expression SEMI NEWLINE;

expression
    : ID CAN_CONTROL listing
    | ID CAN_ORDER ID listing
    | ID INCLUDE listing
    | ID NEXT_TO ID
    ;

listing: ID (COMMA ID)* ;
