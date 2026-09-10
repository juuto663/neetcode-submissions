class Solution:

    def encode(self, strs: List[str]) -> str:
        control_char = '#'
        encoded_str = []

        for word in strs:
            word_length = len(word)
            encoded_str.append(f"{word_length}")
            encoded_str.append(control_char)
            encoded_str.append(word)

        return ''.join(encoded_str)

    def decode(self, s: str) -> List[str]:
        ret = []
        word_length = []
        i = 0
        while i < len(s):
            if s[i] == "#":
                print(word_length)
                length = int(''.join(word_length))
                word_length = []
                ret.append(s[i + 1: i + length + 1])
                i += length + 1
            else:
                word_length.append(s[i])
                i += 1

        return ret
