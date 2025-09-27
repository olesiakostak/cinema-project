class Ticket:
    def __init__(self, id, session_id, seat_id, base_price):
        self.id = id
        self.session_id = session_id
        self.seat_id = seat_id
        self.__base_price = base_price
        self.status = 'available'
        self.purchase_time = None

    def purchase(self, dt):
        if self.status == 'sold':
            return f'Ticket №{self.id} is already sold'
        self.status = 'sold'
        self.purchase_time = dt
        return f'Ticket №{self.id} is successfully sold!'

    @property
    def base_price(self):
        return self.__base_price

    @base_price.setter
    def base_price(self, price):
        self.__base_price = price

    def ticket_info(self):
        return f'Ticket № {self.id}: session {self.session_id}, seat {self.seat_id}, base_price {self.base_price}, status "{self.status}"'

    @staticmethod
    def help():
        return 'For buying a ticket you can use purchase() method'
    
class Discountable:
    def __init__(self, discount):
        self.discount = discount
    
    def apply_discount(self, price):
        return price * (1 - self.discount)
    
class ElectronicTicket(Ticket):
    def __init__(self, id, session_id, seat_id, base_price, email):
        super().__init__(id, session_id, seat_id, base_price)
        self.email = email

    def send_email(self):
        return f'Ticket №{self.id} sent to {self.email}'
    
    def ticket_info(self):
        return super().ticket_info() + f' email {self.email}'

class DiscountedTicket(Ticket, Discountable):
    def __init__(self, id, session_id, seat_id, base_price, discount=0):
        Ticket.__init__(self, id, session_id, seat_id, base_price)
        Discountable.__init__(self, discount)
    
    def final_price(self):
        return self.apply_discount(self.base_price)
    
    def ticket_info(self):
        return super().ticket_info() + f' final_price {self.final_price()}'
    
class DiscountedElectronicTicket(ElectronicTicket, Discountable):
    def __init__(self, id, session_id, seat_id, base_price, email, discount=0):
        ElectronicTicket.__init__(self, id, session_id, seat_id, base_price, email)
        Discountable.__init__(self, discount)

    def final_price(self):
        return self.apply_discount(self.base_price)
    
    def ticket_info(self):
        return super().ticket_info() + f' final price {self.final_price()}'