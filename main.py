import pygame
import Combat.button as button
import Combat.combat as combat
import Combat.combat_unit as combat_unit
import Combat.entity_type as entity_type


#temp code for testing
a = entity_type.entity_data
allies = [a["jack"]]
allies = list(map(combat_unit.Entity.from_type, allies))
enemies = [combat_unit.Entity.from_type(a["enemy"]) for i in range(3)]

window = pygame.display.set_mode((900, 600)) #900, 600 defult

combat_scene = combat.Combat_scene(allies, enemies)
combat_scene.update_surface()


def graphics():
    window.fill((255, 0, 0))
    combat_scene.render(window)
    pygame.display.update()


def check_key(framecount, last_pressed):
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            combat_scene.check_mouse(pos)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


def main():
    running = True
    clock = pygame.time.Clock()
    framecount = 0
    last_pressed = 0
    hp = 20
    while running:
        clock.tick(30)
        framecount += 1
        if framecount % 60 == 0:
            print(clock.get_fps())
        graphics()
        last_pressed = check_key(framecount, last_pressed)


main()
