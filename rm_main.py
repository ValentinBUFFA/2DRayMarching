from shapes import *
import random

clock = pygame.time.Clock()
shape_list = [Line((200,200),(600,700))]
    #Circle((300,200),50),Rectangle((100,50),(50,50)),Rectangle((125, 350),(100,25)),Circle((200,200),25),Circle(((573, 277)),40),Rectangle(((415, 653)),(97,42)),Rectangle(((715, 513)),(41,61)),Circle(((736, 312)),31),Circle(((485, 52)),25),Rectangle(((610, 56)),(90,48)),Circle(((255, 573)),46),Circle(((613, 651)),20),Rectangle(((807, 167)),(58,99)),Rectangle(((810, 85)),(31,98)),Circle(((103, 483)),49),Circle(((300, 719)),22),Circle(((365, 382)),46),Rectangle(((886, 413)),(73,34)),Rectangle(((899, 768)),(79,81)),Circle(((924, 45)),21),Rectangle(((91, 736)),(67,58)),Rectangle(((88, 611)),(32,87)),Circle(((79, 257)),23)]

def adjust_angle(angle):
    return (angle+math.pi)%(2*math.pi) - math.pi

def compute_mouse_angle(mpos):
    (m_x, m_y) = mpos
    m_delta_x = m_x - x
    m_delta_y = m_y - y
    if m_delta_x==0:
        theta = math.copysign(math.pi/2, m_delta_y)
    else:
        theta = math.atan(m_delta_y/m_delta_x) + math.pi * (m_delta_x<0)
        theta = adjust_angle(theta)
    return theta

def ray_fw(rpos, angle, amount):
    return np.add(rpos, (amount*math.cos(angle),amount*math.sin(angle)))

def update(mpos):
    screen.blit(background,(0,0))
    mouse_angle = compute_mouse_angle(mpos)
    rpos = (x,y)
    total_dst = 0
    dst_min = 999999
    while dst_min>1:
        dst_list = []
        for shape in shape_list:
            dst_list.append(shape.dst(rpos))
        dst_min = min(dst_list)
        total_dst += dst_min
        pygame.draw.circle(screen, (233, 196, 106), rpos, dst_min+(dst_min<1), 1) #draw circle around ray steps
        _rpos = ray_fw(rpos, mouse_angle, dst_min) #calculate next ray position

        if _rpos[0]>w_dim[0] or _rpos[0]<0 or _rpos[1]>w_dim[1] or _rpos[1]<0: #check if not out of bound
            dst_min = 0
        rpos = _rpos

    pygame.draw.circle(screen,(231, 111, 81), (x,y),5)
    pygame.draw.line(screen, (231, 111, 81), (x,y), rpos,1)
    pygame.display.flip()

(x,y) = (50,50)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                y-=2
            if event.key == pygame.K_s:
                y+=2
            if event.key == pygame.K_d:
                x+=2
            if event.key == pygame.K_q:
                x-=2
            update(pygame.mouse.get_pos())
            
        if event.type == pygame.MOUSEMOTION:
            update(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                r = random.randrange(15,60)
                shape_list.append(Circle((event.pos),r))
            if event.button == 3:
                s_w = random.randrange(30,100)
                s_h = random.randrange(30,100)
                shape_list.append(Rectangle((event.pos),(s_w,s_h)))
            update(event.pos)
    
    clock.tick(60)
    print(clock.get_fps())