from typing import TypedDict, List


class Task(TypedDict):
    task: str
    completed: str


def add_task(task: str, tasks_list: list):
    tasks_list.append({
        "task": task,
        "completed": False
    })

    print(f"Tarefa {task} foi adicionada com sucesso!")
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
            continue
        case _:
            print("Opção inválida!")

print("Programa finalizado")
