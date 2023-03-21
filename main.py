import telebot
import random


bot = telebot.TeleBot('6245949653:AAGQi6aptB632Ghxp2xKT0KySHI1XyaHb5g')
with open('present.txt', 'r', encoding="utf-8") as podarok:
    with open('worlds.txt', 'r', encoding="utf-8") as f:
        with open('worlds_2.txt', 'r', encoding="utf-8") as g:
            with open('worlds_3.txt', 'r', encoding="utf-8") as h:
                with open('worlds_4.txt', 'r', encoding="utf-8") as j:
                    with open('users.txt', "a", encoding="utf-8") as u:
                        with open('users.txt', "r", encoding="utf-8") as ur:
                            with open('message.txt', "a+", encoding="utf-8") as m:
                                with open('stikers_id.txt') as s:
                                    stikers = s.readlines()
                                    stiker = [line.rstrip() for line in stikers]
                                    world_1 = f.read().split(',')
                                    world_2 = g.read().split(',')
                                    world_3 = h.read().split(',')
                                    world_4 = j.read().split(',')
                                    users_read = ur.read().split('\n')
                                    len_1 = len(world_1)
                                    len_2 = len(world_2)
                                    len_3 = len(world_3)
                                    len_4 = len(world_4)
                                    len_5 = len(stiker)
                                    @bot.message_handler()
                                    def fmk(message):
                                        user_info_2 = f'(username:{message.from_user.username} text:{message.text} date:{message.date})\n'
                                        m.write(user_info_2)
                                        user_info = f'(first_name:{message.from_user.first_name} last_name:{message.from_user.last_name}' \
                                                    f' username:{message.from_user.username})\n'
                                        if user_info not in users_read:
                                            u.write(user_info)



                                        num = random.randint(1, 3)
                                        num_1 = random.randint(0, len_1 - 1)
                                        num_1_2 = random.randint(0, len_1 - 1)
                                        num_2 = random.randint(0, len_2 - 1)
                                        num_3 = random.randint(0, len_3 - 1)
                                        num_4 = random.randint(0, len_4 - 1)
                                        num_5 = random.randint(0, len_5 - 1)
                                        message.text.lower()
                                        mess = message.text.split()
                                        # print(world_1)
                                        # print(num_1)
                                        # print(world_1[num_1])
                                        # print(message.chat.first_name, message.chat.last_name, mess)


                                        if message.text == 'подарок':
                                            bot.send_message(message.chat.id, podarok.read(), parse_mode='html')
                                        # TODO: привет
                                        if 'привет' in mess:
                                            bot.send_message(message.chat.id, f'привет {world_1[num_1]}', parse_mode='html')
                                            bot.send_sticker(message.chat.id, stiker[num_5])

                                        # TODO: я тебя люблю
                                        elif 'я' and 'тебя' and 'люблю' in mess:
                                            if num == 1:
                                                bot.send_message(message.chat.id, f'я тебя тоже {world_1[num_1]}', parse_mode='html')
                                            elif num == 2:
                                                bot.send_message(message.chat.id, f'и я тебя люблю {world_1[num_1]}', parse_mode='html')
                                            elif num == 3:
                                                bot.send_message(message.chat.id, f'я тебя тоже люблю {world_1[num_1]}', parse_mode='html')
                                            bot.send_sticker(message.chat.id, stiker[num_5])
                                        # TODO: у меня все хорошо
                                        elif 'как' and 'дела?' in mess:
                                            if num == 1:
                                                bot.send_message(message.chat.id, f'у меня все {world_2[num_2]}', parse_mode='html')
                                            elif num == 2:
                                                bot.send_message(message.chat.id, f'все {world_2[num_2]}', parse_mode='html')
                                            elif num == 3:
                                                bot.send_message(message.chat.id, f'{world_2[num_2]} у меня ж ты есть ', parse_mode='html')
                                            bot.send_message(message.chat.id, f'а как у тебя {world_1[num_1]}?', parse_mode='html')
                                            bot.send_sticker(message.chat.id, stiker[num_5])

                                        # TODO: ответ на ^
                                        elif 'тоже' in mess:
                                            if num == 1:
                                                bot.send_message(message.chat.id, f'ну и {world_3[num_3]}', parse_mode='html')
                                            elif num == 2:
                                                bot.send_message(message.chat.id, f'вот и {world_3[num_3]}', parse_mode='html')
                                            elif num == 3:
                                                bot.send_message(message.chat.id, f'{world_3[num_3]}', parse_mode='html')
                                            bot.send_sticker(message.chat.id, stiker[num_5])

                                        # TODO: что такое?
                                        elif message.text in world_1:
                                            if num == 1:
                                                bot.send_message(message.chat.id, f'что такое {world_1[num_2]}?', parse_mode='html')
                                            elif num == 2:
                                                bot.send_message(message.chat.id, f'что то случилось {world_1[num_2]}?', parse_mode='html')
                                            elif num == 3:
                                                bot.send_message(message.chat.id, f'слушаю {world_2[num_1]}', parse_mode='html')
                                            bot.send_sticker(message.chat.id, stiker[num_5])

                                        #TODO: я тебя люблю
                                        elif 'я' and 'тебя' and 'люблю' in mess:
                                            if num == 1:
                                                bot.send_message(message.chat.id, f'я тебя тоже {world_1[num_2]}', parse_mode='html')
                                            elif num == 2:
                                                bot.send_message(message.chat.id, f'и я тебя люблю {world_1[num_2]}', parse_mode='html')
                                            elif num == 3:
                                                bot.send_message(message.chat.id, f'я тебя тоже люблю {world_1[num_2]}', parse_mode='html')
                                            bot.send_sticker(message.chat.id, stiker[num_5])

                                        elif 'я' and 'рада' and 'ты' and 'есть' in mess:
                                            bot.send_message(message.chat.id, f'я тоже {world_4[num_4]} рад что ты у меня есть {world_1[num_1]}',
                                                             parse_mode='html')
                                            bot.send_sticker(message.chat.id, stiker[num_5])

                                        # TODO: что делаешь?
                                        elif 'что' and 'делаешь?' in mess:
                                            if num == 1:
                                                bot.send_message(message.chat.id, f'да хуйней одной занимаюсь но скоро тебе отвечу {world_1[num_1]}',
                                                                 parse_mode='html')
                                            elif num == 2:
                                                bot.send_message(message.chat.id, f'да блять дела опять но при первой же возможности отвечу'
                                                                                  f' {world_1[num_1]}', parse_mode='html')
                                            elif num == 3:
                                                bot.send_message(message.chat.id, f'занимаюсь делами но совсем скоро отвечу {world_1[num_1]}',
                                                                 parse_mode='html')
                                            bot.send_message(message.chat.id, f'а ты чем занята {world_1[num_1_2]}?', parse_mode='html')
                                            bot.send_sticker(message.chat.id, stiker[num_5])

                                    bot.polling(none_stop=True)







