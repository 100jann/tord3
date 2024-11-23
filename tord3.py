import streamlit as st
import random
from deep_translator import GoogleTranslator

source_language = 'en'  # English
target_language_mk = 'mk'  # Macedonian
target_language_tr = 'tr'  # Turkish
translator_mk = GoogleTranslator(source=source_language, target=target_language_mk)
translator_tr = GoogleTranslator(source=source_language, target=target_language_tr)

# Truths and Dares in English
truths_en = [
    "What is the biggest fantasy you have never shared?",
    "What is the strangest compliment you have ever received?",
    "What is the most attractive feature of the person opposite you?",
    "What is your favorite sexy outfit?",
    "When was the last time you did something brave for your partner?",
    "What excites you most about the partner to your right?",
    "Have you ever dreamed of someone in this room?",
    "What is the weirdest idea you’ve had for the bedroom?",
    "What is your favorite location for intimate moments?",
    "Pick one: would you rather watch your partner have a threesome with another couple or have your partner watch you?",
    "Do you watch porn? If so, what is your favorite kind of porn to watch alone? If you watch with a partner, what is your favorite kind to watch together?",
    "Prior to meeting your partner, had you ever had a threesome or moresome?",
    "What are the biggest age differences – both younger and older – you’ve experienced between you and a sexual partner?",
    "Do you like any form of pain or dominance/submission play during any sort of sex? Please be specific – e.g., spanking, choking, electricity, scratching, other impact play, etc.",
    "If you could have sex with a celebrity, whom would you choose and why?",
    "Other than your private parts, name an area on your body that’s really sensitive and enjoyable sexually.",
    "Anal sex – yay or nay? What about other forms of anal play?",
    "What is your favorite sex toy? Do you use it on yourself or only on partners?",
    "Have you ever been to a strip club? If not, would you? What about with a partner? Would you like to watch your partner get a lap dance, or have him/her watch you?",
    "When was the last time you pleasured yourself alone, without a partner?",
    "Voyeur or exhibitionist? Would you rather have sex in front of others or watch others have sex?",
    "What is your favorite sexual position? Is it the position you use most often? Why or why not? And if not, what is the one you use most often?",
    "Would you go to a resort for swingers? If so, would you only go as a couple, or would you go alone?",
    "What type of underwear do you like wearing the most? Does this change based on who’s going to see it? What type of underwear do you prefer seeing on a sexual partner?",
    "If you could only have ONE of vaginal, oral, or anal sex for the rest of your life, which would it be and why?",
    "What's the most embarrassing thing you have masturbated with or to?",
    "What's a weird thing you can do with your body? It can be sexual or not.",
    "You're traveling and a very attractive and charming person 20 years your senior offers you $2,000 for one night of anonymous sex. Do you accept? Does this change whether you’re single or part of a couple? If not $2,000, do you have a price you’d do it for?",
    "Have you ever had an orgy (for simplicity’s sake, let’s define it as 5 or more people in the room)? If not, would you?",
    "What type of swimsuit do you prefer, or wish you had the courage to wear? Does it vary based on location? What type of swimsuits do you prefer seeing on others?",
    "What is your favorite physical characteristic on your own body?",
    "How often do you have sex in a week? How often do you wish you had sex?",
    "Have you ever been caught doing naughty stuff by someone you really didn’t want to see you? Describe the situation in detail."
]
dares_en = [
"Kiss someone and rub their chest (OVER clothes).",
    "Kiss someone who isn’t your partner, with tongue.",
    "Remove one article of your own clothing.",
    "Kiss someone’s neck and collar bone.",
    "Rub someone’s private parts, under their pants/skirt but above their underwear.",
    "Nibble someone’s ear until they moan or giggle.",
    "Kiss someone and guide their hands to a place you want them to rub.",
    "Pick someone who isn’t your partner and whisper something you’d like to do with them sexually.",
    "Pick two people other than yourself and have them passionately kiss each other.",
    "Choose someone else to remove an article of clothing.",
    "Pick someone who isn’t your partner, lie down with them, and make out for 20 seconds.",
    "Close your eyes while everyone who wants kisses you, then guess who’s who.",
    "Remove one article of your own clothing.",
    "Choose someone else to remove an article of clothing.",
    "Pick two people and all three of you stand and make out, while touching each other OVER the clothes.",
    "Sit on another player’s lap, or have someone else sit on your lap, until your next turn.",
    "Close your eyes and squeeze other player’s butt cheeks (those who choose to participate), then guess who’s who.",
    "Do your best impression of the worst sex partner you’ve had.",
    "Give 3 spanks to someone or receive 3 spanks from someone (your choice).",
    "Pick two other people to kiss each other.",
    "All male players remove an article of clothing.",
    "All female players remove an article of clothing.",
    "Pick someone who isn’t your partner and whisper something you’d like to do with them sexually.",
    "Kiss someone who isn’t your partner, with tongue.",
    "Pick two people and all three of you stand and make out, while touching each other OVER the clothes.",
    "Remove one article of your own clothing.",
    "Choose someone else to remove an article of clothing.",
    "Put your hands down the pants of partner from other couple until the next 3 challenges are completed & do as you wish",
    "You’re in school & you’ve been a bad student. You must take a spanking & then “time-out” in opposite couple partner lap for 5 minutes.",
    "Take off your pants. The person of the opposite sex, who is not your boyfriend/girlfriend, licks between the legs. If you move, you will have to take off your shirt, and you can only dress it again after 5 minutes. ",
    
]

def translate_text(text, dest_language):
    try:
        translated = GoogleTranslator(source=source_language, target=dest_language).translate(text)
        return translated  # Return the translated string directly
    except Exception as e:
        return f"Translation Error: {e}"

st.title("Truth or Dare / Вистина или Предизвик / Doğruluk mu Cesaret mi")

# Create button container for truth, dare, and random buttons
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        truth_button = st.button("Вистина / Doğruluk")
    with col2:
        dare_button = st.button("Предизвик / Cesaret")
    with col3:
        random_button = st.button("Random")

# Initialize session state to keep track of available truths and dares
if 'truths_remaining' not in st.session_state:
    st.session_state.truths_remaining = truths_en.copy()
    st.session_state.dares_remaining = dares_en.copy()
    st.session_state.truths_used = []
    st.session_state.dares_used = []

# Function to get a random truth or dare and remove it from the list
def get_random_item(item_list, used_list):
    if len(item_list) == 0:  # Reset the list if all items are used
        item_list = truths_en.copy() if used_list == st.session_state.truths_used else dares_en.copy()
        used_list.clear()  # Clear the used list to start fresh
    item = random.choice(item_list)
    item_list.remove(item)
    used_list.append(item)
    return item, item_list, used_list

# Generate truth or dare based on the button pressed
if truth_button:
    # Select a random truth
    truth_en, st.session_state.truths_remaining, st.session_state.truths_used = get_random_item(
        st.session_state.truths_remaining, st.session_state.truths_used)
    truth_mk = translate_text(truth_en, target_language_mk)  # Translate to Macedonian
    truth_tr = translate_text(truth_en, target_language_tr)  # Translate to Turkish

    st.markdown(f"""
        <div class="truth-dare-container">
            <p><strong>Truth:</strong> {truth_en}</p>
            <p><strong>Вистина:</strong> {truth_mk}</p>
            <p><strong>Doğruluk:</strong> {truth_tr}</p>
        </div>
    """, unsafe_allow_html=True)

if dare_button:
    # Select a random dare
    dare_en, st.session_state.dares_remaining, st.session_state.dares_used = get_random_item(
        st.session_state.dares_remaining, st.session_state.dares_used)
    dare_mk = translate_text(dare_en, target_language_mk)  # Translate to Macedonian
    dare_tr = translate_text(dare_en, target_language_tr)  # Translate to Turkish

    st.markdown(f"""
        <div class="truth-dare-container">
            <p><strong>Dare:</strong> {dare_en}</p>
            <p><strong>Предизвик:</strong> {dare_mk}</p>
            <p><strong>Cesaret:</strong> {dare_tr}</p>
        </div>
    """, unsafe_allow_html=True)

if random_button:
    # Randomly decide between truth and dare
    choice = random.choice(["truth", "dare"])
    if choice == "truth":
        truth_en, st.session_state.truths_remaining, st.session_state.truths_used = get_random_item(
            st.session_state.truths_remaining, st.session_state.truths_used)
        truth_mk = translate_text(truth_en, target_language_mk)  # Translate to Macedonian
        truth_tr = translate_text(truth_en, target_language_tr)  # Translate to Turkish

        st.markdown(f"""
            <div class="truth-dare-container">
                <p><strong>Truth:</strong> {truth_en}</p>
                <p><strong>Вистина:</strong> {truth_mk}</p>
                <p><strong>Doğruluk:</strong> {truth_tr}</p>
            </div>
        """, unsafe_allow_html=True)

    else:
        dare_en, st.session_state.dares_remaining, st.session_state.dares_used = get_random_item(
            st.session_state.dares_remaining, st.session_state.dares_used)
        dare_mk = translate_text(dare_en, target_language_mk)  # Translate to Macedonian
        dare_tr = translate_text(dare_en, target_language_tr)  # Translate to Turkish

        st.markdown(f"""
            <div class="truth-dare-container">
                <p><strong>Dare:</strong> {dare_en}</p>
                <p><strong>Предизвик:</strong> {dare_mk}</p>
                <p><strong>Cesaret:</strong> {dare_tr}</p>
            </div>
        """, unsafe_allow_html=True)