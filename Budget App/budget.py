

def create_spend_chart(categories):
  spend = []
  for category in categories:
    temp = 0
    for item in category.ledger:
      if item['amount'] < 0:
        temp += abs(item['amount'])
    spend.append(temp)
  
  total = sum(spend)
  percentage = [i/total * 100 for i in spend]

  s = "Percentage spent by category"
  for i in range(100, -1, -10):
    s += "\n" + str(i).rjust(3) + "|"
    for j in percentage:
      if j > i:
        s += " o "
      else:
        s += "   "
    # Spaces
    s += " "
  s += "\n    ----------"

  cat_length = []
  for cat in categories:
    
    cat_length.append(len(cat.name))
  max_length = max(cat_length)

  for i in range(max_length):
    s += "\n    "
    for j in range(len(categories)):
      if i < cat_length[j]:
        s += " " + categories[j].name[i] + " "
      else:
        s += "   "
    # Spaces
    s += " "

  return s
  

class Category:
    def __init__(self,name):
        self.name=name
        self.ledger=[]
        
    def __str__(self):
      title=f'{self.name:*^30}\n'
      sum=0
      items=""
      for item in self.ledger:
          items += f"{item['description'][0:23]:23}{item['amount']:7.2f}" + '\n'
          sum+=item['amount']

      output=title + items + 'Total: ' + str(sum)
      return output
    
    def deposit(self, amt, des=""):
        self.ledger.append({'amount':amt, 'description':des})
        
    def withdraw(self, amt, des=""):
        
        if (self.check_funds(amt)):
           self.ledger.append({'amount':-amt, 'description':des}) 
           return True
        return False   
            
    def get_balance(self):
        total=0
        for item in self.ledger:
            total+=item['amount']
        return total
    
    def transfer(self,amt, category):
        if self.check_funds(amt):
            self.withdraw(amt,'Transfer to ' +category.name)
            category.deposit(amt,'Transfer from '+ self.name)
            return True
        return False
        
    def check_funds(self, amt):
        if self.get_balance()>=amt:
            return True
        return False  

