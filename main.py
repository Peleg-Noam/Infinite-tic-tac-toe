import pygame as pg
import pygame.mouse


pg.init()
size = (751, 501)
screen = pg.display.set_mode(size)
pg.display.set_caption("Tic Tac Toe")
global square_size
square_size = 50
score_font = pygame.font.Font('freesansbold.ttf', 15)
o_score = 0
o_score_text = score_font.render('O score: ' + str(o_score), True, (10, 0, 0))
o_score_textRect = o_score_text.get_rect()
o_score_textRect.center = (size[0] // 15, size[1] // 20)

x_score = 0
x_score_text = score_font.render('X Score: ' + str(x_score), True, (10, 0, 0))
x_score_textRect = x_score_text.get_rect()
x_score_textRect.center = (size[0] - size[0] // 15, size[1] // 20)

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('X wins!', True, (0,255,255))
textRect = text.get_rect()
textRect.center = (size[0] // 2, size[1] // 2)


rematch_font = pygame.font.Font('freesansbold.ttf', 32)
rematch_text = rematch_font.render('Rematch!', True, (0, 255, 255))
rematch_textRect = rematch_text.get_rect()
rematch_textRect.center = (size[0] // 2, size[1] // 2 + 50)


def turn_to_tuple(test):
    new_str = ""
    new_str2 = ""
    test = test.replace(" ", "")
    num = 1
    while test[num] != ",":
        num += 1
    new_str += test[1:num]
    num += 1
    r = num
    while test[r] != ")":
        r += 1
    new_str2 += test[num:r]
    return int(float(new_str)), int(float(new_str2))


def draw_screen(indexes, offset, playerturn):
    screen.fill((255, 253, 208))
    for x in range(0, size[0], square_size):
        pg.draw.line(screen, (0, 0, 0), (x, 0), (x, size[1]))
    for y in range(0, size[1], square_size):
        pg.draw.line(screen, (0, 0, 0), (0, y), (size[0], y))
    for index in indexes:
        if indexes.index(index) % 2 == playerturn:
            try:
                pg.draw.circle(screen, (0, 0, 255), (index[0] + offset[0], index[1] + offset[1]), square_size/2 - 2, 3)
            except:
                pass
        else:
            try:
                pg.draw.line(screen, (255, 0, 0), (index[0] - square_size/2 + offset[0], index[1] - square_size/2 + offset[1]), (index[0] + square_size/2 + offset[0], index[1] + square_size/2 + offset[1]), 3)
                pg.draw.line(screen, (255, 0, 0), (index[0] + square_size/2 + offset[0], index[1] - square_size/2 + offset[1]), (index[0] - square_size/2 + offset[0], index[1] + square_size/2 + offset[1]), 3)
            except:
                pass


def check_row(indexes, value):
    is_win = False
    state = indexes.index(value) % 2
    for r in range(5):
        if (value[0], value[1] + r * square_size) not in indexes or\
                indexes.index((value[0], value[1] + r * square_size)) % 2 != state:
            is_win = False
            break
        else:
            is_win = True
    return is_win


def check_column(indexes, value):
    is_win = False
    state = indexes.index(value) % 2
    for p in range(5):
        if (value[0] + square_size * p, value[1]) not in indexes \
                or indexes.index((value[0] + square_size * p, value[1])) % 2 != state:
            is_win = False
            break
        else:
            is_win = True
    return is_win


def check_right_diag(indexes, value):
    is_win = False
    state = indexes.index(value) % 2
    for p in range(5):
        if (value[0] + square_size * p, value[1] + square_size * p) not in indexes \
                or indexes.index((value[0] + square_size * p, value[1] + square_size * p)) % 2 != state:
            is_win = False
            break
        else:
            is_win = True
    return is_win


def check_left_diag(indexes, value):
    is_win = False
    state = indexes.index(value) % 2
    for p in range(5):
        if (value[0] - square_size * p, value[1] + square_size * p) not in indexes \
                or indexes.index((value[0] - square_size * p, value[1] + square_size * p)) % 2 != state:
            is_win = False
            break
        else:
            is_win = True
    return is_win


def detect_win(indexes):
    for index in indexes:
        if check_row(indexes, index) or check_column(indexes, index) or check_right_diag(indexes, index) or check_left_diag(indexes, index):
            return True
    return False







def run_game():

    character_turn = "x"
    msg = "nothing"
    receive_msg = "nothing"
    player_turn = 1
    global square_size
    square_size = 40
    x_score = 0
    o_score = 0
    run = True
    win = False
    offset = [0, 0]
    indexes = []
    while run:
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:

                pos = pygame.mouse.get_pos()
                if win:
                    if rematch_textRect[0] <= pos[0] <= rematch_textRect[0] + rematch_textRect[2] \
                            and rematch_textRect[1] <= pos[1] <= rematch_textRect[1] + rematch_textRect[3]:
                        win = False
                        indexes.clear()
                        if character_turn == "o":
                            character_turn = "x"
                        else:
                            character_turn = "o"
                        if player_turn == 0:
                            player_turn = 1
                        else:
                            player_turn = 0

                else:
                    if event.button == 1:
                        pos_index = (pos[0] - offset[0] - pos[0] % square_size + square_size/2, pos[1] - offset[1] - pos[1] % square_size + square_size/2)
                        if pos_index not in indexes:
                            indexes.append((pos[0] - offset[0] - pos[0] % square_size + square_size/2, pos[1] - offset[1] - pos[1] % square_size + square_size/2))
                            if character_turn == "o":
                                character_turn = "x"
                            else:
                                character_turn = "o"
            #elif event.type == pg.MOUSEWHEEL:
                #if 15 < square_size + event.y < 100:
                    #square_size += event.y
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    offset[0] += square_size
                elif event.key == pg.K_RIGHT:
                    offset[0] -= square_size
                elif event.key == pg.K_DOWN:
                    offset[1] -= square_size
                elif event.key == pg.K_UP:
                    offset[1] += square_size
            if event.type == pg.QUIT:
                run = False
                pg.quit()

        draw_screen(indexes, offset, player_turn)
        if not win:
            if detect_win(indexes):
                win = True
                if len(indexes) % 2 == player_turn:
                    text = font.render('X wins!', True, (0, 255, 0))
                    x_score += 1
                else:
                    text = font.render('O wins!', True, (0, 255, 0))
                    o_score += 1

        if win:
            pygame.draw.rect(screen, (100, 100, 22), rematch_textRect)
            screen.blit(text, textRect)
            screen.blit(rematch_text, rematch_textRect)
        x_score_text = score_font.render('X Score: ' + str(x_score), True, (10, 0, 0))
        o_score_text = score_font.render('O score: ' + str(o_score), True, (10, 0, 0))
        screen.blit(o_score_text, o_score_textRect)
        screen.blit(x_score_text, x_score_textRect)

        pg.display.update()
        if character_turn == "o":
            character_turn = "x"
        else:
            character_turn = "o"




if __name__ == '__main__':
    run_game()
