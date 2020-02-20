
class CircularQueue:
    def __init__(self, *args):
        self.stored_list = []
        self.current_position = 0
        for arg in args:
            self.stored_list.append(arg)

    def __str__(self):
        return f"Circular Queue at position {self.current_position}: {self.stored_list}"

    def dequeue(self):
        if self.current_position >= len(self.stored_list):
            self.current_position = 1
            return self.stored_list[0]
        else:
            self.current_position += 1
            return self.stored_list[self.current_position - 1]
