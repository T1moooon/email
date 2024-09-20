import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")
name_site = "https://dvmn.org/referrals/QrwNiRSbhADbrc4ck1pO0mapjWGwcixzLapMOqaK/"
name_friend = "Александр"
name_admin = "Тимон"
letter = """\
From: t1moooong@yandex.ru
To: t1moooong@gmail.com
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

Привет, {f}! {u} приглашает тебя на сайт {s}!

{s} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {s}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {s}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""".format(s = name_site, u = name_admin, f = name_friend)
letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(login, password)
server.sendmail('t1moooong@yandex.ru', 't1moooong@gmail.com', letter)
server.quit()