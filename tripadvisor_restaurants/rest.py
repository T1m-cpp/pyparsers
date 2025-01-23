class Restaurant:
    def __init__(self, name, rating, reviews_count, address, phone, cuisines):
        self.name = name
        self.rating = rating
        self.reviews_count = reviews_count  # Количество отзывов
        self.address = address
        self.phone = phone
        self.cuisines = cuisines

    def __repr__(self):
        return f"Restaurant(name='{self.name}', rating='{self.rating}', address='{self.address}', phone='{self.phone}', cuisines={self.cuisines})"
