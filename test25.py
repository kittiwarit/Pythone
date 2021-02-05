class Nisit:
    def __init__(self,name,surename,year,branch,sex) :
        self.name =  name
        self.surename = surename
        self.year = year
        self.branch = branch
        self.sex = sex
    def  ShowNisit(self) :
        print('Nisit information')
        print('name :',self.name)
        print('surename :',self.surename)
        print('year :',self.year)
        print('branch',self.branch)
        print('sex :',self.sex)

x = Nisit('kittiwarit','akksela','1','ED computer','male')
x.ShowNisit()