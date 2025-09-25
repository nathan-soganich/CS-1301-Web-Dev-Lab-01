import streamlit as st

st.set_page_config(page_title="Phase II Quiz (Simple)", page_icon="🧠", layout="centered")
st.title("Which Study Habit Fits You?")

st.caption(
    "Answer five quick questions. Click **Get result** to see your study-habit profile."
)

# Simple form to collect answers in one submit
with st.form("phase2_quiz"):  # NEW
    # 1) Radio (single choice)
    q1 = st.radio(
        "1) 8:00 AM and you’ve got a tough class—what’s your move?",
        [
            "Gym first, then lecture.",
            "Front row, 10 minutes early.",
            "Watch the recording later.",
            "Study with friends.",
        ],
        index=None,
    )

    # 2) Multiselect
    q2 = st.multiselect(
        "2) Pick your go-to study tools:",
        ["Notion", "Absurd amountd of caffeine", "Google Calendar", "Whiteboard", "Headphones", "Playlist"],
    )

    # 3) Selectbox
    q3 = st.selectbox(
        "3) Where do you focus best?",
        ["Clough Library", "Dorm desk", "Outdoor tables", "Coffee shop", "Any quiet corner"],
        index=None,
        placeholder="Choose a spot...",
    )

    # 4) Slider
    q4 = st.slider(
        "4) Typical focus block length (minutes):",
        min_value=15,
        max_value=120,
        value=45,
        step=5,
    )

    # 5) Number input
    q5 = st.number_input(
        "5) How many planned study sessions per week?",
        min_value=0,
        max_value=30,
        value=7,
        step=1,
    )

    submitted = st.form_submit_button("Get result")  # NEW

if submitted:
    # Minimal scoring (kept straightforward)
    score_focus = score_social = score_ballance = score_flexible = 0

    if q1:
        if "Gym" in q1:
            score_focus += 2; score_flexible += 1
        elif "Front row" in q1:
            score_ballance += 2; score_focus += 1
        elif "recording" in q1:
            score_flexible += 2
        elif "friends" in q1:
            score_social += 2

    if q2:
        if "Anki" in q2: score_ballance += 2
        if "Google Calendar" in q2: score_ballance += 2
        if "Notion" in q2: score_ballance += 1
        if "Whiteboard" in q2: score_focus += 1
        if "Headphones" in q2: score_focus += 2
        if "Playlist" in q2: score_flexible += 1

    if q3:
        if q3 == "Clough Library": score_focus += 1; score_ballance += 1
        elif q3 == "Dorm desk": score_ballance += 2
        elif q3 == "Outdoor tables": score_flexible += 2
        elif q3 == "Coffee shop": score_social += 1; score_flexible += 1
        else: score_focus += 1

    if q4 >= 90: score_focus += 2
    elif q4 >= 60: score_focus += 1; score_ballance += 1
    else: score_flexible += 1

    if q5 >= 14: score_ballance += 2
    elif q5 >= 7: score_ballance += 1
    else: score_flexible += 1

    profile = max(
        [
            ("Laser-Focus Scholar", score_focus),
            ("Systems Planner", score_ballance),
            ("Collab Catalyst", score_social),
            ("Adaptive Generalist", score_flexible),
        ],
        key=lambda x: x[1],
    )[0]

    st.success(f"**You’re a:** {profile}")
    st.metric("Questions answered", 5)  # NEW
    st.balloons()  # NEW

    with st.expander("Why this result?"):
        st.write(
            "- **Laser-Focus Scholar**: longer focus blocks, quiet tools/spaces.\n"
            "- **Systems Planner**: uses scheduling/recall tools; regular sessions.\n"
            "- **Collab Catalyst**: prefers people and lively spaces.\n"
            "- **Adaptive Generalist**: flexible times/locations and methods."
        )



