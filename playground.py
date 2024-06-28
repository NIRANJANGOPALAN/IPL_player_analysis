def balls_to_overs(balls):
    overs = balls // 6
    remaining_balls = balls % 6
    return f"{overs}.{remaining_balls}" if remaining_balls else f"{overs}"

# Apply the conversion
print(balls_to_overs(25))