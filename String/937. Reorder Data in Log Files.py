class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits, letters = [], []
        for log in logs:

            if log.split()[1].isdigit():
                digits.append(log)

            else:
                letters.append(log)
        # 2개의 키를 기준으로 sort 할 때 사용한다.
        # sort의 경우 key 에 함수를 넣어줄 수 있는데, 이때 함수 대신 람다를 사용하면 좋다
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letters + digits