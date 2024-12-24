def aqueduct_length(segments):
    total_length = 0.0

    for horizontal, vertical in segments:
        vertical_km = vertical / 1000.0
        segment_length = (horizontal ** 2 + vertical_km ** 2) ** 0.5
        total_length += segment_length

    return f"{round(total_length, 3):.3f}"

segments = [(2, 10), (3, -5), (1.5, 298), (2.5, -10)]
print(aqueduct_length(segments))
