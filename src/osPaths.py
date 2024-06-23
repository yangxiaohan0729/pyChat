import os
import os.path


def check():
    print("ospaths.py is linked")


def rootDir():  # pragma: no cover
    # return os.path.abspath(os.path.dirname(__file__))
    return os.getcwd()


def getFile(filename):  # pragma: no cover
    try:
        src = os.path.join(rootDir() + filename)
        # Figure out how flask returns static files
        # Tried:
        # - render_template
        # - send_file
        # This should not be so non-obvious
        return open(src).read()
    except IOError as exc:
        return str(exc)
