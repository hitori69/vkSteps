Накрутка шагов ВКонтакте

Инструкция: https://youtu.be/LmyRrAjEeFo

Документация по VK API: https://dev.vk.com/ru/api/api-requests

Если появятся вопросы: https://vk.com/hitori.gotou

Редко бывает, что при получении токена сервер возвращает ошибку с текстом need_captcha. Тогда в ответе от сервера запоминаете значение в captcha_sid и смотрите картинку по ссылке в captcha_img  (там будет картинка с капчей). Далее отправляете новый запрос, аналогичный исходному, за исключением того, что в конце добавляете ещё два параметра:
• captcha_sid — поле captcha_sid, полученное в предыдущем запросе;
• captcha_key — то, что увидели на картинке.
Например:   ....&password=ПАРОЛЬ&captcha_sid=629467422056&captcha_key=дм2е6фр

Если у вас на новом аккаунте нет пароля и вы просто входите по номеру телефона, то в настройках нужно будет включить двухфакторную аутентификацию, тогда появится окно с предложением установить пароль для страницы.

Со смартфона тоже можно накручивать, но получать токен с телефона и вписывать его в файл не очень удобно. Это лучше предварительно сделать на компьютере. На андроиде для запуска кода можно скачать Termux, и в нём установить python и requests.

ВАЖНО! Токен это по факту ключ, который даёт полный доступ к аккаунту через код. Если получать токен описанным в видео способом, то полученный токен будет без срока действия. К тому же через данный токен можно получить доступ даже к сообщениям. Поэтому его важно либо хранить в секрете, либо просто сделать нерабочим за ненадобностью. Для обнуления токена можно либо сменить пароль, либо завершить сеансы. Кнопка завершения сеансов доступна как с телефона, так и с компьютера.

НИКОМУ, НИ ПРИ КАКИХ ОБСТОЯТЕЛЬСТВАХ НЕ ПОКАЗЫВАЙТЕ И НЕ ПЕРЕДАВАЙТЕ СВОЙ ДЕЙСТВУЮЩИЙ ТОКЕН, А ТАКЖЕ НЕ ИСПОЛЬЗУЙТЕ ЕГО В НЕПОНЯТНОМ ВАМ КОДЕ
