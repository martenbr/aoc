import heapq

import aocutils


def main(file):
    print("RUNNING", file)
    tot = 0
    for line in aocutils.readlines(file):
        bid, ore_o, clay_o, obs_o, obs_c, geo_o, geo_obs = aocutils.parseints(line)
        states = [(24, 0, 0, 0, 1, 0, 0, 0, 0)]
        orer_cap = max(clay_o, obs_o, geo_o)
        clayr_cap = obs_c
        obsr_cap = geo_obs
        best = 0
        while states:
            t, geor, obsr, clayr, orer, ore, clay, obs, geo = heapq.heappop(states)
            new_ore = ore + orer
            new_clay = clay + clayr
            new_obs = obs + obsr
            new_geo = geo + geor
            if t == 1:
                if new_geo > best:
                    best = new_geo
                continue

            heapq.heappush(
                states,
                (t - 1, geor, obsr, clayr, orer, new_ore, new_clay, new_obs, new_geo)
            )
            if t > 15 and orer < orer_cap and ore >= ore_o:
                heapq.heappush(
                    states,
                    (t - 1, geor, obsr, clayr, orer + 1, new_ore - ore_o, new_clay, new_obs, new_geo)
                )
            if t > 8 and clayr < clayr_cap and ore >= clay_o:
                heapq.heappush(
                    states,
                    (t - 1, geor, obsr, clayr + 1, orer, new_ore - clay_o, new_clay, new_obs, new_geo)
                )
            if obsr < obsr_cap and ore >= obs_o and clay >= obs_c:
                heapq.heappush(
                    states,
                    (t - 1, geor, obsr + 1, clayr, orer, new_ore - obs_o, new_clay - obs_c, new_obs, new_geo)
                )
            if ore >= geo_o and obs >= geo_obs:
                heapq.heappush(
                    states,
                    (t - 1, geor + 1, obsr, clayr, orer, new_ore - geo_o, new_clay, new_obs - geo_obs, new_geo)
                )
        print(bid, best, best * bid)
        tot += best * bid
    print(tot)


if __name__ == '__main__':
    #main("example.txt")
    main("input.txt")
