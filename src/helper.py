import sys


def args_or_default(default: str) -> str:
    if len(sys.argv) > 1:
        return sys.argv[1]
    return default
