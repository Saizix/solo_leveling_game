import streamlit as st
from datetime import date
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
menu = st.sidebar.radio("Aller vers :", ["🏅 Stats & Rang", "📅 Missions", "🎒 Inventaire"])

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
        "Course rapide 5km 🏃 (+75)": ("🏃 Endurance", 75, 8),
        "Randonnée 2h 🏞️ (+120)": ("🏃 Endurance", 120, 12),
        # Force
        "50 pompes 💪 (+20)": ("💪 Force", 20, 5),
        "100 abdos 💪 (+25)": ("💪 Force", 25, 4),
        "Squats 30 répétitions 💪 (+40)": ("💪 Force", 40, 6),
        "Tractions 10 💪 (+50)": ("💪 Force", 50, 7),
        # Intelligence
        "Lecture 1h 📚 (+60)": ("🧠 Intelligence", 60, 8),
        "Apprendre anglais 🇬🇧 (+40)": ("🧠 Intelligence", 40, 5),
        "Résolution de problèmes logiques 🧠 (+50)": ("🧠 Intelligence", 50, 6),
        "Mémorisation de vocabulaire 🧠 (+30)": ("🧠 Intelligence", 30, 4),
        # Mana
        "Méditer 10 min 🧘 (+15)": ("🔮 Mana", 15, 4),
        "Réduction du stress avec yoga 🔮 (+25)": ("🔮 Mana", 25, 6),
        "Journée sans distractions numériques 🔮 (+40)": ("🔮 Mana", 40, 8),
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
