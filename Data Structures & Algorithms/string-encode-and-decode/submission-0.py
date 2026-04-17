class Solution:
    temp = []
    def encode(self, strs: List[str]) -> str:
        self.temp = strs
        return "".join(strs)

    def decode(self, s: str) -> List[str]:
        return self.temp