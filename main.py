def romanToInt(s):
 
        dict = {'V':'I', 'X':'I', 'L':'X', 'C':'X', 'D':'C', 'M':'C'}
        ref = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        stack = []
        for i in s:
            temp = ''
            check = True
            if stack:
                temp = stack.pop()
                if i in dict:
                    if temp == dict[i]:
                        num = ref[i] - ref[temp]
                        stack.append(num)
                        check = False
                    else:
                        stack.append(temp)
                else:
                    stack.append(temp)
            if check:
                stack.append(i)
                
        sum = 0
        while stack:
            temp = stack.pop()
            if type(temp) != int:
                sum += ref[temp]
            else:
                sum += temp
                
        return sum
        
num = romanToInt("MCMXCIV")
print(num)
