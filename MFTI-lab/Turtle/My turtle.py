import turtle as t
import figures as f

t.speed('fastest')
t.penup()
t.left(155)
t.forward(400)
t.pendown()
t.right(155)

f_list1 = [f.swiss, f.scale(f.rotor(f.swiss, 30), 1.5), f.kv2, f.treugolnik]
f_list2 = [f.kv2, f.rotor(f.kvadrat, 45)]
f_list3 = [f.kvadrat, f.treugolnik]
u_1 = [f.uzor1, f.uzor2]
u_2 = [f.uzor3, f.uzor4]
u_3 = [f.uzor4, f.uzor4]
for i in range(2):
    f.line_of_uzor(u_3, 500, 40, [f.kvadrat, f.kvadrat])
    t.right(90)
    f.line_of_uzor(u_2, 300, 40, [f.kvadrat, f.kvadrat])
    t.right(90)


'''
f.line_of_figs_list(f_list2, 600, 7, zazor=50, krai=40)
t.right(90)
f.line_of_figs_list(f_list3, 400, 5, zazor=50, krai=40)
t.right(90)
f.line_of_figs_list(f_list2, 600, 7, zazor=50, krai=40)
t.right(90)
f.line_of_figs_list(f_list3, 400, 5, zazor=50, krai=40)
t.right(90)
'''
i = input()
