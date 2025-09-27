from datetime import datetime
from app.ticket import (
    Ticket, 
    Discountable, 
    ElectronicTicket, 
    DiscountedTicket, 
    DiscountedElectronicTicket
)

def main():
    ticket1 = Ticket(1, 2, 3, 100)
    ticket2 = ElectronicTicket(2, 1, 3, 120, 'olesia@gmail.com')
    ticket3 = DiscountedTicket(3, 1, 4, 150, 0.2)
    ticket4 = DiscountedElectronicTicket(4, 2, 5, 200, 'sophia@gmail.com', 0.3)

    print(Ticket.help())
    
    ticket1.purchase(datetime.now())
    ticket2.purchase(datetime.now())
    ticket3.purchase(datetime.now())
    ticket4.purchase(datetime.now())

    print(Ticket.help())

    
if __name__ == "__main__":
    main()

