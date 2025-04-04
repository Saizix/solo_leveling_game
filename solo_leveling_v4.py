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
menu = st.sidebar.radio("Aller vers :", ["🏅 Stats & Rang", "📅 Missions", "🎒 Inventaire", "⚔️ Donjons"])

# 🧍 INFO PERSO
niveau = st.session_state.get("niveau", 1)
xp = st.session_state.get("xp", 0)
xp_max = 100 * niveau
energie = st.session_state.get("energie", 100)
stamina = st.session_state.get("stamina", 100)

# Initialisation de l'inventaire et des missions si elles ne sont pas déjà définies
if "inventaire" not in st.session_state:
    st.session_state["inventaire"] = {"Potion de Vie": 2, "Potion d'Energie": 1}

if "stats" not in st.session_state:
    st.session_state["stats"] = {
        "💪 Force": 0,
        "🏃 Endurance": 0,
        "🧠 Intelligence": 0,
        "🎯 Agilité": 0,
        "🔮 Mana": 0,
        "❤️ Vitalité": 0,
        "💼 Discipline": 0
    }

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
        for stat, value in st.session_state["stats"].items():
            st.markdown(f"{stat} : **{value}**")

# 📄 PAGE : MISSIONS
if menu == "📅 Missions":
    st.title(f"📅 Missions du {date.today().strftime('%d/%m/%Y')}")
    
    missions = {
        "10 km à vélo 🚴 (+100)": ("🏃 Endurance", 100, 10),
        "30 min de marche 🚶 (+30)": ("🏃 Endurance", 30, 5),
        "50 pompes 💪 (+20)": ("💪 Force", 20, 5),
        "Lecture 1h 📚 (+60)": ("🧠 Intelligence", 60, 8),
        "Méditer 10 min 🧘 (+15)": ("🔮 Mana", 15, 4),
        "Dormir 8h 😴 (+40)": ("❤️ Vitalité", 40, 10),
        "Journée sans procrastination ✅ (+50)": ("💼 Discipline", 50, 6),
    }

    gagne_xp = 0
    for label, (stat_key, xp_gain, cost) in missions.items():
        if st.checkbox(label, key=label):
            if stamina >= cost:
                st.session_state["stats"][stat_key] += xp_gain
                xp += xp_gain
                stamina -= cost
                gagne_xp += xp_gain
                st.success(f"✅ +{xp_gain} {stat_key}")
            else:
                st.warning(f"⚠️ Pas assez de stamina. Coût: {cost}")

# 📄 PAGE : INVENTAIRE
if menu == "🎒 Inventaire":
    st.title("🎒 Inventaire")
    for item, quantity in st.session_state["inventaire"].items():
        st.markdown(f"**{item}** : {quantity}")

# 📄 PAGE : DONJONS
if menu == "⚔️ Donjons":
    st.title("⚔️ Donjon : Combat épique !")

    # Niveau de difficulté du donjon
    difficulty = st.selectbox("Choisis ton niveau de difficulté", ["Facile", "Moyen", "Difficile"])

    # Ennemis et récompenses
    enemies = {
        "Facile": {"nom": "Gobelin", "hp": 30, "force": 5, "xp": 100},
        "Moyen": {"nom": "Orc", "hp": 50, "force": 10, "xp": 200},
        "Difficile": {"nom": "Dragon", "hp": 100, "force": 20, "xp": 500},
    }

    enemy = enemies[difficulty]

    st.markdown(f"### Ennemis : {enemy['nom']}")
    st.markdown(f"**HP :** {enemy['hp']} | **Force :** {enemy['force']} | **Récompense :** {enemy['xp']} XP")

    if st.button("Lancer le combat"):
        # Combat aléatoire : chance de gagner en fonction de la force de l'utilisateur
        user_strength = st.session_state["stats"]["💪 Force"]
        combat_result = random.randint(1, user_strength + enemy["force"])

        if combat_result > enemy["force"]:
            st.success(f"🎉 Vous avez vaincu le {enemy['nom']} ! Vous gagnez {enemy['xp']} XP.")
            xp += enemy["xp"]
            st.session_state["xp"] = xp  # Mise à jour de l'XP
            st.session_state["energie"] -= 10  # Consommation d'énergie
        else:
            st.error(f"💥 Vous avez perdu contre le {enemy['nom']}. Essayez de vous renforcer avant de revenir.")

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
st.session_state["stats"] = st.session_state["stats"]
st.session_state["inventaire"] = st.session_state["inventaire"]
