from matplotlib import pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import random

fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xlim(0, 20)
ax.set_ylim(0, 20)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.set_title('Random Snake Movement', fontsize=14, fontweight='bold')


snake_length = 5
snake_body = [[10, 10 + i] for i in range(snake_length)]
direction = [0, -1] 
game_over = False
game_won = False


num_points = 5
random_points_x = [random.randint(0, 19) for _ in range(num_points)]
random_points_y = [random.randint(0, 19) for _ in range(num_points)]


line, = ax.plot([], [], 'go-', linewidth=3, markersize=10, label='Snake')
head, = ax.plot([], [], 'ro', markersize=15, label='Head')
points, = ax.plot(random_points_x, random_points_y, 'b*', markersize=15, label='Points')


game_text = ax.text(10, 10, '', fontsize=30, ha='center', va='center',
                    color='white', fontweight='bold',
                    bbox=dict(boxstyle='round', facecolor='black', alpha=0.8))


def init():
    line.set_data([], [])
    head.set_data([], [])
    game_text.set_text('')
    return line, head, points, game_text

def animate(frame):
    global snake_body, direction, game_over, game_won

    if game_won:
        head.set_color('gold')
        line.set_color('gold')
        game_text.set_text('YOU WIN!')
        game_text.set_color('gold')
        return line, head, points, game_text
    
    if game_over:
        line.set_color('red')
        game_text.set_text('GAME OVER')
        game_text.set_color('red')
        return line, head, points, game_text
    

    if random.random() < 0.25:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        opposite = [-direction[0], -direction[1]]
        available = [d for d in directions if d != opposite]
        direction = random.choice(available)
    

    new_head = [
        snake_body[0][0] + direction[0],
        snake_body[0][1] + direction[1]
    ]
    

    new_head[0] = int(new_head[0] % 20)
    new_head[1] = int(new_head[1] % 20)
    
    snake_body.insert(0, new_head)
    

    ate_food = False
    for i in range(1, len(snake_body)):
        if new_head[0] == snake_body[i][0] and new_head[1] == snake_body[i][1]:
            game_over = True
            break
    

    food_index = -1
    for i in range(len(random_points_x)):
        if new_head[0] == random_points_x[i] and new_head[1] == random_points_y[i]:
            food_index = i
            ate_food = True
            break
    

    if food_index >= 0:
        random_points_x.pop(food_index)
        random_points_y.pop(food_index)
        points.set_data(random_points_x, random_points_y)
    
    if(len(random_points_x)==0):
        game_won = True

    if not ate_food:
        snake_body.pop()
    


    x_coords = [pos[0] for pos in snake_body]
    y_coords = [pos[1] for pos in snake_body]
    

    filtered_x = []
    filtered_y = []
    
    for i in range(len(x_coords)):
        filtered_x.append(x_coords[i])
        filtered_y.append(y_coords[i])
        
        if i < len(x_coords) - 1:
            dx = abs(x_coords[i] - x_coords[i+1])
            dy = abs(y_coords[i] - y_coords[i+1])
            
            if dx > 5 or dy > 5:
                filtered_x.append(np.nan)
                filtered_y.append(np.nan)
    
    line.set_data(filtered_x, filtered_y)
    head.set_data([x_coords[0]], [y_coords[0]])
    
    return line, head, points, game_text


anim = FuncAnimation(fig, animate, init_func=init, 
                    frames=200, interval=50, blit=True, repeat=True)

plt.show()