#! /usr/bin/python
# -*- utf-8 -*-

import sys

class PorterStemmer():
    def __init__(self):
        self.b = '' # buffer for word to be stemmed
        self.k = 0 # end-point of the word string
        self.k0 = 0 #
        self.j = 0 # general offset into the string

    def cons(self, i):
        """cons(i) is TRUE <=> b[i] is a consonant"""
        # FALSE if not consonant
        if self.b[i] in (('a','e','i','o','u')):
            return 0
        # y is a consonant when it is the first letter of a syallable
        if self.b[i] == 'y':
            if self.k0 == 0:
                return 1
            else:
                return (not self.cons(i-1))
        return 1

    def cons_seq_counter(self):
        """cons_seq_counter() measures the number of consonant sequence between
        k0 and j. if c is a consonant sequence and v a vowel sequence, and <...>
        indicates arbitrary presence:

            <c><v> gives 0
            <c>vc<v> gives 1
            <c>vcvc<v> gives 2
            <c>vcvcvc<v> gives 3
            ...
        """
        n = 0 # number of consonant sequence
        i = self.k0
        while True: # check the first consonant sequence
            if i > self.j: # out of range
                return n
            if not self.cons(i): # end of first consonant sequence
                break
            i += 1
        i += 1
        while True:
            while True: # check the vowel sequence
                if i > self.j: # out of range
                    return n
                if self.cons(i): # end of vowel sequence
                    break
                i += 1
            i += 1
            n += 1
            while True: # check the consonant sequence
                if i > self.j: # out of range
                    return n
                if not self.cons(i): # end of consonant sequence
                    break
                i += 1
            i += 1

    def vowel_in_stem(self):
        """vowel_in_stem() is TRUE <=> k0,...,j contains a vowel"""
        for i in range(self.k0, self.j+1):
            if not self.cons(i):
                return 1
        return 0

    def double_cons(self, j):
        """double_cons() is TRUE <=> j, j-1 contian a double consonant"""
        if j < (self.k0+1): # out of range
            return 0
        if (self.b[j] != self.b[j-1]): # FALSE if not double
            return 0
        return self.cons(j)

    def cvc(self, i):
        """cvc(i) is TRUE <=> i-2, i-1, i has the form consonant-vowel-consonant
        and also if the second consonant is not w, x or y. this is used when
        trying to restore an e at the end of a short:

            cav(e), lov(e), hop(e), crim(e), but
            snow, box, tray.
        """
        if i < (self.k0 + 2): # out of range
            return 0
        if not self.cons(i) or self.cons(i-1) or not self.cons(i-2):
            return 0
        ch = self.b[i]
        if ch in (('w','x','y')):
            return 0
        return 1

    def ends_with(self, s):
        """ends_with_s(s) is TRUE <=> k0,...,k ends with the string s"""
        length = len(s)
        if s[length-1] != self.b[self.k]: # tiny speed up
            return 0
        if length > (self.k - self.k0 + 1): # out of range
            return 0
        if self.b[self.k-length+1:self.k+1] != s:
            return 0
        self.j = self.k - length
        return 1

    def set_to(self, s):
        """set_to(s) sets (j+1),...,k to the characters in the string s"""
        length = len(s)
        self.b = self.b[:self.j+1] + s + self.b[self.j+length+1]
        self.k = self.j + length

    def r(self, s):
        """r(s) is used further down"""
        if self.cons_seq_counter() > 0:
            self.set_to(s)

    def step1ab(self):
        """step1ab() gets rid of plurals and -ed or -ing. e.g.

            caresses -> caress
            ponies -> poni
            ties -> ti
            caress -> caress
            cats -> cat

            feed -> feed
            agreed -> agree
            disabled -> disable

            matting -> mat
            mating -> mate
            meeting -> meet
            milling -> mill
            messing -> mess

            meetings -> mett
        """
        if self.b[self.k] == 's':
            if self.ends_with("sses"):
                self.k = self.k - 2
            elif self.ends_with("ies"):
                self.set_to("i")
            elif self.b[self.k-1] != 's':
                self.k = self.k - 1
        if self.ends_with("eed"):
            self.k = self.k - 1
        elif (self.ends_with('ed') or self.ends_with('ing')) \
            and self.vowel_in_stem():
            self.k = self.j
            if self.ends_with("at"):   self.set_to("ate")
            elif self.ends_with('bl'): self.set_to("ble")
            elif self.ends_with('iz'): self.set_to('ize')
            elif self.double_cons(self.k):
                self.k = self.k - 1
                ch = self.b[self.k]
                if ch in ('l','s','z'):
                    self.k = self.k + 1
            elif self.cons_seq_counter() == 1 and self.cvc(self.k):
                self.set_to('e')

    def step1c(self):
        """step1c() turns terminaly y to i when there is another vowel in the
        stem"""
        if (self.ends_with('y') and self.vowel_in_stem()):
            self.b = self.b[:self.k] + 'i' + self.b[self.k+1:]

    def step2(self):
        """step2() maps double suffices to single ones"""
        if self.b[self.k - 1] == 'a':
            if self.ends_with("ational"):   self.r("ate")
        elif self.ends_with("tional"):  self.r("tion")
        elif self.b[self.k - 1] == 'c':
            if self.ends_with("enci"):      self.r("ence")
            elif self.ends_with("anci"):    self.r("ance")
        elif self.b[self.k - 1] == 'e':
            if self.ends_with("izer"):      self.r("ize")
        elif self.b[self.k - 1] == 'l':
            if self.ends_with("bli"):       self.r("ble") # --DEPARTURE--
            # To match the published algorithm, replace this phrase with
            #   if self.ends_with("abli"):      self.r("able")
            elif self.ends_with("alli"):    self.r("al")
            elif self.ends_with("entli"):   self.r("ent")
            elif self.ends_with("eli"):     self.r("e")
        elif self.ends_with("ousli"):   self.r("ous")
        elif self.b[self.k - 1] == 'o':
            if self.ends_with("ization"):   self.r("ize")
            elif self.ends_with("ation"):   self.r("ate")
            elif self.ends_with("ator"):    self.r("ate")
        elif self.b[self.k - 1] == 's':
            if self.ends_with("alism"):     self.r("al")
            elif self.ends_with("iveness"): self.r("ive")
            elif self.ends_with("fulness"): self.r("ful")
            elif self.ends_with("ousness"): self.r("ous")
        elif self.b[self.k - 1] == 't':
            if self.ends_with("aliti"):     self.r("al")
            elif self.ends_with("iviti"):   self.r("ive")
            elif self.ends_with("biliti"):  self.r("ble")
        elif self.b[self.k - 1] == 'g': # --DEPARTURE--
            if self.ends_with("logi"):      self.r("log")
        # To match the published algorithm, delete this phrase

    def step3(self):
        """step3() dels with -ic-, -full, -ness etc."""
        if self.b[self.k] == 'e':
            if self.ends_with("icate"):     self.r("ic")
            elif self.ends_with("ative"):   self.r("")
            elif self.ends_with("alize"):   self.r("al")
        elif self.b[self.k] == 'i':
            if self.ends_with("iciti"):     self.r("ic")
        elif self.b[self.k] == 'l':
            if self.ends_with("ical"):      self.r("ic")
            elif self.ends_with("ful"):     self.r("")
        elif self.b[self.k] == 's':
            if self.ends_with("ness"):      self.r("")

    def step4(self):
        """step4() takes off -ant, -ence etc."""
        if self.b[self.k - 1] == 'a':
            if self.ends_with("al"): pass
            else: return
        elif self.b[self.k - 1] == 'c':
            if self.ends_with("ance"): pass
            elif self.ends_with("ence"): pass
            else: return
        elif self.b[self.k - 1] == 'e':
            if self.ends_with("er"): pass
            else: return
        elif self.b[self.k - 1] == 'i':
            if self.ends_with("ic"): pass
            else: return
        elif self.b[self.k - 1] == 'l':
            if self.ends_with("able"): pass
            elif self.ends_with("ible"): pass
            else: return
        elif self.b[self.k - 1] == 'n':
            if self.ends_with("ant"): pass
            elif self.ends_with("ement"): pass
            elif self.ends_with("ment"): pass
            elif self.ends_with("ent"): pass
            else: return
        elif self.b[self.k - 1] == 'o':
            if self.ends_with("ion") and (self.b[self.j] == 's' or self.b[self.j] == 't'): pass
            elif self.ends_with("ou"): pass
            # takes care of -ous
            else: return
        elif self.b[self.k - 1] == 's':
            if self.ends_with("ism"): pass
            else: return
        elif self.b[self.k - 1] == 't':
            if self.ends_with("ate"): pass
            elif self.ends_with("iti"): pass
            else: return
        elif self.b[self.k - 1] == 'u':
            if self.ends_with("ous"): pass
            else: return
        elif self.b[self.k - 1] == 'v':
            if self.ends_with("ive"): pass
            else: return
        elif self.b[self.k - 1] == 'z':
            if self.ends_with("ize"): pass
            else: return
        else:
            return
        if self.cons_seq_counter() > 1:
            self.k = self.j

    def step5(self):
        """step5() removes a final -e if m() > 1, and changes -ll to -l if
        m() > 1.
        """
        self.j = self.k
        if self.b[self.k] == 'e':
            a = self.cons_seq_counter()
            if a > 1 or (a == 1 and not self.cvc(self.k-1)):
                self.k = self.k - 1
        if self.b[self.k] == 'l' and self.double_cons(self.k) \
            and self.cons_seq_counter() > 1:
            self.k = self.k -1

    def stem(self, p, i, j):
        """In stem(p,i,j), p is a char pointer, and the string to be stemmed is
        from p[i] to p[j] inclusive. Typically i is zero and j is the offset to
        the last character of a string, (p[j+i]=='\0'). The stemmer adjust the
        character p[i],...,p[j] and returns the new end-point of the string, k.
        Stemming never increases word length, so i <= k <= j. To turn the
        stemmer into a module, declare 'stem' as exterm, and delete the
        remainder of this file.
        """
        self.b = p
        self.k = j
        self.k0 = i
        if self.k <= self.k0 + 1:
            return self.b

        self.step1ab()
        self.step1c()
        self.step2()
        self.step3()
        self.step4()
        self.step5()
        return self.b[self.k0:self.k+1]

if __name__ == '__main__':
    p = PorterStemmer()
    word = sys.argv[1]
    print p.stem(word, 0, len(word)-1)
    """
    if len(sys.argv) > 1:
        for f in sys.argv[1:]:
            infile = open(f, 'r')
            while 1:
                output = ''
                word = ''
                line = infile.readline()
                if line == '':
                    break
                for c in line:
                    if c.isalpha():
                        word += c.lower()
                    else:
                        if word:
                            output += p.stem(word, 0,len(word)-1)
                            word = ''
                        output += c.lower()
                print output,
            infile.close()
    """
