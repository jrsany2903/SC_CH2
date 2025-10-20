g = {"__CANEXEC__": 0}
stack = []
f = {"clear":lambda x,i: ((g.__setitem__(x, 0) if g["__CANEXEC__"] == len(stack) else None, (0,0))[1]),
     "incr":lambda x,i: ((g.__setitem__(x, g.get(x) + 1)) if g["__CANEXEC__"] == len(stack) else None, (0,0))[1],   
     "decr":lambda x,i: ((g.__setitem__(x, g.get(x) - 1)) if g["__CANEXEC__"] == len(stack) else None, (0,0))[1],
     "while":lambda x,i: ((stack.insert(0, (x,i)) if g.get(x) != 0 and g["__CANEXEC__"] == len(stack) else None), (0,0), g.__setitem__("__CANEXEC__", g["__CANEXEC__"] + 1))[1],
     "end":lambda x,i: ((stack.pop(0)[1],i + 1) if g["__CANEXEC__"] == len(stack) and len(stack) > 0 else (0,0), g.__setitem__("__CANEXEC__", g["__CANEXEC__"] - 1))[0]}
main = lambda c: map(lambda y: list(map(lambda m: list(main(m)), ["".join(list(map(lambda x: (" ".join(x) + ";") ,list(filter(lambda x: x != [''] ,map(lambda x: x.split(" "),map(lambda x: x.strip(), c.split(";")))) ) [y[0]:y[1]])))]  )), map(lambda x: (print(g, stack, x),f[x[1][0]](x[1][1], x[0]))[1], enumerate(filter(lambda x: x != [''] ,  map(lambda x: x.split(" "), map(lambda x: x.strip(), c.split(";")))  ))))
#----------------------------------------------------------





#Source bb code from file
filename = str(input("input filename >>>"))

with open("SC_CH2/"+filename, "r") as file:
    s = str(file.read())

g = {"__CANEXEC__": 0}
stack = []
list(main(s))
print("Final result:\n", g)