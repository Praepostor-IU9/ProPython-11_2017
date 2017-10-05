import random
import sys

class Team():
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.goal = 0
        self.skip = 0
        self.win = 0
        self.draw = 0
        self.loss = 0
    def addResult(self, a, b):
        self.goal += a
        self.skip += b
        if a == b:
            self.score += 1
            self.draw += 1
        elif a > b:
            self.score += 3
            self.win += 1
        else:
            self.loss += 1
class Championship():
    def __init__(self, Teams = [], delta_random = 3):
        self.Teams_map = {}
        self.Teams = []
        self.maxLen = 0
        if Teams:
            i = 0
            for T in Teams:
                if len(T) > self.maxLen:
                    self.maxLen = len(T)
                self.Teams.append(Team(T))
                self.Teams_map[T] = i
                i += 1
        else:
            T = input('Введите названия команд:\n')
            i = 0
            while T:
                if len(T) > self.maxLen:
                    self.maxLen = len(T)
                self.Teams.append(Team(T))
                self.Teams_map[T] = i
                i += 1
                T = input()
        self.delta_random = delta_random
        self.matches = [None]*(len(self.Teams)*(len(self.Teams)-1)//2)
        
        a = b = 0
        for i in range(len(self.Teams)):
            for j in range(i+1, len(self.Teams)):
                a = random.randint(0, self.delta_random)
                b = random.randint(0, self.delta_random)
                self.matches[i*len(self.Teams)+(j-i-1)-i*(i+1)//2] = [a, b]
                self.Teams[i].addResult(a, b)
                self.Teams[j].addResult(b, a)

    def _NewMaches(self):
        a = b = 0
        for i in range(len(self.Teams)):
            for j in range(i, len(self.Teams)):
                a = random.randint(0, self.delta_random)
                b = random.randint(0, self.delta_random)
                self.matches[i*len(self.Teams)+(j-i-1)-i*(i+1)//2] = [a, b]
                self.Team[i].addResult(a, b)
                self.Team[j].addResult(b, a)

    def __getitem__(self, key):
        r = ''
        if type(key) == str:
            a = b = 0
            r = 'Команда '+key+'\n'
            r += 'Результаты:\n'
            j = self.Teams_map[key]
            for i in range(j):
                [a, b] = self.matches[i*len(self.Teams)+(j-i-1)-i*(i+1)//2]
                r += '%+*s vs %-*s => %d:%d\n' % (self.maxLen, key, self.maxLen, self.Teams[i].name, b, a)
                
            for i in range(j+1, len(self.Teams)):
                [a, b] = self.matches[j*len(self.Teams)+(i-j-1)-j*(j+1)//2]
                r += '%+*s vs %-*s => %d:%d\n' % (self.maxLen, key, self.maxLen, self.Teams[i].name, a, b)
        elif type(key) == tuple:
            (key1, key2) = key
            j = self.Teams_map[key1]
            i = self.Teams_map[key2]
            if i > j:
                [a, b] = self.matches[j*len(self.Teams)+(i-j-1)-j*(j+1)//2]
                r = '%+*s vs %-*s => %d:%d\n' % (self.maxLen, key1, self.maxLen, key2, a, b)
            elif i < j:
                [a, b] = self.matches[i*len(self.Teams)+(j-i-1)-i*(i+1)//2]
                r = '%+*s vs %-*s => %d:%d\n' % (self.maxLen, key1, self.maxLen, key2, b, a)
        return r
    def __str__(self):
        win_Rating = sorted(self.Teams, key=lambda x: (x.score, x.win, x.goal-x.skip, x.goal), reverse = True)
        result = 'Результаты чемпионата:\n\n'
        k = len(str(len(self.Teams)))
        m = max(self.maxLen+1, 16)
        result += '┌'+'─'*k+'┬'+'─'*m+'┬────┬──────┬─────┬──────┬────────┬────┐\n'
        result += '│%-*s│%-*s' % (k, '№', m, 'Название команды')
        result += '│Игры│Победы│Ничьи│Пораж.│  Мячи  │Очки│\n'
        i = 1
        for com in win_Rating:
            result += '├'+'─'*k+'┼'+'─'*m+'┼────┼──────┼─────┼──────┼────────┼────┤\n'
            result += '│%*d│%-*s│%*d│%*d│%*d│%*d│%*d--%-*d│%*d│\n' % (k, i, m, com.name, 4, len(win_Rating)-1, 6, com.win, 5, com.draw, 6, com.loss, 3, com.goal, 3, com.skip, 4, com.score)
            i += 1
        result += '└'+'─'*k+'┴'+'─'*m+'┴────┴──────┴─────┴──────┴────────┴────┘\n'
        return result
    
if __name__ == "__main__":
    C = Championship(sys.argv[1:])
    print(C)
    print("Чтобы посмотреть результаты матча между командой_1 и командой_2, введите print(C['команда_1', 'команда_2'])")
    print("Чтобы посмотреть результаты матчей команды_1, введите print(C['команда_1'])")
