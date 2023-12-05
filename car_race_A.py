# Importar o módulo pygame
import pygame, sys
from pygame.locals import *
from math import cos, sin, sqrt, atan, pi


# inicialização do módulo pygame
pygame.init()

# criação de uma janela
largura = 1006  
altura  = 666
tamanho = (largura, altura)
janela  = pygame.display.set_mode(tamanho)
pygame.display.set_caption('CarRace do A_RPSF') #nome da janela
#Nesta janela o ponto (0,0) é o canto superior esquerdo


# número de imagens por segundo
frame_rate = 30

# relógio para controlo do tempo
clock = pygame.time.Clock()

# ler uma imagem em formato bmp
pista = pygame.image.load("circuito.png")
carro = pygame.image.load("carroA.png")

    
#Inicializa o tempo
t=0.0

#########################
#Para escrever o tempo:
font_size = 25
font = pygame.font.Font(None, font_size) # fonte pré-definida
antialias = True # suavização
WHITE = (255, 255, 255)# cor (terno com os valores Red, Green, Blue entre 0 e 255)


# parametrização de uma semi reta
def semi_reta(P0, u, vel, t):
    """
    P0 -> (x0,y0) : posição inicial
    u -> (Ux,Uy) : versor da reta : U = D / |D|, sendo D um vetor da reta
    v -> velocidade, v>0 sentido de u, v<0 sentido contrario a u
    t -> tempo, t=0 corresponde a posição P0
    
    Return: tuplo de tuplos: ((x,y), ângulo) com posição e direção
    
    Equações:
        P = P0 + u * v * t
        |v| = |dP/dt|
    """
    x = P0[0] + u[0] * vel * t
    y = P0[1] + u[1] * vel * t
    
    # cálculo da direção: dP/dt
    vx = u[0] * vel
    vy = u[1] * vel
    angulo = atan(vy/vx)
    if vx<0:
        angulo = angulo + pi
    
    return ((x,y), angulo)


# parametrização de um circulo
def circulo(C, raio, alpha0, vel, t):
    """
    C -> (Cx,Cy) : centro do círculo
    r -> raio
    alpha0 -> ângulo inicial, correspondente a t=0
    velocidade -> v>0 sentido negativo, v<0 sentido positivo
    t -> tempo
    
    Return: tuplo de tuplos: ((x,y), ângulo) com posição e direção
    
    Equações: 
        P = C + (r * cos(alpha0 + omega * t), r * sin(alpha0 + omega * t)), com omega = v/r
        |v| = |dP/dt|
    """
    omega = vel / raio
    x = C[0] + raio * cos(alpha0 + omega * t)
    y = C[1] + raio * sin(alpha0 + omega * t)
    
    # cálculo da direção: dP/dt
    vx = -1 * omega * raio * sin(alpha0 + omega * t)
    vy = omega * raio * cos(alpha0 + omega * t)
    angulo = atan(vy/vx)
    if vx<0:
        angulo = angulo + pi
    
    return ((x,y), angulo)


##################################
##Exemplo ajustado à pista
v_reta = 80
v_curva = v_reta / 2

def parametrizacao (t):
    
    # posição inicial
    if t>=0:
        resultado = ((344,134), 0)
    
    # reta 1
    P0 = (344,134)
    P1 = (795,123)
    dr = (P1[0]-P0[0], P1[1]-P0[1])
    norma_dr = sqrt(dr[0]**2 + dr[1]**2)
    dt =  norma_dr / v_reta
    u = (dr[0]/norma_dr, dr[1]/norma_dr)
    t0 = 0
    t1 = t0 + dt
    if t0 < t <= t1:
        posicao, direcao = semi_reta(P0, u, v_reta, t)
        resultado = (posicao, direcao)
    
    # curva 1
    C = (793,221)
    raio = 97
    theta0 = 0 - pi/2 # porque a nossa referência para 0 radianos é o topo do círculo e aqui é à direita
    theta1 = 3.51 - pi/2
    dtheta = theta1 - theta0
    omega = v_curva / raio
    dt = abs(dtheta/omega)
    t0 = t1
    t1 = t0 + dt
    if t0 < t <= t1:
        posicao, direcao = circulo(C, raio, theta0, v_curva, t-t0)
        resultado = (posicao, direcao)
    
    # reta 2
    P0 = (759,311)
    P1 = (714,290)
    dr = (P1[0]-P0[0], P1[1]-P0[1])
    norma_dr = sqrt(dr[0]**2 + dr[1]**2)
    dt =  norma_dr / v_reta
    u = (dr[0]/norma_dr, dr[1]/norma_dr)
    t0 = t1
    t1 = t0 + dt
    if t0 < t <= t1:
        posicao, direcao = semi_reta(P0, u, v_reta, t-t0)
        resultado = (posicao, direcao)
    
    # curva 2
    C = (700,330)
    raio = 43
    theta0 = 0.41 - pi/2 # porque a nossa referência para 0 radianos é o topo do círculo e aqui é à direita
    theta1 = 4.35 - pi # sentido positivo
    dtheta = theta1 - theta0
    omega = v_curva / raio
    dt = abs(dtheta/omega)
    t0 = t1
    t1 = t0 + dt
    if t0 < t <= t1:
        posicao, direcao = circulo(C, raio, theta0, -v_curva, t-t0)
        resultado = (posicao, direcao)
    
    # reta 3
    P0 = (662,342)
    P1 = (717,465)
    dr = (P1[0]-P0[0], P1[1]-P0[1])
    norma_dr = sqrt(dr[0]**2 + dr[1]**2)
    dt =  norma_dr / v_reta
    u = (dr[0]/norma_dr, dr[1]/norma_dr)
    t0 = t1
    t1 = t0 + dt
    if t0 < t <= t1:
        posicao, direcao = semi_reta(P0, u, v_reta, t-t0)
        resultado = (posicao, direcao)
    
    # curva 3
    C = (621,495)
    raio = 99
    theta0 = 1.24 - pi/2 # porque a nossa referência para 0 radianos é o topo do círculo e aqui é à direita
    theta1 = 3.05 - pi/2 # sentido negativo
    dtheta = theta1 - theta0
    omega = v_curva / raio
    dt = abs(dtheta/omega)
    t0 = t1
    t1 = t0 + dt
    if t0 < t <= t1:
        posicao, direcao = circulo(C, raio, theta0, v_curva, t-t0)
        resultado = (posicao, direcao)
    
    # reta 4
    P0 = (630,596)
    P1 = (522,596)
    dr = (P1[0]-P0[0], P1[1]-P0[1])
    norma_dr = sqrt(dr[0]**2 + dr[1]**2)
    dt =  norma_dr / v_reta
    u = (dr[0]/norma_dr, dr[1]/norma_dr)
    t0 = t1
    t1 = t0 + dt
    if t0 < t <= t1:
        posicao, direcao = semi_reta(P0, u, v_reta, t-t0)
        resultado = (posicao, direcao)
    
    # curva 4
    C = (528,476)
    raio = 120
    theta0 = 3.19 - pi/2 # porque a nossa referência para 0 radianos é o topo do círculo e aqui é à direita
    theta1 = 5.31 - pi/2 # sentido negativo
    dtheta = theta1 - theta0
    omega = v_curva / raio
    dt = abs(dtheta/omega)
    t0 = t1
    t1 = t0 + dt
    if t0 < t <= t1:
        posicao, direcao = circulo(C, raio, theta0, v_curva, t-t0)
        resultado = (posicao, direcao)
    
    # reta 5
    P0 = (430,408)
    P1 = (484,329)
    dr = (P1[0]-P0[0], P1[1]-P0[1])
    norma_dr = sqrt(dr[0]**2 + dr[1]**2)
    dt =  norma_dr / v_reta
    u = (dr[0]/norma_dr, dr[1]/norma_dr)
    t0 = t1
    t1 = t0 + dt
    if t0 < t <= t1:
        posicao, direcao = semi_reta(P0, u, v_reta, t-t0)
        resultado = (posicao, direcao)
    
    # curva 5
    C = (435,292)
    raio = 58
    theta0 = 2.19 - pi/2 # porque a nossa referência para 0 radianos é o topo do círculo e aqui é à direita
    theta1 = 5.45 - pi/2 # sentido positivo
    dtheta = theta1 - theta0
    omega = v_curva / raio
    dt = abs(dtheta/omega)
    t0 = t1
    t1 = t0 + dt
    if t0 < t <= t1:
        posicao, direcao = circulo(C, raio, theta0, -v_curva, t-t0)
        resultado = (posicao, direcao)
    
    # reta 6
    P0 = (383,269)
    P1 = (352,345)
    dr = (P1[0]-P0[0], P1[1]-P0[1])
    norma_dr = sqrt(dr[0]**2 + dr[1]**2)
    dt =  norma_dr / v_reta
    u = (dr[0]/norma_dr, dr[1]/norma_dr)
    t0 = t1
    t1 = t0 + dt
    if t0 < t <= t1:
        posicao, direcao = semi_reta(P0, u, v_reta, t-t0)
        resultado = (posicao, direcao)
    
    # curva 6
    C = (252,302)
    raio = 106
    theta0 = 1.96 - pi/2 # porque a nossa referência para 0 radianos é o topo do círculo e aqui é à direita
    theta1 = 3.63 - pi/2 # sentido negativo
    dtheta = theta1 - theta0
    omega = v_curva / raio
    dt = abs(dtheta/omega)
    t0 = t1
    t1 = t0 + dt
    if t0 < t <= t1:
        posicao, direcao = circulo(C, raio, theta0, v_curva, t-t0)
        resultado = (posicao, direcao)
    
    # reta 7
    P0 = (202,399)
    P1 = (151,366)
    dr = (P1[0]-P0[0], P1[1]-P0[1])
    norma_dr = sqrt(dr[0]**2 + dr[1]**2)
    dt =  norma_dr / v_reta
    u = (dr[0]/norma_dr, dr[1]/norma_dr)
    t0 = t1
    t1 = t0 + dt
    if t0 < t <= t1:
        posicao, direcao = semi_reta(P0, u, v_reta, t-t0)
        resultado = (posicao, direcao)
    
    # curva 7
    C = (228,261)
    raio = 128
    theta0 = 3.80 - pi/2 # porque a nossa referência para 0 radianos é o topo do círculo e aqui é à direita
    theta1 = 6.24 - pi/2 # sentido negativo
    dtheta = theta1 - theta0
    omega = v_curva / raio
    dt = abs(dtheta/omega)
    t0 = t1
    t1 = t0 + dt
    if t0 < t <= t1:
        posicao, direcao = circulo(C, raio, theta0, v_curva, t-t0)
        resultado = (posicao, direcao)
    
    # reta 8
    P0 = (224,134)
    P1 = (342,134)
    dr = (P1[0]-P0[0], P1[1]-P0[1])
    norma_dr = sqrt(dr[0]**2 + dr[1]**2)
    dt =  norma_dr / v_reta
    u = (dr[0]/norma_dr, dr[1]/norma_dr)
    t0 = t1
    t1 = t0 + dt
    if t0 < t <= t1:
        posicao, direcao = semi_reta(P0, u, v_reta, t-t0)
        resultado = (posicao, direcao)
    
    #if t>10:
    #    resultado=(0,0)
    
    # a trajetoria pode ficar mais bem centrada
    # vamos fazer uma translação de toda a trajetoria em  (-10,-10)
    posicao, direcao = resultado
    x,y = posicao
    resultado = ((x-10,y-10), direcao)
    
    return resultado

#######################

#(A) Se descomentar aqui (e comentar B) vejo onde passou/ rasto da trajetória
# Pois neste caso só junta a pista uma vez,
#no outro caso está sempre a juntar/desenhar a pista
#janela.blit(pista, (0, 0)) 

#################################
#Ciclo principal do jogo
posicao = (0,0)
while True:
    tempo = font.render("t="+str(int(t)), antialias, WHITE) 
    janela.blit(pista, (0, 0))  #(B) se descomentar aqui (e comentar (A)) vejo movimento
    p0 = posicao
    posicao, direcao = parametrizacao(t)
    
    # calcular velociadade
    v = sqrt((posicao[0]-p0[0])**2 + (posicao[1]-p0[1])**2)
    velocidade = font.render("v="+str(round(v,2)), antialias, WHITE)
    
    janela.blit(pygame.transform.rotate(carro, -direcao * 180 / pi), posicao)
    janela.blit(tempo, (10, 10))
    janela.blit(velocidade, (10, 30))
    pygame.display.update()
    clock.tick(frame_rate)
    t=t+0.1
    

    
    for event in pygame.event.get():
        #Para sair...
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        #Ao clicar em qualquer local, o tempo recomeça com t=0
        # evento mouse click botão esquerdo (código = 1)
        elif event.type== pygame.MOUSEBUTTONUP and event.button == 1:
            t = 0
            janela.blit(pista, (0, 0))
                       

##        #Quando queremos saber as coordenadas de um ponto: 
##        # descomentar isto e comentar o "evento mouse click"...
##        #"clicar" nesse ponto... o python print as coordenadas.
##        # evento mouse click botão esquerdo (código = 1)
##        elif event.type== pygame.MOUSEBUTTONUP and event.button == 1:
##            (x, y) = event.pos
##            localizacao="posicao=(" + str(x) + "," + str(y) + ")"
##            print(localizacao)


##FAQs:
##Faça uma parametrização e teste no programa,depois faça a seguinte
##            e teste, e continue assim até ao fim.
##            Pois se fizer tudo “no papel” e depois testar no fim,
##            certamente não vai funcionar. 
##
##Quando uma imagem (por exemplo do carro) é colocada no ponto (x,y),
##isso significa que a o canto superior esquerdo dessa imagem
##fica nesse ponto.
     
            




