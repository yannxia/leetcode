class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        neg = False
        if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
            neg = True

        numerator = abs(numerator)
        denominator = abs(denominator)

        real = int(numerator / denominator)
        remind = numerator % denominator

        if remind == 0:
            if neg:
                return "-" + str(real)
            return str(real)

        loops = []
        val = []
        is_loop = True
        found_index = 0
        while True:
            while remind < denominator:
                loops.append(remind)
                remind *= 10
                val.append(str(int(remind / denominator)))

            remind %= denominator

            if remind == 0:
                is_loop = False
                break

            if remind != 0 and remind in loops:
                found_index = loops.index(remind)
                break

        val = ''.join(val)

        if not is_loop:
            if neg:
                return "-" + str(real) + "." + val
            return str(real) + "." + val

        x = val[0:found_index] if found_index != 0 else ''

        v = str(real) + '.' + x + "(" + val[found_index:] + ")"
        if neg:
            return "-" + v
        return v


if __name__ == '__main__':
    s = Solution()
    print(s.fractionToDecimal(-2147483648, 1) == "-2147483648")
    print(s.fractionToDecimal(1, 6) == "0.1(6)")
    print(s.fractionToDecimal(1,
                              214748364) == "0.00(000000465661289042462740251655654056577585848337359161441621040707904997124914069194026549138227660723878669455195477065427143370461252966751355553982241280310754777158628319049732085502639731402098131932683780538602845887105337854867197032523144157689601770377165713821223802198558308923834223016478952081795603341592860749337303449725)")
    print(s.fractionToDecimal(1, 333) == "0.(003)")

    print(s.fractionToDecimal(1, 19) == "0.(052631578947368421)")
    print(s.fractionToDecimal(1, 17) == "0.(0588235294117647)")
    print(s.fractionToDecimal(2, 3) == "0.(6)")
    print(s.fractionToDecimal(4, 333) == "0.(012)")
    print(s.fractionToDecimal(2, 1) == "2")
    print(s.fractionToDecimal(1, 2) == "0.5")
    print(s.fractionToDecimal(-50, 8) == "-6.25")
