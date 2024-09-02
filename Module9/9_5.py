class StepValueError(ValueError):
    pass
class Iterator:
    def __init__(self, start, stop, step=1):
        try:
            if step == 0:
                raise StepValueError("Шаг не может быть равен 0")
            self.start = start
            self.stop = stop
            self.step = step
            self.pointer = self.start
            self.instance()
        except StepValueError as exc:
            print(exc)

    def __iter__(self):
       self.pointer = self.start
       return self

    def __next__(self):
        self.pointer += self.step
        if self.step > 0 and self.pointer > self.stop or self.step < 0 and self.pointer < self.stop:
            raise StepValueError
        return self.pointer

    def instance(self):
        try:
            for i in self:
                print(i, end=' ')
        except StepValueError:
            print()

iter1 = Iterator(100, 200, 0)
iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)
