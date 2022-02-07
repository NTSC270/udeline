class render():

    def draw(board, plr, flag):

        renderboard = [[1 for x in range(5)] for y in range(5)] 
        for x in range(5):
            for y in range(5):
                renderboard[x][y] = board[x][y]
        renderboard[plr[0]][plr[1]] = 2
        renderboard[flag[0]][flag[1]] = 3
        rendered = ""
        for x in range(5):
            for y in range(5):
                if renderboard[x][y] == 0:
                    rendered += "<:__:939505702836244530>"
                if renderboard[x][y] == 1:
                    rendered += "<:wall:939505435260645407>"
                if renderboard[x][y] == 3:
                    rendered += "<:flag:939505295787438113>"
                if renderboard[x][y] == 2:
                    rendered += "<:char:939505296269795378>"
                if renderboard[x][y] == 4:
                    rendered += "<:lava:939610590345834546>"
            rendered += "\n"
        return rendered
                