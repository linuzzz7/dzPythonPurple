# main.py
from shlex import split
from commands.help import help_command
from commands.tasks import (
    create_order, list_orders, edit_order, remove_order,
    done_order, add_tag, remove_tag
)
from helpers.args import parse_add, parse_date

def print_tasks():
    tasks = list_orders()
    if not tasks:
        print("Список задач пуст.")
        return
    for t in tasks:
        due_str = t["due"].strftime("%Y-%m-%d") if t["due"] else "-"
        tags_str = ", ".join(t["tags"] or []) or "-"
        status_emoji = "[DONE]" if t["status"] == "done" else "[NEW]"
        print(f"{status_emoji} {t['id']}: {t['title']} | приоритет: {t['priority']} | срок: {due_str} | теги: {tags_str}")

def main():
    print("Менеджер задач. Введи 'help' для справки.")

    while True:
        try:
            raw = input("\n> ").strip()
            if not raw:
                continue
            parts = split(raw)
            cmd = parts[0].lower()
            args = parts[1:]

            match cmd:
                case "help":
                    help_command()

                case "add":
                    title, prio, due, tags = parse_add(args)
                    task = create_order(title, prio, due, tags)
                    print(f"Создана задача #{task['id']}: {task['title']}")

                case "list":
                    print_tasks()

                case "done":
                    if not args:
                        print("Укажи id: done <id>")
                        continue
                    task_id = int(args[0])
                    done_order(task_id)
                    print(f"Задача #{task_id} отмечена как выполненная")

                case "edit":
                    if len(args) < 2:
                        print("Использование: edit <id> [title=...] [prio=...] [due=YYYY-MM-DD]")
                        continue
                    task_id = int(args[0])
                    title = prio = due = None
                    for arg in args[1:]:
                        if arg.startswith("title="):
                            title = arg.split("=", 1)[1]
                        elif arg.startswith("prio="):
                            prio = arg.split("=", 1)[1].lower()
                        elif arg.startswith("due="):
                            due = parse_date(arg.split("=", 1)[1])
                    edit_order(task_id, title, prio, due)
                    print(f"Задача #{task_id} обновлена")

                case "remove":
                    if not args:
                        print("Укажи id: remove <id>")
                        continue
                    remove_order(int(args[0]))
                    print(f"Задача #{args[0]} удалена")

                case "tags":
                    if len(args) < 3 or args[1] not in ("add", "remove"):
                        print("Использование: tags <id> add|remove <тег>")
                        continue
                    task_id = int(args[0])
                    action = args[1]
                    tag = args[2]
                    if action == "add":
                        add_tag(task_id, tag)
                        print(f"Тег '{tag}' добавлен к задаче #{task_id}")
                    else:
                        remove_tag(task_id, tag)
                        print(f"Тег '{tag}' удалён из задачи #{task_id}")

                case "exit" | "quit":
                    print("Пока!")
                    break

                case _:
                    print("Неизвестная команда. Используй 'help'")

        except ValueError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Неизвестная ошибка: {e}")

if __name__ == "__main__":
    main()