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
    print(ticket1.ticket_info())
    print(ticket2.ticket_info())
    print(ticket3.ticket_info())
    print(ticket4.ticket_info())

    print(ticket1.purchase(datetime.now()))
    print(ticket1.purchase(datetime.now()))
    print(ticket2.purchase(datetime.now()))
    print(ticket3.purchase(datetime.now()))
    print(ticket4.purchase(datetime.now()))

    print(Ticket.help())

    
if __name__ == "__main__":
    main()

