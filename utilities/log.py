import os
from datetime import datetime

class LogMixin:
    """
    Classe para gerenciar logs de ações de usuários.
    """

    def add(self, message):
        """
        Adiciona uma ação ao arquivo de log.

        A ação é registrada com a data e hora atuais no formato 'mm/dd/yyyy | hh:mm:ss'.

        Parameters:
            message (str): Texto que será escrito no arquivo referente a ação efetuada pelo usuário
        """
        
        # Verifica se o arquivo existe, se não existir, cria o arquivo
        if not os.path.exists(f'{self.username}.txt'):
            with open(f'{self.username}.txt', 'w') as file:
                file.write("Arquivo de log criado!\n")
        
        # Obtém a data e a hora no formato desejado
        timestamp = datetime.now().strftime("%m/%d/%Y | %H:%M:%S")

        # Formata a mensagem no formato especificado
        log_message = f"{timestamp} - {self.username}: {message}\n"

        # Adiciona a mensagem ao arquivo de log sem apagar os dados existentes
        with open(f'{self.username}.txt', 'a') as file:
            file.write(log_message)