# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/5


from ...base import StrSplitSolution, TextSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 5

    def extract_number(self, line):
        return [ int(num) for num in line.split() if num.isdigit() ]

    def extract_number_under_section(self, input, section_name):
        numbers = []
        in_section = False

        for line in input:
            if section_name in line:
                in_section = True
                arr = self.extract_number(line)
                if len(arr) == 0:
                    continue
                else:
                    return arr
            
            if in_section:
                if any(char.isdigit() for char in line):
                    arr = self.extract_number(line)
                    numbers.append(arr)
                else:
                    break
        return numbers



    # @answer(1234)
    # def part_1(self) -> int:
    #     seeds = self.extract_number_under_section(self.input, 'seeds:')
    #     seeds_to_soil = self.extract_number_under_section(self.input, 'seed-to-soil map:')
    #     soil_to_fer = self.extract_number_under_section(self.input, 'soil-to-fertilizer map:')
    #     fer_to_water = self.extract_number_under_section(self.input, 'fertilizer-to-water map:')
    #     water_to_light = self.extract_number_under_section(self.input, 'water-to-light map:')
    #     light_to_temper = self.extract_number_under_section(self.input, 'light-to-temperature map:')
    #     temper_to_humid = self.extract_number_under_section(self.input, 'temperature-to-humidity map:')
    #     humid_to_location = self.extract_number_under_section(self.input, 'humidity-to-location map:')
    #     
    #     arr = [seeds_to_soil, soil_to_fer, fer_to_water, water_to_light, light_to_temper, temper_to_humid, humid_to_location]
    #     mn = float('inf')
    #
    #     for s in seeds:
    #         current = s
    #         for b in arr:
    #             for d, ss, r in b:
    #                 if ss <= current < ss + r:
    #                     current = current + d - ss
    #                     break
    #         print(current)
    #         mn = min(mn, current)
    #
    #     return int(mn)


    # @answer(1234)
    def part_2(self) -> int:
        inputs = self.extract_number_under_section(self.input, 'seeds:')
        seeds_to_soil = self.extract_number_under_section(self.input, 'seed-to-soil map:')
        soil_to_fer = self.extract_number_under_section(self.input, 'soil-to-fertilizer map:')
        fer_to_water = self.extract_number_under_section(self.input, 'fertilizer-to-water map:')
        water_to_light = self.extract_number_under_section(self.input, 'water-to-light map:')
        light_to_temper = self.extract_number_under_section(self.input, 'light-to-temperature map:')
        temper_to_humid = self.extract_number_under_section(self.input, 'temperature-to-humidity map:')
        humid_to_location = self.extract_number_under_section(self.input, 'humidity-to-location map:')
        
        arr = [seeds_to_soil, soil_to_fer, fer_to_water, water_to_light, light_to_temper, temper_to_humid, humid_to_location]
        mn = float('inf')

        seeds = []

        for i in range(0, len(inputs), 2):
            seeds.append((inputs[i], inputs[i + 1]))
        print(seeds)
        print('--')
        new = []
        while len(seeds) > 0:
            s, e = seeds.pop()
            for block in arr:
                for a, b, c in block:
                    os = max(s, b)
                    oe = min(e, b + c)
                    if os < oe:
                        new.append((os -b + a, oe -b + a))
                        if os > s:
                            seeds.append((s, os))
                        if e > oe:
                            seeds.append((oe, e))
                            break
                else:
                    new.append((s, e))
        seeds = new

        print(sorted(seeds))
        return -1


    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
