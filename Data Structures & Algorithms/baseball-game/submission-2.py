class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for i in operations:
            if i.isnumeric() or (i[0] == "-" and i[1:].isnumeric()):
                record.append(int(i))

            elif i == "+":
                record.append(record[-1] + record[-2])
            elif i == "C":
                record.pop()
            elif i == "D":
                record.append(2 * record[-1])
                
        return sum(record)
