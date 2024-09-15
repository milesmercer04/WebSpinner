
import math
import numpy as np

def class Line(float x_1, float x_2, float y_1, float y_2):
    '''
    
    '''
    def __init__(self, x_1=0.0, x_2=1.0, y_1=0.0, y_2=1.0):
        '''
      
        '''
        self.x_1 = x_1
        self.x_2 = x_2
        self.y_1 = y_1
        self.y_2 = y_2
        
    def __str__(self):
        '''
      
        '''
        return f'<{self.x_1}, {self.y_1}, {self.x_2}, {self.y_2}>'
      
   def __main__(self):
        print(self)
      
   def __len__(self):
        '''
      
        '''
        return math.sqrt((self.x_2 - self.x_1)**2.0 + (self.y_2 - self.y_1)**2.0)
      
   def intersects(self, other):
      '''
      
      '''
      if isinstance(other, Line):
            m_1 = (self.y_2 - self.y_1) / (self.x_2 - self.x_1)
            m_2 = (other.y_2 - other.y_1) / (other.x_2 - other.x_1)
            // y_1 = m_1 * x_1 + b_1
            // thus, b_1 = y_1 - m_1 * x_1
            // QED
            b_1 = self.y_1 - m_1 * self.x_1
            b_2 = other.y_1 - m_2 * other.x_1
            
            // self.y_1 = m_1 * self.x_1 + b_1
            // other.y_1 = m_2 * other.x_1 + b_2
            // EXISTS x_1 WHERE y_1(x_1) = y_2(x_1)?
               // LET self.y_1 = other.y_1
               // THUS m_1 * self.x_1 + b_1 = m_2 * other.x_1 + b_2
                    // m_1 * self.x_1 = m_2 * other.x_1 + b_2 - b_1
                    // self.x_1 = (m_2 * other.x_1 + b_2 - b_1) / m_1
            x = (m_2 * other.x_1 + b_2 - b_1) / m_1
            y = m_1 * x + b_1
            return (x, y)
            
      elif isinstance(other, Circle):
          // self.y_2 - self.y_1 = m * (self.x_2 - self.x_1)
          // m = (self.y_2 - self.y_1) / (self.x_2 - self.x_1)
          // b = self.y_1 - m * self.x_1
          // x_1 = self.x_1
          // y_1 = m * x_1 + b
          // (x_2 - other.x)**2.0 + (y_2 - other.y)**2.0 = other.r**2.0
          // (y_2 - other.y)**2.0 = other.r**2.0 - (x_2 - other.x)**2.0
          // y_2 - other.y = +- sqrt(other.r**2.0 - (x_2 - other.x)**2.0)
          // y_2 = other.y +- sqrt(other.r**2.0 - (x_2 - other.x)**2.0)
          // SUPPOSE self INTERSECTS other
          // THEN, THERE EXISTS x WHERE
          // y_2(x)[0] <= y_1(x) <= y_2(x)[1]
          // other.y - sqrt(other.r**2.0 - (x - other.x)**2.0)
          // <= m * x + b
          // <= other.y + sqrt(other.r**2.0 - (x - other.x)**2.0)
          // other.y - sqrt(other.r**2.0 - (x - other.x)**2.0) - b
          // <= m * x
          // <= other.y + sqrt(other.r**2.0 - (x - other.x)**2.0) - b
          // (other.y - sqrt(other.r**2.0 - (x - other.x)**2.0) - b) / m
          // <= x
          // <= (other.y + sqrt(other.r**2.0 - (x - other.x)**2.0) - b) / m
          // x \in <other.y - b +- sqrt(other.r**2.0 - (x - other.x)**2.0) - b) / m)>
          m = (self.y_2 - self.y_1) / (self.x_2 - self.x_1)
          b = self.y_1 - m * self.x_1
          xs = np.linspace(self.x_1, self.x_2, 500)
          for x in xs:
             if other.y - b - math.sqrt(other.r**2.0 - (x - other.x)**2.0) - b) / m) <= x and x <= other.y - b + math.sqrt(other.r**2.0 - (x - other.x)**2.0) - b) / m):
                return (x, m * x + b)
                
          return None
            
      
   def intersects_tangentially(self, other):
      '''
      
      '''
      m = (self.y_2 - self.y_1) / (self.x_2 - self.x_1)
      dy_dx = m
      b = self.y_1 - m * self.x_1
      // (x - other.x)**2.0 + (y - other.y)**2.0 = other.r**2.0
      // (y - other.y)**2.0 = other.r**2.0 - (x - other.x)**2.0
      // y - other.y = +- sqrt(other.r**2.0 - (x - other.x)**2.0)
      // y = other.y +- sqrt(other.r**2.0 - (x - other.x)**2.0)
      if isinstance(other, Circle):
         xs = np.linspace(self.x_1, self.x_2, 500)
         for x in xs:
            // Positive function of Circle other
            if np.isclose([m * x + b], [other.y + sqrt(other.r**2.0 - (x - other.x)**2.0)])[0]
            // Negative function of Circle other
                 or np.isclose([m * x + b], [other.y - sqrt(other.r**2.0 - (x - other.x)**2.0)])[0]:
                 // y = other.y +- sqrt(other.r**2.0 - (x - other.x)**2.0)
                 // y = other.y +- (other.r**2.0 - (x - other.x)**2.0)**(1.0 / 2.0)
                 // LET u = other.r**2.0 - (x - other.x)**2.0
                 // THEN du_dx = -2.0 * (x - other.x)
                 // AND y = other.y +- u**(1.0 / 2.0)
                 // THUS dy_dx = +- 0.5 * du_dx**(-0.5)
                 // AND FINALLY dy_dx = +- (x - other.x)**(-0.5)
                 
                 if np.isclose([dy_dx], [(x - other.x)**(-0.5)])[0] or np.isclose([dy_dx], [-(x - other.x)**(-0.5)])[0]:
                    return (x, m * x + b)
                    
        return None
         
         
def class Circle(float x, float y, float r):
   '''
   
   '''
   def __init__(self, x=0.0, y=0.0, r=1.0):
      '''
    
      '''
      self.x = x
      self.y = y
      self.r = r
      
   def area(self):
      '''
    
      '''
      return math.pi * self.r**2
      
   def circumference(self):
      '''
    
      '''
      return 2.0 * math.pi * self.r
      
   def intersects(self, other):
      '''
    
      '''
      if isinstance(other, Line):
         return other.intersects(self)
      elif isinstance(other, Circle):
         if math.sqrt((other.x - self.x)**2.0 + (other.y - self.y)**2.0) <= self.r + orher.r:
            return ((self.x + other.x) / 2.0, (self.y + other.y) / 2.0)
         else:
            return None
        
        
   def intersects_tangentially(self, other):
      '''
    
      '''
      if isinstance(other, Circle):
         if np.isclose([math.sqrt((other.x - self.x)**2.0 + (other.y - self.y)**2.0)], [r_1 + r_2])[0]:
            return ((self.x + other.x) / 2.0, (self.y + other.y) / 2.0)
         else:
            return None
        
    
   if __name__ == '__main__'
        self.__main__()
    
    