#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update box_config with correct probabilities and bonus hours"""

with open('tttpc.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace the entire box_config
# This is a big replacement, so we'll do it carefully

old_config_start = '        box_config = {'
new_config = '''        box_config = {
            "starter_pack": {
                "rewards": [
                    ("⏱ Макс доход игрока", 90, lambda: random.randint(1, 6)),  # 90% шанс
                    ("⏱ Заработок ПК", 9, lambda: random.randint(1, 6)),  # 9% шанс
                    ("🖥 ПК", 0.9, lambda: 1),  # 0.9% шанс
                    ("⚡ Премиум", 0.033, lambda: random.randint(1, 3)),  # 0.1%/3 шанс
                    ("🤖 Спонсор клуба", 0.033, lambda: random.randint(1, 3)),
                    ("🔧 Автоматизация", 0.034, lambda: random.randint(1, 3)),
                ],
                "name": "📦 STARTER PACK"
            },
            "gamer_case": {
                "rewards": [
                    ("⏱ Макс доход игрока", 80, lambda: random.randint(1, 12)),  # 80% шанс
                    ("⏱ Заработок ПК", 19, lambda: random.randint(1, 12)),  # 19% шанс
                    ("🖥 Игровой ПК", 0.7, lambda: 1),  # 0.7% шанс
                    ("⚡ Премиум", 0.1, lambda: random.randint(1, 12)),  # 0.3%/3 шанс
                    ("🤖 Спонсор клуба", 0.1, lambda: random.randint(1, 12)),
                    ("🔧 Автоматизация", 0.1, lambda: random.randint(1, 12)),
                ],
                "name": "🎮 GAMER'S CASE"
            },
            "business_box": {
                "rewards": [
                    ("⏱ Макс доход игрока", 70, lambda: random.randint(1, 24)),  # 70% шанс
                    ("⏱ Заработок ПК", 25, lambda: random.randint(1, 24)),  # 25% шанс
                    ("🖥 Бизнес ПК", 4.5, lambda: 1),  # 4.5% шанс
                    ("⚡ Премиум", 0.167, lambda: random.randint(1, 24)),  # 0.5%/3 шанс
                    ("🤖 Спонсор клуба", 0.167, lambda: random.randint(1, 24)),
                    ("🔧 Автоматизация", 0.166, lambda: random.randint(1, 24)),
                ],
                "name": "💼 BUSINESS BOX"
            },
            "champion_chest": {
                "rewards": [
                    ("⏱ Макс доход игрока", 60, lambda: random.randint(1, 48)),  # 60% шанс
                    ("⏱ Заработок ПК", 30, lambda: random.randint(1, 48)),  # 30% шанс
                    ("🖥 Элитный ПК", 9.3, lambda: 1),  # 9.3% шанс
                    ("⚡ Премиум", 0.233, lambda: random.randint(1, 48)),  # 0.7%/3 шанс
                    ("🤖 Спонсор клуба", 0.233, lambda: random.randint(1, 48)),
                    ("🔧 Автоматизация", 0.234, lambda: random.randint(1, 48)),
                ],
                "name": "🏆 CHAMPION CHEST"
            },
            "pro_gear": {
                "rewards": [
                    ("⏱ Макс доход игрока", 50, lambda: random.randint(1, 72)),  # 50% шанс
                    ("⏱ Заработок ПК", 35, lambda: random.randint(1, 72)),  # 35% шанс
                    ("🖥 Про-комплект ПК", 14, lambda: 1),  # 14% шанс
                    ("⚡ Премиум", 0.333, lambda: random.randint(1, 72)),  # 1.0%/3 шанс
                    ("🤖 Спонсор клуба", 0.333, lambda: random.randint(1, 72)),
                    ("🔧 Автоматизация", 0.334, lambda: random.randint(1, 72)),
                ],
                "name": "🧳 PRO GEAR"
            },
            "legend_vault": {
                "rewards": [
                    ("⏱ Макс доход игрока", 40, lambda: random.randint(1, 96)),  # 40% шанс
                    ("⏱ Заработок ПК", 40, lambda: random.randint(1, 96)),  # 40% шанс
                    ("🖥 Легендарное оборудование", 18.5, lambda: 1),  # 18.5% шанс
                    ("⚡ Премиум", 0.5, lambda: random.randint(1, 96)),  # 1.5%/3 шанс
                    ("🤖 Спонсор клуба", 0.5, lambda: random.randint(1, 96)),
                    ("🔧 Автоматизация", 0.5, lambda: random.randint(1, 96)),
                ],
                "name": "👑 LEGEND'S VAULT"
            },
            "vip_mystery": {
                "rewards": [
                    ("⏱ Макс доход игрока", 30, lambda: random.randint(1, 128)),  # 30% шанс
                    ("⏱ Заработок ПК", 50, lambda: random.randint(1, 128)),  # 50% шанс
                    ("🖥 VIP Ферма", 17, lambda: 1),  # 17% шанс
                    ("⚡ Премиум", 1.0, lambda: random.randint(1, 128)),  # 3%/3 шанс
                    ("🤖 Спонсор клуба", 1.0, lambda: random.randint(1, 128)),
                    ("🔧 Автоматизация", 1.0, lambda: random.randint(1, 128)),
                ],
                "name": "🌟 VIP MYSTERY BOX"
            }
        }'''

# Find the start of box_config
start_idx = content.find(old_config_start)
if start_idx == -1:
    print('ERROR: Could not find box_config')
    exit(1)

# Find the end (next line with "config = box_config.get")
end_marker = '        config = box_config.get'
end_idx = content.find(end_marker, start_idx)
if end_idx == -1:
    print('ERROR: Could not find end of box_config')
    exit(1)

# Replace the config
content = content[:start_idx] + new_config + '\n\n' + content[end_idx:]

with open('tttpc.py', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated box_config with correct probabilities and bonus hours:')
print('- STARTER PACK: Bonuses 1-3 hours')
print('- GAMER CASE: Bonuses 1-12 hours')
print('- BUSINESS BOX: Bonuses 1-24 hours')
print('- CHAMPION CHEST: Bonuses 1-48 hours')
print('- PRO GEAR: Bonuses 1-72 hours')
print('- LEGEND VAULT: Bonuses 1-96 hours')
print('- VIP MYSTERY BOX: Bonuses 1-128 hours')
