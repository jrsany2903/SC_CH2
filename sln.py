a = "clear x; clear y; incr x; incr x; incr x; decr x; incr y; incr y; incr y; incr y; incr y; clear z; while y not 0 do; incr z; decr y; end;"
b = "clear x; clear y; incr x; incr x; incr x; decr x; incr y; incr y; incr y; incr y; incr y; clear z;"
g = {}
stack = []
f = {"clear":(lambda x: g.__setitem__(x, 0)),
     "incr":(lambda x: g.__setitem__(x, g.get(x) + 1)),
     "decr":(lambda x: g.__setitem__(x, g.get(x) - 1)),
     "while":(lambda x: stack.insert(x,0))}
main = lambda b:list(map(lambda x: f[x[0]](x[1]),filter(lambda x: x != [''] ,map(lambda x: x.split(" "),map(lambda x: x.strip(), b.split(";"))))))
print(g)

###notes to finish, enumerate and pass index into f as parameter, save index on stack, recursivly call main on added commands
