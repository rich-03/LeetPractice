class Solution:
    def removeDuplicates(self, S: str) -> str:
        final_string = []
        for variable in S:
            if final_string and variable == final_string[-1]:
                final_string.pop()
                continue
            final_string.append(variable)

        return ''.join(final_string)
