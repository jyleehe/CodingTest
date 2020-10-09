def solution(tickets):
    answer = []

    visited = []
    begin = "ICN"
    visited.append(begin)
    collected = [0] * len(tickets)

    def dfs(bg, vs, cl):
        if sum(cl) == len(tickets):
            answer.append(vs)
            return

        for i, ti in enumerate(tickets):
            if ti[0] == bg and cl[i] != 1:
                vs.append(ti[1])
                # cl.append(ti)
                cl[i] = 1
                dfs(ti[1], vs[:], cl[:])
                vs.pop()
                # cl.pop()
                cl[i] = 0

    dfs(begin, visited, collected)

    if len(answer) > 1:
        answer = sorted(answer)[0]
    else:
        answer = answer[0]

    return answer