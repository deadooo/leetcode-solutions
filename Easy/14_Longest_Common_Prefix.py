def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    fl = ""
    comPre = ""
    validComPre = False
    if strs:
        lowerWords = [word.lower() for word in strs]
        if not strs[0]:
            return ""
        if len(strs) == 1:
            return strs[0][0]
        listSize = len(lowerWords) - 1
        for i in range(len(lowerWords[0])):
            try:
                for index, word in enumerate(lowerWords):
                    if fl:
                        if word[i] == fl:
                            validComPre = True
                        else: 
                            validComPre = False
                            break
                    else:
                        fl = word[i]
                    if validComPre and index == listSize:
                        comPre += fl
                        fl = ""
            except IndexError:
                continue
            if validComPre == False:
                break
        return comPre

    
# Testing
strs = ["flower", "flow", "flight"]
strs = ["a"]
strs = ["aca","cba"]
# strs = [""]
# strs = ["c", "acc", "ccc"]
# strs = ["dog","racecar","car"]
print(f"compref: {longestCommonPrefix(strs)}")
# Notes
# First String, First Letter, For loop entire first letter of all words


