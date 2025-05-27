import json
from utils import create_nft, generate_qr, send_to_telegram

def run():
    with open("tasks.json", "r", encoding="utf-8") as f:
        tasks = json.load(f)

    for task in tasks:
        if task["status"] == "new":
            report = create_nft(task)
            payment_qr = generate_qr(task)
            send_to_telegram(f"{report}\n\n{payment_qr}")
            task["status"] = "done"

    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

run()
