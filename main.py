import streamlit as st
import base64

foundations_ai_button = f"""<form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
  <input type="hidden" name="cmd" value="_s-xclick" />
  <input type="hidden" name="hosted_button_id" value="KVR7Y9BWP4U2N" />
  <input type="hidden" name="currency_code" value="RUB" />
  <input type="image" src="https://www.paypalobjects.com/ru_RU/i/btn/btn_buynow_SM.gif" border="0" name="submit" title="PayPal — это безопасный и быстрый способ оплаты через интернет!" alt="Купить сейчас" />
</form>"""


transformers_text_course = f"""<form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
  <input type="hidden" name="cmd" value="_s-xclick" />
  <input type="hidden" name="hosted_button_id" value="YWH5YZSYM9FVS" />
  <input type="hidden" name="currency_code" value="RUB" />
  <input type="image" src="https://www.paypalobjects.com/ru_RU/i/btn/btn_buynow_SM.gif" border="0" name="submit" title="PayPal — это безопасный и быстрый способ оплаты через интернет!" alt="Купить сейчас" />
</form>"""

# Assuming you have a list of dictionaries for each product
products = [
    {"image": "Used/AICourse.png", "title": "Введение в Искусственный Интеллект с Python для Начинающих", "details_url": "https://stepik.org/course/193579/promo", "buy_url": f"{foundations_ai_button}"},
    {"image": "Used/TransformersCourse.png", "title": "Поколение ИИ: Большие Языковые Модели для Работы с Текстом", "details_url": "https://stepik.org/course/175490/promo", "buy_url": f"{transformers_text_course}"},
    # Add all your products here (total 12)
    {"image": "Used/DeepLearningCourse.png", "title": "Поколение ИИ: Практическое Глубокое Обучение с Pytorch", "details_url": "#", "buy_url": "#"},
    {"image": "Used/LogicCourse.png", "title": "Логика и Теория Игр для ИИ, Аналитики Данных и Data Science", "details_url": "#", "buy_url": "#"},
    
]

# Function to set a background image
# def set_background_image(image_path):
#     with open(image_path, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read()).decode()
#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background-image: url("data:image/png;base64,{encoded_string}");
#             background-size: cover;
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# # Set background image
# set_background_image('./Background2.png')
# # set_background_image('')

# Function to set a black background
def set_black_background():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: black;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Set black background
set_black_background()


# Header
st.header("Аве Кодер")

# Explaining "Как это работает"
# st.write("Here you explain how it works...")

# Function to display a single product
def display_product(product):
    st.image(product["image"], width=200)  # Adjust width as necessary
    st.write(product["title"])  # Display the product title
    links = []
    if product["details_url"] != "#":
        links.append(f"[Подробнее]({product['details_url']})")
    if product["buy_url"] != "#":
        links.append(f"{product['buy_url']}")
    if links:
        st.markdown(" ".join(links), unsafe_allow_html=True)
    else:
        st.write("Скоро") 

   
# Display products in rows of 3
for i in range(0, len(products), 3):
    cols = st.columns(3)
    for col, product in zip(cols, products[i:i+3]):
        with col:
            display_product(product)

st.markdown("""
    <br>
    <hr>
    <br>
""", unsafe_allow_html=True)

# Footer
st.write("Как Это Работает")
st.write("""Вы можете посмотреть подробности понравившегося курса на Stepik, кликнув по ссылке 'Подробнее'. Когда вы решите купить нужный курс, кликайте по ссылке
         'Купить', оплачивайте через PayPal и в течении короткого времени вам на почту придет ссылка на курс. Все готово - вы можете начинать учиться. 
         ВАЖНО: при покупке курса через Paypal, убедитесь, что вы указали правильный мейл, доступ на Stepik будет предоставлен именно для указанного мейла.
         Если у вас есть вопросы, вы можете задать их в специализированной группе в Телеграм: [{https://t.me/ave_courses}]  """)


