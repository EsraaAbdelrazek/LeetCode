class Spreadsheet:
    def __init__(self, rows: int):
        self.map = {}

    def setCell(self, cell: str, value: int) -> None:
        self.map[cell] = value

    def resetCell(self, cell: str) -> None:
        if cell in self.map:
            del self.map[cell]

    def getValue(self, formula: str) -> int:
        i = formula.index("+")
        cell1 = formula[1:i]
        cell2 = formula[i+1:]

        val1 = self.map.get(cell1, 0) if cell1[0].isalpha() else int(cell1)
        val2 = self.map.get(cell2, 0) if cell2[0].isalpha() else int(cell2)

        return val1 + val2