"""
Wrong Answer
34 / 40 testcases passed

Use Testcase
Output
1533398211
Expected
1546649980
"""
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # factory's count >= robots'
        # first k factories pair with first k robots is optimal
        # compare redundant factories
        # if i_robot and i-1_robot both have min dist at factory j
        # compare dt(i-1, j) + dt(i, j+1) with dt(i-1, j-1) + dt(i, j)
        # R1---F1---R2
        srob = sorted(robot)
        sfac = sorted(factory)
        # unpack factory
        ufac = []
        for pos, cnt in sfac:
            ufac.extend([pos] * cnt)

        m = len(srob)
        n = len(ufac)
        # distance matrix
        dt = [[float("inf")] * n for _ in range(m)]
        # repair factories of robots
        repair = [-1] * m

        # pre_min_distance, pre_min_factory_index
        pre_mdist = pre_fac = None
        # curr robot position
        curr_robpos = srob[0]
        for j in range(n - (m - 1)):
            dist = abs(curr_robpos - ufac[j])
            dt[0][j] = dist
            if pre_mdist is None or dist < pre_mdist:
                pre_mdist = dist
                pre_fac = j
            elif dist > pre_mdist:
                break
        repair[0] = pre_fac

        for i in range(1, m):
            curr_robpos = srob[i]
            curr_mdist = curr_fac = None
            for j in range(pre_fac, n - (m - i - 1)):
                dist = abs(curr_robpos - ufac[j])
                dt[i][j] = dist
                if curr_mdist is None or dist < curr_mdist:
                    curr_mdist = dist
                    curr_fac = j
                elif dist > curr_mdist:
                    break

            if curr_fac == pre_fac:
                # optimal first k pairs
                if pre_fac == i - 1:
                    curr_fac += 1
                # remain factories == remain robots
                elif n - (m - i - 1) - pre_fac == 2:
                    curr_fac += 1
                elif dt[i - 1][curr_fac] + dt[i][curr_fac + 1] \
                    <= dt[i - 1][curr_fac - 1] + dt[i][curr_fac]:
                    curr_fac += 1
                else:
                    repair[i - 1] -= 1
            # curr_fac > pre_fac
            repair[i] = curr_fac
            pre_fac = curr_fac

        return sum(dt[i][repair[i]] for i in range(m))