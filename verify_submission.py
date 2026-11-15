"""Проверка готового комплекта сдачи, без запуска обучения."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent
nb = json.loads((root / "hw1.ipynb").read_text(encoding="utf-8"))
codes = [c for c in nb["cells"] if c["cell_type"] == "code"]
errors = [(c.get("id", "?"), o.get("ename", "error")) for c in codes for o in c.get("outputs", []) if o.get("output_type") == "error"]
assert all(c.get("execution_count") is not None for c in codes), "Не все кодовые ячейки выполнены"
assert not errors, f"Ошибки в сохранённых outputs: {errors}"
required = ["metrics.json", "bonus_metrics.json", "report.md", "resnet20.pt", "fashion_standard.pt", "fashion_pgd_at.pt"]
for filename in required:
    assert (root / "artifacts" / filename).is_file(), f"Отсутствует {filename}"
metrics = json.loads((root / "artifacts" / "metrics.json").read_text(encoding="utf-8"))
bonus = json.loads((root / "artifacts" / "bonus_metrics.json").read_text(encoding="utf-8"))
assert metrics["fast_mode"] is False, "Нужен финальный режим"
assert metrics["attack_track"] == "targeted", "Не совпадает ветка"
assert len(metrics["cifar"]["history"]["test_acc"]) == 20
plots = list((root / "artifacts" / "plots").glob("*.png"))
assert len(plots) >= 10, "Ожидаемые графики отсутствуют"
print(f"OK: {len(codes)} исполненных ячеек, {len(plots)} графиков, {len(bonus['bonus_tasks'])} бонусных разделов")
print(f"ResNet-20 test accuracy: {metrics['cifar']['history']['test_acc'][-1]:.2%}")
