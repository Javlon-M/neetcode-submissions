class LinkedList:
    
    def __init__(self):
        self.linked_list = []
    
    def get(self, index: int) -> int:
        if index >= len(self.linked_list):
            return -1
        return self.linked_list[index]

    def insertHead(self, val: int) -> None:
        self.linked_list = [val] + self.linked_list

    def insertTail(self, val: int) -> None:
        self.linked_list.append(val)

    def remove(self, index: int) -> bool:
        if index >= len(self.linked_list): 
            return False
        tmp = []
        for i in range(len(self.linked_list)):
            if i == index:
                continue
            tmp.append(self.linked_list[i])

        self.linked_list = tmp
        return True

    def getValues(self) -> List[int]:
        return self.linked_list
