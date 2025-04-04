import streamlit as st
from datetime import date
import random

# 📌 CONFIG DE LA PAGE
st.set_page_config(page_title="Solo Leveling IRL", page_icon="🗡️", layout="wide")

# 🧍 PERSONNAGE
st.title("🧍‍♂️ Mon Personnage Solo Leveling")

# Variables de base
niveau = st.session_state.get("niveau", 1)
xp = st.session_state.get("xp", 0)
xp_max = 100 * niveau
energie = st.session_state.get("energie", 100)  # Energie
stamina = st.session_state.get("stamina", 100)  # Stamina
reputation = st.session_state.get("reputation", 0)  # Réputation avec les factions
quêtes_accomplies = st.session_state.get("quêtes_accomplies", 0)  # Quêtes accomplies
rang = "Novice"  # Rang par défaut

# 🏆 DÉFINITION DES RANGS AVANCÉS
if niveau <= 5:
    rang = "Novice"
elif niveau <= 10:
    rang = "Guerrier"
elif niveau <= 15:
    rang = "Chevalier"
elif niveau <= 20:
    rang = "Maître"
elif niveau <= 25:
    rang = "Légende"
elif niveau <= 30:
    rang = "Légende Suprême"
elif niveau <= 40:
    rang = "Immortel"
elif niveau <= 50:
    rang = "Dieu"
else:
    rang = "Créateur"

# Affichage du rang
st.markdown(f"**Rang actuel :** {rang}")
st.markdown(f"**Niveau :** {niveau}")
st.progress(xp / xp_max)

# 📊 STATS DE BASE
stats = st.session_state.get("stats", {
    "💪 Force": 0,
    "🏃 Endurance": 0,
    "🧠 Intelligence": 0,
    "🎯 Agilité": 0,
    "🔮 Mana": 0,
    "❤️ Vitalité": 0,
    "💼 Discipline": 0
})

# Disposition avec des colonnes
col1, col2 = st.columns(2)
with col1:
    st.markdown("## 📊 Stats")
    for stat, value in stats.items():
        st.write(f"{stat} : {value}")

with col2:
    st.markdown("## 📦 Inventaire")
    inventaire = st.session_state.get("inventaire", {"Potion de Vie": 2, "Potion d'Energie": 1})  # Inventaire
    for item, quantity in inventaire.items():
        st.write(f"{item}: {quantity}")

# 🎯 SYSTÈME DE QUÊTES AVANCÉES
st.markdown(f"## 📅 Missions du {date.today().strftime('%d/%m/%Y')}")

missions = {
    # Endurance
    "Faire 10 km à vélo 🚴‍♂️ (+100 Endurance)": ("🏃 Endurance", 100, 10),
    "30 minutes de marche 🚶‍♂️ (+30 Endurance)": ("🏃 Endurance", 30, 5),
    "30 minutes de cardio 🏋️‍♂️ (+50 Endurance)": ("🏃 Endurance", 50, 7),

    # Force
    "Musculation - Pecs 💪 (+40 Force)": ("💪 Force", 40, 10),
    "Musculation - Biceps 💪 (+30 Force)": ("💪 Force", 30, 8),
    "Musculation - Autre 💪 (+20 Force)": ("💪 Force", 20, 6),
    "Faire 50 pompes 💪 (+20 Force)": ("💪 Force", 20, 5),
    "Faire 100 abdos 💪 (+25 Force)": ("💪 Force", 25, 4),

    # Intelligence
    "Lecture profonde 📖 (+50 Intelligence)": ("🧠 Intelligence", 50, 6),
    "Lecture manga 📖 (+20 Intelligence)": ("🧠 Intelligence", 20, 4),
    "Étudier anglais 30 min 🇬🇧 (+40 Intelligence)": ("🧠 Intelligence", 40, 5),
    "Étudier pendant 1h 📚 (+60 Intelligence)": ("🧠 Intelligence", 60, 8),

    # Mana
    "Méditer 10 minutes 🧘 (+15 Mana)": ("🔮 Mana", 15, 4),
    "Session de respiration profonde 🌬️ (+20 Mana)": ("🔮 Mana", 20, 6),

    # Vitalité
    "Boire 2l d'eau 💧 (+20 Vitalité)": ("❤️ Vitalité", 20, 5),
    "Passer seulement 3h sur son téléphone 📱 (+30 Vitalité)": ("❤️ Vitalité", 30, 7),
    "Faire sa skin care 🧴 (+15 Vitalité)": ("❤️ Vitalité", 15, 3),
    "Dormir 8h 😴 (+40 Vitalité)": ("❤️ Vitalité", 40, 10),
    "Se réveiller avant 10h ⏰ (+10 Vitalité)": ("❤️ Vitalité", 10, 2),

    # Discipline
    "Passer une journée sans procrastiner ✅ (+50 Discipline)": ("💼 Discipline", 50, 6),
    "Faire 3 fois du sport par semaine 🏋️‍♂️ (+100 Discipline)": ("💼 Discipline", 100, 10)
}

# ✅ COCHER LES MISSIONS
gagne_xp = 0
for label, (stat_key, xp_gain, energy_cost) in missions.items():
    if st.checkbox(label, key=label):
        if stamina >= energy_cost:
            stats[stat_key] += xp_gain
            xp += xp_gain
            stamina -= energy_cost  # Réduction de la stamina après la mission
            gagne_xp += xp_gain
            st.write(f"Mission accomplie: {label} - +{xp_gain} {stat_key}!")
        else:
            st.warning(f"Pas assez d'énergie pour accomplir cette mission. Coût: {energy_cost} énergie.")

# 🎯 SYSTÈME DE RANG ET PRESTIGE
if xp >= xp_max:
    xp -= xp_max
    niveau += 1
    xp_max = 100 * niveau
    st.balloons()
    st.success(f"🎉 Tu as monté de niveau ! Maintenant tu es un {rang}.")

    # Récompenses pour chaque rang
    if rang == "Novice":
        st.markdown("🎁 Récompense : 1 Potion de Vie et +10% XP pour le prochain niveau.")
        inventaire["Potion de Vie"] += 1
    elif rang == "Guerrier":
        st.markdown("🎁 Récompense : +20% à la force pour 24h.")
        stats["💪 Force"] += 20
    elif rang == "Chevalier":
        st.markdown("🎁 Récompense : Nouvelle compétence 'Saut de Combat' débloquée.")
        st.write("Compétence: Augmente l'agilité de 30% pendant 30 minutes.")
    elif rang == "Maître":
        st.markdown("🎁 Récompense : Augmentation de l'intelligence et de la vitalité pour toute la journée.")
        stats["🧠 Intelligence"] += 10
        stats["❤️ Vitalité"] += 10
    elif rang == "Légende":
        st.markdown("🎁 Récompense : Compétence légendaire 'Maîtrise absolue'. Toutes les stats augmentées de 5%.")
        for key in stats:
            stats[key] += 5
    elif rang == "Légende Suprême":
        st.markdown("🎁 Récompense : +50% d'XP pour chaque mission réussie !")
        st.write("Prépare-toi pour un nouveau défi, la difficulté des missions va augmenter.")
    elif rang == "Immortel":
        st.markdown("🎁 Récompense : Nouvelle compétence 'Régénération' activée. Restaure 10% de ton énergie chaque jour.")
    elif rang == "Dieu":
        st.markdown("🎁 Récompense : Tu as débloqué le pouvoir de contrôler les éléments. +100% de force, endurance et vitalité.")
    elif rang == "Créateur":
        st.markdown("🎁 Récompense ultime : Tu peux maintenant réincarner ton personnage pour un défi encore plus grand.")

# 💾 SAUVEGARDE DES DONNÉES
st.session_state["niveau"] = niveau
st.session_state["xp"] = xp
st.session_state["stats"] = stats
st.session_state["energie"] = energie
st.session_state["stamina"] = stamina
st.session_state["reputation"] = reputation
st.session_state["inventaire"] = inventaire
st.session_state["quêtes_accomplies"] = quêtes_accomplies + 1 if gagne_xp > 0 else quêtes_accomplies

# 📈 AFFICHAGE RÉCAP
if gagne_xp > 0:
    st.markdown("### ✅ Gains aujourd'hui :")
    st.write(f"**XP gagné :** {gagne_xp}")
    for stat, value in stats.items():
        st.write(f"{stat} : {value}")
    st.write(f"**Energie restante :** {stamina}")
    st.write(f"**Stamina restante :** {stamina}")

