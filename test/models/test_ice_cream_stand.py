from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand:

    def test_flavors_available_sucess(self):
        restaurant_name = 'Danis Ice Cream Palor'
        cuisine_type = 'Sorvete'
        flavors_list = ['Açaí', 'Cupuaçu', 'Tucumã', 'Taberebá', 'Chocolate', 'Limão', 'Graviola']
        resultado_esperado = f"\n No momento temos os seguintes sabores de sorvete disponíveis: {flavors_list}"
        ice_cream_stand = IceCreamStand(restaurant_name, cuisine_type, flavors_list)

        # Chamada
        resultado = ice_cream_stand.flavors_available()

        assert resultado_esperado == resultado

    def test_no_flavors_no_available(self):
        restaurant_name = 'Danis Ice Cream Palor'
        cuisine_type = 'Sorvete'
        flavors_list = []
        resultado_esperado = "Estamos sem estoque atualmente!"
        ice_cream_stand = IceCreamStand(restaurant_name, cuisine_type, flavors_list)

        # Chamada
        resultado = ice_cream_stand.flavors_available()

        assert resultado_esperado == resultado

    def test_find_flavor_sucess(self):
        restaurant_name = 'Danis Ice Cream Palor'
        cuisine_type = 'Sorvete'
        flavors_list = ['Açaí', 'Cupuaçu', 'Tucumã', 'Taberebá', 'Chocolate']
        flavor = 'Tucumã'
        resultado_esperado = f"Temos no momento {flavor}!"
        ice_cream_stand = IceCreamStand(restaurant_name, cuisine_type, flavors_list)

        # Chamada
        resultado = ice_cream_stand.find_flavor(flavor)

        assert resultado_esperado == resultado

    def test_find_flavor_no_stock(self):
        restaurant_name = 'Danis Ice Cream Palor'
        cuisine_type = 'Sorvete'
        flavors_list = []
        flavor = 'Cajá'
        resultado_esperado = "Estamos sem estoque atualmente!"
        ice_cream_stand = IceCreamStand(restaurant_name, cuisine_type, flavors_list)

        # Chamada
        resultado = ice_cream_stand.find_flavor(flavor)

        assert resultado_esperado == resultado

    def test_add_flavor_available(self):
        restaurant_name = 'Danis Ice Cream Palor'
        cuisine_type = 'Sorvete'
        flavors_list = ['Açaí', 'Cupuaçu', 'Tucumã', 'Taberebá', 'Chocolate', 'Limão', 'Graviola']
        flavor = 'Cupuaçu'
        resultado_esperado = "\nSabor já disponivel!"
        ice_cream_stand = IceCreamStand(restaurant_name, cuisine_type, flavors_list)

        # Chamada
        resultado = ice_cream_stand.add_flavor(flavor)

        assert resultado_esperado == resultado

    def test_add_flavor_stock(self):
        restaurant_name = 'Danis Ice Cream Palor'
        cuisine_type = 'Sorvete'
        flavors_list = ['Açaí', 'Cupuaçu', 'Tucumã', 'Taberebá', 'Chocolate', 'Limão', 'Graviola']
        flavor = 'Flocos'
        resultado_esperado = f"{flavor} adicionado ao estoque!"
        ice_cream_stand = IceCreamStand(restaurant_name, cuisine_type, flavors_list)

        # Chamada
        resultado = ice_cream_stand.add_flavor(flavor)

        assert resultado_esperado == resultado

    def test_add_flavor_no_stock(self):
        restaurant_name = 'Danis Ice Cream Palor'
        cuisine_type = 'Sorvete'
        flavors_list = []
        flavor = 'Manga'
        resultado_esperado = "Estamos sem estoque atualmente!"
        ice_cream_stand = IceCreamStand(restaurant_name, cuisine_type, flavors_list)

        # Chamada
        resultado = ice_cream_stand.add_flavor(flavor)

        assert resultado_esperado == resultado
