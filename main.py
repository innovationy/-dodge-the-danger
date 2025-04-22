def on_countdown_end():
    # 倒计时结束时如果玩家存活则胜利
    game.over(True, effects.confetti)
    game.splash("You Win!", "Score: " + str(info.score()))
info.on_countdown_end(on_countdown_end)

def on_on_overlap(sprite, otherSprite):
    # 碰撞后立即结束游戏
    game.over(False, effects.melt)
    mySprite.say_text("GAME OVER", 1000)
    # 停止所有游戏活动
    music.stop_all_sounds()
    sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

# 初始化部分
projectile: Sprite = None
mySprite: Sprite = None

# 设置游戏音乐
music.play(music.string_playable("E B C5 A B G A F ", 120),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)

# 初始化倒计时（30秒）
info.start_countdown(30)
info.set_score(0)  # 初始化分数

# 创建背景（添加太空背景）
scene.set_background_image(img("""
    d d d d d d d d d d d d d d d d
    d d d d d d d d d d d d d d d d
    d d 5 5 d d d d d d d d 5 5 d d
    d d 5 5 5 d d d d d d 5 5 5 d d
    d d d 5 5 5 d d d d 5 5 5 d d d
    d d d d 5 5 5 d d 5 5 5 d d d d
    d d d d d 5 5 5 5 5 5 d d d d d
    d d d d d d 5 5 5 5 d d d d d d
    d d d d d d 5 5 5 5 d d d d d d
    d d d d d 5 5 5 5 5 5 d d d d d
    d d d d 5 5 5 d d 5 5 5 d d d d
    d d d 5 5 5 d d d d 5 5 5 d d d
    d d 5 5 5 d d d d d d 5 5 5 d d
    d d 5 5 d d d d d d d d 5 5 d d
    d d d d d d d d d d d d d d d d
    d d d d d d d d d d d d d d d d
"""))

# 创建玩家角色（飞船）
mySprite = sprites.create(img("""
    . . . . . . . 9 9 . . . . . . .
    . . . . . . 9 9 9 9 . . . . . .
    . . . . . 9 9 9 9 9 9 . . . . .
    . . . . 9 9 9 9 9 9 9 9 . . . .
    . . . 9 9 9 9 9 9 9 9 9 9 . . .
    . . 9 9 9 1 1 9 9 1 1 9 9 9 . .
    . 9 9 9 9 1 1 9 9 1 1 9 9 9 9 .
    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
    . 9 9 9 9 9 9 9 9 9 9 9 9 9 9 .
    . . . 9 9 9 9 9 9 9 9 9 9 . . .
"""), SpriteKind.player)
controller.move_sprite(mySprite, 100, 0)
mySprite.set_stay_in_screen(True)
mySprite.set_position(75, 100)

def on_update_interval():
    global projectile
    # 创建下落的危险物体（陨石）
    projectile = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . 8 8 8 8 8 8 8 8 . . . .
        . . 8 8 8 8 8 8 8 8 8 8 8 8 . .
        . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 .
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
        . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 .
        . . 8 8 8 8 8 8 8 8 8 8 8 8 . .
        . . . . 8 8 8 8 8 8 8 8 . . . .
        . . . . . . . . . . . . . . . .
    """), SpriteKind.enemy)
    projectile.set_position(randint(0, scene.screen_width()), 0)
    projectile.set_velocity(randint(-30, 30), randint(50, 80))  # 添加随机水平移动

# 添加存活时间积分功能（每秒加10分）
def on_update_interval2():
    info.change_score_by(10)
game.on_update_interval(1000, on_update_interval2)

# 调整敌人生成频率（每0.5秒生成一个）
game.on_update_interval(500, on_update_interval)