def solution(towers):
    # Write your code here
    min_moves = 0
    # Sort the towers
    towers.sort()
    # Get the middle tower
    mid = towers[len(towers) // 2]
    # Loop through the towers
    for tower in towers:
        # If the tower is less than the middle, we add the difference to the min_moves
        if tower < mid:
            min_moves += mid - tower
        # If the tower is more than the middle, we subtract the difference from the min_moves
        elif tower > mid:
            min_moves += tower - mid
    return min_moves


print(solution([1, 4, 3, 2]))
