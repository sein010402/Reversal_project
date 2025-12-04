import pygame, math, random

#1. 게임초기화
pygame.init()

#2. 게임창 옵션 설정
size = [500, 750]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("hangman")

#3. 게임 내 필요한 설정
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)
hint_font = pygame.font.Font("C:/Windows/Fonts/a고딕12.ttf", 80)
entry_font = pygame.font.Font("C:/Windows/Fonts/a고딕14.ttf", 60)
no_font = pygame.font.Font("C:/Windows/Fonts/a고딕14.ttf", 40)
title_font = pygame.font.Font("C:/Windows/Fonts/a고딕18.ttf", 80)
sub_title_font = pygame.font.Font("C:/Windows/Fonts/a고딕14.ttf", 20)
finish_font = pygame.font.Font("C:/Windows/Fonts/a고딕14.ttf", 30)

def tup_r(tup):
    temp_list = []
    for a in tup :
        temp_list.append(round(a))
    return tuple(temp_list)

exit = False

while not exit:
    entry_text = ""
    drop = False
    enter_go = False
    ready = False
    game_over = False
    save = False
    play_again = False


    # A가 영어단어 1개를 생각한다
    f = open(r"C:\Users\lsi\python_vsc\game_project\voca.txt", "r", encoding='UTF-8')
    raw_data = f.read()
    f.close()
    data_list = raw_data.split("\n")
    data_list = data_list[:-1]

    while True :
        r_index = random.randrange(0,len(data_list))
        word = data_list[r_index].replace(u"\xa0",u" ").split(" ")[1]
        if len(word) <= 6 :
            break
    word = word.upper()

    # 단어의 글자 수만큼 밑줄을 긋는다
    word_show = "_"*len(word)
    try_num = 0
    ok_list = []
    no_list = []

    k = 0
    # 시작화면
    while not exit :
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            if event.type == pygame.KEYDOWN:
                ready = True
        if ready == True: break
        
        screen.fill(white)
        title = title_font.render("HANGMAN", True, black)
        title_size = title.get_size()
        title_pos = (size[0]/2-title_size[0]/2, size[1]/2-title_size[1]/2)
        screen.blit(title, title_pos)
        
        sub_title = sub_title_font.render("Press any key to start", True, black)
        sub_title_size = sub_title.get_size()
        sub_title_pos = (size[0]/2-sub_title_size[0]/2, size[1]*3/5-sub_title_size[1]/2)
        if pygame.time.get_ticks()%1000 > 300 :
            screen.blit(sub_title, sub_title_pos)
        
        pygame.display.flip()
        


    #4. 메인 이벤트
    while not exit :
        #4-1. FPS설정
        clock.tick(60)
        #4-2. 각종 입력 감지
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            if event.type == pygame.KEYDOWN:
                if drop == False and try_num == 8:
                    continue
                if game_over == True: play_again = True
                key_name = pygame.key.name(event.key)
                if (key_name == "return" or key_name == "enter") :
                    if entry_text != "" and (ok_list+no_list).count(entry_text) == 0:
                        enter_go = True
                elif len(key_name) == 1:
                    if (ord(key_name) >= 65 and ord(key_name) <= 90) or (ord(key_name) >= 97 and ord(key_name) <= 122):
                        entry_text = key_name.upper()
                    else : entry_text = ""
                else : entry_text = ""

                    
        #4-3. 입력, 시간에 따른 변화
        if play_again == True : break
        if try_num == 8 : k += 1
        if enter_go == True:
            result = word.find(entry_text)
            if result == -1 :
                try_num += 1
                no_list.append(entry_text)
            else :
                ok_list.append(entry_text)
                for i in range(len(word)):
                    if word[i] == entry_text:
                        word_show = word_show[:i] + entry_text + word_show[i+1:]
            enter_go = False
            entry_text = ""
        if drop == True:
            game_over = True 
            word_show = word
        if word_show.find("_") == -1 and game_over==False:
            game_over = True
            save = True
            
        #4-4. 그리기
        screen.fill(white)
        A =tup_r((0,size[1]*2/3))
        B = (size[0], A[1])
        C = tup_r((size[0]/6, A[1]))
        D = (C[0], C[0])
        E = tup_r((size[0]/2, D[0]))
        if save != True :
            pygame.draw.line(screen, black, A, B, 3)
            pygame.draw.line(screen, black, C, D, 3)
            pygame.draw.line(screen, black, D, E, 3)
        
        F = tup_r((E[0], E[1]+size[0]/6))
        if drop == False or save != True :
            pygame.draw.line(screen, black, E, F, 3)
        
        
        r_head = round(size[0]/12)
        if drop == True : G = (F[0], F[1]+r_head+k*10)
        else : G = (F[0], F[1]+r_head)
        if try_num >= 1 or save == True: pygame.draw.circle(screen, black, G, r_head, 3)
        
        H = (G[0], G[1]+r_head)
        I = (H[0], H[1]+r_head)
        if try_num >= 2 or save == True: pygame.draw.line(screen, black, H, I, 3)
        
        l_arm = r_head*2
        J = tup_r((I[0]-l_arm*math.cos(30*math.pi/180), 
                I[1]+l_arm*math.sin(30*math.pi/180)))
        K = tup_r((I[0]+l_arm*math.cos(30*math.pi/180), 
                I[1]+l_arm*math.sin(30*math.pi/180)))
        if try_num >= 3 or save == True: pygame.draw.line(screen, black, I, J, 3)
        if try_num >= 4 or save == True: pygame.draw.line(screen, black, I, K, 3)
        
        L = (I[0], I[1]+l_arm)
        if try_num >= 5 or save == True: pygame.draw.line(screen, black, I, L, 3)
        
        l_leg = round(l_arm*1.5)
        M = tup_r((L[0]-l_leg*math.cos(60*math.pi/180), 
                L[1]+l_leg*math.sin(60*math.pi/180)))
        N = tup_r((L[0]+l_leg*math.cos(60*math.pi/180), 
                L[1]+l_leg*math.sin(60*math.pi/180)))
        if try_num >= 6 or save == True: pygame.draw.line(screen, black, L, M, 3)
        if try_num >= 7 or save == True: pygame.draw.line(screen, black, L, N, 3)
        
        if drop == False and try_num == 8:
            O = tup_r((size[0]/2-size[0]/6, (E[1]+F[1])/2))
            P = (O[0]+k*2, O[1])
            if P[0] > size[0]/2+size[0]/6 :
                P = tup_r((size[0]/2+size[0]/6 , O[1]))
                drop = True
                k = 0
            pygame.draw.line(screen, red, O, P, 3)
        
        #힌트 표시하기
        hint = hint_font.render(word_show, True, black)
        hint_size = hint.get_size()
        hint_pos = tup_r((size[0]/2-hint_size[0]/2, 
                        size[1]*5/6-hint_size[1]/2))
        screen.blit(hint, hint_pos)
        
        #입력창 표시하기
        entry = entry_font.render(entry_text, True, white)
        entry_size = entry.get_size()
        entry_pos = (size[0]/2-entry_size[0]/2, size[1]*17/18-entry_size[1]/2)
        
        entry_bg_size = 60
        pygame.draw.rect(screen, black, tup_r((size[0]/2-entry_bg_size/2, 
                                            size[1]*17/18-entry_bg_size/2, 
                                            entry_bg_size, entry_bg_size)))
        screen.blit(entry, entry_pos)
        
        # 오답 표시하기
        no_text = " ".join(no_list)
        no = no_font.render(no_text, True, red)
        no_pos = tup_r((20, size[1]*2/3+20))
        screen.blit(no, no_pos)
    
    #종료 화면
    if game_over == True :
        finish_bg = pygame.Surface(size)
        finish_bg.fill(black)
        finish_bg.set_alpha(200)
        screen.blit(finish_bg, (0,0))
        if save == True : finish_text = "You saved the man"
        else : finish_text = "You killed the man"
        finish = finish_font.render(finish_text, True, white)
        finish_size = finish.get_size()
        finish_pos = tup_r((size[0]/2-finish_size[0]/2, size[1]/2-finish_size[1]/2))
        screen.blit(finish, finish_pos)
        sub_title = sub_title_font.render("Press any key to play again", True, white)
        sub_title_size = sub_title.get_size()
        sub_title_pos = (size[0]/2-sub_title_size[0]/2, size[1]*3/5-sub_title_size[1]/2)
        screen.blit(sub_title, sub_title_pos)    
        #4-5. 업데이트
        pygame.display.flip()

#5. 게임종료
pygame.quit()