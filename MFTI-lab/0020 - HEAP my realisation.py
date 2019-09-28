class My_heap():
    # выделю 1000, добавлять по 1000/
    # нулевую не использую для мин-кучи изменить на 'min'
    def __init__(self, limit=1000, additions=1000, type='max'):
        self.heap = [0] * (limit + 1)
        self.limit = limit
        self.nextIdx = 1
        self.addition = additions
        if type == 'max':
            self.oper = int.__lt__
        elif type == 'min':
            self.oper = int.__gt__

    def insert(self, item: int):
        self.heap[self.nextIdx] = item
        self.nextIdx += 1
        if self.nextIdx > self.limit:
            self.heap = self.heap + [0] * self.addition
            self.limit += self.addition
        self._pass_up(self.nextIdx - 1)

    def extract(self) -> int:
        result = self.heap[1]
        self.heap[1] = self.heap[self.nextIdx - 1]
        self.nextIdx -= 1
        self._pass_dn(1)
        return result

    def _pass_up(self, idx):
        prnt = self._parent(idx)
        if prnt and self.oper(self.heap[prnt], self.heap[idx]):
            self.heap[prnt],  self.heap[idx] = self.heap[idx], self.heap[prnt]
            self._pass_up(prnt)

    def _pass_dn(self, idx):
        chld = self._best_child(idx)
        if not chld:
            return
        if self.oper(self.heap[idx], self.heap[chld]):
            self.heap[idx], self.heap[chld] = \
                self.heap[chld], self.heap[idx]
            self._pass_dn(chld)

    def _best_child(self, idx):
        if 2 * idx + 1 > self.nextIdx - 1:
            if 2 * idx <= self.nextIdx - 1:
                # только один потомок
                return 2 * idx
            else:   # ни одного
                return None
        elif self.oper(self.heap[2*idx], self.heap[2*idx+1]):
            return 2 * idx + 1
        else:
            return 2 * idx

    def _parent(selfs, idx):
        return idx // 2

n = int(input())
heap = My_heap()
for i in range(n):
    op = input()
    if op[:6] == 'Insert':
        heap.insert(int(op[7:]))
    elif op == 'ExtractMax':
        print(heap.extract())

'''
8
Insert 200
Insert 10
Insert 5
Insert 500
ExtractMax
ExtractMax
ExtractMax
ExtractMax

'''