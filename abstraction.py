from abc import ABC, abstractmethod

class book(ABC):
        @abstractmethod
        def tamil_book(self):
         pass
        @abstractmethod
        def english_book(self):
          pass   
class ponniyinselvan(book):
    def tamil_book(self):
        print("This is tamil_book----ponniyiselvan")
    def english_book(self):
        print("This not a english book")
class onedaylife(book):
    def english_book(self):
        print("This is english book----one day life")
    def tamil_book(self):
        print("This not a tamil book")

ponniyinselvan=ponniyinselvan()
onedaylife=onedaylife() 
ponniyinselvan.tamil_book() 
onedaylife.english_book( )                               