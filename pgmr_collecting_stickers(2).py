# 스티커 모으기 (2)
# 영님의 문제를 풀어보고자 했으나 굉장히 어렵군요.
# 출처: https://programmers.co.kr/learn/courses/18/lessons/1881

# N개의 스티커가 원형으로 연결되어 있습니다. 다음 그림은 N = 8인 경우의 예시입니다.
# image
# 원형으로 연결된 스티커에서 몇 장의 스티커를 뜯어내어 뜯어낸 스티커에 적힌 숫자의 합이 최대가 되도록 하고 싶습니다. 단 스티커 한 장을 뜯어내면 양쪽으로 인접해있는 스티커는 찢어져서 사용할 수 없게 됩니다.
#
# 예를 들어 위 그림에서 14가 적힌 스티커를 뜯으면 인접해있는 10, 6이 적힌 스티커는 사용할 수 없습니다. 스티커에 적힌 숫자가 배열 형태로 주어질 때, 스티커를 뜯어내어 얻을 수 있는 숫자의 합의 최댓값을 return 하는 solution 함수를 완성해 주세요. 원형의 스티커 모양을 위해 배열의 첫 번째 원소와 마지막 원소가 서로 연결되어 있다고 간주합니다.
#
# 제한 사항
# sticker는 원형으로 연결된 스티커의 각 칸에 적힌 숫자가 순서대로 들어있는 배열로, 길이(N)는 1 이상 100,000 이하입니다.
# sticker의 각 원소는 스티커의 각 칸에 적힌 숫자이며, 각 칸에 적힌 숫자는 1 이상 100 이하의 자연수입니다.
# 원형의 스티커 모양을 위해 sticker 배열의 첫 번째 원소와 마지막 원소가 서로 연결되어있다고 간주합니다.

# 최대 2칸을 건너뛰는 경우가 생긴다고 생각했고, 시작 위치를 3가지 경우로 나눠서 풀면 될 줄 알았는데 실패.
# DP 개념을 충분히 장착하고 DP 개념에 맞춰서 규칙 설정하여 풀어보자

def solution(sticker):
    ans = 0
    ansarr = [0, 0, 0]
    wait = [0, 0, 0]
    len_s = len(sticker)

    rotated = [sticker[i:] + sticker[:i] for i in range(3)]
    # print(rotated)
    for j in range(3):
        for i, num in enumerate(rotated[j][:-1]):
            if wait[j] != 0:
                wait[j] -= 1
                continue
            else:
                space1 = num
                space2 = sticker[i + 1]
                if space1 < space2 and i + 1 != len_s:
                    ansarr[j] += space2
                    wait[j] += 2
                else:
                    ansarr[j] += space1
                    wait[j] += 1

    print(ansarr)
    ans = sorted(ansarr, reverse=True)[0]

    return ans

if __name__ == "__main__":
    prob = [14, 6, 5, 11, 3, 9, 2, 10]
    print(solution(prob))