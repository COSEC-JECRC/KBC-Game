def lifeline(l, q, lcount, advote, half, flip, exadv):
    if lcount < 4:
        if l == 1:
            if advote != 0:
                lcount += 1
                advote -=1
                if q == 1:
                    vote = {'A': 13, 'B': 1, 'C': 6, 'D': 80}
                    print('The audience has the following opinions...')
                    print(vote)
                    a = input('Enter your option    ')
                    if a == 'd' or a == 'D':
                        print('You are right')
                        print('You have won 1000 Rs.')
                    else:
                        print('NO....Sorry to say but you are wrong')
                        return 0
                elif q == 2:
                    vote = {'A': 23 , 'B': 9, 'C': 8, 'D': 60}
                    print('The audience has the following opinions...')
                    print(vote)
                    a = input('Enter your option    ')
                    if a == 'd' or a == 'D':
                        print('You are right')
                        print('You have won 2000 Rs.')
                    else:
                        print('NO....Sorry to say but you are wrong')
                        return 0
                elif q == 3:
                    vote = {'A': 60, 'B': 9, 'C': 8, 'D': 23}
                    print('The audience has the following opinions...')
                    print(vote)
                    a = input('Enter your option    ')
                    if a == 'a' or a == 'A':
                        print('You are right')
                        print('You have won 3000 Rs.')
                    else:
                        print('NO....Sorry to say but you are wrong')
                        return 0
                elif q == 4:
                    vote = {'A': 9, 'B': 1, 'C': 75, 'D': 15}
                    print('The audience has the following opinions...')
                    print(vote)
                    a = input('Enter your option    ')
                    if a == 'c' or a == 'C':
                        print('You are right')
                        print('You have won 5000 Rs.')
                    else:
                        print('NO....Sorry to say but you are wrong')
                        return 0
                elif q == 5:
                    vote = {'A': 22, 'B': 1, 'C': 8, 'D': 69}
                    print('The audience has the following opinions...')
                    print(vote)
                    a = input('Enter your option    ')
                    if a == 'd' or a == 'D':
                        print('You are right')
                        print('You have won 10000 Rs.')
                    else:
                        print('NO....Sorry to say but you are wrong')
                        return 0
                elif q == 6:
                    vote = {'A': 9, 'B': 0, 'C': 81, 'D': 10}
                    print('The audience has the following opinions...')
                    print(vote)
                    a = input('Enter your option    ')
                    if a == 'c' or a == 'C':
                        print('You are right')
                        print('You have won 20000 Rs.')
                    else:
                        print('NO....Sorry to say but you are wrong')
                        return 0
                elif q == 7:
                    vote = {'A': 80, 'B': 1, 'C': 13, 'D': 6}
                    print('The audience has the following opinions...')
                    print(vote)
                    a = input('Enter your option    ')
                    if a == 'a' or a == 'A':
                        print('You are right')
                        print('You have won 40000 Rs.')
                    else:
                        print('NO....Sorry to say but you are wrong')
                        return 0
                elif q == 8:
                    vote = {'A': 13, 'B': 7, 'C': 7, 'D': 73}
                    print('The audience has the following opinions...')
                    print(vote)
                    a = input('Enter your option    ')
                    if a == 'd' or a == 'D':
                        print('You are right')
                        print('You have won 80000 Rs.')
                    else:
                        print('NO....Sorry to say but you are wrong')
                        return 0
                elif q == 9:
                    vote = {'A': 15, 'B': 25, 'C': 20, 'D': 40}
                    print('The audience has the following opinions...')
                    print(vote)
                    a = input('Enter your option    ')
                    if a == 'd' or a == 'D':
                        print('You are right')
                        print('You have won 160000 Rs.')
                    else:
                        print('NO....Sorry to say but you are wrong')
                        return 0
                elif q == 10:
                    vote = {'A': 62, 'B': 1, 'C': 2, 'D': 35}
                    print('The audience has the following opinions...')
                    print(vote)
                    a = input('Enter your option    ')
                    if a == 'a' or a == 'A':
                        print('You are right')
                        print('You have won 320000 Rs.')
                    else:
                        print('NO....Sorry to say but you are wrong')
                        return 0
                elif q == 11:
                    vote = {'A': 13, 'B': 8 , 'C': 74, 'D': 5}
                    print('The audience has the following opinions...')
                    print(vote)
                    a = input('Enter your option    ')
                    if a == 'c' or a == 'C':
                        print('You are right')
                        print('You have won 640000 Rs.')
                    else:
                        print('NO....Sorry to say but you are wrong')
                        return 0
                elif q == 12:
                    vote = {'A': 6, 'B': 1, 'C': 10, 'D': 83}
                    print('The audience has the following opinions...')
                    print(vote)
                    a = input('Enter your option    ')
                    if a == 'd' or a == 'D':
                        print('You are right')
                        print('You have won 1250000 Rs.')
                    else:
                        print('NO....Sorry to say but you are wrong')
                        return 0
                elif q == 13:
                    vote = {'A': 18, 'B': 1, 'C': 22, 'D': 59}
                    print('The audience has the following opinions...')
                    print(vote)
                    a = input('Enter your option    ')
                    if a == 'd' or a == 'D':
                        print('You are right')
                        print('You have won 2500000 Rs.')
                    else:
                        print('NO....Sorry to say but you are wrong')
                        return 0
                elif q == 14:
                    vote = {'A': 20, 'B': 29, 'C': 30, 'D': 21}
                    print('The audience has the following opinions...')
                    print(vote)
                    a = input('Enter your option    ')
                    if a == 'c' or a == 'C':
                        print('You are right')
                        print('You have won 5000000 Rs.')
                    else:
                        print('NO....Sorry to say but you are wrong')
                        return 0
                elif q == 15:
                    vote = {'A': 26, 'B': 21, 'C': 25, 'D': 28}
                    print('The audience has the following opinions...')
                    print(vote)
                    a = input('Enter your option    ')
                    if a == 'd' or a == 'D':
                        print('You are right')
                        print('You have won 10000000 Rs.')
                    else:
                        print('NO....Sorry to say but you are wrong')
                        return 0
                else:                                                     #Last Question
                    vote = {'A': 24, 'B': 25, 'C': 26, 'D': 25 }
                    print('The audience has the following opinions...')
                    print(vote)
                    a = input('Enter your option    ')
                    if a == 'c' or a == 'C':
                        print('You are right')
                        print('You have won 70000000 Rs.')
                    else:
                        print('NO....Sorry to say but you are wrong')
                        return 0
            else:
                print('You have already used this lifeline')
                print()
                print('Select a lifeline')
                print('1.AUDIENCE VOTE        2.50-50')
                print('3.FLIP THE QUESTION    4.EXPERT ADVICE')
                l = int(input('Enter the lifeline you want to use [1/2/3/4]'))
                lifeline(l, q, lcount, advote, half, flip, exadv)



        elif l == 2:
            if half != 0:
                lcount += 1
                half -= 1
                if q == 1:
                    print('Now you have the following options')
                    print('A.One                      B.              ')
                    print('C.                         D.Four          ')
                    a = input('Enter your option    ')
                    if a == 'd' or a == 'D':
                        print('You are right')
                        print('You have won 1000 Rs.')
                    else:
                        print('NO....Sorry to say but you are wrong')
                        return 0
                elif q == 2:
                    print('Now you have the following options')
                    print('A.Bharat Mata           B.                     ')
                    print('C.                      D.Bhagwan(God)          ')
                    a = input('Enter your option    ')
                    if a == 'd' or a == 'D':
                        print('You are right')
                        print('You have won 2000 Rs.')
                    else:
                        print('NO....Sorry to say but you are wrong')
                        return 0
                elif q == 3:
                    print('Now you have the following options')
                    print('A.Euro                   B.              ')
                    print('C.                       D.Lira          ')
                    a = input('Enter your option    ')
                    if a == 'a' or a == 'A':
                        print('You are right')
                        print('You have won 3000 Rs.')
                    else:
                        print('NO....Sorry to say but you are wrong')
                        return 0
                elif q == 4:
                    print('Now you have the following options')
                    print('A.                          B.')
                    print('C.Five Continents           D.Five Oceans')
                    a = input('Enter your option    ')
                    if a == 'c' or a == 'C':
                        print('You are right')
                        print('You have won 5000 Rs.')
                    else:
                        print('NO....Sorry to say but you are wrong')
                        return 0
                elif q == 5:
                    print('Now you have the following options')
                    print('A.5 August 2018         B.')
                    print('C.                      D.5August 2019')
                    a = input('Enter your option    ')
                    if a == 'd' or a == 'D':
                        print('You are right')
                        print('You have won 10000 Rs.')
                    else:
                        print('NO....Sorry to say but you are wrong')
                        return 0
                elif q == 6:
                    print('Now you have the following options')
                    print('A.                  B.')
                    print('C.Sikkim            D.Goa ')
                    a = input('Enter your option    ')
                    if a == 'c' or a == 'C':
                        print('You are right')
                        print('You have won 20000 Rs.')
                    else:
                        print('NO....Sorry to say but you are wrong')
                        return 0
                elif q == 7:
                    print('Now you have the following options')
                    print('A.Finger Print       B.')
                    print('C.                   D.Eye Colour          ')
                    a = input('Enter your option    ')
                    if a == 'a' or a == 'A':
                        print('You are right')
                        print('You have won 40000 Rs.')
                    else:
                        print('NO....Sorry to say but you are wrong')
                        return 0
                elif q == 8:
                    print('Now you have the following options')
                    print('A.Fivev               B.')
                    print('C.                    D.Zero          ')
                    a = input('Enter your option    ')
                    if a == 'd' or a == 'D':
                        print('You are right')
                        print('You have won 80000 Rs.')
                    else:
                        print('NO....Sorry to say but you are wrong')
                        return 0
                elif q == 9:
                    print('Now you have the following options')
                    print('A.                   B.Chakravarti')
                    print('C.                   D.Sudarshana Chakar          ')
                    a = input('Enter your option    ')
                    if a == 'd' or a == 'D':
                        print('You are right')
                        print('You have won 160000 Rs.')
                    else:
                        print('NO....Sorry to say but you are wrong')
                        return 0
                elif q == 10:
                    print('Now you have the following options')
                    print('A.Dhanbad               B.')
                    print('C.                      D.14 Varanasi')
                    a = input('Enter your option    ')
                    if a == 'a' or a == 'A':
                        print('You are right')
                        print('You have won 320000 Rs.')
                    else:
                        print('NO....Sorry to say but you are wrong')
                        return 0
                elif q == 11:
                    print('Now you have the following options')
                    print('A.2015                      B.')
                    print('C.2017                      D.')
                    a = input('Enter your option    ')
                    if a == 'c' or a == 'C':
                        print('You are right')
                        print('You have won 640000 Rs.')
                    else:
                        print('NO....Sorry to say but you are wrong')
                        return 0
                elif q == 12:
                    print('Now you have the following options')
                    print('A.Islam                 B.')
                    print('C.                      D.Janism')
                    a = input('Enter your option    ')
                    if a == 'd' or a == 'D':
                        print('You are right')
                        print('You have won 1250000 Rs.')
                    else:
                        print('NO....Sorry to say but you are wrong')
                        return 0
                elif q == 13:
                    print('Now you have the following options')
                    print('A.                      B.')
                    print('C.Shivank bhaiya        D.All of tha above')
                    a = input('Enter your option    ')
                    if a == 'd' or a == 'D':
                        print('You are right')
                        print('You have won 2500000 Rs.')
                    else:
                        print('NO....Sorry to say but you are wrong')
                        return 0
                elif q == 14:
                    print('Now you have the following options')
                    print('A.                     B.Hindi')
                    print('C.Malayalm             D.          ')
                    a = input('Enter your option    ')
                    if a == 'c' or a == 'C':
                        print('You are right')
                        print('You have won 5000000 Rs.')
                    else:
                        print('NO....Sorry to say but you are wrong')
                        return 0
                elif q == 15:
                    print('Now you have the following options')
                    print('A.Sept 22               B.')
                    print('C.                      D.Sept 8          ')
                    a = input('Enter your option    ')
                    if a == 'd' or a == 'D':
                        print('You are right')
                        print('You have won 10000000 Rs.')
                    else:
                        print('NO....Sorry to say but you are wrong')
                        return 0
                else:
                    print('Now you have the following options')
                    print('A.                           B.Louis Morgam')
                    print('C.Charles Babbage            D.          ')
                    a = input('Enter your option    ')
                    if a == 'c' or a == 'C':
                        print('You are right')
                        print('You have won 70000000 Rs.')
                    else:
                        print('NO....Sorry to say but you are wrong')
                        return 0

            else:
                print('You have already used this lifeline')
                print()
                print('Select a lifeline')
                print('1.*-*-*-*-*-*-*        2.50-50')
                print('3.FLIP THE QUESTION    4.EXPERT ADVICE')
                l = int(input('Enter the lifeline you want to use [2/3/4]'))
                lifeline(l, q, lcount, advote, half, flip, exadv)

        elif l == 3:
            if flip ==1:
                print('The new Question is on your screen now->')
                print()
                print('Que. Who is the only Woman Cheif Minister in India at present?')
                print('Your options are as follows:-')
                print('A.Mamta Benerjee          B.Nirmala Sitaraman')
                print('C.Sushma Swaraj           D.Vasundra Raje')
                a = input('Enter your option    ')
                if a == 'a' or a == 'A':
                    print('You are right')
                    if q == 1:
                        print('You have won 1000 Rs.')
                    elif q == 2:
                        print('You have won 2000 Rs.')
                    elif q == 3:
                        print('You have won 3000 Rs.')
                    elif q == 4:
                        print('You have won 5000 Rs.')
                    elif q == 5:
                        print('You have won 10000 Rs.')
                    elif q == 6:
                        print('You have won 20000 Rs.')
                    elif q == 7:
                        print('You have won 40000 Rs.')
                    elif q == 8:
                        print('You have won 80000 Rs.')
                    elif q == 9:
                        print('You have won 160000 Rs.')
                    elif q == 10:
                        print('You have won 320000 Rs.')
                    elif q == 11:
                        print('You have won 640000 Rs.')
                    elif q == 12:
                        print('You have won 1250000 Rs.')
                    elif q == 13:
                        print('You have won 2500000 Rs.')
                    elif q == 14:
                        print('You have won 5000000 Rs.')
                    elif q == 15:
                        print('You have won 10000000 Rs.')
                    else:
                        print('You have won 70000000 Rs.')
                else:
                    return 0
            else:
                print('You have already used this lifeline')
                print()
                print('Select a lifeline')
                print('1.AUDIENCE VOTE        2.50-50')
                print('3.FLIP THE QUESTION    4.EXPERT ADVICE')
                l = int(input('Enter the lifeline you want to use [1/2/3/4]'))
                lifeline(l, q, lcount, advote, half, flip, exadv)
        else:
            if exadv == 1:
                print('Expert opinion says')
                if q == 1:
                    print('You should go with option D')
                    a = input('Enter your option    ')
                    if a == 'd' or a == 'D':
                        print('You are right')
                        print('You have won 1000 Rs.')
                    else:
                        return 0
                elif q == 2:
                    print('You should go with option D')
                    a = input('Enter your option    ')
                    if a == 'd' or a == 'D':
                        print('You are right')
                        print('You have won 2000 Rs.')
                    else:
                        return 0
                elif q == 3:
                    print('You should go with option A')
                    a = input('Enter your option    ')
                    if a == 'a' or a == 'A':
                        print('You are right')
                        print('You have won 3000 Rs.')
                    else:
                        return 0
                elif q == 4:
                    print('You should go with option C')
                    a = input('Enter your option    ')
                    if a == 'c' or a == 'C':
                        print('You are right')
                        print('You have won 5000 Rs.')
                    else:
                        return 0
                elif q == 5:
                    print('You should go with option D')
                    a = input('Enter your option    ')
                    if a == 'd' or a == 'D':
                        print('You are right')
                        print('You have won 10000 Rs.')
                    else:
                        return 0
                elif q == 6:
                    print('You should go with option C')
                    a = input('Enter your option    ')
                    if a == 'c' or a == 'C':
                        print('You are right')
                        print('You have won 20000 Rs.')
                    else:
                        return 0
                elif q == 7:
                    print('You should go with option A')
                    a = input('Enter your option    ')
                    if a == 'a' or a == 'A':
                        print('You are right')
                        print('You have won 40000 Rs.')
                    else:
                        return 0
                elif q == 8:
                    print('You should go with option D')
                    a = input('Enter your option    ')
                    if a == 'd' or a == 'D':
                        print('You are right')
                        print('You have won 80000 Rs.')
                    else:
                        return 0
                elif q == 9:
                    print('You should go with option D')
                    a = input('Enter your option    ')
                    if a == 'd' or a == 'D':
                        print('You are right')
                        print('You have won 160000 Rs.')
                    else:
                        return 0
                elif q == 10:
                    print('You should go with option A')
                    a = input('Enter your option    ')
                    if a == 'a' or a == 'A':
                        print('You are right')
                        print('You have won 320000 Rs.')
                    else:
                        return 0
                elif q == 11:
                    print('You should go with option C')
                    a = input('Enter your option    ')
                    if a == 'c' or a == 'C':
                        print('You are right')
                        print('You have won 640000 Rs.')
                    else:
                        return 0
                elif q == 12:
                    print('You should go with option D')
                    a = input('Enter your option    ')
                    if a == 'd' or a == 'D':
                        print('You are right')
                        print('You have won 1250000 Rs.')
                    else:
                        return 0
                elif q == 13:
                    print('You should go with option D')
                    a = input('Enter your option    ')
                    if a == 'd' or a == 'D':
                        print('You are right')
                        print('You have won 2500000 Rs.')
                    else:
                        return 0
                elif q == 14:
                    print('You should go with option C')
                    a = input('Enter your option    ')
                    if a == 'c' or a == 'C':
                        print('You are right')
                        print('You have won 5000000 Rs.')
                    else:
                        return 0
                elif q == 15:
                    print('You should go with option D')
                    a = input('Enter your option    ')
                    if a == 'd' or a == 'D':
                        print('You are right')
                        print('You have won 10000000 Rs.')
                    else:
                        return 0
                else:
                    print('You should go with option C')
                    a = input('Enter your option    ')
                    if a == 'c' or a == 'C':
                        print('You are right')
                        print('You have won 70000000 Rs.')
                    else:
                        return 0

            else:
                print('You have already used this lifeline')
                print()
                print('Select a lifeline')
                print('1.AUDIENCE VOTE        2.50-50')
                print('3.FLIP THE QUESTION    4.EXPERT ADVICE')
                l = int(input('Enter the lifeline you want to use [1/2/3/4]'))
                lifeline(l, q, lcount, advote, half, flip, exadv)
    else:
        print('Sorry all Life Lines are used')
        return 1


def game(name, lcount, advote, half, flip, exadv):
    print('First Question for Rs. 1000 is on your screen now')
    print()
    print('Que.1 In the game of ludo the discs or tokens are of how many colours?')
    print('Your options are as follows:-')
    print('A.One           B.Two')
    print('C.Three         D.Four')
    q = 1
    a = input('Enter your option \n(To use a life line press l)\n(To quit press q)   ')
    if a == 'd' or a == 'D':
        print()
        print('You are right')
        print('You have won 1000 Rs.')
    elif a == 'l' or a == 'L':
        print('You have  following lifelines Lifelines')
        print('1.AUDIENCE VOTE        2.50-50')
        print('3.FLIP THE QUESTION    4.EXPERT ADVICE')
        l = int(input('Enter the lifeline you want to use [1/2/3/4]'))
        lr = lifeline(l, q, lcount, advote, half, flip, exadv)
        lcount += 1
        if l == 1:
            advote = 0
        elif l == 2:
            half = 0
        elif l == 3:
            flip = 0
        else:
            exadv = 0
        if lr == 0:
            return 0
        elif lr == 1:
            a = input('Enter your option \n(To quit press q)   ')
            if a == 'c' or a == 'C':
                print()
                print('You are right')
                print('You have won 1000 Rs.')
            elif a == 'q' or a == 'Q':
                print('So Mr.', name, "thanks for playing with us")
                return 0

            else:
                print('NO....Sorry to say but you are wrong')
                return 0

    elif a == 'q' or a == 'Q':
        print('So Mr.', name, "thanks for playing with us")
        return 0

    else:
        print('NO....Sorry to say but you are wrong')
        return 0

    print()
    print('\n\n\n\n\n\nSecond Question for Rs. 2000 is on your screen now')
    print()
    print('Que.2 In the Film “OMG Oh My God” Kanji Bhai filed a case against whom for the damage of his shop due to an earthquake ?')
    print('Your options are as follows:-')
    print('A.Bharat Mata                  B.Parliament(Bhartiya Sansad')
    print('C.Mumbai City                  D.Bhagwan(god)')
    a = input('Enter your option \n (To use a life line press l) \n(To quit press q)   ')
    q = 2
    if a == 'd' or a == 'D':
        print()
        print('You are right')
        print('You have won 2000 Rs.')
    elif a == 'l' or a == 'L':
        print('You have  following lifelines Lifelines')
        print('1.AUDIENCE VOTE        2.50-50')
        print('3.FLIP THE QUESTION    4.EXPERT ADVICE')
        l = int(input('Enter the lifeline you want to use [1/2/3/4]'))
        lr = lifeline(l, q, lcount, advote, half, flip, exadv)
        lcount += 1
        if l == 1:
            advote = 0
        elif l == 2:
            half = 0
        elif l == 3:
            flip = 0
        else:
            exadv = 0
        if lr == 0:
            return 0
        elif lr == 1:
            a = input('Enter your option \n(To quit press q)   ')
            if a == 'c' or a == 'C':
                print('You are right')
                print('You have won 2000 Rs.')
            elif a == 'q' or a == 'Q':
                print('So Mr.', name, "thanks for playing with us")
                return 1000

            else:
                print('NO....Sorry to say but you are wrong')
                return 0
    elif a == 'q' or a == 'Q':
        print('So Mr.', name, "thanks for playing with us")
        return 1000
    else:
        print('NO....Sorry to say but you are wrong')
        return 0

    print()
    print('\n\n\n\n\n\nThird Question for Rs. 3000 is on your screen now')
    print()
    print('Que.3 What has been e currency of Greece sine 2002?')
    print('Your options are as follows:-')
    print('A.Euro                B.Aburoad')
    print('C.Drachma             D.Lira')
    a = input('Enter your option \n (To use a life line press l) \n(To quit press q)   ')
    q = 3
    if a == 'a' or a == 'A':
        print()
        print('You are right')
        print('You have won 3000 Rs.')
    elif a == 'l' or a == 'L':
        print('You have  following lifelines Lifelines')
        print('1.AUDIENCE VOTE        2.50-50')
        print('3.FLIP THE QUESTION    4.EXPERT ADVICE')
        l = int(input('Enter the lifeline you want to use [1/2/3/4]'))
        lr = lifeline(l, q, lcount, advote, half, flip, exadv)
        lcount += 1
        if l == 1:
            advote = 0
        elif l == 2:
            half = 0
        elif l == 3:
            flip = 0
        else:
            exadv = 0
        if lr == 0:
            return 0
        elif lr == 1:
            a = input('Enter your option \n(To quit press q)   ')
            if a == 'c' or a == 'C':
                print('You are right')
                print('You have won 3000 Rs.')
            elif a == 'q' or a == 'Q':
                print('So Mr.', name, "thanks for playing with us")
                return 2000

            else:
                print('NO....Sorry to say but you are wrong')
                return 0
    elif a == 'q' or a == 'Q':
        print('So Mr.', name, "thanks for playing with us")
        return 2000
    else:
        print('NO....Sorry to say but you are wrong')
        return 0

    print()
    print('\n\n\n\n\n\nForth Question for Rs. 5000 is on your screen now')
    print()
    print('Que.4 What do the five rings of the Olympics represent?')
    print('Your options are as follows:-')
    print('A.Five Games                 B.Five Languages')
    print('C.Five Continents                  D.Five Oceans')
    a = input('Enter your option \n (To use a life line press l) \n(To quit press q)   ')
    q = 4
    if a == 'c' or a == 'C':
        print()
        print('You are right')
        print('You have won 5000 Rs.')
    elif a == 'l' or a == 'L':
        print('You have  following lifelines Lifelines')
        print('1.AUDIENCE VOTE        2.50-50')
        print('3.FLIP THE QUESTION    4.EXPERT ADVICE')
        l = int(input('Enter the lifeline you want to use [1/2/3/4]'))
        lr = lifeline(l, q, lcount, advote, half, flip, exadv)
        lcount += 1
        if l == 1:
            advote = 0
        elif l == 2:
            half = 0
        elif l == 3:
            flip = 0
        else:
            exadv = 0
        if lr == 0:
            return 0
        elif lr == 1:
            a = input('Enter your option \n(To quit press q)   ')
            if a == 'c' or a == 'C':
                print('You are right')
                print('You have won 5000 Rs.')
            elif a == 'q' or a == 'Q':
                print('So Mr.', name, "thanks for playing with us")
                return 3000

            else:
                print('NO....Sorry to say but you are wrong')
                return 0
    elif a == 'q' or a == 'Q':
        print('So Mr.', name, "thanks for playing with us")
        return 3000
    else:
        print('NO....Sorry to say but you are wrong')
        return 0

    print()
    print('\n\n\n\n\n\nFifth Question Rs. 10000 is on your screen now')
    print()
    print('Que.5 On which date was Article 370 removed by the Government?')
    print('Your options are as follows:-')
    print('A. 5 August 2018        B. 10 August 2019')
    print('C. 4 August 2019        D. 5 August 2019')
    a = input('Enter your option \n (To use a life line press l) \n(To quit press q)   ')
    q = 5
    if a == 'd' or a == 'D':
        print()
        print('You are right')
        print('You have won 10000 Rs.')
    elif a == 'l' or a == 'L':
        print('You have  following lifelines Lifelines')
        print('1.AUDIENCE VOTE        2.50-50')
        print('3.FLIP THE QUESTION    4.EXPERT ADVICE')
        l = int(input('Enter the lifeline you want to use [1/2/3/4]'))
        lr = lifeline(l, q, lcount, advote, half, flip, exadv)
        lcount += 1
        if l == 1:
            advote = 0
        elif l == 2:
            half = 0
        elif l == 3:
            flip = 0
        else:
            exadv = 0
        if lr == 0:
            return 0
        elif lr == 1:
            a = input('Enter your option \n(To quit press q)   ')
            if a == 'c' or a == 'C':
                print('You are right')
                print('You have won 10000 Rs.')
            elif a == 'q' or a == 'Q':
                print('So Mr.', name, "thanks for playing with us")
                return 5000

            else:
                print('NO....Sorry to say but you are wrong')
                return 0
    elif a == 'q' or a == 'Q':
        print('So Mr.', name, "thanks for playing with us")
        return 5000
    else:
        print('NO....Sorry to say but you are wrong')
        return 0

    print("\n\n\n\n\n\n")
    print("Congratulations Mr. ", name, "You have cleared the first checkpoint ")
    print()
    print('Now you will surely take away Rs. 10000 with you')

    print()
    print('Sixth Question for Rs. 20000 is on your screen now')
    print()
    print('Que.6 Which is the least populated state of India?')
    print('Your options are as follows:-')
    print('A.Manipur            B.Arunachal Pradesh')
    print('C.Sikkim             D.Goa')
    a = input('Enter your option \n (To use a life line press l) \n(To quit press q)   ')
    q = 6
    if a == 'c' or a == 'C':
        print()
        print('You are right')
        print('You have won 20000 Rs.')
    elif a == 'l' or a == 'L':
        print('You have  following lifelines Lifelines')
        print('1.AUDIENCE VOTE        2.50-50')
        print('3.FLIP THE QUESTION    4.EXPERT ADVICE')
        l = int(input('Enter the lifeline you want to use [1/2/3/4]'))
        lr = lifeline(l, q, lcount, advote, half, flip, exadv)
        lcount += 1
        if l == 1:
            advote = 0
        elif l == 2:
            half = 0
        elif l == 3:
            flip = 0
        else:
            exadv = 0
        if lr == 0:
            return 10000
        elif lr == 1:
            a = input('Enter your option \n(To quit press q)   ')
            if a == 'c' or a == 'C':
                print('You are right')
                print('You have won 20000 Rs.')
            elif a == 'q' or a == 'Q':
                print('So Mr.', name, "thanks for playing with us")
                return 10000

            else:
                print('NO....Sorry to say but you are wrong')
                return 10000
    elif a == 'q' or a == 'Q':
        print('So Mr.', name, "thanks for playing with us")
        return 10000
    else:
        print('NO....Sorry to say but you are wrong')
        return 10000

    print()
    print('\n\n\n\n\n\nSeventh Question for Rs. 40000 is on your screen now')
    print()
    print('Que.7 Which of these cannot be the same for two different persons ?')
    print('Your options are as follows:-')
    print('A.Finger Prints         B.Skin colour')
    print('C.Blood Group           D.Eye colour')
    a = input('Enter your option \n (To use a life line press l) \n(To quit press q)   ')
    q = 7
    if a == 'a' or a == 'A':
        print()
        print('You are right')
        print('You have won 40000 Rs.')
    elif a == 'l' or a == 'L':
        print('You have  following lifelines Lifelines')
        print('1.AUDIENCE VOTE        2.50-50')
        print('3.FLIP THE QUESTION    4.EXPERT ADVICE')
        l = int(input('Enter the lifeline you want to use [1/2/3/4]'))
        lr = lifeline(l, q, lcount, advote, half, flip, exadv)
        lcount += 1
        if l == 1:
            advote = 0
        elif l == 2:
            half = 0
        elif l == 3:
            flip = 0
        else:
            exadv = 0
        if lr == 0:
            return 10000
        elif lr == 1:
            a = input('Enter your option \n(To quit press q)   ')
            if a == 'c' or a == 'C':
                print('You are right')
                print('You have won 40000 Rs.')
            elif a == 'q' or a == 'Q':
                print('So Mr.', name, "thanks for playing with us")
                return 20000

            else:
                print('NO....Sorry to say but you are wrong')
                return 10000
    elif a == 'q' or a == 'Q':
        print('So Mr.', name, "thanks for playing with us")
        return 20000
    else:
        print('NO....Sorry to say but you are wrong')
        return 10000

    print()
    print('\n\n\n\n\n\nEighth Question for Rs. 80000 is on your screen now')
    print()
    print('Que.8 .How many bones does an elephant’s trunk have ?')
    print('Your options are as follows:-')
    print('A.Five               B.One')
    print('C.Ten                D.Zero')
    a = input('Enter your option \n (To use a life line press l) \n(To quit press q)   ')
    q = 8
    if a == 'd' or a == 'D':
        print()
        print('You are right')
        print('You have won 80000 Rs.')
    elif a == 'l' or a == 'L':
        print('You have  following lifelines Lifelines')
        print('1.AUDIENCE VOTE        2.50-50')
        print('3.FLIP THE QUESTION    4.EXPERT ADVICE')
        l = int(input('Enter the lifeline you want to use [1/2/3/4]'))
        lr = lifeline(l, q, lcount, advote, half, flip, exadv)
        lcount += 1
        if l == 1:
            advote = 0
        elif l == 2:
            half = 0
        elif l == 3:
            flip = 0
        else:
            exadv = 0
        if lr == 0:
            return 10000
        elif lr == 1:
            a = input('Enter your option \n(To quit press q)   ')
            if a == 'c' or a == 'C':
                print('You are right')
                print('You have won 80000 Rs.')
            elif a == 'q' or a == 'Q':
                print('So Mr.', name, "thanks for playing with us")
                return 40000

            else:
                print('NO....Sorry to say but you are wrong')
                return 10000
    elif a == 'q' or a == 'Q':
        print('So Mr.', name, "thanks for playing with us")
        return 40000
    else:
        print('NO....Sorry to say but you are wrong')
        return 10000

    print()
    print('\n\n\n\n\n\nNinth Question for Rs. 160000 is on your screen now')
    print()
    print('Que.9 What is the name of Lord Vishnu’s Chakra ?')
    print('Your options are as follows:-')
    print('A.Chakrapani                  C.Chakravarti')
    print('C.Surya Chandra               D.Sudarshana Chakar ')
    a = input('Enter your option \n (To use a life line press l) \n(To quit press q)   ')
    q = 9
    if a == 'd' or a == 'D':
        print()
        print('You are right')
        print('You have won 160000 Rs.')
    elif a == 'l' or a == 'L':
        print('You have  following lifelines Lifelines')
        print('1.AUDIENCE VOTE        2.50-50')
        print('3.FLIP THE QUESTION    4.EXPERT ADVICE')
        l = int(input('Enter the lifeline you want to use [1/2/3/4]'))
        lr = lifeline(l, q, lcount, advote, half, flip, exadv)
        lcount += 1
        if l == 1:
            advote = 0
        elif l == 2:
            half = 0
        elif l == 3:
            flip = 0
        else:
            exadv = 0
        if lr == 0:
            return 10000
        elif lr == 1:
            a = input('Enter your option \n(To quit press q)   ')
            if a == 'c' or a == 'C':
                print('You are right')
                print('You have won 160000 Rs.')
            elif a == 'q' or a == 'Q':
                print('So Mr.', name, "thanks for playing with us")
                return 80000

            else:
                print('NO....Sorry to say but you are wrong')
                return 10000
    elif a == 'q' or a == 'Q':
        print('So Mr.', name, "thanks for playing with us")
        return 80000
    else:
        print('NO....Sorry to say but you are wrong')
        return 10000

    print()
    print('\n\n\n\n\n\nTenth Question for Rs. 320000 is on your screen now')
    print()
    print('Que.10 Which city is wasseypur situated ?')
    print('Your options are as follows:-')
    print('A.Dhanbad            B.Ranchi')
    print('C.Patna            D.Varanasi')
    a = input('Enter your option \n (To use a life line press l)   ')
    q = 10
    if a == 'a' or a == 'A':
        print()
        print('You are right')
        print('You have won 320000 Rs.')
    elif a == 'l' or a == 'L':
        print('You have  following lifelines Lifelines')
        print('1.AUDIENCE VOTE        2.50-50')
        print('3.FLIP THE QUESTION    4.EXPERT ADVICE')
        l = int(input('Enter the lifeline you want to use [1/2/3/4]'))
        lr = lifeline(l, q, lcount, advote, half, flip, exadv)
        lcount += 1
        if l == 1:
            advote = 0
        elif l == 2:
            half = 0
        elif l == 3:
            flip = 0
        else:
            exadv = 0
        if lr == 0:
            return 10000
        elif lr == 1:
            a = input('Enter your option \n(To quit press q)   ')
            if a == 'c' or a == 'C':
                print('You are right')
                print('You have won 320000 Rs.')
            elif a == 'q' or a == 'Q':
                print('So Mr.', name, "thanks for playing with us")
                return 160000

            else:
                print('NO....Sorry to say but you are wrong')
                return 10000
    elif a == 'q' or a == 'Q':
        print('So Mr.', name, "thanks for playing with us")
        return 160000
    else:
        print('NO....Sorry to say but you are wrong')
        return 10000

    print("\n\n\n\n\n\n")
    print("Congratulations Mr. ", name, "You have cleared the Second checkpoint ")
    print()
    print('Now you will surely take away Rs. 320000 with you')

    print()
    print('Eleventh Question for Rs. 640000 is on your screen now')
    print()
    print('Que.11 When was "COSEC" comunity established at ju officially?')
    print('Your options are as follows:-')
    print('A.2015            B.2016 ')
    print('C.2017            D.2018')
    a = input('Enter your option \n (To use a life line press l) \n(To quit press q)   ')
    q = 11
    if a == 'c' or a == 'C':
        print()
        print('You are right')
        print('You have won 640000 Rs.')
    elif a == 'l' or a == 'L':
        print('You have  following lifelines Lifelines')
        print('1.AUDIENCE VOTE        2.50-50')
        print('3.FLIP THE QUESTION    4.EXPERT ADVICE')
        l = int(input('Enter the lifeline you want to use [1/2/3/4]'))
        lr = lifeline(l, q, lcount, advote, half, flip, exadv)
        lcount += 1
        if l == 1:
            advote = 0
        elif l == 2:
            half = 0
        elif l == 3:
            flip = 0
        else:
            exadv = 0
        if lr == 0:
            return 320000
        elif lr == 1:
            a = input('Enter your option \n(To quit press q)   ')
            if a == 'c' or a == 'C':
                print('You are right')
                print('You have won 640000 Rs.')
            elif a == 'q' or a == 'Q':
                print('So Mr.', name, "thanks for playing with us")
                return 320000

            else:
                print('NO....Sorry to say but you are wrong')
                return 320000
    elif a == 'q' or a == 'Q':
        print('So Mr.', name, "thanks for playing with us")
        return 320000
    else:
        print('NO....Sorry to say but you are wrong')
        return 320000

    print()
    print('\n\n\n\n\n\nTwelveth Question for Rs. 1250000 is on your screen now')
    print()
    print('Que.12 Bahubali festival is related to')
    print('Your options are as follows:-')
    print('A.Islam                    B.Hinduism')
    print('C.Buddhism                 D.Jainism')
    a = input('Enter your option \n (To use a life line press l) \n(To quit press q)   ')
    q = 12
    if a == 'd' or a == 'D':
        print()
        print('You are right')
        print('You have won 1250000 Rs.')
    elif a == 'l' or a == 'L':
        print('You have  following lifelines Lifelines')
        print('1.AUDIENCE VOTE        2.50-50')
        print('3.FLIP THE QUESTION    4.EXPERT ADVICE')
        l = int(input('Enter the lifeline you want to use [1/2/3/4]'))
        lr = lifeline(l, q, lcount, advote, half, flip, exadv)
        lcount += 1
        if l == 1:
            advote = 0
        elif l == 2:
            half = 0
        elif l == 3:
            flip = 0
        else:
            exadv = 0
        if lr == 0:
            return 320000
        elif lr == 1:
            a = input('Enter your option \n(To quit press q)   ')
            if a == 'c' or a == 'C':
                print('You are right')
                print('You have won 1250000 Rs.')
            elif a == 'q' or a == 'Q':
                print('So Mr.', name, "thanks for playing with us")
                return 640000

            else:
                print('NO....Sorry to say but you are wrong')
                return 320000
    elif a == 'q' or a == 'Q':
        print('So Mr.', name, "thanks for playing with us")
        return 640000
    else:
        print('NO....Sorry to say but you are wrong')
        return 320000

    print()
    print('\n\n\n\n\n\nThirteenth Question for Rs. 2500000 is on your screen now')
    print()
    print('Que.13 who invented "cosec" community at ju?')
    print('Your options are as follows:-')
    print('a.prashant bhaiya            b.akshay bhaiya')
    print('C.shivank bhaiya             D.all of the above')
    a = input('Enter your option \n (To use a life line press l) \n(To quit press q)   ')
    q = 13
    if a == 'd' or a == 'D':
        print()
        print('You are right')
        print('You have won 2500000 Rs.')
    elif a == 'l' or a == 'L':
        print('You have  following lifelines Lifelines')
        print('1.AUDIENCE VOTE        2.50-50')
        print('3.FLIP THE QUESTION    4.EXPERT ADVICE')
        l = int(input('Enter the lifeline you want to use [1/2/3/4]'))
        lr = lifeline(l, q, lcount, advote, half, flip, exadv)
        lcount += 1
        if l == 1:
            advote = 0
        elif l == 2:
            half = 0
        elif l == 3:
            flip = 0
        else:
            exadv = 0
        if lr == 0:
            return 320000
        elif lr == 1:
            a = input('Enter your option \n(To quit press q)   ')
            if a == 'c' or a == 'C':
                print('You are right')
                print('You have won 2500000 Rs.')
            elif a == 'q' or a == 'Q':
                print('So Mr.', name, "thanks for playing with us")
                return 1250000

            else:
                print('NO....Sorry to say but you are wrong')
                return 320000
    elif a == 'q' or a == 'Q':
        print('So Mr.', name, "thanks for playing with us")
        return 1250000
    else:
        print('NO....Sorry to say but you are wrong')
        return 320000

    print()
    print('\n\n\n\n\n\nFourteenth Question for Rs. 5000000 is on your screen now')
    print()
    print('Que.14 The language of Lakshadweep. a Union Territory of India, is?')
    print('Your options are as follows:-')
    print('A.Tamil                   B.Hindi')
    print('C.Malayalm                D.Telgu')
    a = input('Enter your option \n (To use a life line press l) \n(To quit press q)  ')
    q = 14
    if a == 'c' or a == 'C':
        print()
        print('You are right')
        print('You have won 5000000 Rs.')
    elif a == 'l' or a == 'L':
        print('You have  following lifelines Lifelines')
        print('1.AUDIENCE VOTE        2.50-50')
        print('3.FLIP THE QUESTION    4.EXPERT ADVICE')
        l = int(input('Enter the lifeline you want to use [1/2/3/4]'))
        lr = lifeline(l, q, lcount, advote, half, flip, exadv)
        lcount += 1
        if l == 1:
            advote = 0
        elif l == 2:
            half = 0
        elif l == 3:
            flip = 0
        else:
            exadv = 0
        if lr == 0:
            return 320000
        elif lr == 1:
            a = input('Enter your option \n(To quit press q)   ')
            if a == 'c' or a == 'C':
                print('You are right')
                print('You have won 5000000 Rs.')
            elif a == 'q' or a == 'Q':
                print('So Mr.', name, "thanks for playing with us")
                return 2500000

            else:
                print('NO....Sorry to say but you are wrong')
                return 320000
    elif a == 'q' or a == 'Q':
        print('So Mr.', name, "thanks for playing with us")
        return 2500000
    else:
        print('NO....Sorry to say but you are wrong')
        return 320000

    print()
    print('\n\n\n\n\n\nFifteenth Question for Rs. 10000000 is on your screen now')
    print()
    print('Que.15 The International Literacy Day is observed on?')
    print('Your options are as follows:-')
    print('A.Sept 22            B.Nov 28')
    print('C.May 2              D.Sep 8')
    a = input('Enter your option \n (To use a life line press l) \n(To quit press q)   ')
    q = 15
    if a == 'd' or a == 'D':
        print()
        print('You are right')
        print('You have won 10000000 Rs.')
    elif a == 'l' or a == 'L':
        print('You have  following lifelines Lifelines')
        print('1.AUDIENCE VOTE        2.50-50')
        print('3.FLIP THE QUESTION    4.EXPERT ADVICE')
        l = int(input('Enter the lifeline you want to use [1/2/3/4]'))
        lr = lifeline(l, q, lcount, advote, half, flip, exadv)
        lcount += 1
        if l == 1:
            advote = 0
        elif l == 2:
            half = 0
        elif l == 3:
            flip = 0
        else:
            exadv = 0
        if lr == 0:
            return 320000
        elif lr == 1:
            a = input('Enter your option \n(To quit press q)   ')
            if a == 'c' or a == 'C':
                print('You are right')
                print('You have won 10000000 Rs.')
            elif a == 'q' or a == 'Q':
                print('So Mr.', name, "thanks for playing with us")
                return 5000000

            else:
                print('NO....Sorry to say but you are wrong')
                return 320000
    elif a == 'q' or a == 'Q':
        print('So Mr.', name, "thanks for playing with us")
        return 5000000
    else:
        print('NO....Sorry to say but you are wrong')
        return 320000

    print()
    print('\n\n\n\n\n\nSixteenth Question for Rs. 70000000 is on your screen now')
    print()
    print("Que.16 who invented compact disk?")
    print('Your options are as follows:-')
    print('A.James.t.russel                 B.Louis Morgam')
    print('C.Charles Babbage                D.None of the above')
    a = input('Enter your option \n (To use a life line press l) \n(To quit press q)   ')
    q = 16
    if a == 'c' or a == 'C':
        print()
        print('You are right')
        print('You have won 70000000 Rs.')
    elif a == 'l' or a == 'L':
        print('You have  following lifelines Lifelines')
        print('1.AUDIENCE VOTE        2.50-50')
        print('3.FLIP THE QUESTION    4.EXPERT ADVICE')
        l = int(input('Enter the lifeline you want to use [1/2/3/4]'))
        lr = lifeline(l, q, lcount, advote, half, flip, exadv)
        lcount += 1
        if l == 1:
            advote = 0
        elif l == 2:
            half = 0
        elif l == 3:
            flip = 0
        else:
            exadv = 0
        if lr == 0:
            return 320000
        elif lr == 1:
            a = input('Enter your option \n(To quit press q)   ')
            if a == 'c' or a == 'C':
                print('You are right')
                print('You have won 70000000 Rs.')
            elif a == 'q' or a == 'Q':
                print('So Mr.', name, "thanks for playing with us")
                return 10000000

            else:
                print('NO....Sorry to say but you are wrong')
                return 320000
    elif a == 'q' or a == 'Q':
        print('So Mr.', name, "thanks for playing with us")
        return 10000000
    else:
        print('NO....Sorry to say but you are wrong')
        return 320000






def log_in() :
    user_name= input("Please enter your user name: ")
    f= open(str(user_name) + ".txt" , "r+")
    name=f.readline()
    f.readline()
    file_pass = f.readline()                                   #Previous(Real) password
    user_pass = input("Please enter your password: ")
    if file_pass == user_pass + "\n":                          #TO check weather the password is correct or not

        print('\n')
        print("\t\t\tWELCOME TO KBC")
        print('\n')
        print('\t\t    Kaun Banega Crorepati ')
        print('\n')
        print('\t\t    PRESENTED BY JU')
        print('\n')
        print('\t\tCO-SPONSERED BY COSEC JU')
        print('\n')
        print('\t       CREATED BY COSEC TEAM 2')
        print()
        # name = input('Sir/Mam Please Enter Your Name -> ')

        print()
        print('WELCOME', name)
        print()
        time.sleep(5)
        print("Read the instructions in 10sec\n")
        print('Before beginning the game,', end=' ')
        print('let us discuss the rules of the game->')
        print()
        print('1. There will be 15 Questions in the game,', end=' ')
        print('beginning from Rs. 1000 to Rs. 10000000')
        print('2. There will be Two Check Points in the game', end=' ')
        print('one at Question no. 5 and other at Question no. 10')
        print('3. After Crossing each Check Points you will surely', end='')
        print('take at least the CheckPoint Prize Amount with you')
        print('4. After Crossing the 2nd Checkpoint one more question', end=' ')
        print('i.e. Question no. 16 of Rs.70000000 will unlock')
        print('5. To help you out with typical questions there will be 4 life lines')
        print('   (i). AUDIENCE VOTE')
        print('   (ii). FLIP THE QUESTION')
        print('   (iii). EXPERT ADVICE')
        print('   (iv). 50-50')
        print('6. You can use only one lifeline at a time')
        print('7. After using a lifeline you cannot quit the game')
        print()
        time.sleep(10)
        print('So Mr. ', name, "let's begin KAUN BANEGA CROREPATI")
        x = input('Ready to Begin [y/n]  ')
        print()
        lcount = 0
        advote = 1
        half = 1
        exadv = 1
        flip = 1
        if x == 'y':
            result = game(name, lcount, advote, half, flip, exadv)
        else:
            print('Is this a kind of joke to you')
            x = input('Press y  ')
            if x == 'y':
                result = game(name, lcount, advote, half, flip, exadv)

        f.write(str(result).ljust(15,'-') + time.ctime() + "\n")
        f.close()


        print('So Mr. ', name, 'thanks for playing with us ')
        print('You have won Rs.', result)
        print('This Python Program is Created By COSEC TEAM 2')



        # print("Your account is loged in sucessfully")
    else :
         print("your ID or password is incorrect")
         f.close()
         again = input("If you want to log in again then  press y or if not then press n [y/n] ")
         if again == 'y':
             log_in()
         else :
              return 0









def creat_account ():
    name = input("Please enter your name: ")
    username = input("Please enter your user name you want to use: ")
    f=open(str(username) + ".txt" , 'w')

    f.write(name + "\n")
    emailid = input("Please enter your email ID: ")
    f.write(emailid + "\n")
    password1 = input("Please enter your password: ")
    password2 = input("Please re-enter your password: ")
    if password1 == password2 :
         f.write(password1 + "\n")
         # again = input("If you want to log in then  press y or if not then press n [y/n] ")
         # if again == 'y' :
         f.close()
         #     log_in()
         # else:
         return 0

    else:
        print("your password is incorrect")
        f.close()
        again = input("If you want to create account again then  press y or if not then press n [y/n] ")
        if again == 'y':
            creat_account()
        else:
            return 0








import time
print("Hello \n welcome to login / create account page")
account = input("If you have already have a account then press y of not then press n [y/n]: ")
if account == 'y' :
    log_in()
elif account =='n':
    creat_account()
else:
    print("Your input is WRONG")

# again = input("If you want to log in then  press y or if not then press n [y/n]:  ")
# if again == 'y' :
#     log_in()
















