# Final
from shlex import split
from commands.help import help_command
from commands.add import add_command
from commands.list import list_command
from commands.done import done_command
from commands.edit import edit_command
from commands.remove import remove_command
from commands.tags import tags_command
from storage.file import load, save

def main():
    tasks, next_id = load()
    print("Менеджер заказов. Введи 'help' для справки.")

    while True:
        try:
            raw = input("\n> ").strip()
            if not raw:
                continue
            parts = split(raw)
            cmd = parts[0].lower()
            args = parts[1:]

            if cmd == "help":
                help_command()
            elif cmd == "add":
                next_id = add_command(tasks, args, next_id)
            elif cmd == "list":
                list_command(tasks, args)
            elif cmd == "done":
                done_command(tasks, args)
            elif cmd == "edit":
                edit_command(tasks, args)
            elif cmd == "remove":
                remove_command(tasks, args)
            elif cmd == "tags":
                tags_command(tasks, args)
            elif cmd == "exit":
                save(tasks)
                print("Пока!")
                break
            else:
                print("Неизвестная команда")

            if cmd in ["add", "edit", "remove", "tags", "done"]:
                save(tasks)

        except KeyboardInterrupt:
            save(tasks)
            print("\nПока!")
            break

if __name__ == "__main__":
    main()
