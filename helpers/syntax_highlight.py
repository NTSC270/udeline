from pygments.formatters import TerminalFormatter
from pygments import highlight, lexers
lexer = lexers.get_lexer_by_name("python")

formatter = TerminalFormatter(full=True, style='material')

def highlighting(code):

    output = highlight(code, lexer, formatter)
    return output
