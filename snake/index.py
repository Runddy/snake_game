import pygame, sys, time, random

pygame.init ()

font=pygame.font.Font(None,30)


play_surface =pygame.display.set_mode((500,500))

fps= pygame.time.Clock()

def food():
    random_pos = random.randint(0,49)*10
    food_pos = [random_pos,random_pos]
    return food_pos


def main ():
    snake_pos = [100,50]
    snake_body = [[100,50],[90,50],[80,50]]
    changue = "Right"


    run = True
    food_pos = food()
    score = 0
    while run : 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run= False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT :
                    changue="Rigth"
                if event.key == pygame.K_LEFT :
                    changue="Left"
                if event.key == pygame.K_UP :
                    changue="Up"
                if event.key == pygame.K_DOWN :
                    changue="Down"
        if changue=="Rigth":
            snake_pos[0] +=10
        if changue=="Left":
            snake_pos[0] -=10
        if changue=="Up":
            snake_pos[1] -=10
        if changue=="Down":
            snake_pos[1] +=10
        snake_body.insert(0,list(snake_pos))
        if snake_pos == food_pos:
            food_pos = food()
            score += 1
            print(score)
        else:
            snake_body.pop()
            

    # color  window 
        play_surface.fill(	( 0,255, 0))
        for pos in snake_body:
            pygame.draw.rect(play_surface,(200,200,200),pygame.Rect(pos[0],pos[1],10,10))
        #food of snake
        pygame.draw.rect(play_surface,(169,6,6),pygame.Rect(food_pos[0],food_pos[1],10,10))
        #score 
        text = font.render(str(score),0,(255, 255, 255))

#?Score position 
        play_surface.blit(text,(480,20))


        if score <5:
            fps.tick(10)

        if score >= 7:
            fps.tick(20)

        if score >= 14:
            fps.tick(40)
        if score >= 20:
            fps.tick(80)    
 #! lmit 
        if snake_pos [0] <=0 or snake_pos [0] >=500:
            run = False
            print("You lose")
        if snake_pos [1] <=0 or snake_pos [1] >=500:
            run = False
            print("You lose")     
        #create a snake

        pygame.display.flip()
        fps.tick(10)
main()
pygame.quit()

