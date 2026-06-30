class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ''
        current_num= 0
        for c in s:
            if c.isdigit():
                current_num = current_num*10+int(c)
            elif c=='[':
                stack.append((current_string, current_num))
                current_string=''
                current_num=0
            elif c ==']':
                string, num = stack.pop()
                current_string = string +current_string*num 
            else:
                current_string+=c
        return current_string