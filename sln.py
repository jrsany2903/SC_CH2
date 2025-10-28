g = {"__CANEXEC__": 0, "0":0}
stack = []
f = {"clear":lambda x: ((g.__setitem__(x[1][1], 0) if g["__CANEXEC__"] == len(stack) else None, (0,0, "__run__")))[1],
     "incr":lambda x: ((g.__setitem__(x[1][1], g[x[1][1]] + int(x[1][2]))) if len(x[1]) > 2 else (g.__setitem__(x[1][1], g[x[1][1]] + 1)) if g["__CANEXEC__"] == len(stack) else None, (0,0 , "__run__"))[1],   
     "decr":lambda x: ((g.__setitem__(x[1][1], g[x[1][1]] - int(x[1][2]))) if len(x[1]) > 2 else (g.__setitem__(x[1][1], g[x[1][1]] - 1)) if g["__CANEXEC__"] == len(stack) else None, (0,0 , "__run__"))[1],
     "while":lambda x: ((stack.insert(0, (x[1][1],x[0])) if g["__CANEXEC__"] == len(stack) and f["__ifeval__"](x[1][1:-1]) else None), (0,0, "__run__"), g.__setitem__("__CANEXEC__", g["__CANEXEC__"] + 1))[1],
     "end":lambda x: ((stack.pop(0)[1],x[0] + 1, "__run__") if g["__CANEXEC__"] == len(stack) and len(stack) > 0 else (0,0, "__run__"), g.__setitem__("__CANEXEC__", g["__CANEXEC__"] - 1))[0],
     "#": lambda x: (0,0, "__run__"), 
     "__ifeval__": lambda x: g[x[0]] != g[x[2]] if x[1] == "not" else g[x[0]] == g[x[2]],
     "if":lambda x:((stack.insert(0, (x[1][1],x[0])) if g["__CANEXEC__"] == len(stack) and f["__ifeval__"](x[1][1:-1])  else None), (0,0, "__run__"), g.__setitem__("__CANEXEC__", g["__CANEXEC__"] + 1))[1],
     "endif":lambda x: ((stack.pop(0),(0,0, "__run__"))[1] if g["__CANEXEC__"] == len(stack) and len(stack) > 0 else (0,0, "__run__"), g.__setitem__("__CANEXEC__", g["__CANEXEC__"] - 1))[0],
     "deffn": lambda x: (stack.insert(0, (x[1][1],x[0], "fn")) if g["__CANEXEC__"] == len(stack) else None, g.__setitem__("__CANEXEC__", g["__CANEXEC__"] + 2), (0,0,"__run__"))[2],
     "endfn": lambda x: ((stack[0][1] + 1,x[0], stack.pop(0)[0]), g.__setitem__("__CANEXEC__", g["__CANEXEC__"] - 2))[0],
     "copy": lambda x: ((0,0,"__run__"),g.__setitem__(x[1][1], g[x[1][2]]) if g["__CANEXEC__"] == len(stack) else None)[0],
     "del": lambda x: ((0,0,"__run__"),g.pop(x[1][1]) if g["__CANEXEC__"] == len(stack) else None)[0]}
#fn unfinished prevent execution in def
main = lambda c: map(lambda y: list(map(lambda m: list(main(m)) if y[2] == "__run__" else f.__setitem__(y[2], lambda t: ((0,0,"__run__"),list(main(m)))[0]), ["".join(list(map(lambda x: (" ".join(x) + ";") ,list(filter(lambda x: x != [''] ,map(lambda x: x.split(" "),map(lambda x: x.strip(), c.split(";")))) ) [y[0]:y[1]])))]  )), map(lambda x: (print(g, stack, x),f[x[1][0]](x))[1], enumerate(filter(lambda x: x != [''] ,  map(lambda x: x.split(" "), map(lambda x: x.strip(), c.split(";")))  ))))
#----------------------------------------------------------

'''
DOCUMENTATION

clear var;
sets global variable "var" to 0

incr var [a];
increases global variable "var" by 1 or by a if provided

decr var [a];
decreases global variable "var" by 1 or by a if provided

while expr do;
starts a while loop that loops if expr returns true

expr
expressions take the form of (var1 not var2) or (var1 is var2)
"0" is also a defined global literal so you can do var1 not 0

end;
this defines the end of a while loop

if expr then;
defines an if block that only runs if expr returns true

endif;
ends an if block

deffn fname;
begins a function definition for a function called fname

endfn;
defines the end of a function definition

copy var1 var2;
copies the value of var2 into var1

del var;
deletes a variable

'''

#Source bb code from file
filename = str(input("input filename >>>"))

with open("SC_CH2/"+filename, "r") as file:
    s = str(file.read())

g = {"__CANEXEC__": 0, "0":0}
stack = []
list(main(s))
print("Final result:\n", g)
