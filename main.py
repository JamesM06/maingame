
fire_ball: Sprite = None
mySprite: Sprite = None
MAX_SCREEN_SIZE_X = 160

def on_a_pressed():
    global fire_ball
    mySprite.set_image(img("""
        ........................
        ........................
        ........................
        ...........ccc..........
        ...........cccc.........
        .......ccc..ccccccc.....
        .......cccccc555555cc...
        ........ccb5555555555c..
        .....cc..b555555555555c.
        .....cccb55555bcc555555c
        ......cb555555555c55d55c
        ......b5555555555555555c
        ...cc.b555dd5555bb1bbbc.
        ....ccd55ddddd5bbbb335c.
        ...ccbdddddddd5bbbb335c.
        .ccccddddddddd55bb3335c.
        cdcccdddddb55bb55b3335c.
        cddbddddddb555bb553335c.
        cddddddddddb5555b5555c..
        ccddddddbd55bb55cbccc...
        .ccddddbbbdd55ccbbc.....
        ...ccbbbcbddddccdddc....
        .....ccccdd555dccccc....
        ........cccccccc........
        """))
    fire_ball = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . 4 4 . . . . . . .
            . . . . . . 4 5 5 4 . . . . . .
            . . . . . . 2 5 5 2 . . . . . .
            . . . . . . . 2 2 . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        mySprite,
        50,
        0)
        
def enemy_spawner():
    pause(1000)
    enemysprite = sprites.create_projectile_from_side(img("""
        4 4 4 . . 4 4 4 4 4 . . . . . .
        4 5 5 4 4 5 5 5 5 5 4 4 . . . .
        b 4 5 5 1 5 1 1 1 5 5 5 4 . . .
        . b 5 5 5 5 1 1 5 5 1 1 5 4 . .
        . b d 5 5 5 5 5 5 5 5 1 1 5 4 .
        b 4 5 5 5 5 5 5 5 5 5 5 1 5 4 .
        c d 5 5 5 5 5 5 5 5 5 5 5 5 5 4
        c d 4 5 5 5 5 5 5 5 5 5 5 1 5 4
        c 4 5 5 5 d 5 5 5 5 5 5 5 5 5 4
        c 4 d 5 4 5 d 5 5 5 5 5 5 5 5 4
        . c 4 5 5 5 5 d d d 5 5 5 5 5 b
        . c 4 d 5 4 5 d 4 4 d 5 5 5 4 c
        . . c 4 4 d 4 4 4 4 4 d d 5 d c
        . . . c 4 4 4 4 4 4 4 4 5 5 5 4
        . . . . c c b 4 4 4 b b 4 5 4 4
        . . . . . . c c c c c c b b 4 .
    """), -20, 0)
    enemysprite.set_position(MAX_SCREEN_SIZE_X, randint(5, 100))
def win_condition():
    if mySprite.overlaps_with(fire_ball):
        game.game_over(True)
    return None


scene.set_background_color(9)
mySprite = sprites.create(img("""
        ........................
        ........................
        ...........ccc..........
        ...........cccc.........
        .......ccc..ccccccc.....
        .......cccccc555555cc...
        ........ccb5555555555c..
        .....cc..b555555555555c.
        .....cccb555555ff155555c
        ......cb55555555ff55d55c
        ......b5555555555555555c
        ...cc.b555dd5555bb13bbc.
        ...cccd55ddddd555b3335c.
        .....bdddddddddd55b335c.
        ..cccdddddb55bbddd5555c.
        ..cccdddddb555bbbbcccc..
        ...ccddddddb5555cbcdc...
        ccccbdddddd5cb55cbcc....
        cddddddddd5555ccbbc.....
        .cddddddbdd555bbbcc.....
        ..ccdddbbbdd55cbcdc.....
        ....ccbbcbddddccdddcc...
        ......cccdd555dcccccc...
        ........cccccccc........
        """),
    SpriteKind.player)
mySprite.set_position(15, 20)
mySprite.set_stay_in_screen(True)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

controller.move_sprite(mySprite, 0)
#Win_condition = False
forever(enemy_spawner)
forever(win_condition())