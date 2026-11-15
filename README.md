# Домашняя работа № 1 — глубокое обучение

**Темы:** свёртки, обратное распространение, receptive field, BatchNorm, AdamW, ResNet на CIFAR-10, PGD-атаки и adversarial training на FashionMNIST. Реализованы и выполнены бонусы 7.1–7.5 (максимум 4 бонусных балла согласно условиям).

## Статус выполнения

- Все ячейки `hw1.ipynb` выполнены, результаты и визуализации сохранены непосредственно в ноутбуке.
- Финальные настройки: `FAST_MODE=False`, `ATTACK_TRACK='targeted'` (ветка 5.2), `BONUS_TASKS={'7.1','7.2','7.3','7.4','7.5'}`.
- Среда, использованная для экспериментов: Google Colab, NVIDIA T4, PyTorch `2.14.1+cu130`, CUDA.
- Использованы CIFAR-10 (50 000 train / 10 000 test) и FashionMNIST (60 000 train / 1 000 test, как задано кодом ноутбука).

## Основные результаты

| Эксперимент | Результат |
| --- | ---: |
| ResNet-20 на CIFAR-10 — test accuracy после 20 эпох | **82,95%** |
| Plain-20 / Plain-56 — test accuracy после 10 эпох | 77,83% / 53,50% |
| FashionMNIST standard CNN — clean accuracy | 91,70% |
| FashionMNIST PGD-AT — clean accuracy | 84,40% |
| Standard / PGD-AT — PGD-20 accuracy при ε=0,1 | 0,50% / **72,00%** |
| AdamW / Muon — CIFAR-10 test accuracy | 82,95% / 84,88% |

Это результаты одного запуска с зафиксированным seed. Подробные метрики и ограничения приведены в `artifacts/report.md` и `artifacts/metrics.json` / `bonus_metrics.json`.

## Структура

```text
.
├── hw1.ipynb                 # Решения, тесты, пояснения и outputs
├── requirements.txt          # Исходные зафиксированные зависимости задания
├── verify_submission.py      # Локальная проверка комплекта
└── artifacts/
    ├── metrics.json
    ├── bonus_metrics.json
    ├── report.md
    ├── resnet20.pt
    ├── fashion_standard.pt
    ├── fashion_pgd_at.pt
    └── plots/                 # Графики обучения и атак
```

В каталоге `artifacts/` находятся **результаты уже проведённого эксперимента**, поэтому для просмотра выводов не требуется снова обучать модели.

## Как воспроизвести

1. Откройте `hw1.ipynb` в Jupyter или Google Colab с GPU и доступом в интернет.
2. Проверьте совместимость PyTorch/torchvision с CUDA в выбранной среде. Файл `requirements.txt` сохранён из исходного задания (PyTorch 2.11.0); реальный финальный прогон проводился на версии **2.14.1+cu130**. При воспроизведении используйте совместимую GPU-сборку PyTorch и torchvision, соответствующую вашей среде.
3. Убедитесь, что `FAST_MODE=False` и `ATTACK_TRACK='targeted'` (все бонусы увеличивают время исполнения).
4. Выполните ячейки по порядку. CIFAR-10 и FashionMNIST загрузятся автоматически; датасеты в репозиторий не включены.
5. После выполнения notebook пересоздаст `artifacts/` и отчёт по фактическим метрикам. Запустите `python verify_submission.py` для проверки состава файлов.

**Примечание:** Веса, графики и метрики уже сохранены; время выполнения и точные результаты могут отличаться на другом GPU и с другими версиями библиотек.
