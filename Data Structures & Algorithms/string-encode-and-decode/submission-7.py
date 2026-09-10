class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = []
        delimiter = "#"
        for s in strs:
            ret += str(len(s)) + delimiter
            ret += s
        print("".join(ret))
        return "".join(ret)
        
    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0

        while (i < len(s)):
            j = i
            while(s[j] != "#"):
                j += 1
            length = int(s[i:j])
            word = s[j + 1: j + 1 + length]
            ret.append(word)
            i = j + 1 + length
        return ret
