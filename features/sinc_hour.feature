Feature: Ajustar o horário do Control ID
    Como um usuário do Control ID
    Eu quero ajustar o horário do sistema
    Para que ele esteja correto e sincronizado com a hora local

    Scenario: Ajustar o horário para o horário de Brasília
        Given que esteja logado no sistema do Control ID
        When eu acessar as configurações de horário
        And eu selecionar o horário de Brasília (GMT-3)
        And eu salvar as alterações
        Then o horário do sistema deve ser atualizado para o horário de Brasília
