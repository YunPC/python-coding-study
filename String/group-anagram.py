import collections


# naive
class String:
    def __init__(self, string):
        self.string = string
        self.typical = "".join(sorted(list(string), key=str))


def solution1(strs):
    strings = [String(string) for string in strs]
    string_set = set()

    for string in strs:
        string_set.add("".join(sorted(list(string), key=str)))

    answer = []
    string_list = list(string_set)
    while string_list:
        pop = string_list.pop(0)
        temp = []
        for string in strings:
            if pop == string.typical:
                temp.append(string.string)
        answer.append(temp)

    return answer


# solution
def solution2(strs):
    ans = collections.defaultdict(list)
    for s in strs:
        ans[tuple(sorted(s))].append(s)
    return ans.values()


# practical
def solution3(strs):
    ans = {}
    for string in strs:
        key = tuple(sorted(string))
        if key in ans:
            ans[key].append(string)
        else:
            ans[key] = [string]

    return ans.values()


if __name__ == "__main__":
    print(solution1(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(solution3(["eat", "tea", "tan", "ate", "nat", "bat"]))
