import pygame 

class InterfacePy:

    def __init__(self, pix_width, pix_length, edge, grey, red):
        self.edge = edge
        self.pix_length = pix_length
        self.pix_width = pix_width
        self.grey = grey
        self.red = red
        self.screen = pygame.display.set_mode((pix_width, pix_length))

        self.dict_rotation = dict()
        self.dict_rotation['']=0
        self.dict_rotation['UP']=0
        self.dict_rotation['DOWN']=180
        self.dict_rotation['LEFT']=90
        self.dict_rotation['RIGHT']=-90

        self.define_borders_and_images()

    def define_borders_and_images(self):

        self.rect_border_l = pygame.Rect((0,0),(self.edge,self.pix_length))
        self.image_border_l = pygame.Surface((self.edge,self.pix_length))
        self.image_border_l .fill(self.grey)

        self.rect_border_r = pygame.Rect((self.pix_width-self.edge,0),(self.pix_width-self.edge,self.pix_length))
        self.image_border_r = pygame.Surface((self.edge,self.pix_length))
        self.image_border_r .fill(self.grey)

        self.rect_border_up = pygame.Rect((self.edge,0),(self.edge,self.edge))
        self.image_border_up = pygame.Surface((self.pix_width-2*self.edge,self.edge))
        self.image_border_up .fill(self.grey)

        self.rect_border_down = pygame.Rect((self.edge,self.pix_length-self.edge),(self.pix_width-self.edge,self.pix_length))
        self.image_border_down = pygame.Surface((self.pix_width-2*self.edge,self.edge))
        self.image_border_down .fill(self.grey)

        self.image_new_ball = pygame.Surface((self.edge, self.edge))
        self.image_new_ball .fill(self.red)  

        self.image_head = pygame.image.load("head_snake.png")
        self.image_body = pygame.image.load("body_snake.png")
        


    def refresh(self, snake, game):
        self.screen.blit(self.image_border_l, self.rect_border_l)
        self.screen.blit(self.image_border_r, self.rect_border_r)
        self.screen.blit(self.image_border_up, self.rect_border_up)        
        self.screen.blit(self.image_border_down, self.rect_border_down)        

        pix_new_ball=(game.new_ball[0]*self.edge,game.new_ball[1]*self.edge)
        rect_new_ball = pygame.Rect(pix_new_ball, (pix_new_ball[0]+self.edge, pix_new_ball[1]+self.edge))
        self.screen.blit(self.image_new_ball, rect_new_ball)
        
        pix_head = (snake.body[0][0]*self.edge, snake.body[0][1]*self.edge)
        rect_head = pygame.Rect(pix_head, (pix_head[0]+self.edge, pix_head[1]+self.edge))
        image_head=pygame.transform.rotate(self.image_head,self.dict_rotation.get(game.direction))
        self.screen.blit(image_head, rect_head)
        
        for square in snake.body:
            if square!=snake.body[0]:
                pix=(square[0]*self.edge,square[1]*self.edge)
                rect = pygame.Rect(pix, (pix[0]+self.edge, pix[1]+self.edge))
                self.screen.blit(self.image_body, rect)

        pygame.display.update()  



    def change_direction(self, event, game):
        if event.key == pygame.K_DOWN or event.key == pygame.K_UP or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:

            if event.key == pygame.K_DOWN and game.direction != 'UP':
                game.direction = 'DOWN'
            elif event.key == pygame.K_UP and game.direction != 'DOWN':
                game.direction = 'UP'
            elif event.key == pygame.K_LEFT and game.direction != 'RIGHT':
                game.direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and game.direction != 'LEFT':
                game.direction = 'RIGHT'

                   
    