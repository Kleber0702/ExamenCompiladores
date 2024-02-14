import ply.lex as lex

class Lexer:
    tokens = [
        'DELIMITADOR',
        'OPERADOR',
        'PALABRA_RESERVADA',
        'ENTERO',
        'IDENTIFICADOR',
        'PUNTO',  # Token para el punto "."
    ]

    t_ignore = ' \t'
    contador_lineas = 1
    token_count = {}  # Diccionario para contar los tokens

    reserved = {
        'for': 'FOR',
        'do': 'DO',
        'public': 'PUBLIC',
        'static': 'STATIC',
        'const': 'CONST',
        'main': 'MAIN',
        'class': 'CLASS',
        'int': 'INT',  # Agregado int como palabra reservada
        'programa': 'PROGRAMA',  # Agregado 'programa' como palabra reservada
        'read':'READ',
        'end': 'END',
        'printf': 'PRINTF',
    }

    tokens += reserved.values()

    @staticmethod
    def t_DELIMITADOR(t):
        r'[{}();]'
        return t

    @staticmethod
    def t_OPERADOR(t):
        r'[-+*/=<>]'
        return t

    @staticmethod
    def t_ENTERO(t):
        r'-?\b\d+\b'
        return t

    @staticmethod
    def t_IDENTIFICADOR(t):
        r'\b[a-zA-Z]+\b'  # Identificadores: cualquier combinación de letras
        if t.value == 'suma':
            t.type = 'IDENTIFICADOR'  # Marcar 'suma' como un identificador
        else:
            t.type = 'PALABRA_RESERVADA' if t.value in Lexer.reserved else 'IDENTIFICADOR'
        # Contador de tokens
        Lexer.token_count.setdefault(t.type, 0)
        Lexer.token_count[t.type] += 1
        return t

    @staticmethod
    def t_PUNTO(t):
        r'\.'
        return t

    @staticmethod
    def t_PALABRA_RESERVADA(t):
        r'for|do|public|static|const|main|class|programa|read|printf|end'  # Agregado 'programa' como palabra reservada
        t.type = Lexer.reserved.get(t.value, 'PALABRA_RESERVADA')
        return t

    @staticmethod
    def t_newline(t):
        r'\n+'
        Lexer.contador_lineas += t.value.count('\n')
        t.lexer.lineno += t.value.count('\n')

    @staticmethod
    def t_eof(t):
        t.lexer.lineno += t.value.count('\n')
        return None

    @staticmethod
    def t_error(t):
        print(f"Error léxico: Carácter inesperado '{t.value[0]}' en la línea {Lexer.contador_lineas}")
        t.lexer.skip(1)

    @staticmethod
    def build():
        return lex.lex(module=Lexer())


lexer = Lexer.build()
