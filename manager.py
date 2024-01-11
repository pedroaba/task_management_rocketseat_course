from typing import TypedDict, List


class Task(TypedDict):
    task: str
    completed: str


def add_task(task: str, tasks_list: list[Task]):
    tasks_list.append({
        "task": task,
        "completed": False
    })

    print(f"Tarefa {task} foi adicionada com sucesso!")
    return


def view_tasks(task_list: list[Task]):
    print("\nLista de tarefas:")
    for index, task in enumerate(task_list, start=1):
        status = "✓" if task["completed"] else " "
        task_name = task["task"]

        print(f"{index}. [{status}] {task_name}")
    return


def update_task_name(
        task_list: List[Task], 
        task_index: int, 
        new_task_name: str
    ):
    right_task_index = int(task_index) - 1
    quantity_of_tasks = len(task_list)
    if 0 <= right_task_index < quantity_of_tasks:
        task_list[right_task_index]["task"] = new_task_name

        print(f"Tarefa {task_index} atualizada para {new_task_name}")
    else:
        print("Índice de tarefa inválida!")
    return


def complete_task(task_list: List[Task], task_index: int):
    right_task_index = int(task_index) - 1
    quantity_of_tasks = len(task_list)
    if 0 <= right_task_index < quantity_of_tasks:
        task_list[right_task_index]["completed"] = True

        print(f"Tarefa {task_index} marcada como completada")
    else:
        print("Índice de tarefa inválida!")
    return


def delete_completed_tasks(tasks: List[Task]):
    for task in tasks:
        if task["completed"]:
            tasks.remove(task)

    print("Tarefas completadas foram deletadas")
    return


tasks: List[Task] = []
while True:
    print("\nMenu do Gerenciador de Lista de tarefas:")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    choice = input("Digite a sua escolha: ")

    if choice == "6":
        break

    match choice:
        case "1":
            task_name = input("Digite o nome da tarefa que deseja adicionar: ")
            add_task(task_name, tasks)
        case "2":
            view_tasks(tasks)
        case "3":
            view_tasks(tasks)

            task_index = input("Digite o número da tarefa que deseja atualizar: ")
            new_task_name = input("Digite o novo nome da tarefa: ")

            update_task_name(tasks, task_index, new_task_name)
        case "4":
            view_tasks(tasks)

            task_index = input("Digite o número da tarefa que deseja completar: ")
            complete_task(tasks, task_index)
        case "5":
            delete_completed_tasks(tasks)
            view_tasks(tasks)
        case _:
            print("Opção inválida!")

print("Programa finalizado")
