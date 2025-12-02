#import json
from shlex import split
from commands.help import help_command
from commands.add import add_command
from tasks.tasks import Task, make_task
from helpers.args import parse_date
from storage.file import load, save

def main():
    file_path = "tasks.json"
    tasks, next_id = load()
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
                    next_id = add_command(tasks, args, next_id)
                    save(tasks)
                case "list":
                    pass
                case "remove":
                    pass
                case "edit":
                    pass         
                case "tags":
                    pass
                case "exit":
                    save(tasks)
                    break
                case _:
                    print("Неизвестная команда.")
        except KeyboardInterrupt:
            save_tasks(file_path, tasks)
            print("\nЗавершение приложения")
            break
        except Exception as e:
            save_tasks(file_path, tasks)
            print(f"[ERROR]: {e}")

if __name__ == "__main__":
    main()
