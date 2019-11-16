import logging

from rita import engine
from rita.parser import RitaParser

logger = logging.getLogger(__name__)


def compile_string(raw, compile_fn=None):
    parser = RitaParser()
    parser.build()
    root = parser.parse(raw)
    logger.debug(root)
    if compile_fn:
        compile_tree = compile_fn
    else:
        compile_tree = engine.get_default()
    return list(compile_tree(root))


def compile(fname, compile_fn=None):
    with open(fname, "r") as f:
        raw = f.read()

    return compile_string(raw, compile_fn)
