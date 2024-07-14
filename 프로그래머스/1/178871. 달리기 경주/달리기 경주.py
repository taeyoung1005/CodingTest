def solution(players, callings):
    answer = []
    player_indices = {player: i for i, player in enumerate(players)}
    
    for call in callings:
        call_index = player_indices[call]
        
        temp = players[call_index-1]
        players[call_index-1] = call
        players[call_index] = temp
        
        player_indices[call] -= 1
        player_indices[temp] += 1
    
    answer = players
    return answer
