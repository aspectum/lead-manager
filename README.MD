python manage.py loaddata backend/fixtures/leadstatus_fixture.json



Ações frontend:
* mostrar lista de leads (tabela com a lead no status correspondente)
    - backend deve fornecer leads
        -- GET lead-list tá fazendo isso
        -- filtrar por usuário/sla
        -- ou selecionar o status e retornar leads daquele status?
* nova lead
    - POST lead-list
        -- cria lead, cria opportunities associadas
* mover lead
    - PUT pra editar a lead
        -- se for do 1 pro 2 criar customer
        -- se for do 2 pro 3 tem a parada de agendar a reuniao, que no backend vai ter que ser PUT pra alterar descricaao
* cadastro
    - POST users
        -- aceitar nao autenticado
* login