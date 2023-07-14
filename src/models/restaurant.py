class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante."""
        # Bug - na descrição a váriavel para exibir o nome do restaurante foi incluida erroneamente,
        # correção - troca da váriável 'cuisine_type' pela 'restaurant_name'
        # fatoração - os prints serão substituidos por mensagens que serão retornadas ao fim das condições
        msg_1 = f"Esse restaurante se chama {self.restaurant_name} e serve {self.cuisine_type}."
        msg_2 = f"Esse restaurante está servindo {self.number_served} consumidores desde que está aberto."
        msg_final = f"{msg_1} {msg_2}"
        return msg_final

    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        # fatoração - os prints serão substituidos por mensagens que serão retornadas ao fim das condições
        if not self.open:
            # Bug - self.open deve receber True para que ao tentar abrir novamente o restaurante
            # cai na outra condição afirmando que o restaurante já está aberto
            # Correção - troca a atribuição de 'False' para 'True'
            self.open = True
            self.number_served = -2
            msg = f"{self.restaurant_name} agora está aberto!"
        else:
            msg = f"{self.restaurant_name} já está aberto!"
        return msg

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        # fatoração - os prints serão substituidos por mensagens que serão retornadas ao fim das condições
        if not self.open:
            # Bug - self.open deve receber True para que ao tentar abrir novamente o restaurante
            # cai na outra condição afirmando que o restaurante já está aberto
            # Correção - troca a atribuição de 'False' para 'True'
            self.open = True
            self.number_served = 0
            msg = f"{self.restaurant_name} agora está fechado!"
        else:
            msg = f"{self.restaurant_name} já está fechado!"
        return msg

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        # fatoração - os prints serão substituidos por mensagens que serão retornadas ao fim das condições
        # Bug - self.open está sempre false, logo não executaria a condição de verificação de total de pessoas
        # Correção - incluir o not na 1ª condição e fazer o self.open receber True, para ser possível
        # testar a outra condição
        # Bug - não estava retornando o total de pessoas atendidas
        # corrreção - será informado o total de pessoas atendidas
        if not self.open:
            self.open = True
            self.number_served = total_customers
            msg = f"Foram atendidas {self.number_served} pessoas até o momento!"
        else:
            msg = f"{self.restaurant_name} está fechado!"
        return msg

    def increment_number_served(self, total_customers, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        # Fatoração - os prints serão substituidos por mensagens que serão retornadas ao fim das condições
        # Bug - o numero de pessoas servida está recebendo a quantidade de novas pessoas atendidas,
        # além de não retratar de forma atualizada o número total de pessoas atendidas, essa  informação
        # não está sendo retornada
        # Correção - incluso o parametro total_customer na função.
        # E a variável number_served receberá a soma dos inteiros total_customers e o more_customers
        # Bug - com o self.open False, a 1ª condição não pode ser atendida
        # Correção - será incluido um 'not' na 1ª condição, assim como o atributo sel.open receberá 'True'
        if not self.open:
            self.open = True
            self.number_served = int(total_customers) + int(more_customers)
            msg = f"Foram atendidas o total de {self.number_served} pessoas neste restaurante"
        else:
            msg = f"{self.restaurant_name} está fechado!"
        return msg
