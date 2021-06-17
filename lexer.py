from rply import LexerGenerator

lg = LexerGenerator()
lg.add('START', r'start')
lg.add('STOP',r'stop')
lg.add('WAIT', r'wait')
lg.add('NUMBER', r'\d+')
lg.add('SELECT', r'select')
lg.add('SEARCH', r'search')
lg.add('UNLOCKPW', r'unlockpw')
lg.add('WRITE', r'write')
lg.add('LOCK', r'lock')
lg.add("WORD", r"[a-z]+")
lg.add("EQUALS", r"=")
lg.add('STRING', r'"[^("|\n)]*"')
lg.add('OPEN_PAREN', r'\(')
lg.add('CLOSE_PAREN', r'\)')
lg.ignore(r"\s+")  # Ignore whitespace 
lg.ignore(r"#.*\n")  # Ignore comments

lexer = lg.build()

#am start -a android.intent.action.VIEW -d facebook://facebook.com/inbox
#dumpsys package | grep -Eo "^[[:space:]]+[0-9a-f]+[[:space:]]+com.twitter.android/[^[:space:]]+" | grep -oE "[^[:space:]]+$"

