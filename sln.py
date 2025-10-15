a = "clear x; clear y; incr x; incr x; incr x; decr x; incr y; incr y; incr y; incr y; incr y; clear z; while y not 0 do; incr z; decr y; end 0;"#extra 0 on end to match format
b = "clear x; clear y; incr x; incr x; incr x; decr x; incr y; incr y; incr y; incr y; incr y; clear z;"
nestedtest = "clear x; clear y; incr x; incr x; incr x; decr x; incr y; incr y; incr y; incr y; incr y; clear z; while y not 0 do; incr z; decr y; while x not 0 do; decr x; incr y; end 0; incr z; end 0;"
g = {"__CANEXEC__": True}
stack = []
f = {"clear":lambda x,i: ((g.__setitem__(x, 0) if g["__CANEXEC__"] else None, (0,0))[1]),
     "incr":lambda x,i: ((g.__setitem__(x, g.get(x) + 1)) if g["__CANEXEC__"] else None, (0,0))[1],   
     "decr":lambda x,i: ((g.__setitem__(x, g.get(x) - 1)) if g["__CANEXEC__"] else None, (0,0))[1],
     "while":lambda x,i: ((stack.insert(0, (x,i)) if g.get(x) != 0 else g.__setitem__("__CANEXEC__", False)), (0,0))[1],
     "end":lambda x,i: ((stack.pop(0)[1],i + 1) if g["__CANEXEC__"] and len(stack) > 0 else (0,0), g.__setitem__("__CANEXEC__", True))[0]}

main = lambda c: map(lambda y: list(map(lambda m: list(main(m)), ["".join(list(map(lambda x: (" ".join(x) + ";") ,list(filter(lambda x: x != [''] ,map(lambda x: x.split(" "),map(lambda x: x.strip(), c.split(";")))) ) [y[0]:y[1]])))]  )), map(lambda x: (print(g, stack, x),f[x[1][0]](x[1][1], x[0]))[1], enumerate(filter(lambda x: x != [''] ,  map(lambda x: x.split(" "), map(lambda x: x.strip(), c.split(";")))  ))))
list(main(nestedtest))

print("Final result:\n", g)

#almost working, can exec needs to be a integer to count nested exec restrictions