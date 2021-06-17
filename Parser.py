from rply import ParserGenerator
from boxes import (
    StatementBox, StatementsBox, IntBox, ExpressionBox, ExpressionSBox, MainBox, ActionBox, WordBox, StringBox
)

pg = ParserGenerator(["START","STOP","LOCK","WRITE","SEARCH",
                    "UNLOCKPW","WORD","EQUALS","WAIT","NUMBER","STRING"])


@pg.production("main : statements expressions")
def main(p):
    return MainBox(p[0],p[1])

@pg.production("statements : statements statement")
def expr_statements(p):
    return StatementsBox(p[0], p[1])
@pg.production("statements : ")
def expr_empty_statements(p):
    return StatementsBox()
@pg.production("statement : word EQUALS number")
#@pg.production("statement : word EQUALS string")
def statement_op(p):
    return StatementBox(p[0], p[2])

@pg.production("expressions : expressions expression")
def expr_expressions(p):
    return ExpressionSBox(p[0], p[1])

@pg.production("expressions : ")
def expr_empty_expressions(p):
    return ExpressionSBox()

@pg.production("expression : action word")
@pg.production("expression : action number")
@pg.production("expression : action string")
def expression_op(p):
    return ExpressionBox(p[0], p[1])



@pg.production("action : WRITE")
@pg.production("action : UNLOCKPW")
@pg.production("action : LOCK")
@pg.production("action : WAIT")
@pg.production("action : SEARCH")
@pg.production("action : START")
@pg.production("action : STOP")
def action(p):
    return ActionBox(p[0])


@pg.production("word : WORD")
def word(p):
    return WordBox(p[0])
@pg.production("string : STRING")
def string(p):
    return StringBox(p[0])
@pg.production("number : NUMBER")
def number(p):
    return IntBox(p[0])

parser = pg.build()