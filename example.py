# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 14:32:45 2020

@author: qtckp
"""

import os

from content_detector.detector import get_content_from_text



if __name__=='__main__':
    
    
    lines = [
        "знаю JS, CSS, C++",
             'ms word, excel',
             "Мы ищем опытного Android-разработчика для разработки мобильной версии проекта по управлению жизненным циклом зданий.   Требования:  Опыт создания Android-приложений от 3-лет Хорошее знание методологии ООП Понимание принципов работы сервисно-ориентированной архитектуры Знание паттернов проектирование и умение их применять Желательно хорошее знание английского языка Большим плюсом будет наличие примеров работ  Условия:  Трудоустройство согласно ТК РФ Стабильная высокая «белая» заработная плата (зависит от уровня мастерства кандидата и обсуждается индивидуально при собеседовании) Гибкий график работы Возможность работы как в офисе, так и удаленно"]
    print(get_content_from_text(lines))
    
    
    for file_number in (0,1,2,3,4,5):
        
        print()
        with open(f"{os.path.dirname(__file__)}/learning/train_samples/{file_number}.txt", 'r', encoding = 'utf-8') as f:
            lines = f.readlines()
        
        answer = get_content_from_text(lines)
        print(f"file {file_number}:")
        print(answer)


