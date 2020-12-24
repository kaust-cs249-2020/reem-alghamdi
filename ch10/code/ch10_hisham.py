import numpy as np


def HMMProfile(theta, alphabet, multalign, pseudocount=0):
    a = np.array(list(map(list, multalign)))
    n, m = a.shape
    # compute column id where insertion fraction is greater than theta
    col_is_m = np.apply_along_axis(lambda r: np.sum(r == '-') < n * theta, 0, a)
    col_to_state = np.cumsum(col_is_m)
    # compute the symbols translation table
    symbols = {s: i for (i, s) in enumerate(alphabet)}
    # compute the name_state translation table
    max_state_id = max(col_to_state)
    name_state = {}
    name_state['S'] = 0
    name_state['I0'] = 1
    for i in range(1, max(col_to_state) + 1):
        name_state['M' + str(i)] = 3 * i - 1
        name_state['D' + str(i)] = 3 * i
        name_state['I' + str(i)] = 3 * i + 1
    name_state['E'] = 3 * max_state_id + 2
    state_name = [None] * len(name_state)
    for k, v in name_state.items():
        state_name[v] = k

    # emission
    emission = np.zeros((len(name_state), len(symbols)))
    for i in range(n):
        for j in range(m):
            insert_flag = not col_is_m[j]
            state_id = col_to_state[j]
            e = a[i, j]
            if e in symbols:
                emission[name_state[('I' if insert_flag else 'M') + str(state_id)], symbols[e]] += 1

                # transition
    transition = np.zeros((len(name_state), len(name_state)))
    for i in range(n):
        prev_state_name = 'S'
        for j in range(m):
            state_id = col_to_state[j]
            insert_flag = not (col_is_m[j])
            delete_flag = not (a[i, j] in symbols)
            if (insert_flag) and (delete_flag):
                if j == m - 1:
                    transition[name_state[prev_state_name], name_state['E']] += 1
            else:
                if (not insert_flag) and (not delete_flag):
                    curr_state_name = 'M' + str(state_id)
                elif insert_flag and (not delete_flag):
                    curr_state_name = 'I' + str(state_id)
                elif (not insert_flag) and delete_flag:
                    curr_state_name = 'D' + str(state_id)

                transition[name_state[prev_state_name], name_state[curr_state_name]] += 1
                prev_state_name = curr_state_name
                # last column specific case
                if j == m - 1:
                    transition[name_state[prev_state_name], name_state['E']] += 1

    # normalize matrices probability
    for i in name_state.values():
        csum = emission[i, :].sum()
        if (csum > 0):
            emission[i, :] /= csum
    for i in name_state.values():
        csum = transition[i, :].sum()
        if (csum > 0):
            transition[i, :] /= csum

    # adding pseudocount if needed
    if pseudocount > 0:
        # emission :
        # add pseudocount only for 'I' and 'M' states
        m, n = emission.shape
        for i in range(1, m - 1):
            if (i % 3):
                emission[i, :] += pseudocount
        for i in name_state.values():
            csum = emission[i, :].sum()
            if (csum > 0):
                emission[i, :] /= csum
        # emission :
        # add transition only for allowed transition states
        m, n = transition.shape
        for i in range(0, m - 1):
            a = int(min((i + 1) / 3 * 3 + 1, n))
            b = int(min((i + 1) / 3 * 3 + 4, n))
            transition[i, a:b] += pseudocount
        for i in name_state.values():
            csum = transition[i, :].sum()
            if (csum > 0):
                transition[i, :] /= csum

    return transition, emission, alphabet, state_name


def HMMProfileDecoding(x, symbols, states, transition, emission):
    assert transition.shape == (len(states), len(states))
    assert emission.shape == (len(states), len(symbols))
    rsymbols = {k: i for (i, k) in enumerate(symbols)}
    rstates = {k: i for (i, k) in enumerate(states)}

    n = len(x) + 1
    m = len(states) // 3
    dscore = np.empty(shape=(m, n), dtype=float)
    mscore = np.empty(shape=(m, n), dtype=float)
    iscore = np.empty(shape=(m, n), dtype=float)

    dbackt = np.empty(shape=(m, n), dtype=tuple)
    mbackt = np.empty(shape=(m, n), dtype=tuple)
    ibackt = np.empty(shape=(m, n), dtype=tuple)

    # fill up values with None
    dbackt.fill(None)
    mbackt.fill(None)
    ibackt.fill(None)

    # fill up values with 666
    dscore.fill(666)
    mscore.fill(666)
    iscore.fill(666)

    # initialize non-reachable values with 777
    dscore[0, :] = 777
    mscore[:, 0] = 777
    mscore[0, :] = 777
    iscore[1:, 0] = 777

    def recurrence_M(l, k):
        assert l > 1 and k > 1
        d_prev_id = rstates['D' + str(l - 1)]
        m_prev_id = rstates['M' + str(l - 1)]
        i_prev_id = rstates['I' + str(l - 1)]
        m_curr_id = rstates['M' + str(l)]
        k_id = rsymbols[x[k - 1]]
        score_M = mscore[l - 1, k - 1] + np.log(emission[m_curr_id, k_id] * transition[m_prev_id, m_curr_id])
        score_D = dscore[l - 1, k - 1] + np.log(emission[m_curr_id, k_id] * transition[d_prev_id, m_curr_id])
        score_I = iscore[l - 1, k - 1] + np.log(emission[m_curr_id, k_id] * transition[i_prev_id, m_curr_id])
        score_max = max(score_M, score_D, score_I)
        if score_M == score_max:
            return (score_M, ('M', l - 1, k - 1))
        if score_D == score_max:
            return (score_D, ('D', l - 1, k - 1))
        if score_I == score_max:
            return (score_I, ('I', l - 1, k - 1))

    def recurrence_D(l, k):
        d_prev_id = rstates['D' + str(l - 1)]
        m_prev_id = rstates['M' + str(l - 1)]
        i_prev_id = rstates['I' + str(l - 1)]
        d_curr_id = rstates['D' + str(l)]
        score_M = mscore[l - 1, k] + np.log(1 * transition[m_prev_id, d_curr_id])
        score_D = dscore[l - 1, k] + np.log(1 * transition[d_prev_id, d_curr_id])
        score_I = iscore[l - 1, k] + np.log(1 * transition[i_prev_id, d_curr_id])
        score_max = max(score_M, score_D, score_I)
        if score_M == score_max:
            return (score_M, ('M', l - 1, k))
        if score_D == score_max:
            return (score_D, ('D', l - 1, k))
        if score_I == score_max:
            return (score_I, ('I', l - 1, k))

    def recurrence_I(l, k):
        d_curr_id = rstates['D' + str(l)]
        m_curr_id = rstates['M' + str(l)]
        i_curr_id = rstates['I' + str(l)]
        k_id = rsymbols[x[k - 1]]
        score_M = mscore[l, k - 1] + np.log(emission[i_curr_id, k_id] * transition[m_curr_id, i_curr_id])
        score_D = dscore[l, k - 1] + np.log(emission[i_curr_id, k_id] * transition[d_curr_id, i_curr_id])
        score_I = iscore[l, k - 1] + np.log(emission[i_curr_id, k_id] * transition[i_curr_id, i_curr_id])
        score_max = max(score_M, score_D, score_I)
        if score_M == score_max:
            return (score_M, ('M', l, k - 1))
        if score_D == score_max:
            return (score_D, ('D', l, k - 1))
        if score_I == score_max:
            return (score_I, ('I', l, k - 1))

            # initialize viterbi graph top row I0

    i0_id = rstates['I0']
    s_id = rstates['S']
    k_id = rsymbols[x[0]]
    iscore[0, 1] = np.log(emission[i0_id, k_id] * transition[s_id, i0_id])
    ibackt[0, 1] = None
    for k in range(2, n):
        i0_id = rstates['I0']
        k_id = rsymbols[x[k - 1]]
        iscore[0, k] = iscore[0, k - 1] + np.log(emission[i0_id, k_id] * transition[i0_id, i0_id])
        ibackt[0, k] = ('I', 0, k - 1)

    # initialize viterbi graph top row M1
    m1_id = rstates['M1']
    s_id = rstates['S']
    k_id = rsymbols[x[0]]
    mscore[1, 1] = np.log(emission[m1_id, k_id] * transition[s_id, m1_id])
    mbackt[1, 1] = None
    for k in range(2, n):
        m1_id = rstates['M1']
        i0_id = rstates['I0']
        k_id = rsymbols[x[k - 1]]
        mscore[1, k] = iscore[0, k - 1] + np.log(emission[m1_id, k_id] * transition[i0_id, m1_id])
        mbackt[1, k] = ('I', 0, k - 1)

    # initialize viterbi graph top row D1
    d1_id = rstates['D1']
    s_id = rstates['S']
    dscore[1, 0] = np.log(1 * transition[s_id, d1_id])
    dbackt[1, 0] = None
    for k in range(1, n):
        i0_id = rstates['I0']
        d1_id = rstates['D1']
        dscore[1, k] = iscore[0, k] + np.log(1 * transition[i0_id, d1_id])
        dbackt[1, k] = ('I', 0, k)

    # initialize viterbi graph first left column D0,D1,....
    dscore[1, 0] = 0
    dbackt[1, 0] = None
    for l in range(2, m):
        d_prev_id = rstates['D' + str(l - 1)]
        d_curr_id = rstates['D' + str(l)]
        dscore[l, 0] = dscore[l - 1, 0] + np.log(1 * transition[d_prev_id, d_curr_id])
        dbackt[l, 0] = ('D', l - 1, 0)

    # initialize viterbi graph second left column I1,I2,....
    for l in range(1, m):
        d_curr_id = rstates['D' + str(l)]
        i_curr_id = rstates['I' + str(l)]
        k_id = rsymbols[x[0]]
        iscore[l, 1] = dscore[l, 0] + np.log(emission[i_curr_id, k_id] * transition[d_curr_id, i_curr_id])
        ibackt[l, 1] = ('D', l, 0)

    # initialize viterbi graph second left column M2,M3,....
    for l in range(2, m):
        d_prev_id = rstates['D' + str(l - 1)]
        m_curr_id = rstates['M' + str(l)]
        k_id = rsymbols[x[0]]
        mscore[l, 1] = dscore[l - 1, 0] + np.log(emission[m_curr_id, k_id] * transition[d_prev_id, m_curr_id])
        mbackt[l, 1] = ('D', l - 1, 0)

    # recurrence on I1 row
    for k in range(2, n):
        (iscore[1, k], ibackt[1, k]) = recurrence_I(1, k)

    # recurrence on second second left column D2,D3,....
    for l in range(2, m):
        (dscore[l, 1], dbackt[l, 1]) = recurrence_D(l, 1)

    # recurrence from the 2,2 corner...
    for l in range(2, m):
        for k in range(2, n):
            (mscore[l, k], mbackt[l, k]) = recurrence_M(l, k)
            (dscore[l, k], dbackt[l, k]) = recurrence_D(l, k)
            (iscore[l, k], ibackt[l, k]) = recurrence_I(l, k)

    # backtracking max score from back pointers

    mm_id = rstates['M' + str(m - 1)]
    dm_id = rstates['D' + str(m - 1)]
    im_id = rstates['I' + str(m - 1)]
    e_id = rstates['E']
    score_M = mscore[m - 1, n - 1] + np.log(transition[mm_id, e_id])
    score_D = dscore[m - 1, n - 1] + np.log(transition[dm_id, e_id])
    score_I = iscore[m - 1, n - 1] + np.log(transition[im_id, e_id])
    score_max = max(score_M, score_D, score_I)

    hidden_path = []
    if score_M == score_max:
        hidden_path.append('M' + str(m - 1))
        (state, l, k) = mbackt[m - 1, n - 1]
    elif score_D == score_max:
        hidden_path.append('D' + str(m - 1))
        (state, l, k) = dbackt[m - 1, n - 1]
    elif score_I == score_max:
        hidden_path.append('I' + str(m - 1))
        (state, l, k) = ibackt[m - 1, n - 1]

    while True:
        if state == 'M':
            hidden_path.append('M' + str(l))
            backt = mbackt
        if state == 'D':
            hidden_path.append('D' + str(l))
            backt = dbackt
        if state == 'I':
            hidden_path.append('I' + str(l))
            backt = ibackt
        if backt[l, k] == None:
            break
        (state, l, k) = backt[l, k]

    return ' '.join(hidden_path[::-1])


def HMMProfileHiddenPath(x, theta, pseudocount, alphabet, multalign):
    (t, e, a, s) = HMMProfile(theta, alphabet, multalign, pseudocount=pseudocount)
    ret = HMMProfileDecoding(x, a, s, t, e)
    return ret


def PrintHMMProfile(transition, emission, alphabet, state_name):
    __emission = np.round(emission, 3)
    __transition = np.round(transition, 3)
    ret = ''
    # ret += '\t' + '\t'.join(state_name) + '\n'
    ret += '\t' + '\t'.join(state_name) + '\n'
    for i, s in enumerate(state_name):
        l = s + '\t'
        l += '\t'.join(
            [format("%.3g" % __transition[i, j]) if __transition[i, j] != 1 else '1.0' for j in range(len(state_name))])
        ret += l + '\n'
    ret += '--------\n'
    ret += '\t' + '\t'.join(alphabet)
    for i, s in enumerate(state_name):
        l = '\n' + s + '\t'
        l += '\t'.join(
            [format("%.3g" % __emission[i, j]) if __emission[i, j] != 1 else '1.0' for j in range(len(alphabet))])
        ret += l
    return ret


def HMMParameterEstimation(x, alphabet, path, states):
    assert len(x) == len(path)
    m = len(alphabet)
    n = len(states)
    p = len(path)
    transition = np.zeros((n, n))
    emission = np.zeros((n, m))
    rsymbols = {k: i for (i, k) in enumerate(alphabet)}
    rstates = {k: i for (i, k) in enumerate(states)}

    for i in range(p):
        sy_id = rsymbols[x[i]]
        st_id = rstates[path[i]]
        emission[st_id, sy_id] += 1.

    for i in range(1, p):
        curr_st_id = rstates[path[i]]
        prev_st_id = rstates[path[i - 1]]
        transition[prev_st_id, curr_st_id] += 1

    def matrix_norm(mtx):
        a, b = mtx.shape
        for i in range(a):
            csum = mtx[i, :].sum()
            if csum == 0:
                mtx[i, :] = 1. / b
            else:
                mtx[i, :] /= 1. * csum
        return

    matrix_norm(transition)
    matrix_norm(emission)

    return transition, emission


def HMMDecoding(emission, symbols, states, transition_matrix, emission_matrix):
    assert transition_matrix.shape == (len(states), len(states))
    assert emission_matrix.shape == (len(states), len(symbols))
    rstates = {v: k for (k, v) in states.items()}

    def __log_weight(l, k, i):
        si = symbols[emission[i]]
        return np.log(emission_matrix[k, si] * transition_matrix[l, k])

    score = np.empty(shape=(len(states), len(emission)), dtype=float)
    backt = np.zeros(shape=(len(states), len(emission)), dtype=int)

    score[:, 0] = np.log(1. / len(states) * emission_matrix[:, symbols[emission[0]]])
    for i in range(1, len(emission)):
        for k in range(len(states)):
            pscore = np.array(list(map(lambda l: score[l, i - 1] + __log_weight(l, k, i), range(len(states)))))
            score[k, i] = pscore.max()
            backt[k, i] = pscore.argmax()
    # backtracking max score from backt pointers
    rpath = []
    state = score[:, len(emission) - 1].argmax()
    rpath.append(rstates[state])
    for i in range(1, len(emission))[::-1]:
        state = backt[state, i]
        rpath.append(rstates[state])
    return ''.join(rpath[::-1])


def ParseEmissionTransitionMatrix(lines):
    emission = lines[0]
    symbols = lines[2].split(' ')
    states = lines[4].split(' ')
    transition_matrix = np.zeros((len(states), len(states)), dtype=np.longfloat)
    for i in range(len(states)):
        transition_matrix[i, :] = list(map(np.longfloat, lines[i + 7].split('\t')[1:len(states) + 1]))
    emission_matrix = np.zeros((len(states), len(symbols)), dtype=np.longfloat)
    for i in range(len(states)):
        emission_matrix[i, :] = list(map(np.longfloat, lines[i + 9 + len(states)].split('\t')[1:len(symbols) + 1]))
    return emission, symbols, states, transition_matrix, emission_matrix


def HMMViterbiLearning(it, x, symbols, states, transition, emission):
    dsymbols = {s: i for (i, s) in enumerate(symbols)}
    dstates = {s: i for (i, s) in enumerate(states)}
    for j in range(it):
        path = HMMDecoding(x, dsymbols, dstates, transition, emission)
        (transition, emission) = HMMParameterEstimation(x, symbols, path, states)
    #     print(PrintHMMProfile(transition, emission, symbols, states))
    #     print('**************************************')
    # print()
    return transition, emission


def SoftDecoding(string, states, transition, emission):
    forward = {}
    forward[0] = {}
    for i in states:
        forward[0][i] = {}
        forward[0][i] = 1.0/len(states)*emission[i][string[0]]
    for i in range(1, len(string)):
        forward[i] = {}
        for j in states:
            forward[i][j] = 0
            for k in states:
                forward[i][j] += forward[i-1][k]*transition[k][j]*emission[j][string[i]]

    backward = {}
    backward[len(string)-1] = {}
    for i in states:
        backward[len(string)-1][i] = {}
        backward[len(string)-1][i] = 1.0 ###*emission[i][re_string[0]]
    for i in range(len(string)-2, -1,-1):
        backward[i] = {}
        for j in states:
            backward[i][j] = 0
            for k in states:
                backward[i][j] += backward[i+1][k]*transition[j][k]*emission[k][string[i+1]]
    res = {}
    for i in range(len(string)):
        res[i] = {}
        total = 0
        for j in states:
            res[i][j] = forward[i][j]*backward[i][j]
            total +=  res[i][j]
        for j in states:
            res[i][j] = res[i][j]/total

    return res


if __name__ == '__main__':
    # x = 'xxxzxyyxyyyxxzyyyxzxzyyyzxzzxyyyyzyyyxxxxyzzyzzxzyxyxzyzyyxyzxyyxxyxyzxyxyyxzzzzyxyxyyxxxxzxxzzxxzxx'
    # alphabet = 'x y z'.split()
    # path = 'ABBBCBBACCCBACACBBCACABCBCCBAAABCAACBBABCCCBCAABCCBCABBBBCABCBCAAAABBBAAAAAABCBBBCBABACCAABBBAACABAC'
    # states = 'A B C'.split()

    # theta = 0.365
    # pseudocount = 0.01
#     multalign = """ECACBB-EECBECDDECD---CADDA-DD-BAEBAECCAA--DB-B-EA
# --EBBBEEEADCCD-E--CEECAEAAD--BBAAB-DCC--BCEBDB-B-
# ACDCBBAEEBDEC-BECDABD-AEDADDD-C-ABCDCBE-ECE-DBBBA
# EC-CEBDE-A-EC-BDEDCBACAED-DCD-BA-BCDCADABCEAABBEA
# ECACBBAAEADDCDBEC-ECDCCEDADCDBBEBB-D-CEAB-E-DB-CA""".split()
#     ret = HMMProfileHiddenPath(x, theta, pseudocount, alphabet, multalign)
#     print(ret)

    # (t, e) = HMMParameterEstimation(x, alphabet, path, states)
    # ret = PrintHMMProfile(t, e, alphabet, states)
    # print(ret)

    # with open("../data/hshm") as f:
    #     text = f.read()
    #     lines = text.split('\n')
    #     it = int(lines[0])
    #     x,symbols,states,t,e = ParseEmissionTransitionMatrix(lines[2:])
    #     t,e = HMMViterbiLearning(it,x,symbols,states,t,e)
    #     ret = PrintHMMProfile(t,e,symbols,states)
    #     print(ret)


    with open("../data/hshm") as f:
        lines = f.readlines()
        string = lines[0].strip()
        alphabet = lines[2].strip().split()
        states = lines[4].strip().split()
        transition = {}
        for i in states:
            transition[i] = dict((x, 0) for x in states)
        emission = {}
        for i in states:
            emission[i] = dict((x, 0) for x in alphabet)

        for i in range(7, 7 + len(states)):
            items = lines[i].strip().split()
            for j in range(1, len(items)):
                transition[states[i - 7]][states[j - 1]] = float(items[j])

        for i in range(9 + len(states), 9 + 2 * len(states)):
            items = lines[i].strip().split()
            for j in range(1, len(items)):
                emission[states[i - 9 - len(states)]][alphabet[j - 1]] = float(items[j])

        res = SoftDecoding(string, states, transition, emission)
        for i in states:
            print(i, end="\t")
        print()
        for i in range(len(string)):
            for j in states:
                print(res[i][j], end="\t")
            print()