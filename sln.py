a = "clear x; clear y; incr x; incr x; incr x; decr x; incr y; incr y; incr y; incr y; incr y; clear z; while y not 0 do; incr z; decr y; end 0;"#extra 0 on end to match format
b = "clear x; clear y; incr x; incr x; incr x; decr x; incr y; incr y; incr y; incr y; incr y; clear z;"
g = {}
stack = []
f = {"clear":lambda x,i: ((g.__setitem__(x, 0), (0,0))[1]),
     "incr":lambda x,i: ((g.__setitem__(x, g.get(x) + 1)), (0,0))[1],   
     "decr":lambda x,i: ((g.__setitem__(x, g.get(x) - 1)), (0,0))[1],
     "while":lambda x,i: ((stack.insert(0, (x,i)) if g.get(x) != 0 else None), (0,0), print(stack))[1],
     "end":lambda x,i: (print(stack, i, "ss"),(stack.pop(0)[1],i + 1))[1]}
#main = lambda b:list(map(lambda x: f[x[1][0]](x[1][1], x[0]),enumerate(filter(lambda x: x != [''] ,map(lambda x: x.split(" "),map(lambda x: x.strip(), b.split(";")))))))
#
#test = lambda c: list(map(lambda x: (f[x[1][0]](x[1][1], x[0]), print(x[1][0]))[0], enumerate(filter(lambda x: x != [''] ,map(lambda x: x.split(" "),map(lambda x: x.strip(), c.split(";")))))))

#test(a)

main = lambda c: map(lambda y: list(map(lambda m: (print(m, "safas"),main(m))[0], list(map(lambda x: (" ".join(x) + ";") ,list(filter(lambda x: x != [''] ,map(lambda x: x.split(" "),map(lambda x: x.strip(), c.split(";")))) ) [y[0]:y[1]]))))       ,list(map(lambda x: (print(stack, x, "sds"),f[x[1][0]](x[1][1], x[0]))[1], enumerate(filter(lambda x: x != [''] ,map(lambda x: x.split(" "),map(lambda x: x.strip(), c.split(";"))))))))
#### Almost works, however the m passed in the lambda funtion here is individual lines not full loop block


list(main(a))    
#print(*main(a))
#main = lambda b:list(map(lambda x: f[x[0]](x[1]),filter(lambda x: x != [''] ,map(lambda x: x.split(" "),map(lambda x: x.strip(), b.split(";"))))))
print(stack)
print(g)

###notes to finish, enumerate and pass index into f as parameter, save index on stack, recursivly call main on added commands
