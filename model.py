class Grocery:
    def __init__(self,_id=0,name='',price='',img=None,types='',quantity=''):
        self.grocId = _id
        self.grocName = name
        self.grocPrice = price
        self.grocImg = img
        self.grocType = types
        self.grocQuantity = quantity

    def __repr__(self):
        return f'Grocery[{self.grocId},{self.grocName},{self.grocPrice},{self.grocImg},{self.grocType},{self.grocQuantity}]'


# SQL QUERY  
'''
CREATE DATABASE GROCERYDB;

 CREATE TABLE `grocery` (
  `grocId` int(11) NOT NULL AUTO_INCREMENT,
  `grocName` varchar(50) DEFAULT NULL,
  `grocPrice` double(10,2) DEFAULT NULL,
  `grocImg` varchar(100) DEFAULT NULL,
  `grocType` varchar(50) DEFAULT NULL,
  `grocQuantity` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`grocId`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4;
'''
  



      

    


    
