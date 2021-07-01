class Rectangle:
    def __init__(self, width,height):
        self.width=width
        self.height=height
    
    def __str__(self):
        return "Rectangle(width=" + str(self.width) +", height=" + str(self.height)+")"
    
    def get_area(self):
        return self.width*self.height
    
    def set_width(self,width):
        self.width=width

    def set_height(self,height):
        self.height=height    

    def get_perimeter(self):
        return (2*self.width + 2*self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        pic=''
        if self.width>50 or self.height>50:
            return 'Too big for picture.'
        else:
            for i in range(self.height):
                for j in range(self.width):
                    pic+='*'
                pic+='\n'
            return pic      
            

    def get_amount_inside(self, shape):
        max_width = self.width // shape.width
        max_height = self.height // shape.height
        return max_width * max_height




class Square(Rectangle):
    def __init__(self,length):
        super().__init__(length,length)
    
    def __str__(self):
        return "Square(side="+ str(self.width)+")" 
        
    
    def set_side(self,length):
        self.width=length
        self.height=length
    
    
    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side   
        
