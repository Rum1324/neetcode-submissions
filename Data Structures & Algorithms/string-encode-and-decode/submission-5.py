class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for string in strs:
            result += str(len(string)) + "#" + string

        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        result = []

        current_index = 0
        len_string = 0
        while current_index < len(s):
            # read number & '#'
            digit = s[current_index]
            while s[current_index+1] != '#':
                current_index += 1
                digit += s[current_index]
                
            len_string = int(digit)

            # slice index and append to list

            result.append(s[current_index+  2 :current_index+  2+len_string])
            
            # update current_index
            current_index = current_index + len_string + 2
        
        return result