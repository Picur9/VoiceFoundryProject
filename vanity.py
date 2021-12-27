'''
Functionality:
    - Generates a vanity number from a phone number

It can be observed that each digit represents 3 or 4 different letters in the alphabet apart from 0 and 1 which doesn't represent any.

Map each of the numbers recursive with their string of probable letters, i.e 2 with “abc”, 3 with “def” etc. 
numbersMap[i] stores all characters that correspond to digit i in phone

The helper method _split_word(word) will return all substings and each weight that can be found in the transformed number.
Different rules could be set up for defining what weighs more. ATM the more and longer the words are would come out on top.
In addition with some letters (eg. A, B, I, R U, Y) and some numbers (eg. 1, 2, 4) that can mean a word on their own adding some extra weight.
Ordinals (a number followed by 'st', 'nd', 'rd' or 'th') are also considered to be valid and weight more than just regular numbers.

The helper method _get_words(phone) will return all possible words that can be obtained by input number in an order of the length
of the valid substings it contains. 

The helper method _get_all(phone) will return all possible alphanumeric variations that can be obtained by input number. 

The helper method _get_numbers(number, output, txt, idx, l) will return all possible words that can be obtained by input number. 
The output words are one by one stored in output[]. The txt is appended with the current digit on the current posisiton,
adding all 3 or 4 possible characters for current digit  and recur for remaining digits.
'''

import twl

def generate(phone, limit=5):
    return _Vnty()._get_words(phone)[:limit]

class _Vnty():
    def __init__(self):
        self.numbersMap = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        self.validNums = ("1", "2", "4")
        self.validChars = ("i", "r", "u", "y")
        self.ordinals = ((1,"st"), (2,"nd"), (3,"rd"), (0,"th"))
    def _is_valid_num(self, num, sub, i, l):
        return (
            num in self.validNums and
            (i == 0 or not sub[i-1].isnumeric()) and
            (i == l-1 or not sub[i+1].isnumeric())
        )
    def _is_ordinal(self, num, txt):
        if not num.isnumeric():
            return False
        for ord in self.ordinals:
            if ord[1] == txt and (ord[0] == 0 or ord[0] == int(num)):
                return True
        return False
    def _split_word(self, str):
        yield [str]
        for i in range(1, len(str)):
            start = str[0:i]
            end = str[i:]
            yield [start, end]
            for split in self._split_word(end):
                result = [start]
                result.extend(split)
                yield result
    def _get_words(self, phone):
        resp = []
        last = phone[-7:]
        rest = phone[:-7]
        lr = len(rest)
        if rest != "" and rest != "+":
            rest += "-"
        for w in self._get_all(last):
            subs = list(self._split_word(w))
            max = 0
            formatted = ""
            for sub in subs: 
                sl = len(sub)
                p = 0
                f = ""
                for i in range(0,sl):
                    part = sub[i]
                    l = len(part)
                    if part.isnumeric():
                        f+= part
                        if self._is_valid_num(part, sub, i, sl):
                            p+= 2
                            f+= "-"
                        elif i == sl-1 or not sub[i+1].isnumeric():
                            f+= "-"
                    elif l == 1:
                        if part in self.validChars:
                            p+= 1
                            f += part.upper() + "-"
                        else:
                            p = 0
                            break
                    elif l == 2 and i > 0 and self._is_ordinal(sub[i-1], part):
                        p+= 2 ** 2
                        f += part + "-"
                    elif twl.check(part):
                        p+= 2 ** l
                        f += part + "-"
                    else:
                        p = 0
                        break
                p = p/sl
                if p > max:
                    max = p
                    formatted = f[:-1]
            if max > 0: 
                resp.append((rest + formatted, max))
        resp.sort(key=lambda x: x[1], reverse=True)
        return list(map(lambda x: x[0], resp))
    def _get_all(self, phone):
        resp = []
        numbers = []
        for n in phone.lstrip("+"):
            numbers.append(int(n))
        self._get_numbers(numbers, resp, "", 0, len(numbers))
        return resp
    def _get_numbers(self, number, output, txt, idx, l):
        if(idx >= l):
            output.append(txt)
            return
        
        num = number[idx]
        self._get_numbers(number, output, txt + str(num), idx + 1, l)

        for element in self.numbersMap[num]:
            self._get_numbers(number, output, txt + element, idx + 1, l)
