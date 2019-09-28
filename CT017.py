ns = {'global': {'Type': 'NS', 'Name': 'global', 'Parent': None}}

def find(name, d):
    if d.get(name) != None:
        return d.get(name)
    for k, v in d.items():
        if k in ['Type', 'Name', 'Parent']:
            continue
        d1 = find(name, v)
        if d1 != None:
            return d1
    return None


# cmds = [input().split() for i in range(int(input()))]

cmds = [['add', 'global', 'a'],
        ['create', 'foo', 'global'],
        ['add', 'foo', 'b'],
        ['get', 'foo', 'a'],
        ['get', 'foo', 'c'],
        ['create', 'bar', 'foo'],
        ['add', 'bar', 'a'],
        ['get', 'bar', 'a'], ['get', 'bar', 'b']]


for cmd, arg1, arg2 in cmds:
    if cmd == 'create':
        dx = find(arg2, ns)
        dx[arg1] = {'Type': 'NS', 'Name': arg1, 'Parent': arg2}

    elif cmd == 'add':
        dx = find(arg1, ns)
        dx[arg2] = {'Type': 'var', 'Name': arg2, 'Parent': arg1}

    elif cmd == 'get':
        nstoFind = find(arg1, ns)
        var = arg2

        if nstoFind.get(var) != None:
            print(arg1)
        else:
            while nstoFind['Parent'] != None:
                nstoFind = find(nstoFind['Parent'], ns)
                if nstoFind.get(var) != None:
                    print(nstoFind['Name'])
                    break
            else:
                print('None')

'''
create <namespace> <parent> –  создать новое пространство имен с именем 
        <namespace> внутри пространства <parent>
add <namespace> <var> – добавить в пространство <namespace> переменную <var>
get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> 
    при запросе из пространства <namespace>, или None, 
    если такого пространства не существует'''