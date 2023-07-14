from src.models.restaurant import Restaurant


class TestRestaurant:

    def test_describe_restaurant(self):
        restaurant_name = 'Sabor Amazônico'
        cuisine_type = 'Peixes'
        number_served = '0'
        resultado_esperado = f"Esse restaurante se chama {restaurant_name} e serve {cuisine_type}." \
                             f" Esse restaurante está servindo {number_served} consumidores desde que está aberto."
        restaurant = Restaurant(restaurant_name, cuisine_type)

        # chamada
        resultado = restaurant.describe_restaurant()

        assert resultado_esperado == resultado

    def test_open_restaurant(self):
        restaurant_name = 'Sabor Amazônico'
        cuisine_type = "Peixes"
        resultado_esperado = f"{restaurant_name} agora está aberto!"
        restaurant = Restaurant(restaurant_name, cuisine_type)

        # Chamada
        resultado = restaurant.open_restaurant()

        assert resultado_esperado == resultado

    def test_already_open_restaurant(self):
        restaurant_name = 'Sabor Amazônico'
        cuisine_type = "Peixes"
        resultado_esperado = f"{restaurant_name} já está aberto!"
        restaurant = Restaurant(restaurant_name, cuisine_type)

        # Chamada
        resultado = restaurant.open_restaurant()
        resultado = restaurant.open_restaurant()

        assert resultado_esperado == resultado

    def test_close_restaurant(self):
        restaurant_name = 'Sabor Amazônico'
        cuisine_type = "Peixes"
        resultado_esperado = f"{restaurant_name} agora está fechado!"
        restaurant = Restaurant(restaurant_name, cuisine_type)

        # Chamada
        resultado = restaurant.close_restaurant()

        assert resultado_esperado == resultado

    def test_already_close_restaurant(self):
        restaurant_name = 'Sabor Amazônico'
        cuisine_type = "Peixes"
        resultado_esperado = f"{restaurant_name} já está fechado!"
        restaurant = Restaurant(restaurant_name, cuisine_type)

        # Chamada
        resultado = restaurant.close_restaurant()
        resultado = restaurant.close_restaurant()

        assert resultado_esperado == resultado

    def test_set_number_served(self):
        restaurant_name = 'Sabor Amazônico'
        cuisine_type = "Peixes"
        total_customers = '40'
        resultado_esperado = f"Foram atendidas {total_customers} pessoas até o momento!"
        restaurant = Restaurant(restaurant_name, cuisine_type)

        # Chamada
        resultado = restaurant.set_number_served(total_customers)

        assert resultado_esperado == resultado

    def test_set_number_served_closed(self):
        restaurant_name = 'Sabor Amazônico'
        cuisine_type = "Peixes"
        total_customers = '0'
        resultado_esperado = f"{restaurant_name} está fechado!"
        restaurant = Restaurant(restaurant_name, cuisine_type)

        # Chamada
        resultado = restaurant.set_number_served(total_customers)
        resultado = restaurant.set_number_served(total_customers)

        assert resultado_esperado == resultado

    def test_increment_number_served(self):
        restaurant_name = 'Sabor Amazônico'
        cuisine_type = "Peixes"
        total_customers = '30'
        more_customers = '14'
        numbers_served = int(total_customers) + int(more_customers)

        resultado_esperado = f"Foram atendidas o total de {numbers_served} pessoas neste restaurante"
        restaurant = Restaurant(restaurant_name, cuisine_type)

        # Chamada
        resultado = restaurant.increment_number_served(total_customers, more_customers)

        assert resultado_esperado == resultado

    def test_increment_number_served_close(self):
        restaurant_name = 'Sabor Amazônico'
        cuisine_type = "Peixes"
        total_customers = '30'
        more_customers = '14'
        numbers_served = int(total_customers) + int(more_customers)

        resultado_esperado = f"{restaurant_name} está fechado!"
        restaurant = Restaurant(restaurant_name, cuisine_type)

        # Chamada
        resultado = restaurant.increment_number_served(total_customers, more_customers)
        resultado = restaurant.increment_number_served(total_customers, more_customers)

        assert resultado_esperado == resultado
