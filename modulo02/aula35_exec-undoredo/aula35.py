"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamamos, desfaz a última ação)
    opção de refazer (a cada vez que chamamos, refaz a última ação)

    ['Tarefa 1', 'Tarefa 2']
    ['Tarefa 1'] <- Desfazer
    ['Tarefa 1', 'Tarefa 2'] <- Refazer

    input <- nova tarefa
"""


def add_task(task, tasks):
    tasks.append(task)


def get_tasks(tasks):
    print(f'Lista de tarefas: {tasks}', end='\n\n')


def undo(tasks, temp):
    if not tasks:
        print('Nada para desfazer.')
        return

    temp.insert(0, tasks.pop())


def redo(tasks, temp):
    if not temp:
        print('Nada para refazer.')
        return

    tasks.append(temp[0])
    del (temp[0])


if __name__ == '__main__':
    tarefas = []
    temp = []

while True:
    cmd = input(f'Comandos\n1-Adicionar tarefa\n2-Listar tarefas\n3-Desfazer\n4-Refazer\n5-Sair\nDigite valor:')
    if cmd == '1':
        task = input('Digite tarefa: ')
        add_task(task, tarefas)
    elif cmd == '2':
        get_tasks(tarefas)
    elif cmd == '3':
        undo(tarefas, temp)
    elif cmd == '4':
        redo(tarefas, temp)
    elif cmd == '5':
        break
