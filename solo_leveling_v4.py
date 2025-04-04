import streamlit as st
from datetime import date

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
    st.title(f"📅 Missions du {date.today().strftime('%d/%m/%Y')}")
    missions = {
        # Endurance
        "10 km à vélo 🚴 (+100)": ("🏃 Endurance", 100, 10),
        "30 min de marche 🚶 (+30)": ("🏃 Endurance", 30, 5),
        "30 min cardio 🏋️‍♂️ (+50)": ("🏃 Endurance", 50, 7),
        "1h de course 🏃 (+150)": ("🏃 Endurance", 150, 15),
        "5 km en randonnée 🏞️ (+80)": ("🏃 Endurance", 80, 10),
        "Faire 1h de vélo en extérieur 🚴‍♂️ (+150)": ("🏃 Endurance", 150, 12),
        "Escalader une montagne 🏔️ (+200)": ("🏃 Endurance", 200, 20),
        "Natation 30 min 🏊‍♂️ (+100)": ("🏃 Endurance", 100, 10),

        # Force
        "50 pompes 💪 (+20)": ("💪 Force", 20, 5),
        "100 abdos 💪 (+25)": ("💪 Force", 25, 4),
        "100 tractions 💪 (+30)": ("💪 Force", 30, 8),
        "20 min de gainage 🧘 (+50)": ("💪 Force", 50, 7),
        "200 squats 🏋️‍♂️ (+60)": ("💪 Force", 60, 15),
        "Soulever 50 kg 💪 (+100)": ("💪 Force", 100, 20),
        "Faire 30 burpees 🔥 (+50)": ("💪 Force", 50, 12),

        # Intelligence
        "Lecture 1h 📚 (+60)": ("🧠 Intelligence", 60, 8),
        "Apprendre anglais 🇬🇧 (+40)": ("🧠 Intelligence", 40, 5),
        "Révision pour un examen 📖 (+100)": ("🧠 Intelligence", 100, 12),
        "Rédiger un résumé de livre 📖 (+50)": ("🧠 Intelligence", 50, 6),
        "Résoudre un problème mathématique compliqué ➗ (+80)": ("🧠 Intelligence", 80, 10),
        "Rédiger un essai de 500 mots 📝 (+120)": ("🧠 Intelligence", 120, 15),
        "Apprendre 20 nouveaux mots dans une langue étrangère 🗣️ (+60)": ("🧠 Intelligence", 60, 7),
        "Suivre un cours en ligne pendant 1h 💻 (+100)": ("🧠 Intelligence", 100, 15),

        # Mana
        "Méditer 10 min 🧘 (+15)": ("🔮 Mana", 15, 4),
        "Visualisation 10 min 💭 (+20)": ("🔮 Mana", 20, 5),
        "Réduire son temps d'écran 1h 📴 (+30)": ("🔮 Mana", 30, 6),
        "30 min de visualisation de ses objectifs 🎯 (+25)": ("🔮 Mana", 25, 7),
        "Lire un livre sur la gestion du stress 📚 (+50)": ("🔮 Mana", 50, 8),
        "Créer un tableau de vision 🔮 (+35)": ("🔮 Mana", 35, 6),
        "Suivre une séance de relaxation guidée 🌙 (+40)": ("🔮 Mana", 40, 8),

        # Vitalité
        "Dormir 8h 😴 (+40)": ("❤️ Vitalité", 40, 10),
        "Boire 2L d'eau 💧 (+20)": ("❤️ Vitalité", 20, 4),
        "Manger équilibré 🍎 (+30)": ("❤️ Vitalité", 30, 6),
        "Prendre une douche froide 🚿 (+30)": ("❤️ Vitalité", 30, 7),
        "Marcher dans la nature 1h 🌳 (+40)": ("❤️ Vitalité", 40, 8),
        "Faire une pause sans écran pendant 30 min 📴 (+20)": ("❤️ Vitalité", 20, 5),

        # Discipline
        "Journée sans procrastination ✅ (+50)": ("💼 Discipline", 50, 6),
        "Planification d'objectifs 🗂️ (+40)": ("💼 Discipline", 40, 5),
        "Faire une to-do list et la compléter ✅ (+30)": ("💼 Discipline", 30, 4),
        "Compléter une liste de tâches difficile ✅ (+60)": ("💼 Discipline", 60, 10),
        "Méditer 15 min en pleine conscience 🧘‍♀️ (+40)": ("💼 Discipline", 40, 8),
        "Tenir un journal pendant 1 semaine 📝 (+70)": ("💼 Discipline", 70, 12),
        "Planifier la semaine à venir 📅 (+50)": ("💼 Discipline", 50, 6),

        # Missions spéciales
        "Participer à un défi de groupe (100 km en 1 mois) 💪 (+500)": ("🏃 Endurance", 500, 50),
        "Accomplir un objectif important à long terme 🎯 (+1000)": ("💪 Force", 1000, 100),
        "Suivre un programme de développement personnel pendant 30 jours 🌟 (+1000)": ("🧠 Intelligence", 1000, 120),
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
