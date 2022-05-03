def generateParanthesis(num_pair):
    openN = num_pair
    closeN = num_pair
    tempStr = []
    res = []

    def backtrack(openN, closeN, tempStr, res):
        if open==closeN==0:
            res.append("".join(tempStr))
            return 
        if openN!=0:
            tempStr.append("(")
            # openN-=1
            backtrack(openN-1, closeN, tempStr, res)
            tempStr.pop()
        if closeN>openN:
            tempStr.append(")")
            # openN-=1

            backtrack(openN, closeN-1,  tempStr, res)
            tempStr.pop()

    backtrack(openN, closeN, tempStr, res)
    return res
print(generateParanthesis(3))