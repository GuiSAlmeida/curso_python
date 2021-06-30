class LogMixin:
    """
    cria um arquivo de log com infos e errors.
    """
    @staticmethod
    def write(msg):
        with open('log.log', 'a+') as f:
            f.write(msg)
            f.write('\n')

    def log_info(self, msg):
        """
        grava mensagem de info no arquivo
        :param msg:
        :return:
        """
        self.write(f'INFO: {msg}')


    def log_error(self, msg):
        """
        grava mensagem de erro no arquivo
        :param msg:
        :return:
        """
        self.write(f'ERROR: {msg}')
