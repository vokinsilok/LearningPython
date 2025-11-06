class Notebook:

    def __init__(self):
        self.__notes = []

    def __getitem__(self, idx: int) -> str:
        return self.__notes[idx]


    def add(self, note: str)-> None:
        self.__notes.append(note)

    def __len__(self) -> int:
        return len(self.__notes)

    def __iter__(self):
        return iter(self.__notes)



nt = Notebook()
nt.add('a')
nt.add('b')
nt.add('c')
print(list(nt))
print(nt[1])
print(len(nt))

