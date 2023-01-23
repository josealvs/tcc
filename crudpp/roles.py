from rolepermissions.roles import AbstractUserRole

class Professor(AbstractUserRole):
    available_permissions = {'criar_projetos': True, 'criar_atividades': True}

class Aluno(AbstractUserRole):
    available_permissions = {'ver_projetos': True, 'ver_atividades': True}