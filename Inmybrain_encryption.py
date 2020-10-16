

def solution(enc, kstring):
    res = ''
    target = enc

    for k in kstring:
        # 나머지 문자열에서 키값 찾기
        for i, s in enumerate(target):
            if k != s: # for original string
                res += s
            else: # for key
                target = target[i+1:] # 키값은 복호화 skip
                break # 다음 키값으로 이동

    res += target # key 모두 찾고 마지막 남은 문자열 반영
    return res



if __name__ == "__main__":
    inputs = []
    answers = []
    prob = ["kkaxbycyz", "abc"]
    ans = "kkxyyz"
    inputs.append(prob)
    answers.append(ans)
    prob = ["acbbcdc", "abc"]
    ans = "cbdc"
    inputs.append(prob)
    answers.append(ans)

    for (ele, key), an in zip(inputs, answers):
        ansarr = solution(ele, key)
        print("correct?: {}".format(ansarr == an))
        print("predict: {}".format(ansarr))
        print("answer: {}".format(an))
        print("")