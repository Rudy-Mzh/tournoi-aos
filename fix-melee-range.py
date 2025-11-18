#!/usr/bin/env python3
"""
Script pour retirer l'attribut 'range' des armes de type 'melee' dans index.html
AoS V4 n'a pas de range pour les armes de mêlée (combat universel à 3")
"""

import re

# Lire le fichier
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern pour trouver un bloc d'arme melee avec range
# On cherche: type: "melee", suivi éventuellement d'autres lignes, puis range: X,
pattern = r'(type:\s*["\']melee["\'],?\s*\n)(\s*range:\s*\d+,?\s*\n)'

# Compter les remplacements
count = len(re.findall(pattern, content))

# Retirer les lignes 'range:' qui suivent 'type: "melee"'
content_fixed = re.sub(pattern, r'\1', content)

# Sauvegarder
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content_fixed)

print(f"✅ Correction terminée: {count} attributs 'range' retirés des armes de mêlée")
print(f"✅ Format V4 appliqué: armes melee = Attacks/Hit/Wound/Rend/Damage (pas de Range)")
