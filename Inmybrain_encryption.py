

def solution(enc, kstring):
    res = ''
    print(enc, kstring)
    target = enc

    for k in kstring:
        # 나머지에서
        for i, s in enumerate(target):
            if k != s: # for original string
                res += s
            else: # for key
                target = target[i+1:] # skip this char.
                break
    res += target
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