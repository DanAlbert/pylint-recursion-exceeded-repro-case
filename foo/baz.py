import foo.bar


def baz():
    qux = foo.bar.bar()
    return [qux]


quux = baz() + []
quux.append('')
