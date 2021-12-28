'''
Functionality:
    - Generates a vanity number from a phone number

It can be observed that each digit represents 3 or 4 different letters in the alphabet apart from 0 and 1 
which doesn't represent any.

Map each of the numbers recursive with their string of probable letters, i.e 2 with “abc”, 3 with “def” etc. 
numbersMap[i] stores all characters that correspond to digit i in phone

The helper method _get_substrings(self, word) will return all substing words that can be found in the transformed number.

The helper method _get_words(self, phone) will return all possible words that can be obtained by the last 7 digit of the input number 
in the order of the length of the valid substings it contains. 

The helper method _get_all(self, phone) will return all possible alphanumeric variations that can be obtained by 
the input number. 

The helper method _get_numbers(self, number, output, txt, idx, l) will return all possible words that can be obtained 
by the input number. 

The output words are one by one stored in output[]. The txt is appended with the current digit on the current posisiton,
adding all 3 or 4 possible characters for current digit  and recur for remaining digits.

'''

import twl

def generate(phone,limit=5):
    return _Vnty()._get_words(phone)[:limit]


class _Vnty():
    def __init__(self):
        self.numbersMap = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    def _get_substrings(self, word):
        start = 0
        l = len(word)
        words = []
        for i, c in enumerate(word):
            if c.isdigit():
                if start != i:
                    words.append(word[start: i])
                start = i+1
            elif l-1 == i:
                words.append(word[start: l])
        return words
    def _get_words(self, phone):
        resp = []
        last = phone[-7:]
        rest = phone[:-7]
        lr = len(rest)
        if rest != "" and rest != "+":
            rest += "-"
        for w in self._get_all(last):
            subs = self._get_substrings(w)
            valid = len(subs) > 0
            l = 0
            for sub in subs:
                if twl.check(sub):
                    l+= len(sub)
                else:
                    l = 0
                    break
            if l != 0:
                resp.append((rest+w, l))
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
