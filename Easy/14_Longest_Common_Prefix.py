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


#Failed
# fl = ""
    # com_prefix = ""
    # valid = False
    # lowerlist = [word.lower() for word in strs]
    # if not(len(strs) >= 1 and len(strs) <= 200):
    #     return ""
    # elif len(strs) == 1:
    #     return strs[0][0]
    # for i in range(len(lowerlist[0])):
    #     count = 0
    #     for x in range(len(lowerlist)):
    #         if not(len(lowerlist[x][i]) >= 0 and len(lowerlist[x][i]) <= 200):
    #             return ""
    #         try:
    #             if count == 0:
    #                 fl = lowerlist[x][i]
    #             if lowerlist[x][i] == fl and count != 0:
    #                 valid = True
    #             elif lowerlist[x][i] != fl:
    #                 valid = False
    #             count += 1
    #         except IndexError:
    #             return ""
    #     if valid:
    #         com_prefix += fl
    #         valid = False
    #     else:
    #         return com_prefix
    # return ""