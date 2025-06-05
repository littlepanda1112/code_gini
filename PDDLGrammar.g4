grammar PDDLGrammar;

/*
 * Parser Rules
 */
// Domain description
domain: LB DEFINE LB DOMAIN NAME RB
           objectDefine
           //typeDefine
           terconditionDefine
           constraintDefine
           actionDefine*
        RB;
objectDefine: LB COLON OBJS listVariable RB;
//numericDefine: LB COLON NUMS numericSymbol+ RB;
//numericSymbol: NAME;
//typeDefine: LB COLON TYPE typeName RB;
terconditionDefine: LB COLON TERCONDITION emptyOrPreGD RB;
constraintDefine:LB COLON CONSTRAINT emptyOrPreGD RB;
//predicateDefine: LB COLON PREDICATE atomFormSkeleton+ RB;
//atomFormSkeleton: LB predicate listVariable oneofDefine? RB;
predicate: NAME;
//typeDeclaration: NAME | LB NAME constTerm constTerm RB;
types: OBJECT | AGENT | NAME;
//interval: LSB constTerm constTerm RSB;
actionDefine: LB COLON ACTION actionSymbol
                (COLON PARAMETER LB listVariable RB)?
                (COLON PRECONDITION emptyOrPreGD)?
                (COLON EFFECT emptyOrEffect)?
              RB;
actionSymbol: NAME;
typeName:NORMAL|MISERE;

emptyOrPreGD: gd # isGd
            | LB RB  # preGDBracket
            ;
emptyOrEffect: effect # isEffect
            | LB RB  # effectBracket
            ;

listName: NAME* | NAME+ MINUS types listName;
listVariable: VAR* | VAR+ MINUS types listVariable;
oneofDefine: ONEOF VAR+;

gd: termAtomForm                        # atom
  | LB AND gd+ RB                       # and
  | LB OR gd+ RB                        # or
  | LB NOT gd RB                        # not
  | LB IMPLIES gd gd RB                   # imply
  | LB EXISTS LB listVariable RB gd RB  # exists
  | LB FORALL LB listVariable RB gd RB  # forall
  ;

termAtomForm: LB predicate term* RB     # predicateA
            | LB EQ term term RB        # equal
            | LB NEQ term term RB       # nEqual
            | LB LT term term RB        # lessThan
            | LB LEQ term term RB       # lessThanEqual
            | LB GT term term RB        # greaterThan
            | LB GEQ term term RB       # greaterThanEqual
            | LB MODTEST term term term RB #modTest
            ;
termLiteral: termAtomForm | LB NOT termAtomForm RB;

constTerm: NAME
         | INTEGER
//         | LB MINUS constTerm RB
//         | LB MINUS constTerm constTerm RB
//         | LB PLUS constTerm constTerm RB
         ;

term: NAME                   # name
    | VAR                    # var
    | INTEGER                # integer
    | LB term RB             #bracketTerm
    | LB MINUS term RB       # minusTerm
    | LB MINUS term term RB  # minusTermTerm
    | LB MOD term term RB  # modTermTerm
    | LB term MINUS term RB    # termMinusTerm
    | LB term MOD term RB    # termModTerm
    | LB PLUS term term RB   # plusTermTerm
    | LB MULT term term RB   #multTermTerm
     ;

effect: LB AND cEffect+ RB  # andCEffect
      | cEffect             # ceffect
      ;

cEffect: LB WHEN gd condEffect RB # whenCondEffect
       | pEffect                  # cEffectPEffect
       ;

condEffect: LB AND pEffect+ RB  # andPEffect
          | pEffect             # condEffectPEffect
          ;

pEffect: LB assignop VAR term RB;

assignop: INC               # inc
        | DEC               # dec
        | ASSIGN            # assign
        ;


        
problemName: NAME;
domainName: NAME;
agentDefine: LB COLON AGENT NAME+ RB;
objectDeclaration: LB COLON OBJS listName RB;
//numericSetting: LB COLON NUMS (LB numericSymbol INTEGER RB)+
//              RB;



init: LB COLON INIT constTermAtomForm* RB;
/*constTermGd: constTermAtomForm
           | constTermLiteral
           | LB AND constTermGd+ RB
           | LB OR constTermGd+ RB
           | LB NOT constTermGd RB
           | LB IMPLY constTermGd constTermGd RB
           | LB EXISTS LB listVariable RB gd RB
           | LB FORALL LB listVariable RB gd RB;*/

constTermAtomForm: LB predicate constTerm* RB
                 | LB EQ constTerm constTerm RB
                 | LB LT constTerm constTerm RB
                 | LB LEQ constTerm constTerm RB
                 | LB GT constTerm constTerm RB
                 | LB GEQ constTerm constTerm RB
                 | LB MODTEST constTerm constTerm constTerm RB;
/*constTermLiteral: constTermAtomForm | LB NOT constTermAtomForm RB;*/

/*
 * Lexer Rules
 */

// Keywords
DOMAIN: 'domain';
PROBLEM: 'problem';
DEFINE: 'define';
AGENTID: 'agentid';
CONST: 'constants';
TYPE: 'type';
PREDICATE: 'predicates';
ACTION: 'action';
EVENT: 'event';
EVENTS: 'events';
PLDEGREE: 'pldegree';
EVENTMODEL: 'eventmodel';
PARAMETER: 'parameters';
TERCONDITION: 'tercondition';
PRECONDITION: 'precondition';
CONSTRAINT:'constraint';
RESPONSE: 'response';
OBSERVATION: 'observation';
MIN: 'min';
MAX: 'max';
NUMS: 'numbers';
NORMAL:'normal';
MISERE: 'misere';
EFFECT: 'effect';
OBJECT: 'object';
INC: 'increase';
DEC: 'decrease';
ASSIGN: 'assign';
AGENT: 'agent';
EITHER: 'either';

OBJS: 'objects';

INIT: 'init';
GOAL: 'goal';

// Common used in domain and problem
LB: '(';
RB: ')';
LSB: '[';
RSB: ']';
COLON: ':';
QM: '?';
POINT: '.';
UL: '_';
MINUS: '-';
PLUS: '+';
MULT: '*';
DIV: '/';
MOD: '%';
MODTEST:'%=';
EQ: '=';
NEQ: '!=';
LT: '<';
LEQ: '<=';
GT: '>';
GEQ: '>=';
AND: 'and';
OR: 'or';
NOT: 'not';
ONEOF: 'oneof';
IMPLIES: 'Implies';
FORALL: 'forall';
EXISTS: 'exists';
WHEN: 'when';

NAME: LETTER CHAR*;
INTEGER: DIGIT+;


fragment LETTER: [a-zA-Z];
fragment DIGIT: [0-9];
fragment CHAR: LETTER | DIGIT | MINUS | PLUS | MOD | UL | MULT | LB | RB;
fragment BRACKET: LB | RB;


//NUMBER: 
//DECIMAL: POINT DIGIT+;
VAR: QM NAME;
FUNSYM : NAME;

WS: [ \t\r\n]+ -> skip;
