# -*- coding: utf-8 -*-
import telebot
import constants, os
import botan
from telebot import types

bot = telebot.TeleBot(constants.token)

@bot.message_handler(commands=["start"])
def start(c):
    bot.send_photo(c.chat.id,
                   photo="https://photos.app.goo.gl/jBnxr8v3o1CS58O53")
    key = types.InlineKeyboardMarkup(row_width=1)
    but_1 = types.InlineKeyboardButton(text="Русский", callback_data="rus")
    but_2 = types.InlineKeyboardButton(text="English", callback_data="eng")
    but_3 = types.InlineKeyboardButton(text="Deutsch", callback_data="ger")
    key.add(but_1, but_2, but_3)
    bot.send_message(c.chat.id, "Выберите язык интерфейса:\n\nSelect the interface language:\n\nWählen Sie die Sprache der Benutzeroberfläche:", reply_markup=key)

def rus_menu(bot, message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row("Объем инвестиций", "Истории успеха")
    user_markup.row("Территориальное расположение")
    user_markup.row("Путеводитель инвестора")
    user_markup.row("Контакты", "🇬🇧", "🇩🇪")
    bot.send_message(message.from_user.id, "Выберите интересующий Вас пункт", reply_markup=user_markup)

def eng_menu(bot, message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row("Investment size", "Success Stories")
    user_markup.row("Geographical location")
    user_markup.row("Guide to Investment")
    user_markup.row("Contacts", "🇷🇺", "🇩🇪")
    bot.send_message(message.from_user.id, "Select the item you are interested in", reply_markup=user_markup)

def ger_menu(bot, message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row("Volumen der Investitionen", "Erfolgsgeschichten")
    user_markup.row("Geografische Lage")
    user_markup.row("Leitfaden für Investoren")
    user_markup.row("Kontaktieren Sie uns", "🇷🇺", "🇬🇧")
    bot.send_message(message.from_user.id, "Select the item you are interested in", reply_markup=user_markup)

@bot.callback_query_handler(func=lambda c:True)
def inlin(c):
    if c.data == "rus":
        user_markup = telebot.types.ReplyKeyboardMarkup(True)
        user_markup.row("Объем инвестиций", "Истории успеха")
        user_markup.row("Территориальное расположение")
        user_markup.row("Путеводитель инвестора")
        user_markup.row("Контакты","🇬🇧", "🇩🇪")
        bot.send_message(c.message.chat.id, "Выберите интересующий Вас пункт", reply_markup=user_markup)
    if c.data == "eng":
        user_markup = telebot.types.ReplyKeyboardMarkup(True)
        user_markup.row("Investment size", "Success Stories")
        user_markup.row("Geographical location")
        user_markup.row("Guide to Investment")
        user_markup.row("Contacts", "🇷🇺", "🇩🇪")
        bot.send_message(c.message.chat.id, "Select the item you are interested in", reply_markup=user_markup)
    if c.data == "ger":
        user_markup = telebot.types.ReplyKeyboardMarkup(True)
        user_markup.row("Volumen der Investitionen", "Erfolgsgeschichten")
        user_markup.row("Geografische Lage")
        user_markup.row("Leitfaden für Investoren")
        user_markup.row("Kontaktieren Sie uns", "🇷🇺", "🇬🇧")
        bot.send_message(c.message.chat.id, "Wählen Sie den Artikel aus, an dem Sie interessiert sind", reply_markup=user_markup)

# Русское меню (колбэки) ===========================================================

    if c.data == "Динамика инвестиций":
        directory = "C:/DOCinvest/1Объем инвестиций/1Динамика инвестиций"
        all_files_directory = os.listdir(directory)
        print(all_files_directory)
        for file in all_files_directory:
            doc = open(directory + "/" + file, "rb")
            bot.send_chat_action(c.message.chat.id, "upload_document")
            bot.send_document(c.message.chat.id, doc)
    if c.data == "Краткие сведения":
        directory = "C:/DOCinvest/1Объем инвестиций/2Краткие сведения"
        all_files_directory = os.listdir(directory)
        print(all_files_directory)
        for file in all_files_directory:
            doc = open(directory + "/" + file, "rb")
            bot.send_chat_action(c.message.chat.id, "upload_document")
            bot.send_document(c.message.chat.id, doc)

    if c.data == "DANONE":
        bot.send_photo(c.message.chat.id, photo="https://photos.app.goo.gl/ZrqfKmMjXo04U7ov1")
        key = types.InlineKeyboardMarkup(row_width=2)
        but_1 = types.InlineKeyboardButton(text="История успеха", callback_data="История успеха DANONE")
        but_2 = types.InlineKeyboardButton(text="Больше фото", callback_data="danonefoto")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, "История успеха фирмы DANONE", reply_markup=key)
    if c.data == "История успеха DANONE":
        directory = "C:/DOCinvest/2Истории успеха/1Данон/история"
        all_files_directory = os.listdir(directory)
        print(all_files_directory)
        for file in all_files_directory:
            doc = open(directory + "/" + file, "rb")
            bot.send_chat_action(c.message.chat.id, "upload_document")
            bot.send_document(c.message.chat.id, doc)

    if c.data == "NESTLE":
        bot.send_photo(c.message.chat.id, photo="https://photos.app.goo.gl/3LfFracV9alZtcRs2")
        key = types.InlineKeyboardMarkup(row_width=2)
        but_1 = types.InlineKeyboardButton(text="История успеха", callback_data="История успеха NESTLE")
        but_2 = types.InlineKeyboardButton(text="Больше фото", callback_data="nestlefoto")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, "История успеха фирмы NESTLE", reply_markup=key)
    if c.data == "История успеха NESTLE":
        directory = "C:/DOCinvest/2Истории успеха/2Нестле/история"
        all_files_directory = os.listdir(directory)
        print(all_files_directory)
        for file in all_files_directory:
            doc = open(directory + "/" + file, "rb")
            bot.send_chat_action(c.message.chat.id, "upload_document")
            bot.send_document(c.message.chat.id, doc)

    if c.data == "CLAAS":
        bot.send_photo(c.message.chat.id, photo="https://photos.app.goo.gl/LnT7TzS4lbQlBtnd2")
        key = types.InlineKeyboardMarkup(row_width=2)
        but_1 = types.InlineKeyboardButton(text="История успеха", callback_data="История успеха CLAAS")
        but_2 = types.InlineKeyboardButton(text="Больше фото", callback_data="claasfoto")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, "История успеха фирмы CLAAS", reply_markup=key)
    if c.data == "История успеха CLAAS":
        directory = "C:/DOCinvest/2Истории успеха/3Клаас/история"
        all_files_directory = os.listdir(directory)
        print(all_files_directory)
        for file in all_files_directory:
            doc = open(directory + "/" + file, "rb")
            bot.send_chat_action(c.message.chat.id, "upload_document")
            bot.send_document(c.message.chat.id, doc)

    if c.data == "KNAUF":
        bot.send_photo(c.message.chat.id, photo="https://photos.app.goo.gl/bjVcvnDokd1yao5e2")
        key = types.InlineKeyboardMarkup(row_width=2)
        but_1 = types.InlineKeyboardButton(text="История успеха", callback_data="История успеха KNAUF")
        but_2 = types.InlineKeyboardButton(text="Больше фото", callback_data="knauffoto")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, "История успеха фирмы KNAUF", reply_markup=key)
    if c.data == "История успеха KNAUF":
        directory = "C:/DOCinvest/2Истории успеха/4Кнауф/история"
        all_files_directory = os.listdir(directory)
        print(all_files_directory)
        for file in all_files_directory:
            doc = open(directory + "/" + file, "rb")
            bot.send_chat_action(c.message.chat.id, "upload_document")
            bot.send_document(c.message.chat.id, doc)

    if c.data == "Карта Краснодарского края":
        directory = "C:/DOCinvest/3Территориальное расположение/1Карта КК"
        all_files_directory = os.listdir(directory)
        print(all_files_directory)
        for file in all_files_directory:
            doc = open(directory + "/" + file, "rb")
            bot.send_chat_action(c.message.chat.id, "upload_document")
            bot.send_document(c.message.chat.id, doc)
    if c.data == "Проекты муниципальных образований":
        directory = "C:/DOCinvest/3Территориальное расположение/2Проекты по МО"
        all_files_directory = os.listdir(directory)
        print(all_files_directory)
        for file in all_files_directory:
            doc = open(directory + "/" + file, "rb")
            bot.send_chat_action(c.message.chat.id, "upload_document")
            bot.send_document(c.message.chat.id, doc)

    if c.data == "danonefoto":
        bot.send_photo(c.message.chat.id, photo="https://photos.app.goo.gl/Xfv5mPA7WVvYHgmR2")
        bot.send_photo(c.message.chat.id, photo="https://photos.app.goo.gl/vcJQmWza7QWTZx2T2")
        bot.send_photo(c.message.chat.id, photo="https://photos.app.goo.gl/1fGzJdJfG9X1titH2")
    if c.data == "nestlefoto":
        bot.send_photo(c.message.chat.id, photo="https://photos.app.goo.gl/bLxcYCZTyX7hpnkV2")
        bot.send_photo(c.message.chat.id, photo="https://photos.app.goo.gl/TV5qwm2HqC1zdIqD3")
        bot.send_photo(c.message.chat.id, photo="https://photos.app.goo.gl/WCeaa71Jn9DMeipy2")
    if c.data == "claasfoto":
        bot.send_photo(c.message.chat.id, photo="https://photos.app.goo.gl/UCwYnSuB1mKxrCVH2")
        bot.send_photo(c.message.chat.id, photo="https://photos.app.goo.gl/5ZPLzDLhbFbGIhYe2")
        bot.send_photo(c.message.chat.id, photo="https://photos.app.goo.gl/jOs3oFmmeXG3ZaNI2")
    if c.data == "knauffoto":
        bot.send_photo(c.message.chat.id, photo="https://photos.app.goo.gl/GQADYR0wZKEuf47f2")
        bot.send_photo(c.message.chat.id, photo="https://photos.app.goo.gl/uWVePJIX0dritTeG3")
        bot.send_photo(c.message.chat.id, photo="https://photos.app.goo.gl/TlSJuxfRdvRqlivs2")


# Английское меню (колбэки) ===========================================================

    if c.data == "Dynamics of investments":
        directory = "C:/DOCinvest/1Объем инвестиций/1Динамика инвестиций"
        all_files_directory = os.listdir(directory)
        print(all_files_directory)
        for file in all_files_directory:
            doc = open(directory + "/" + file, "rb")
            bot.send_chat_action(c.message.chat.id, "upload_document")
            bot.send_document(c.message.chat.id, doc)
    if c.data == "Brief information":
        directory = "C:/DOCinvest/1Объем инвестиций/2Краткие сведения"
        all_files_directory = os.listdir(directory)
        print(all_files_directory)
        for file in all_files_directory:
            doc = open(directory + "/" + file, "rb")
            bot.send_chat_action(c.message.chat.id, "upload_document")
            bot.send_document(c.message.chat.id, doc)

    if c.data == "engDANONE":
        bot.send_photo(c.message.chat.id, photo="https://photos.app.goo.gl/ZrqfKmMjXo04U7ov1")
        key = types.InlineKeyboardMarkup(row_width=2)
        but_1 = types.InlineKeyboardButton(text="Success Stories", callback_data="DANONE Success Stories")
        but_2 = types.InlineKeyboardButton(text="More photo", callback_data="danonefoto")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, "DANONE Success Stories", reply_markup=key)
    if c.data == "DANONE Success Stories":
        directory = "C:/DOCinvest/2Истории успеха/1Данон/история"
        all_files_directory = os.listdir(directory)
        print(all_files_directory)
        for file in all_files_directory:
            doc = open(directory + "/" + file, "rb")
            bot.send_chat_action(c.message.chat.id, "upload_document")
            bot.send_document(c.message.chat.id, doc)

    if c.data == "engNESTLE":
        bot.send_photo(c.message.chat.id, photo="https://photos.app.goo.gl/3LfFracV9alZtcRs2")
        key = types.InlineKeyboardMarkup(row_width=2)
        but_1 = types.InlineKeyboardButton(text="Success Stories", callback_data="NESTLE Success Stories")
        but_2 = types.InlineKeyboardButton(text="More photo", callback_data="nestlefoto")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, "NESTLE Success Stories", reply_markup=key)
    if c.data == "NESTLE Success Stories":
        directory = "C:/DOCinvest/2Истории успеха/2Нестле/история"
        all_files_directory = os.listdir(directory)
        print(all_files_directory)
        for file in all_files_directory:
            doc = open(directory + "/" + file, "rb")
            bot.send_chat_action(c.message.chat.id, "upload_document")
            bot.send_document(c.message.chat.id, doc)

    if c.data == "engCLAAS":
        bot.send_photo(c.message.chat.id, photo="https://photos.app.goo.gl/LnT7TzS4lbQlBtnd2")
        key = types.InlineKeyboardMarkup(row_width=2)
        but_1 = types.InlineKeyboardButton(text="Success Stories", callback_data="CLAAS Success Stories")
        but_2 = types.InlineKeyboardButton(text="More photo", callback_data="claasfoto")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, "CLAAS Success Stories", reply_markup=key)
    if c.data == "CLAAS Success Stories":
        directory = "C:/DOCinvest/2Истории успеха/3Клаас/история"
        all_files_directory = os.listdir(directory)
        print(all_files_directory)
        for file in all_files_directory:
            doc = open(directory + "/" + file, "rb")
            bot.send_chat_action(c.message.chat.id, "upload_document")
            bot.send_document(c.message.chat.id, doc)

    if c.data == "engKNAUF":
        bot.send_photo(c.message.chat.id, photo="https://photos.app.goo.gl/bjVcvnDokd1yao5e2")
        key = types.InlineKeyboardMarkup(row_width=2)
        but_1 = types.InlineKeyboardButton(text="Success Stories", callback_data="KNAUF Success Stories")
        but_2 = types.InlineKeyboardButton(text="More photo", callback_data="knauffoto")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, "KNAUF Success Stories", reply_markup=key)
    if c.data == "KNAUF Success Stories":
        directory = "C:/DOCinvest/2Истории успеха/4Кнауф/история"
        all_files_directory = os.listdir(directory)
        print(all_files_directory)
        for file in all_files_directory:
            doc = open(directory + "/" + file, "rb")
            bot.send_chat_action(c.message.chat.id, "upload_document")
            bot.send_document(c.message.chat.id, doc)

    if c.data == "Map of the Krasnodar Territory":
        directory = "C:/DOCinvest/3Территориальное расположение/1Карта КК"
        all_files_directory = os.listdir(directory)
        print(all_files_directory)
        for file in all_files_directory:
            doc = open(directory + "/" + file, "rb")
            bot.send_chat_action(c.message.chat.id, "upload_document")
            bot.send_document(c.message.chat.id, doc)
    if c.data == "Projects of municipalities":
        directory = "C:/DOCinvest/3Территориальное расположение/2Проекты по МО"
        all_files_directory = os.listdir(directory)
        print(all_files_directory)
        for file in all_files_directory:
            doc = open(directory + "/" + file, "rb")
            bot.send_chat_action(c.message.chat.id, "upload_document")
            bot.send_document(c.message.chat.id, doc)

# Немецкое меню (колбэки) ===========================================================
    if c.data == "Dynamik der Investitionen":
        directory = "C:/DOCinvest/1Объем инвестиций/1Динамика инвестиций"
        all_files_directory = os.listdir(directory)
        print(all_files_directory)
        for file in all_files_directory:
            doc = open(directory + "/" + file, "rb")
            bot.send_chat_action(c.message.chat.id, "upload_document")
            bot.send_document(c.message.chat.id, doc)
    if c.data == "Kurze Information":
        directory = "C:/DOCinvest/1Объем инвестиций/2Краткие сведения"
        all_files_directory = os.listdir(directory)
        print(all_files_directory)
        for file in all_files_directory:
            doc = open(directory + "/" + file, "rb")
            bot.send_chat_action(c.message.chat.id, "upload_document")
            bot.send_document(c.message.chat.id, doc)

    if c.data == "gerDANONE":
        bot.send_photo(c.message.chat.id, photo="https://photos.app.goo.gl/ZrqfKmMjXo04U7ov1")
        key = types.InlineKeyboardMarkup(row_width=2)
        but_1 = types.InlineKeyboardButton(text="Erfolgsgeschichte", callback_data="DANONE Erfolgsgeschichte")
        but_2 = types.InlineKeyboardButton(text="Mehr Fotos", callback_data="danonefoto")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, "DANONE Erfolgsgeschichte", reply_markup=key)
    if c.data == "DANONE Erfolgsgeschichte":
        directory = "C:/DOCinvest/2Истории успеха/1Данон/история"
        all_files_directory = os.listdir(directory)
        print(all_files_directory)
        for file in all_files_directory:
            doc = open(directory + "/" + file, "rb")
            bot.send_chat_action(c.message.chat.id, "upload_document")
            bot.send_document(c.message.chat.id, doc)

    if c.data == "gerNESTLE":
        bot.send_photo(c.message.chat.id, photo="https://photos.app.goo.gl/3LfFracV9alZtcRs2")
        key = types.InlineKeyboardMarkup(row_width=2)
        but_1 = types.InlineKeyboardButton(text="Erfolgsgeschichte", callback_data="NESTLE Erfolgsgeschichte")
        but_2 = types.InlineKeyboardButton(text="Mehr Fotos", callback_data="nestlefoto")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, "NESTLE Erfolgsgeschichte", reply_markup=key)
    if c.data == "NESTLE Erfolgsgeschichte":
        directory = "C:/DOCinvest/2Истории успеха/2Нестле/история"
        all_files_directory = os.listdir(directory)
        print(all_files_directory)
        for file in all_files_directory:
            doc = open(directory + "/" + file, "rb")
            bot.send_chat_action(c.message.chat.id, "upload_document")
            bot.send_document(c.message.chat.id, doc)

    if c.data == "gerCLAAS":
        bot.send_photo(c.message.chat.id, photo="https://photos.app.goo.gl/LnT7TzS4lbQlBtnd2")
        key = types.InlineKeyboardMarkup(row_width=2)
        but_1 = types.InlineKeyboardButton(text="Erfolgsgeschichte", callback_data="CLAAS Erfolgsgeschichte")
        but_2 = types.InlineKeyboardButton(text="Mehr Fotos", callback_data="claasfoto")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, "CLAAS Erfolgsgeschichte", reply_markup=key)
    if c.data == "CLAAS Erfolgsgeschichte":
        directory = "C:/DOCinvest/2Истории успеха/3Клаас/история"
        all_files_directory = os.listdir(directory)
        print(all_files_directory)
        for file in all_files_directory:
            doc = open(directory + "/" + file, "rb")
            bot.send_chat_action(c.message.chat.id, "upload_document")
            bot.send_document(c.message.chat.id, doc)

    if c.data == "gerKNAUF":
        bot.send_photo(c.message.chat.id, photo="https://photos.app.goo.gl/bjVcvnDokd1yao5e2")
        key = types.InlineKeyboardMarkup(row_width=2)
        but_1 = types.InlineKeyboardButton(text="Erfolgsgeschichte", callback_data="KNAUF Erfolgsgeschichte")
        but_2 = types.InlineKeyboardButton(text="Mehr Fotos", callback_data="knauffoto")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, "KNAUF Erfolgsgeschichte", reply_markup=key)
    if c.data == "KNAUF Erfolgsgeschichte":
        directory = "C:/DOCinvest/2Истории успеха/4Кнауф/история"
        all_files_directory = os.listdir(directory)
        print(all_files_directory)
        for file in all_files_directory:
            doc = open(directory + "/" + file, "rb")
            bot.send_chat_action(c.message.chat.id, "upload_document")
            bot.send_document(c.message.chat.id, doc)

    if c.data == "Karte der Region Krasnodar":
        directory = "C:/DOCinvest/3Территориальное расположение/1Карта КК"
        all_files_directory = os.listdir(directory)
        print(all_files_directory)
        for file in all_files_directory:
            doc = open(directory + "/" + file, "rb")
            bot.send_chat_action(c.message.chat.id, "upload_document")
            bot.send_document(c.message.chat.id, doc)
    if c.data == "Projekte von Gemeinden":
        directory = "C:/DOCinvest/3Территориальное расположение/2Проекты по МО"
        all_files_directory = os.listdir(directory)
        print(all_files_directory)
        for file in all_files_directory:
            doc = open(directory + "/" + file, "rb")
            bot.send_chat_action(c.message.chat.id, "upload_document")
            bot.send_document(c.message.chat.id, doc)
# ===================================================================================

@bot.message_handler(content_types=["text"])
def handle_start(message):

# РУССКОЕ МЕНЮ (Основа) ========================================================
    if message.text == "Объем инвестиций":
        key = types.InlineKeyboardMarkup(row_width=1)
        but_1 = types.InlineKeyboardButton(text="Динамика инвестиций", callback_data="Динамика инвестиций")
        but_2 = types.InlineKeyboardButton(text="Краткие сведения", callback_data="Краткие сведения")
        key.add(but_1, but_2)
        bot.send_message(message.chat.id, "Объем инвестиций в экономику Краснодарского края", reply_markup=key)
        botan.track(constants.botan_key, message.chat.id, message, "Объем инвестиций")
    if message.text == "Истории успеха":
        key = types.InlineKeyboardMarkup(row_width=1)
        but_1 = types.InlineKeyboardButton(text="DANONE", callback_data="DANONE")
        but_2 = types.InlineKeyboardButton(text="NESTLE", callback_data="NESTLE")
        but_3 = types.InlineKeyboardButton(text="CLAAS", callback_data="CLAAS")
        but_4 = types.InlineKeyboardButton(text="KNAUF", callback_data="KNAUF")
        key.add(but_1, but_2, but_3, but_4)
        bot.send_message(message.chat.id, "Истории успеха", reply_markup=key)
        botan.track(constants.botan_key, message.chat.id, message, "Истории успеха")
    if message.text == "Территориальное расположение":
        key = types.InlineKeyboardMarkup(row_width=1)
        but_1 = types.InlineKeyboardButton(text="Карта Краснодарского края", callback_data="Карта Краснодарского края")
        but_2 = types.InlineKeyboardButton(text="Проекты муниципальных образований", callback_data="Проекты муниципальных образований")
        key.add(but_1, but_2)
        bot.send_message(message.chat.id, "Территориальное расположение", reply_markup=key)
        botan.track(constants.botan_key, message.chat.id, message, "Территориальное расположение")
    if message.text == "Путеводитель инвестора":
        bot.send_message(message.from_user.id, "Происходит загрузка файла в формате PDF (4,5 mb)")
        directory = "C:/DOCinvest/4Путеводитель инвестора/1На русском языке"
        all_files_directory = os.listdir(directory)
        print(all_files_directory)
        for file in all_files_directory:
            doc = open(directory + "/" + file, "rb")
            bot.send_chat_action(message.chat.id, "upload_document")
            bot.send_document(message.chat.id, doc)
    if message.text == "Контакты":
        bot.send_message(message.chat.id, """\r
        <b>Департамент инвестиций и развития малого и среднего предпринимательства Краснодарского края</b>\n
        <i>Адрес: 350014, г, Краснодар, ул. Красная, 35
        investkuban@krasnodar.ru</i>\n
        <a href="https://goo.gl/maps/ARh9L6EuPR52" title="Показать на карте">Показать на карте</a>""",
                         parse_mode="HTML")
        bot.send_message(message.chat.id, "+78612517360")
        bot.send_message(message.chat.id, "Для консультации на русском языке пишите @georgy_gubin")
        botan.track(constants.botan_key, message.chat.id, message, "Контакты")
    if message.text == "Contacts":
        bot.send_message(message.chat.id, """\r
        <b>Department of Investments and Development of Small and Medium Enterprises of Krasnodar Region</b>\n
        <i>Address: 350014, г, Краснодар, ул. Красная, 35
        investkuban@krasnodar.ru</i>\n
        <a href="https://goo.gl/maps/ARh9L6EuPR52" title="Show on the map">Show on the map</a>""",
                         parse_mode="HTML")
        bot.send_message(message.chat.id, "+78612517360")
        bot.send_message(message.chat.id, "For consultation in English, write @roman_portnoy")
        botan.track(constants.botan_key, message.chat.id, message, "Контакты")
    if message.text == "Kontaktieren Sie uns":
        bot.send_message(message.chat.id, """\r
        <b>Abteilung für Investitionen und Entwicklung von kleinen und mittleren Unternehmen der Region Krasnodar</b>\n
        <i>Adresse: 350014, г, Краснодар, ул. Красная, 35
        investkuban@krasnodar.ru</i>\n
        <a href="https://goo.gl/maps/ARh9L6EuPR52" title="Auf Karte anzeigen">Auf Karte anzeigen</a>""",
                         parse_mode="HTML")
        bot.send_message(message.chat.id, "+78612517360")
        bot.send_message(message.chat.id, "Für eine Beratung auf Deutsch schreiben Sie bitte @roman_portnoy")
        botan.track(constants.botan_key, message.chat.id, message, "Контакты")
    if message.text == "🇷🇺":
        rus_menu(bot, message)
    if message.text == "🇬🇧":
        eng_menu(bot, message)
    if message.text == "🇩🇪":
        ger_menu(bot, message)

# АНГЛИЙСКОЕ МЕНЮ (Основа) ========================================================
    if message.text == "Investment size":
        key = types.InlineKeyboardMarkup(row_width=1)
        but_1 = types.InlineKeyboardButton(text="Dynamics of investments", callback_data="Dynamics of investments")
        but_2 = types.InlineKeyboardButton(text="Brief information", callback_data="Brief information")
        key.add(but_1, but_2)
        bot.send_message(message.chat.id, "The volume of investments into the economy of the Krasnodar Territory", reply_markup=key)
        botan.track(constants.botan_key, message.chat.id, message, "Investment size")
    if message.text == "Success Stories":
        key = types.InlineKeyboardMarkup(row_width=1)
        but_1 = types.InlineKeyboardButton(text="DANONE", callback_data="engDANONE")
        but_2 = types.InlineKeyboardButton(text="NESTLE", callback_data="engNESTLE")
        but_3 = types.InlineKeyboardButton(text="CLAAS", callback_data="engCLAAS")
        but_4 = types.InlineKeyboardButton(text="KNAUF", callback_data="engKNAUF")
        key.add(but_1, but_2, but_3, but_4)
        bot.send_message(message.chat.id, "Success Stories", reply_markup=key)
        botan.track(constants.botan_key, message.chat.id, message, "Success Stories")
    if message.text == "Geographical location":
        key = types.InlineKeyboardMarkup(row_width=1)
        but_1 = types.InlineKeyboardButton(text="Map of the Krasnodar Territory", callback_data="Map of the Krasnodar Territory")
        but_2 = types.InlineKeyboardButton(text="Projects of municipalities", callback_data="Projects of municipalities")
        key.add(but_1, but_2)
        bot.send_message(message.chat.id, "Geographical location", reply_markup=key)
        botan.track(constants.botan_key, message.chat.id, message, "Geographical location")
    if message.text == "Guide to Investment":
        bot.send_message(message.from_user.id, "The file is being downloaded in PDF format (4,5 mb)")
        directory = "C:/DOCinvest/4Путеводитель инвестора/2На английском языке"
        all_files_directory = os.listdir(directory)
        print(all_files_directory)
        for file in all_files_directory:
            doc = open(directory + "/" + file, "rb")
            bot.send_chat_action(message.chat.id, "upload_document")
            bot.send_document(message.chat.id, doc)
# НЕМЕЦКОЕ МЕНЮ (Основа) ========================================================
    if message.text == "Volumen der Investitionen":
        key = types.InlineKeyboardMarkup(row_width=1)
        but_1 = types.InlineKeyboardButton(text="Dynamik der Investitionen", callback_data="Dynamik der Investitionen")
        but_2 = types.InlineKeyboardButton(text="Kurze Information", callback_data="Kurze Information")
        key.add(but_1, but_2)
        bot.send_message(message.chat.id, "Das Volumen der Investitionen in die Wirtschaft der Region Krasnodar", reply_markup=key)
        botan.track(constants.botan_key, message.chat.id, message, "Volumen der Investitionen")
    if message.text == "Erfolgsgeschichten":
        key = types.InlineKeyboardMarkup(row_width=1)
        but_1 = types.InlineKeyboardButton(text="DANONE", callback_data="gerDANONE")
        but_2 = types.InlineKeyboardButton(text="NESTLE", callback_data="gerNESTLE")
        but_3 = types.InlineKeyboardButton(text="CLAAS", callback_data="gerCLAAS")
        but_4 = types.InlineKeyboardButton(text="KNAUF", callback_data="gerKNAUF")
        key.add(but_1, but_2, but_3, but_4)
        bot.send_message(message.chat.id, "Erfolgsgeschichten", reply_markup=key)
        botan.track(constants.botan_key, message.chat.id, message, "Erfolgsgeschichten")
    if message.text == "Geografische Lage":
        key = types.InlineKeyboardMarkup(row_width=1)
        but_1 = types.InlineKeyboardButton(text="Karte der Region Krasnodar", callback_data="Karte der Region Krasnodar")
        but_2 = types.InlineKeyboardButton(text="Projekte von Gemeinden", callback_data="Projekte von Gemeinden")
        key.add(but_1, but_2)
        bot.send_message(message.chat.id, "Geografische Lage", reply_markup=key)
        botan.track(constants.botan_key, message.chat.id, message, "Geografische Lage")
    if message.text == "Leitfaden für Investoren":
        bot.send_message(message.from_user.id, "Die Datei wird im PDF-Format heruntergeladen (4,5 mb)")
        directory = "C:/DOCinvest/4Путеводитель инвестора/2На английском языке"
        all_files_directory = os.listdir(directory)
        print(all_files_directory)
        for file in all_files_directory:
            doc = open(directory + "/" + file, "rb")
            bot.send_chat_action(message.chat.id, "upload_document")
            bot.send_document(message.chat.id, doc)


while True:
    try:
        bot.polling(none_stop=True)

    # ConnectionError and ReadTimeout because of possible timout of the requests library

    # TypeError for moviepy errors

    # maybe there are others, therefore Exception
    except Exception as e:
        telebot.logger.error(e)
        time.sleep(15)