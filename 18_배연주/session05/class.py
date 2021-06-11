class Schedule:
    def __init__(self, day, title, start):
        self.day = day
        self.title = title
        self.start = start

    def showSchedule(self):
        print(f'{self.day}요일 일정 : {self.start}시에 {self.title}')

    def reschedule(self, option, time):
        start = self.start
        if option == '+':
            self.start += time
            print(f'{self.day}요일 {start}시에 예정되어 있던 {self.title} 시간이 {self.start}시로 미뤄졌습니다.')
        elif option == '-':
            self.start -= time
            print(f'{self.day}요일 {start}시에 예정되어 있던 {self.title} 시간이 {self.start}시로 앞당겨졌습니다.')


PS = Schedule("화", "알고리즘 스터디", 22)
Lion = Schedule("수", "멋사 세션", 19)

PS.showSchedule()
Lion.showSchedule()

PS.reschedule('-', 2)
Lion.reschedule('+', 1)
