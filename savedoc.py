<div class="mainMenu">
        <div class="dropdown">
            <ul>
                <li ><button class="dropbtn"><a href="#">МАГАЗИН</a></button></li>
                    <ul class="dropdownContent">
                        <li><a href="#">КОЛЬЦА</a></li>
                        <li><a href="#">КОЛЬЕ</a></li>
                        <li><a href="#">БРАСЛЕТЫ</a></li>
                        <li><a href="#">СЕРЬГИ</a></li>
                        <li><a href="#">ЛУЛЫ</a></li>
                    </ul>
                <li><a href="#">ОПЛАТА И ДОСТАВКА</a></li>
                <li><a href="#">ОБРАТНАЯ СВЯЗЬ</a></li>
                <li><a href="#">TELEGRAM</a></li>
                <li><a href="#">ВКОНТАКТЕ</a></li>
                <li><a href="#">МОЙ АККАУНТ</a></li>
            </ul>
        </div>
    </div>
    
    
    
css 
html {
    font-family: Arial, Helvetica, sans-serif;
}

.dropbtn {
    background-color: #4caf50;
    color: white;
    padding: 16px;
    font-size: 16px;
    border: none;
}

.dropdown {
    position: relative;
    display: inline-block;
}

.dropdownContent {
    display: none;
    position: absolute;
    background-color: #f1f1f1;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
    z-index: 1;
}

.dropdownContent a {
    color: black;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
}

.dropdownContent a:hover {background-color: pink;} /* Изменение цвета выпадающих ссылок при наведении курсора */
.dropdown:hover .dropdownContent {display: block;} /* Показать выпадающее меню при наведении курсора */
.dropdown:hover .dropbtn{background-color: #3e8e41;} /* Изменение цвета фона кнопки раскрывающегося списка при отображении содержимого раскрывающегося списка */