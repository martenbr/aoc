import heapq

import aocutils


def main(file):
    print("RUNNING", file)
    tot = 1
    blueprints = [aocutils.parseints(line) for line in aocutils.readlines(file)]
    for bp in blueprints[0:3]:
        bid, ore_o, clay_o, obs_o, obs_c, geo_o, geo_obs = bp
        states = [(32, 0, 0, 0, 1, 0, 0, 0, 0)]
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

            idle_ok = True

            can_build_ore = False
            can_build_clay = False
            if clayr <= 1 and orer < orer_cap and ore >= ore_o:
                can_build_ore = True
                heapq.heappush(
                    states,
                    (t - 1, geor, obsr, clayr, orer + 1, new_ore - ore_o, new_clay, new_obs, new_geo)
                )
            if t > 10 and clayr < clayr_cap and ore >= clay_o:
                can_build_clay = True
                heapq.heappush(
                    states,
                    (t - 1, geor, obsr, clayr + 1, orer, new_ore - clay_o, new_clay, new_obs, new_geo)
                )
            if can_build_clay and can_build_ore:
                idle_ok = False

            if obsr < obsr_cap and ore >= obs_o and clay >= obs_c:
                idle_ok = False
                heapq.heappush(
                    states,
                    (t - 1, geor, obsr + 1, clayr, orer, new_ore - obs_o, new_clay - obs_c, new_obs, new_geo)
                )
            if ore >= geo_o and obs >= geo_obs:
                idle_ok = False
                heapq.heappush(
                    states,
                    (t - 1, geor + 1, obsr, clayr, orer, new_ore - geo_o, new_clay, new_obs - geo_obs, new_geo)
                )

            if idle_ok:
                heapq.heappush(
                    states,
                    (t - 1, geor, obsr, clayr, orer, new_ore, new_clay, new_obs, new_geo)
                )
        print(bid, best)
        tot *= best
    print(tot)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
