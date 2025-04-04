import streamlit as st
from datetime import datetime
import random

# 🎮 CONFIG PAGE
st.set_page_config(page_title="Solo Leveling IRL", page_icon="🗡️", layout="wide")

# 💥 STYLE CUSTOM CSS (thème sombre + RPG UI)
st.markdown("""
    <style>
    body {
        background-color: #111 !important;
        color: white;
    }
    .block-container {
        padding: 2rem 2rem 2rem 2rem;
    }
    h1, h2, h3, h4 {
        color: #FFD700;
    }
    .stProgress > div > div > div > div {
        background-color: #FFD700;
    }
    </style>
""", unsafe_allow_html=True)

# 📋 SIDEBAR - MENU NAVIGATION
st.sidebar.title("📜 Menu")
menu = st.sidebar.radio("Aller vers :", ["🏅 Stats & Rang", "📅 Missions", "🎒 Inventaire", "🗡️ Donjon"])

# 🧍 INFO PERSO
niveau = st.session_state.get("niveau", 1)
xp = st.session_state.get("xp", 0)
xp_max = 100 * niveau
energie = st.session_state.get("energie", 100)
stamina = st.session_state.get("stamina", 100)
inventaire = st.session_state.get("inventaire", {"Potion de Vie": 2, "Potion d'Energie": 1})
stats = st.session_state.get("stats", {
    "💪 Force": 0,
    "🏃 Endurance": 0,
    "🧠 Intelligence": 0,
    "🎯 Agilité": 0,
    "🔮 Mana": 0,
    "❤️ Vitalité": 0,
    "💼 Discipline": 0
})

# 🧱 RANGS
if niveau <= 5:
    rang = "🪶 Novice"
elif niveau <= 10:
    rang = "⚔️ Guerrier"
elif niveau <= 15:
    rang = "🛡️ Chevalier"
elif niveau <= 20:
    rang = "🔥 Maître"
elif niveau <= 25:
    rang = "🌟 Légende"
elif niveau <= 30:
    rang = "👑 Légende Suprême"
elif niveau <= 40:
    rang = "💀 Immortel"
elif niveau <= 50:
    rang = "🌌 Dieu"
else:
    rang = "🧙 Créateur"

# 💥 ÉVÉNEMENTS SPÉCIAUX
evenements_speciaux = {
    "Raid Dimanche": {
        "description": "Un raid spécial avec des récompenses d'XP doublées.",
        "date": "dimanche",  # Se déclenche chaque dimanche
        "bonus": lambda: xp * 2  # Double l'XP pour ce jour-là
    },
    "Vacances": {
        "description": "Bonus d'XP pendant les vacances !",
        "date": "vacances",  # Se déclenche pendant les vacances
        "bonus": lambda: xp + 50  # Ajoute 50 d'XP supplémentaires
    }
}

# Vérifier si un événement spécial se produit
def appliquer_evenements_speciaux():
    aujourd'hui = datetime.now()  # Assurez-vous d'avoir bien cette ligne
    jour_semaine = aujourd'hui.strftime("%A").lower()  # Récupérer le jour de la semaine (ex: lundi, dimanche)
    mois = aujourd'hui.month  # Récupérer le mois actuel

    # Vérifier le Raid Dimanche
    if "Raid Dimanche" in evenements_speciaux and jour_semaine == "dimanche":
        st.success(f"🎉 Événement Spécial : {evenements_speciaux['Raid Dimanche']['description']}")
        global xp
        xp = evenements_speciaux["Raid Dimanche"]["bonus"]()  # Appliquer le bonus d'XP

    # Vérifier les vacances (par exemple décembre, janvier, etc.)
    if "Vacances" in evenements_speciaux and mois in [12, 1]:  # Décembre et Janvier
        st.success(f"🎉 Événement Spécial : {evenements_speciaux['Vacances']['description']}")
        global xp
        xp = evenements_speciaux["Vacances"]["bonus"]()  # Appliquer le bonus d'XP

# 📄 PAGE : STATS & RANG
if menu == "🏅 Stats & Rang":
    st.title("🧍‍♂️ Fenêtre de Statut")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"### 🎖️ Rang : {rang}")
        st.markdown(f"**Niveau :** {niveau}")
        st.markdown("**Barre d'expérience :**")
        st.progress(xp / xp_max)
        st.markdown(f"**Énergie :** {energie}")
        st.markdown(f"**Stamina :** {stamina}")

    with col2:
        st.markdown("### 📊 Statistiques")
        for stat, value in stats.items():
            st.markdown(f"{stat} : **{value}**")

# 📄 PAGE : MISSIONS
if menu == "📅 Missions":
    st.title(f"📅 Missions du {datetime.today().strftime('%d/%m/%Y')}")
    missions = {
        # Endurance
        "10 km à vélo 🚴 (+100)": ("🏃 Endurance", 100, 10),
        "30 min de marche 🚶 (+30)": ("🏃 Endurance", 30, 5),
        "Course rapide 5km 🏃 (+75)": ("🏃 Endurance", 75, 8),
        "Course rapide 10km 🏃 (+100)": ("🏃 Endurance", 100, 10),
        "30 min cardio 🏋️‍♂️ (+50)": ("🏃 Endurance", 50, 7),
        # Force
        "Seance de musculation 💪 (+75)": ("💪 Force", 75, 8),
        "50 pompes 💪 (+20)": ("💪 Force", 20, 5),
        "100 abdos 💪 (+25)": ("💪 Force", 25, 4),
        # Intelligence
        "Etudier pendant 1h 🧠 (+60)": ("🧠 Intelligence", 60, 8),
        "Lecture 1h 📚 (+50)": ("🧠 Intelligence", 50, 6),
        "Apprendre anglais 🇬🇧 (+40)": ("🧠 Intelligence", 40, 5),
        # Mana
        "Étirements 30 min 🧘‍♂️ (+15)": ("❤️ Vitalité", 15, 4),
        "Méditer 10 min 🧘 (+40)": ("🔮 Mana", 40, 5),
        # Vitalité
        "Dormir 8h 😴 (+40)": ("❤️ Vitalité", 40, 10),
        "Boire 2L d'eau 💧 (+20)": ("❤️ Vitalité", 20, 3),
        "Repas équilibré 🥗 (+30)": ("❤️ Vitalité", 30, 5),
        "Étirements 30 min 🧘‍♂️ (+50)": ("❤️ Vitalité", 50, 7),
        # Discipline
        "Journée sans procrastination ✅ (+50)": ("💼 Discipline", 50, 6),
        "Planifier la semaine ✅ (+40)": ("💼 Discipline", 40, 5),
        "Suivre la to-do list à 100% ✅ (+60)": ("💼 Discipline", 60, 7),
    }

    gagne_xp = 0
    for label, (stat_key, xp_gain, cost) in missions.items():
        if st.checkbox(label, key=label):
            if stamina >= cost:
                stats[stat_key] += xp_gain
                xp += xp_gain
                stamina -= cost
                gagne_xp += xp_gain
                st.success(f"✅ +{xp_gain} {stat_key}")
            else:
                st.warning(f"⚠️ Pas assez de stamina. Coût: {cost}")

# 📄 PAGE : INVENTAIRE
if menu == "🎒 Inventaire":
    st.title("🎒 Inventaire")
    for item, quantity in inventaire.items():
        st.markdown(f"**{item}** : {quantity}")

# 🗡️ PAGE : DONJON
if menu == "🗡️ Donjon":
    st.title("🏰 Donjon - Affrontez des défis !")

    # Donjon : Étapes
    donjon_etapes = [
        ("Faire 50 pompes 💪", 20, "💪 Force", 5),
        ("Faire 100 squats 🏋️‍♂️", 25, "💪 Force", 7),
        ("Courir 10 km 🚴", 50, "🏃 Endurance", 10),
        ("Résoudre un puzzle 🧠", 40, "🧠 Intelligence", 5),
        ("Méditer 15 min 🧘", 15, "🔮 Mana", 4),
        ("Dormir 8h 😴", 40, "❤️ Vitalité", 10),
        ("Lire 1h 📚", 30, "💼 Discipline", 6)
    ]

    if "etape_donjon" not in st.session_state:
        st.session_state.etape_donjon = 0  # Commence à la première étape du donjon

    etape_donjon = st.session_state.etape_donjon

    if etape_donjon < len(donjon_etapes):
        etape_nom, xp_gain, stat, cost = donjon_etapes[etape_donjon]

        st.markdown(f"### Étape {etape_donjon + 1}: {etape_nom}")
        st.progress(etape_donjon / len(donjon_etapes))

        # Vérifier si le joueur a assez d'énergie pour accomplir l'étape
        if st.button("Accomplir cette étape"):
            if stamina >= cost:
                stats[stat] += xp_gain
                xp += xp_gain
                stamina -= cost
                st.session_state.etape_donjon += 1  # Passe à l'étape suivante
                st.success(f"🎉 Étape terminée ! +{xp_gain} {stat}.")
            else:
                st.warning(f"⚠️ Pas assez d'énergie pour accomplir cette étape. Coût: {cost}.")
    else:
        st.success("🎉 Félicitations, tu as terminé ce donjon pour aujourd'hui !")

# 🎉 LEVEL UP
if xp >= xp_max:
    niveau += 1
    xp -= xp_max
    xp_max = 100 * niveau
    st.balloons()
    st.success(f"🆙 Niveau supérieur ! Tu es maintenant niveau {niveau} ({rang})")

# 💾 SAUVEGARDE
st.session_state["niveau"] = niveau
st.session_state["xp"] = xp
st.session_state["energie"] = energie
st.session_state["stamina"] = stamina
st.session_state["stats"] = stats
st.session_state["inventaire"] = inventaire
